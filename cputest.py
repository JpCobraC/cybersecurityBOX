import time
import math
import multiprocessing

def realizar_calculo_pesado(iteracoes):
    """Função que roda em cada núcleo individualmente"""
    pi_estimado = 0
    sinal = 1
    for i in range(1, iteracoes * 2, 2):
        pi_estimado += sinal * (4 / i)
        sinal = -sinal
        _ = math.sin(i) * math.sqrt(i)
    return pi_estimado

def testar_cpu_multicore():
    # Detecta quantos núcleos (threads) sua CPU tem
    num_nucleos = multiprocessing.cpu_count()
    iteracoes_por_nucleo = 15_000_000 # Carga por núcleo

    print(f"🔥 Iniciando Teste Multi-Core 🔥")
    print(f"Sua CPU tem {num_nucleos} núcleos lógicos detectados.")
    print(f"Executando {iteracoes_por_nucleo:,} iterações em CADA núcleo simultaneamente...\n")

    tempo_inicio = time.perf_counter()

    # Cria uma piscina de processos para usar todos os núcleos
    with multiprocessing.Pool(processes=num_nucleos) as pool:
        # Prepara a lista de tarefas (uma para cada núcleo)
        tarefas = [iteracoes_por_nucleo] * num_nucleos
        # Distribui o trabalho e aguarda todos terminarem
        pool.map(realizar_calculo_pesado, tarefas)

    tempo_fim = time.perf_counter()
    tempo_total = tempo_fim - tempo_inicio

    # Cálculo de métrica
    total_iteracoes_geral = iteracoes_por_nucleo * num_nucleos
    ops_por_segundo = total_iteracoes_geral / tempo_total

    print("--- RESULTADOS DO TESTE MULTI-CORE ---")
    print(f"Tempo total de execução com todos os núcleos: {tempo_total:.4f} segundos")
    print(f"Total de iterações processadas combinadas: {total_iteracoes_geral:,}")
    print(f"Score Multi-Thread: {int(ops_por_segundo / 1000)} pontos")

if __name__ == "__main__":
    testar_cpu_multicore()