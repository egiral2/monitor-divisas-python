# 📈 Monitor de Divisas y Criptoactivos en Tiempo Real

Sistema automatizado de captura, análisis cuantitativo y visualización de series temporales para el mercado de divisas (**EUR/USD**) y criptoactivos (**BTC/EUR**). El proyecto consume datos vivos desde APIs financieras públicas, calcula indicadores técnicos mediante `pandas` y genera informes visuales estructurados en `matplotlib`.

---

## 🚀 Características Principales

* **Ingesta de Datos en Tiempo Real:** Conexión mediante peticiones HTTP a la API pública de *CoinGecko* (Bitcoin) y del *Banco Central Europeo / Frankfurter* (tipo de cambio EUR/USD).
* **Persistencia de Datos:** Generación de estado actual en formato JSON (`reporte_financiero.json`) y almacenamiento incremental en time-series dentro de un archivo CSV (`historial_divisas.csv`).
* **Análisis Cuantitativo:** Cálculo de retornos porcentuales período a período, medias móviles simples (SMA de 3 períodos) y métricas de volatilidad (desviación típica).
* **Visualización de Datos Multi-panel:** Generación automática de gráficos técnicos en dos subplots (línea de precio + media móvil en el panel superior y diagrama de barras de rendimientos en el panel inferior).
* **Automatización del Sistema:** Preparado para ejecución periódica desatendida mediante Systemd Timers o tareas Cron.

---

## 📂 Estructura del Proyecto

| Archivo / Directorio | Descripción |
| :--- | :--- |
| `monitor.py` | Script principal de extracción de APIs, triangulación de divisas y registro de datos. |
| `analisis_avanzado.py` | Módulo estadístico basado en Pandas para el cálculo de retornos y medias móviles. |
| `graficar.py` | Motor de visualización con Matplotlib para la creación de subplots financieros. |
| `historial_divisas.csv` | Base de datos en formato time-series con el historial de capturas. |
| `.gitignore` | Configuración para la exclusión de outputs temporales (`.json`, `.png`). |

---

## 🛠️ Requisitos e Instalación

### Prerrequisitos
Python 3.10+ y las siguientes librerías de procesamiento de datos:

```bash
pip install pandas matplotlib numpy
