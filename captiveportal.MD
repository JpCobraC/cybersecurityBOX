# Captive Portal Educativo para Cibersegurança

Este documento descreve a arquitetura, os arquivos de configuração e os comandos utilizados para implantar um ambiente controlado de conscientização em cibersegurança. O objetivo do laboratório é simular um ponto de acesso Wi-Fi aberto que intercepta o tráfego de dispositivos conectados e exibe automaticamente uma página de alerta sobre os riscos de redes públicas.

## 🛠️ Arquitetura do Sistema

O laboratório foi construído em uma TV Box rodando **Armbian** com um adaptador Wi-Fi USB baseado no chipset **Ralink RT2573** (driver `rt73usb`). A estrutura divide-se em três pilares principais:

```
[Dispositivo Alvo] 
       │ (Wi-Fi Aberto) ──> hostapd
       │ (IP & DNS)     ──> dnsmasq (Sequestro de DNS/DoH via IPtables)
       ▼ (HTTP Porta 80)──> Nginx (Página de Alerta)

```

---

## 📁 Arquivos de Configuração

### 1. Ponto de Acesso Wi-Fi (`/etc/hostapd/hostapd-educativo.conf`)

Responsável por criar a camada física e transmitir o sinal de rede sem fio de forma aberta. O parâmetro `bssid` foi alterado para mitigar o cache de conectividade de dispositivos móveis.

```ini
interface=wlx001d0fb108a0
driver=nl80211
ssid=Acesso Wi-Fi Gratis
bssid=00:1d:0f:b1:08:b1
hw_mode=g
channel=6
auth_algs=1
wmm_enabled=0

```

### 2. Servidor DHCP e DNS (`/etc/dnsmasq-educativo.conf`)

Configura a distribuição de endereços IP na sub-rede `192.168.10.0/24` e força o redirecionamento de requisições DNS.

```ini
interface=wlx001d0fb108a0
dhcp-range=192.168.10.10,192.168.10.100,255.255.255.0,12h
dhcp-option=3,192.168.10.1
dhcp-option=6,192.168.10.1

# Interceptação de DNS local (Curinga)
address=/#/192.168.10.1

# Proteções contra vazamento de tráfego e DoH
no-resolv
no-poll
filter-AAAA
server=8.8.8.8

```

### 3. Servidor Web HTTP (`/etc/nginx/sites-available/default`)

Configura o Nginx para capturar as URLs nativas de teste de conectividade (Android, iOS e Windows) e redirecioná-las de forma agressiva para o portal.

```nginx
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html;

    server_name _;

    # Endpoints de Captive Portal de Sistemas Operacionais
    location /generate_204 { return 200 "<html><head><meta http-equiv='refresh' content='0;url=http://192.168.10.1/'></head></html>"; }
    location /check_network_status { return 200 "<html><head><meta http-equiv='refresh' content='0;url=http://192.168.10.1/'></head></html>"; }
    location /connecttest.txt { return 200 "<html><head><meta http-equiv='refresh' content='0;url=http://192.168.10.1/'></head></html>"; }
    location /hotspot-detect.html { return 200 "<html><head><meta http-equiv='refresh' content='0;url=http://192.168.10.1/'></head></html>"; }

    # Captura reversa agressiva
    location / {
        rewrite ^(.*)$ http://192.168.10.1/ permanent;
        try_files $uri $uri/ /index.html;
    }

    error_page 404 /index.html;
}

```

---

## 💻 Comandos Utilizados (Manual de Operação)

### 🚀 1. Preparação e Inicialização da Interface

Comandos necessários para instalar dependências, garantir o firmware do chipset e configurar o endereço IP estático da interface sem fio.

```bash
# Instalação dos pacotes essenciais e firmware Ralink
sudo apt update && sudo apt install hostapd dnsmasq nginx firmware-misc-nonfree -y

# Recarregar o módulo do driver para garantir a leitura do firmware rt73.bin
sudo modprobe -r rt73usb
sudo modprobe rt73usb

# Reset e atribuição de IP na interface sem fio
sudo ip link set wlx001d0fb108a0 down
sudo ip addr flush dev wlx001d0fb108a0
sudo ip addr add 192.168.10.1/24 dev wlx001d0fb108a0
sudo ip link set wlx001d0fb108a0 up

```

### 🔒 2. Regras de Firewall e Roteamento (IPtables)

Regras críticas para realizar o mascaramento de rede (NAT) através da interface de internet principal (`eth0`), sequestrar requisições DNS tradicionais (porta 53) e mitigar o DNS Seguro/criptografado (DoH) nas portas 443/853.

```bash
# Ativar o encaminhamento de pacotes no kernel do Linux
sudo sysctl -w net.ipv4.ip_forward=1

# Limpar regras de encaminhamento e aplicar Mascaramento de rede (NAT)
sudo iptables -F FORWARD
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

# Sequestro de tráfego DNS convencional vindo da interface Wi-Fi
sudo iptables -t nat -A PREROUTING -i wlx001d0fb108a0 -p udp --dport 53 -j REDIRECT --to-ports 53
sudo iptables -t nat -A PREROUTING -i wlx001d0fb108a0 -p tcp --dport 53 -j REDIRECT --to-ports 53

# Bloqueio estratégico de DoH para servidores de DNS conhecidos (Força fallback para o dnsmasq)
sudo iptables -A FORWARD -i wlx001d0fb108a0 -p tcp --dport 443 -d 8.8.8.8,8.8.4.4,1.1.1.1,9.9.9.9 -j DROP
sudo iptables -A FORWARD -i wlx001d0fb108a0 -p tcp --dport 853 -j DROP

```

### 🚦 3. Execução dos Serviços em Primeiro Plano (Modo Debug)

Para fins de auditoria e análise de comportamento dos alvos em tempo real, os daemons de rede devem ser executados em sessões de terminal separadas.

```bash
# Terminal 1: Inicialização do sinal Wi-Fi
sudo hostapd /etc/hostapd/hostapd-educativo.conf

# Terminal 2: Parada do serviço global e inicialização do DHCP/DNS educativo
sudo systemctl stop dnsmasq
sudo dnsmasq -C /etc/dnsmasq-educativo.conf -d

# Terminal 3: Teste de sintaxe e reinicialização do Servidor Web Nginx
sudo nginx -t
sudo systemctl restart nginx

```

---

## 📝 Notas de Mitigação do Sistema Alvo

Sistemas operacionais móveis modernos implementam mecanismos de segurança rígidos para contornar ataques à rede. Durante os testes, o comportamento do dispositivo pode exigir:

* **Desativação temporária de Dados Móveis:** Impede que o aparelho envie os testes HTTP por fora do Wi-Fi.
* **Redefinição do Cache de Rede:** O Android memoriza falhas em SSIDs anteriores; mudar o parâmetro `bssid` no `hostapd` simula um hardware inédito e força um novo ciclo de checagem.