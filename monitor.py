import json
import urllib.request
from datetime import datetime

def obtener_precio_crypto():
    """Obtiene el precio actual de Bitcoin en EUR usando una API pública."""
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=eur"
    
    try:
        # Petición a la red
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            return data["bitcoin"]["eur"]
    except Exception as e:
        print(f"❌ Error al consultar Bitcoin: {e}")
        return None

def obtener_tipo_cambio_eur_usd():
    """Obtiene el tipo de cambio EUR/USD oficial del Banco Central Europeo."""
    url = "https://api.frankfurter.app/latest?from=EUR&to=USD"
    
    try:
        # Añadimos la cabecera User-Agent para evitar el error 403
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            return data["rates"]["USD"]
    except Exception as e:
        print(f"❌ Error al consultar tipo de cambio EUR/USD: {e}")
        return None

def generar_reporte():
    print("🔄 Conectando con los servidores financieros...")
    
    btc_eur = obtener_precio_crypto()
    eur_usd = obtener_tipo_cambio_eur_usd()
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if btc_eur and eur_usd:
        # Cálculo derivado: Precio de BTC expresado en USD a través del tipo de cambio
        btc_usd = btc_eur * eur_usd
        
        reporte = {
            "timestamp": fecha_actual,
            "btc_eur": btc_eur,
            "eur_usd": eur_usd,
            "btc_usd": round(btc_usd, 2)
        }
        
        print("\n=== 📈 REPORTE FINANCIERO EN TIEMPO REAL ===")
        print(f"Fecha: {fecha_actual}")
        print(f"1 EUR = {eur_usd:.4f} USD")
        print(f"1 BTC = {btc_eur:,.2f} EUR")
        print(f"1 BTC = {btc_usd:,.2f} USD (Calculado)")
        print("===========================================\n")
        
        # Guardar en JSON
        with open("reporte_financiero.json", "w", encoding="utf-8") as f:
            json.dump(reporte, f, indent=4)
        print("✅ Reporte guardado en 'reporte_financiero.json'")
    else:
        print("❌ No se pudieron obtener todos los datos.")

if __name__ == "__main__":
    generar_reporte()
