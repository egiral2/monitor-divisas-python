import pandas as pd
import matplotlib.pyplot as plt
from analisis_avanzado import cargar_y_preparar_datos, calcular_indicadores_financieros

def generar_grafico_avanzado():
    df = cargar_y_preparar_datos()
    if df is None or len(df) < 2:
        print("No hay suficientes datos")
        return
    df = calcular_indicadores_financieros(df)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    ax1.plot(df["timestamp"], df["btc_eur"], marker="o", color="orange", label="precio BTC(€)", linewidth=2)
    ax1.plot(df["timestamp"], df["sma_3"], linestyle="--", color="blue", label="SMA (3p)", alpha=0.8)
    ax1.set_title("Análisis financiero de Bitcoin (EUR)", fontsize=14)
    ax1.set_ylabel("Precio (€)")
    ax1.grid(True, linestyle="--", alpha=0.5)
    ax1.legend()

    ancho_barra = 2 / 1440
    ax2.bar(
        df["timestamp"], 
        df["retorno_pct"], 
        width=ancho_barra, 
        color=df["retorno_pct"].apply(lambda x: "green" if x >= 0 else "red"), 
        alpha=0.7
    )
    ax2.axhline(0, color="black", linestyle="--", linewidth=0.8)
    ax2.set_ylabel("Retorno (%)")
    ax2.set_xlabel("Fecha / Hora")
    ax2.grid(True, linestyle="--", alpha=0.5)

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("analisis_tecnico.png")
    print("Gráfico avanzado guardado con éxito como 'analisis_tecnico.png'")

if __name__ == "__main__":
    generar_grafico_avanzado()
