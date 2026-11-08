# Semana 14 - Análisis temporal y visualización | Taller RPM'S

## Objetivo
Analizar la evolución mensual de las órdenes de trabajo, calcular una media móvil de tres meses, comparar tipos de servicio y crear medidas DAX para los indicadores.

## Datos y alcance
Se utiliza la base maestra académica de 240 órdenes simuladas del Taller RPM'S. No son registros reales. La fecha analizada es `fecha_ingreso`, entre 2026-01-05 y 2026-10-31.

## 1. Serie temporal: resample y media móvil
El archivo `analisis_temporal.py` convierte `fecha_ingreso` a fecha, la establece como índice y aplica `resample('MS').size()` para contar órdenes por mes. Después calcula `rolling(window=3, min_periods=1).mean()` como media móvil de tres meses. Los resultados quedan en `serie_temporal_mensual.csv`.

Órdenes por mes: Jan 2026: 22, Feb 2026: 22, Mar 2026: 25, Apr 2026: 24, May 2026: 25, Jun 2026: 24, Jul 2026: 25, Aug 2026: 25, Sep 2026: 24, Oct 2026: 24.

Interpretación: los conteos mensuales presentan variaciones. La media móvil reduce el efecto de cambios puntuales y permite observar mejor el comportamiento general. Con solo diez meses de datos no se puede afirmar que exista estacionalidad anual recurrente; harían falta varios años para comparar los mismos meses.

## 2. Visualizaciones
- `01_evolucion_temporal.png`: evolución mensual y media móvil de tres meses. El título comunica que hay fluctuaciones y que la media móvil las suaviza.
- `02_comparacion_servicios.png`: compara la cantidad de órdenes por tipo de servicio. Valores: Mecánica técnica: 96, Mecánica avanzada: 72, Mecánica rápida: 72. El servicio técnico concentra 96 de 240 órdenes (40%).

Ambos gráficos parten de cero en el eje de cantidades y muestran unidades explícitas.

## 3. Medidas DAX
El archivo `medidas_rpms.dax` contiene dos medidas: `Total Ordenes` cuenta las filas de la tabla y `Media Movil 3 Meses` calcula el promedio mensual de órdenes dentro de los tres meses que terminan en la fecha del contexto.

Para usar la media móvil, importa el CSV con el nombre `OrdenesRPM`, crea una tabla `Calendario` con una columna `Fecha`, marca esa tabla como tabla de fechas y relaciona `Calendario[Fecha]` con `OrdenesRPM[fecha_ingreso]`. Las medidas se recalculan con los filtros del informe, por lo que permiten analizar periodos y categorías sin crear columnas repetidas.

## Findings

The dataset contains 240 simulated workshop work orders recorded from January to October 2026. Monthly order counts change over time, so the series does not show a perfectly constant level. The three-month moving average smooths short-term fluctuations and makes the general direction easier to observe. The evolution chart compares the monthly order count with this moving average. The comparison chart shows that technical service represents the largest share of work orders, with 96 orders (40%) compared with 72 quick-service orders and 72 advanced-service orders. Because the dataset covers only ten months and one year, it is not enough to confirm a recurring annual seasonal pattern.


## Archivos
- `analisis_temporal.py`: código reproducible de análisis y gráficos.
- `ordenes_trabajo_RPM.csv`: base de datos usada.
- `serie_temporal_mensual.csv`: resultado del resample y media móvil.
- `01_evolucion_temporal.png` y `02_comparacion_servicios.png`: visualizaciones.
- `medidas_rpms.dax`: medidas para Power BI.
