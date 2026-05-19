# CybersecurityBOX: Laboratório Portátil de Cibersegurança em Dispositivos ARM

## Resumo Executivo

O projeto **CybersecurityBOX** consiste no desenvolvimento de um laboratório portátil de cibersegurança de baixo custo, utilizando infraestrutura computacional reciclada baseada em TV Boxes. O objetivo principal é demonstrar a viabilidade do reaproveitamento desses dispositivos para a execução de ferramentas de segurança em nível de produção (monitoramento, detecção de intrusão e análise de tráfego), criando um ambiente de alta fidelidade para pesquisa quantitativa, ensino prático e experimentação de segurança na borda (*Edge Security*).

## Motivação e Diferenciais

O projeto endereça o alto custo de infraestrutura de laboratórios convencionais e a escassez de hardware dedicado por meio de abordagens de *Green Computing* e *Edge Computing*. Seus principais diferenciais incluem:

* **Sustentabilidade Tecnológica:** Redução de lixo eletrônico (*e-waste*) através da descaracterização e reaproveitamento de hardware ARM subutilizado de consumo em massa.
* **Portabilidade Plug-and-Play:** Laboratório compacto e transportável, ideal para demonstrações, minicursos, oficinas e atividades extensionistas.
* **Eficiência de Custo e Democratização:** Alternativa economicamente viável para viabilizar o ensino prático de segurança da informação em instituições com restrições orçamentárias.
* **Frente de Pesquisa Empírica:** Base para análises estatísticas de consumo energético, limites de *throughput* de processamento sob ataque e resiliência de protocolos de rede modernos na borda.

---

## Arquitetura e Capacidades do Cluster

O cluster de TV Boxes é projetado para operar como uma rede de sensores distribuídos. Cada nó do cluster assume funções modulares e independentes:

* **Honeypots:** Simulação de serviços vulneráveis (SSH/Telnet) para atração, captura e análise de táticas, técnicas e procedimentos (TTPs) de potenciais invasores (ex: **Cowrie**).
* **IDS/IPS:** Detecção e prevenção de atividades suspeitas, varreduras e anomalias de rede em tempo real (ex: **Suricata**).
* **Análise de Tráfego:** Inspeção profunda de pacotes e auditoria de redes (ex: **Wireshark / TShark / tcpdump**).
* **Monitoramento e Telemetria:** Agregação centralizada de logs e dashboards de visualização analítica (ex: **Grafana**).

### Estudo de Caso de Borda: Rogue AP Educacional e Resiliência DoH

Aproveitando as interfaces Wi-Fi nativas (ou dongles USB baseados no chipset *Ralink RT2573*), a infraestrutura hospeda scripts automatizados para a criação de *Access Points* falsos (*Rogue APs*).

Para contornar as proteções de privacidade modernas de sistemas operacionais móveis, o ecossistema implementa uma técnica de filtragem na camada de transporte (via IPTables) que bloqueia o tráfego de DNS Seguro (**DoH/DoT**), forçando os dispositivos a realizarem um *fallback* para o DNS convencional. Isso permite a interceptação controlada de requisições e o redirecionamento agressivo (via Nginx) para um *Captive Portal* educativo focado em conscientização de segurança.

---

## Matriz de Validação Experimental (Metas Próximas)

Para validar a viabilidade científica da plataforma, o projeto executará quatro frentes de testes controlados:

| Experimento | Metodologia | Métricas Alvo |
| --- | --- | --- |
| **Estresse de Tráfego (IDS)** | Inundação de pacotes via `pktgen`/`iperf3` em diferentes faixas de banda (10 a 100 Mbps). | Taxa de descarte de pacotes (*Packet Drop Rate*) e consumo de CPU. |
| **Co-alocação de VNFs** | Ativação simultânea do Suricata + Cowrie sob ataques simulados de força bruta. | Estabilidade de memória RAM e impacto na latência de rede. |
| **Auditoria Energética** | Medição contínua via wattímetro digital em estados ocioso, nominal e sob estresse. | Consumo em Watts (W) e cálculo da pegada de carbono mitigada. |
| **Eficácia de Fallback DoH** | Conexão de dispositivos de controle atualizados (Android, iOS e Windows 11). | *Captive Portal Detection Time* e taxa de sucesso de conversão. |

