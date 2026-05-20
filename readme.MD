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

## Guia de Instalação do Armbian na TV Box

Este guia descreve os passos práticos para transformar uma TV Box comercial em um nó Linux funcional para o cluster do **CybersecurityBOX**.

> [!WARNING]
> **A MENTIRA DO ANDROID (E DO CPU-Z):** Nunca confie nas informações mostradas pelo Android ou por aplicativos como CPU-Z, AIDA64 e Device Info em TV Boxes genéricas. Os fabricantes frequentemente alteram arquivos do sistema (`build.prop`) para mascarar o hardware real (ex: exibindo "Allwinner H6" ou "4GB RAM / 64GB ROM" quando na verdade o dispositivo possui um Rockchip RK3228A antigo com apenas 1GB de RAM e 8GB de armazenamento).
> 
> **Desmontar a TV Box é obrigatório** para identificar visualmente o SoC (processador), chip de Wi-Fi/Bluetooth e memória RAM gravados na placa de circuito impresso (PCB).

### Passo a Passo de Instalação

#### 1. Identificação Real do Hardware (Desmontagem)
- Desconecte a TV Box de qualquer fonte de energia.
- Utilize uma espátula plástica para desencaixar a tampa inferior/superior. Verifique se há parafusos escondidos sob os pés de borracha.
- Remova o dissipador de calor metálico de cima do processador (se houver) e leia a inscrição impressa (silkscreen) diretamente sobre o chip:
  - **Rockchip:** RK3228A, RK3229, RK3318, RK3328, etc.
  - **Allwinner:** H3, H6, H616, H313, etc.
  - **Amlogic:** S905, S905W, S905X, etc.
- Anote também a identificação do chip de Wi-Fi/Bluetooth (ex: *RTL8723BS*, *SV6256*, *XR819*) para habilitar a rede sem fio posteriormente.
- Tire uma foto ou anote o modelo exato impresso na placa mãe (ex: `MXQ-RK3229-V1.2`), pois ela ajudará a selecionar a DTB correspondente.

