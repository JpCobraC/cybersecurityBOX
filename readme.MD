# Laboratório Portátil de Cibersegurança com TV Box

## Sobre o Projeto

A proposta consiste no desenvolvimento de um laboratório portátil de cibersegurança utilizando TV Box recicladas ou descaracterizadas como infraestrutura computacional de baixo custo. A ideia central é reaproveitar dispositivos normalmente subutilizados para executar ferramentas reais de monitoramento, detecção de intrusão e análise de tráfego de rede, criando um ambiente prático para ensino, pesquisa e experimentação em segurança da informação.

## Arquitetura e Ferramentas

Cada TV Box pode assumir uma função específica dentro do laboratório, como:
- Execução de honeypots para captura de tentativas de invasão.
- Sistemas IDS/IPS para detecção de atividades suspeitas na rede.
- Servidores de monitoramento e coleta de logs.
- Dashboards para visualização de eventos em tempo real.

Ferramentas como **Cowrie**, **Suricata**, **Grafana** e **Wireshark** podem ser utilizadas na composição da arquitetura experimental.

## Objetivos e Impacto

O diferencial da proposta está na combinação entre **sustentabilidade tecnológica**, **baixo custo** e **aplicabilidade educacional**. Em vez de depender exclusivamente de servidores convencionais ou laboratórios caros, o projeto busca demonstrar que dispositivos ARM reciclados podem oferecer desempenho suficiente para atividades introdutórias e intermediárias em cibersegurança, especialmente em instituições com restrição orçamentária.

Além da aplicação didática, o projeto permite a realização de análises quantitativas sobre:
- Consumo energético.
- Desempenho computacional.
- Estabilidade operacional.
- Capacidade de processamento de eventos de segurança.

Dessa forma, a pesquisa pode contribuir tanto para a área de ensino de computação quanto para estudos relacionados a edge computing, computação verde e infraestrutura distribuída de segurança.

## Portabilidade

Outro ponto relevante é a portabilidade da solução. O laboratório pode ser facilmente transportado e montado em diferentes ambientes, permitindo sua utilização em oficinas, minicursos, atividades extensionistas e demonstrações práticas. Isso amplia o potencial de democratização do acesso a ambientes experimentais de cibersegurança.

A expectativa é avaliar até que ponto dispositivos de baixo custo podem atuar como sensores distribuídos de segurança, oferecendo uma alternativa viável para formação prática em redes e segurança da informação.

## A Ideia: Ponto de Acesso Falso Educacional

Se a sua TV Box tiver uma placa Wi-Fi compatível com modo monitor (ou se você espetar um dongle USB de R$ 20 que aceite), você pode programar um script em Python para criar um ponto de acesso falso automatizado que intercepta requisições DNS dos celulares ao redor, exibindo uma página de alerta educacional sobre os perigos de Wi-Fi público.
