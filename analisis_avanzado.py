import pandas as pd
import numpy as np

def cargar_y_preparar_datos(filepath="historial_divisas.csv"):
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        print(f"No se encuentra el archivo {filepath}")
        return None
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp").reset_index(drop=True)
    return df

def calcular_indicadores_financieros(df):
    df["retorno_pct"] = df["btc_eur"].pct_change() * 100
    df["sma_3"] = df["btc_eur"].rolling(window=3).mean()
    df["volatilidad_3p"] = df["btc_eur"].rolling(window=3).std()
    return df

def generar_resumen_estadistico(df):
    precio_actual = df["btc_eur"].iloc[-1]
    precio_inicial = df["btc_eur"].iloc[0]
    variacion_total = ((precio_actual - precio_inicial) / precio_inicial) * 100

    volatilidad_media = df["retorno_pct"].std()
    maximo = df["btc_eur"].max()
    minimo = df["btc_eur"].min()

    print("\n================================================")
    print(" INFORME DE ANÁLISIS CUANTITATIVO Y ESTADÍSTICO")
    print("================================================")
    print(f"Número total de observaciones: {len(df)}")
    print(f"Precio inicial registrado:     {precio_inicial:,.2f} €")
    print(f"Precio actual (último):        {precio_actual:,.2f} €")
    print(f"Rango de precios:              Mín: {minimo:,.2f} € | Máx: {maximo:,.2f} €")
    print(f"Rendimiento total del periodo: {variacion_total:+.4f}%")
    print(f"Volatilidad (Desv Típica %):   {volatilidad_media:+.4f}%")
    print("================================================\n")

    print("Ultimos 5 registros con indicadores calculados:")
    print(df[["timestamp", "btc_eur", "retorno_pct", "sma_3"]].tail(5).to_string(index=False))

if __name__ == "__main__":
    df = cargar_y_preparar_datos()
    if df is not None and len(df) > 1:
        df = calcular_indicadores_financieros(df)
        generar_resumen_estadistico(df)
    else:
        print("Se necesitan al menos 2 registros en 'historial_divisas.csv' para calcular variaciones.")
