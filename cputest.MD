# Benchmark de CPU em Python (Multi-Core)

Este documento registra o funcionamento e os resultados práticos do script de teste de estresse e medição de desempenho de CPU desenvolvido em Python.

## 1. Objetivo do Projeto
Avaliar o poder de processamento bruto de diferentes hardwares e sistemas operacionais. O script força **100% de uso de todos os núcleos lógicos da CPU** de forma simultânea, gerando uma pontuação (*Score*) baseada em eficiência temporal.

---

## 2. Como Funciona o Script

### A. Carga de Estresse Matemático
Para garantir que o teste meça apenas o processador (sem interferência de discos lentos ou latência de internet), o script executa um loop puramente matemático:
* **Série de Leibniz para Pi:** Aproximação geométrica de número decimal, forçando o uso de ponto flutuante.
* **Funções Trigonométricas (`math.sin`) e Radiciação (`math.sqrt`):** Operações complexas que saturam a FPU (Unidade de Ponto Flutuante) do chip.

### B. Paralelismo Real (Multi-Core)
Por padrão, o Python roda em uma única linha de execução (Single-Thread). Este script utiliza a biblioteca `multiprocessing` para criar processos independentes para cada núcleo detectado pelo sistema operacional, distribuindo a carga igualmente e estressando o chip por completo.

### C. Lógica do Score (Pontuação)
O desempenho é calculado através de um cronômetro de alta precisão (`time.perf_counter`). A fórmula para a pontuação é:

$$Score = \frac{\text{Iterações por Núcleo} \times \text{Total de Núcleos}}{\text{Tempo de Execução} \times 1000}$$

*Quanto menor o tempo de execução para concluir a carga de trabalho, maior será o Score final.*

---

## 3. Resultados dos Testes de Campo

O script foi executado em cinco ambientes distintos (Arquiteturas x86 e ARM), gerando os seguintes dados comparativos:

| Dispositivo / Processador | Sistema Operacional | Núcleos | Tempo (s) | Iterações Totais | Score Final |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Intel Core Ultra 9 285H** | Windows 11 | 16 | 3.6046 | **240.000.000** | **66.581** |
| **Intel Core i5-1145G7** | Ubuntu (WSL2 em Win11) | 8 | 5.7282 | 120.000.000 | 20.949 |
| **Intel Core i5-3470** | Ubuntu Server | 4 | **3.5679** | 60.000.000 | 16.816 |
| **Rockchip RK3318** | Armbian Headless | 4 | 37.9601 | 60.000.000 | 1.580 |
| **Rockchip RK3229** | Armbian Headless | 4 | 44.1465 | 60.000.000 | 1.359 |

---

## 4. Análise Técnica dos Resultados

### 1. Desktops/Servidores vs. TV Boxes (x86 vs. ARM)
A diferença entre os processadores de arquitetura x86 (Intel) e ARM (Rockchip) é brutal. O **i5-3470** foi cerca de **10 vezes mais rápido** que o **RK3318**. Isso reflete a proposta de cada hardware: chips de TV Box priorizam consumo mínimo de energia (frequentemente < 5W), enquanto chips de Desktop priorizam vazão de dados e performance bruta.

### 2. O Embate das TV Boxes (RK3318 vs. RK3229)
O chip **RK3318** superou o **RK3229** com uma vantagem de aproximadamente **16% em velocidade**. Embora ambos tenham 4 núcleos, o RK3318 utiliza núcleos mais modernos (Cortex-A53 de 64 bits), o que garante melhor desempenho para servidores caseiros (como Pi-hole ou Home Assistant).

### 3. O Impacto do Sistema Operacional (i5-3470 vs. i5-1145G7)
O **i5-3470** (um processador antigo de 3ª geração) terminou sua carga na metade do tempo do **i5-1145G7** (11ª geração). Isso ocorreu por dois motivos:
1. **Diferença de Escopo de Trabalho:** O i5-1145G7 identificou 8 núcleos virtuais (Hyper-Threading) e processou o **dobro** de volume de dados (120 milhões de iterações) comparado aos 4 núcleos do i5-3470 (60 milhões).
2. **Sobrecarga (Overhead) do S.O.:** O i5-3470 rodou em um ambiente **Ubuntu Server limpo**, sem interface gráfica e com pouquíssimos processos em segundo plano. Já o i5-1145G7 rodou em ambiente Windows 11 com telemetria, antivírus e sincronização do OneDrive ativos, dividindo a atenção do processador.

### 4. A Alta Performance de Nova Geração (Core Ultra 9 285H)
O processador **Intel Core Ultra 9 285H** (arquitetura híbrida de nova geração com 16 núcleos lógicos sob Windows 11) atingiu o maior score registrado no teste, alcançando **66.581 pontos**. Ele processou um total massivo de **240.000.000 de iterações** em apenas **3.6046 segundos**, demonstrando a alta capacidade paralela e eficiência da nova arquitetura de CPUs móveis de alto desempenho.
