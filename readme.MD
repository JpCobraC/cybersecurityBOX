# CibersecurityBOX: Laboratório Portátil de Cibersegurança em Dispositivos ARM

## Resumo Executivo
O projeto **CibersecurityBOX** consiste no desenvolvimento de um laboratório portátil de cibersegurança de baixo custo, utilizando infraestrutura computacional reciclada baseada em TV Boxes. O objetivo principal é demonstrar a viabilidade do reaproveitamento desses dispositivos para a execução de ferramentas de segurança em nível de produção (monitoramento, detecção de intrusão e análise de tráfego), criando um ambiente de alta fidelidade para pesquisa, ensino e experimentação.

## Motivação e Diferenciais
O projeto endereça o alto custo de infraestrutura de laboratórios convencionais por meio de abordagens de *Green Computing* e *Edge Computing*. Seus principais diferenciais incluem:
- **Sustentabilidade Tecnológica:** Redução de lixo eletrônico através da descaracterização e reaproveitamento de hardware ARM subutilizado.
- **Portabilidade:** Laboratório compacto e transportável (plug-and-play), ideal para demonstrações, minicursos, oficinas e atividades extensionistas.
- **Eficiência de Custo:** Alternativa economicamente viável para a democratização do ensino prático de segurança da informação em instituições de ensino.
- **Pesquisa Quantitativa:** Base para análises de consumo energético, throughput de processamento de segurança e estabilidade operacional em hardware de borda (edge).

## Arquitetura e Capacidades
O cluster de TV Boxes é projetado para operar como uma rede de sensores distribuídos. Cada nó do cluster pode assumir funções modulares:
- **Honeypots:** Simulação de serviços vulneráveis para atração e captura de táticas, técnicas e procedimentos (TTPs) de potenciais invasores (ex: **Cowrie**).
- **IDS/IPS:** Detecção e prevenção de atividades suspeitas e anomalias de rede (ex: **Suricata**).
- **Análise de Tráfego:** Inspeção profunda de pacotes (ex: **Wireshark / TShark**).
- **Monitoramento e Telemetria:** Agregação de logs e dashboards de visualização em tempo real (ex: **Grafana**).

### Estudo de Caso e Conscientização: Rogue AP Educacional
Aproveitando a flexibilidade de rede do hardware, o projeto engloba testes de segurança sem fio (Wireless Security). Utilizando as interfaces Wi-Fi nativas em modo monitor (ou com o uso de um dongle USB externo de baixo custo), a infraestrutura é capaz de hospedar scripts desenvolvidos em Python para a criação automatizada de Access Points falsos (Rogue APs). Estes interceptam as requisições DNS de celulares nas proximidades, direcionando os usuários para um "Captive Portal" com o intuito exclusivo de exibir alertas e orientações sobre os perigos da conexão em redes Wi-Fi públicas e abertas.

---

## Roadmap de Implementação e Checklist

Abaixo estão as etapas de execução do projeto, estruturadas cronologicamente desde a preparação do hardware até os testes finais:

### Fase 1: Preparação da Infraestrutura Física e Lógica
- [x] Mapeamento e inventário das TV Boxes disponíveis (arquitetura do processador, RAM e armazenamento).
- [x] Execução de testes de estresse de CPU, estabilidade e capacidade térmica (benchmark e monitoramento).
- [x] Instalação e configuração do sistema operacional (Armbian / distros Linux baseadas em Debian/Ubuntu) nas TV Boxes.
- [x] Configuração inicial de rede, definição de IPs estáticos e provisionamento de acesso remoto seguro (SSH).

### Fase 2: Implantação do Core de Segurança
- [ ] Implantação de sistema de detecção de intrusão (Instalação e tunning do **Suricata**).
- [ ] Configuração de ferramentas para sniffing e análise de pacotes (**Wireshark / tcpdump**).
- [x] Configuração do sistema de **Honeypot** para simulação de falhas e monitoramento de ataques no nível de rede.

### Fase 3: Telemetria, Visualização e Segurança Sem Fio
- [x] Setup da stack de telemetria e servidor de consolidação de logs.
- [ ] Desenvolvimento de dashboards no **Grafana** para visualização centralizada dos eventos de segurança em tempo real.
- [ ] Validação das interfaces Wi-Fi em Modo Monitor (testes com placa onboard vs. dongle USB).
- [ ] Desenvolvimento do script em Python para criação automatizada do Rogue AP educacional e interceptação de DNS.
- [ ] Criação do portal cativo (landing page HTML/CSS) focado em conscientização de segurança para o usuário final.

### Fase 4: Validação, Pesquisa e Apresentação
- [ ] Validação geral do laboratório através de simulações controladas de ataque (Red Teaming interno).
- [ ] Coleta de dados de desempenho dos sensores sob carga (análise do trade-off entre hardware de baixo custo e volume de tráfego).
- [ ] Documentação completa dos resultados obtidos.
- [ ] Estruturação do modelo de minicurso/oficina para demonstração prática e replicação da arquitetura.