---

## Roadmap de Implementação e Checklist

### Fase 1: Preparação da Infraestrutura Física e Lógica

* [x] Mapeamento e inventário das TV Boxes disponíveis (arquitetura do processador, RAM e armazenamento).
* [x] Execução de testes de estresse de CPU, estabilidade e capacidade térmica inicial (benchmark).
* [x] Instalação e configuração do sistema operacional (**Armbian** / distros Linux baseadas em Debian/Ubuntu).
* [x] Configuração inicial de rede e provisionamento de acesso remoto seguro (SSH) via **Tailscale** com tunelamento em instâncias **Oracle Cloud** (evasão de CGNAT).

### Fase 2: Implantação do Core de Segurança

<<<<<<< HEAD
### Fase 3: Telemetria, Visualização e Segurança Sem Fio
- [x] Setup da stack de telemetria e servidor de consolidação de logs.
- [ ] Desenvolvimento de dashboards no **Grafana** para visualização centralizada dos eventos de segurança em tempo real.
- [ ] Validação das interfaces Wi-Fi em Modo Monitor (testes com placa onboard vs. dongle USB).
- [ ] Desenvolvimento do script em Python para criação automatizada do Rogue AP educacional e interceptação de DNS.
- [X] Criação do portal cativo (landing page HTML/CSS) focado em conscientização de segurança para o usuário final.
=======
* [ ] Implantação do sistema de detecção de intrusão (Instalação e *tuning* fino do **Suricata**).
* [ ] Configuração de ferramentas para sniffing e análise de pacotes de dados (**tcpdump/TShark**).
* [x] Configuração e customização do **Cowrie Honeypot** para registro de ataques em nível de rede.
>>>>>>> 731ef6f (Update readme.MD)

### Fase 3: Telemetria, Redes Sem Fio e Conscientização

* [x] Setup da stack de telemetria e servidor de consolidação de logs.
* [ ] Desenvolvimento de dashboards no **Grafana** para visualização centralizada dos eventos em tempo real.
* [x] Validação das interfaces Wi-Fi em Modo Monitor (testes com o driver `rt73usb`).
* [x] Criação da infraestrutura do Rogue AP (alinhamento de `hostapd`, `dnsmasq` e regras de firewall para mitigação de DoH).
* [x] Criação do portal cativo landing page em HTML/CSS focada em educação digital.

### Fase 4: Formalização, Pesquisa Empírica e Análise de Dados

* [ ] Execução da **Matriz de Validação Experimental** (Coleta de dados de throughput, energia, DoH e estresse térmico de 24h).
* [ ] Formalização do Modelo de Ameaças do laboratório utilizando o framework **STRIDE** e mapeamento de logs contra a matriz **MITRE ATT&CK**.
* [ ] Abstração da lógica de interceptação e engenharia de tráfego em formato de **Pseudocódigo / Fluxograma Formal** (independente de software).
* [ ] Processamento estatístico dos resultados obtidos (médias, desvios padrões e gráficos de dispersão de desempenho).
* [ ] Estruturação do modelo pedagógico de minicurso/oficina para replicação da arquitetura e atividades de extensão.

### Fase 5: Escalonamento e Orquestração Avançada (Projetos Futuros)

* [ ] Conteinerização modular de todas as ferramentas do core de segurança.
* [ ] Implantação de um cluster orquestrado via Kubernetes leve para cenários de borda (**K3s**).
* [ ] Automação do provisionamento, tolerância a falhas e balanceamento de carga dos sensores distribuídos entre as TV Boxes do cluster.