#### 2. Obtenção da Imagem do Armbian
- Acesse os fóruns oficiais da comunidade Armbian ou repositórios dedicados a TV Boxes ARM (como as imagens mantidas por *ophub* ou comunidades do *multitool* para chips Rockchip).
- **Links úteis e oficiais de download e suporte:**
  - [Armbian para TV Boxes RK322x (Página Oficial)](https://armbian.com/pt/boards/rk322x-box)
  - [Armbian para RK3328 Heltec (Página Oficial)](https://armbian.com/pt/boards/rk3328-heltec)
  - [Tópico do Fórum Armbian: CSC Armbian para placas RK322x](https://forum.armbian.com/topic/34923-csc-armbian-for-rk322x-tv-box-boards/)
- Baixe a versão estável mais recente do Armbian. Recomenda-se a build **Server/Headless** (Debian ou Ubuntu) para economizar processamento e memória RAM.

#### 3. Gravação da Imagem (Métodos de Flash)
Você pode gravar o Armbian utilizando diferentes métodos de acordo com o processador e as ferramentas disponíveis:

*   **Método A: Via Multitool (Recomendado para chips Rockchip)**
    O **Multitool** é uma ferramenta gráfica executada a partir de um cartão SD projetada para facilitar o backup e gravação de sistemas operacionais em TV Boxes de arquitetura Rockchip (RK3229, RK3228A, RK3318, etc.).
    1. Baixe a imagem do Multitool e grave-a em um cartão SD usando BalenaEtcher ou Rufus.
    2. Após gravado, reinsira o cartão SD no PC e coloque a imagem `.img` (ou `.img.xz`) do Armbian dentro da pasta `/images/` (ou `/multitool/images/`) criada no cartão SD.
    3. Insira o SD na TV Box desligada, segure o botão de **reset físico** (dentro da entrada AV) e conecte o cabo de energia.
    4. Na interface do Multitool, faça o **Backup** completo da memória interna (eMMC) original.
    5. Escolha a opção de apagar/formatar o eMMC e, em seguida, grave a imagem do Armbian (que está na pasta `/images/`) diretamente no eMMC da TV Box.
    6. Ao concluir, desligue o aparelho, retire o cartão SD e ligue novamente. O sistema iniciará a partir do eMMC.

*   **Método B: Via Cabo USB Macho-Macho (USB A/A)**
    Indicado para gravação direta da imagem na eMMC a partir de um computador, sem precisar do cartão SD na TV Box.
    1. Utilize um cabo USB Macho-Macho para conectar o computador a uma porta USB específica da TV Box (geralmente a porta OTG ou a traseira/lateral marcada).
    2. Baixe e abra o utilitário oficial do fabricante do processador no computador:
       - **Rockchip:** RKDevTool (ou RKBatchTool) no Windows / `upgrade_tool` no Linux.
       - **Amlogic:** USB Burning Tool.
       - **Allwinner:** LiveSuit ou PhoenixSuit.
    3. Pressione e segure o botão de **reset físico** (dentro do conector AV) da TV Box e conecte o cabo de alimentação. O software no PC detectará o dispositivo em modo de recuperação/gravação (Loader ou Maskrom).
    4. Carregue a imagem (.img ou .bin do firmware correspondente) no aplicativo e execute a gravação na eMMC.

*   **Método C: Via Comando `dd` (Terminal Linux)**
    Adequado para gravação de baixo nível diretamente no cartão SD (a partir de um PC com Linux) ou para gravação da eMMC caso esteja rodando um live system Linux temporário na TV Box.
    1. Identifique o dispositivo de destino correto utilizando `lsblk` ou `sudo fdisk -l` (ex: `/dev/sdX` para o cartão SD/pendrive, `/dev/mmcblk0` para a memória interna eMMC).
    2. Execute a gravação da imagem utilizando o comando `dd` (com privilégios root):
       ```bash
       sudo dd if=caminho_da_imagem_armbian.img of=/dev/DESTINO bs=1M status=progress && sync
       ```
       > [!CAUTION]
       > O comando `dd` é destrutivo e não possui confirmação de segurança. Certifique-se de que o dispositivo definido em `of=` é de fato a unidade correta (cartão SD ou eMMC). Especificar a unidade do sistema do seu computador causará perda permanente de dados.

#### 4. Configuração da DTB (Device Tree Blob)
*A DTB é o arquivo responsável por mapear as portas físicas, RAM e componentes do chip para o kernel Linux.*
- Com a gravação concluída, abra a partição de boot do cartão SD (geralmente chamada de `BOOT` ou `armbi-boot`) em seu computador.
- Localize o diretório de DTBs (geralmente `/dtb/` ou `/boot/dtb/`) e identifique o arquivo `.dtb` mais adequado para o seu processador e placa.
- Abra o arquivo de configuração de boot (geralmente `uEnv.txt`, `armbianEnv.txt` ou `/boot/extlinux/extlinux.conf`) no seu editor de texto e ajuste a variável `fdtfile` ou `dtb_name` para apontar para o seu arquivo DTB selecionado.
  - *Exemplo:* `fdtfile=rockchip/rk3229-mxqpro.dtb`

#### 5. Inicialização (Primeiro Boot)
- Insira o cartão MicroSD ou pendrive configurado na TV Box com ela desligada.
- Conecte um cabo HDMI a uma tela e um teclado USB para acompanhar o boot.
- **Pressione e segure o botão de reset físico.** Ele normalmente fica oculto no fundo do conector P2/AV (entrada de áudio analógico). Use um palito de dente ou clipe de papel para pressioná-lo de forma segura até sentir o clique.
- Enquanto mantém o botão de reset pressionado, conecte o cabo de alimentação na TV Box.
- Continue segurando por cerca de 5 a 10 segundos após a tela inicial de boot do Armbian ou da ferramenta Multitool aparecer, então solte-o.
- Siga as instruções na tela para concluir o setup inicial (definir a senha do usuário `root`, criar um novo usuário e configurar o fuso horário).

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

* [ ] Implantação do sistema de detecção de intrusão (Instalação e *tuning* fino do **Suricata**).
* [ ] Configuração de ferramentas para sniffing e análise de pacotes de dados (**tcpdump/TShark**).
* [x] Configuração e customização do **Cowrie Honeypot** para registro de ataques em nível de rede.

### Fase 3: Telemetria, Redes Sem Fio e Conscientização

* [x] Setup da stack de telemetria e servidor de consolidação de logs.
* [ ] Desenvolvimento de dashboards no **Grafana** para visualização centralizada dos eventos em tempo real.
* [x] Validação das interfaces Wi-Fi em Modo Monitor (testes com o driver `rt73usb` e placa onboard vs. dongle USB).
* [x] Criação da infraestrutura do Rogue AP (alinhamento de `hostapd`, `dnsmasq` e regras de firewall para mitigação de DoH, e script em Python).
* [x] Criação do portal cativo (landing page HTML/CSS) focado em conscientização e educação de segurança para o usuário final.

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