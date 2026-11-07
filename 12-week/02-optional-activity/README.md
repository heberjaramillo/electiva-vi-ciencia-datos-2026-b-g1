# Semana 12 – Rediseño de un gráfico

**Asignatura:** Ciencia de Datos  
**Unidad:** Unidad 3 – Análisis temporal, visualización y optimización  
**Actividad:** Rediseña un gráfico  
**Caso de estudio:** Producción industrial  
**Estudiante:** Heber Armando Jaramillo Sanchez  
**Periodo:** 2026-B

## 1. Objetivo
Aplicar principios de visualización para mejorar la lectura e interpretación de los datos de producción industrial.

## 2. Datos utilizados
Se utilizaron datos simulados de unidades producidas entre enero y junio. Estos valores son exclusivamente demostrativos y deben reemplazarse por datos reales si el profesor exige trabajar con el conjunto de datos de clase.

| Mes | Unidades producidas |
|---|---:|
| Enero | 820 |
| Febrero | 860 |
| Marzo | 845 |
| Abril | 910 |
| Mayo | 940 |
| Junio | 980 |

## 3. Diagnóstico del gráfico original
El gráfico inicial presenta un eje vertical que comienza en 800 unidades en lugar de cero. Esta escala truncada exagera visualmente las diferencias entre los meses. Además, el título “Producción” no comunica qué conclusión debe obtener el lector.

![Gráfico antes](imagenes/01_grafico_antes.png)

## 4. Rediseño aplicado
Se mantuvo el gráfico de barras porque permite comparar cantidades entre categorías temporales discretas. El eje vertical comienza en cero para representar las diferencias proporcionalmente. Se agregó un título que resume el comportamiento observado, etiquetas con los valores y un color de acento para destacar junio, que registra la mayor producción.

![Gráfico después](imagenes/02_grafico_despues.png)

## 5. Justificación (3–4 líneas)
Se corrigió el eje vertical para evitar que las diferencias entre meses se vieran exageradas y facilitar una comparación honesta. Se conservó el gráfico de barras porque es adecuado para comparar la producción mensual. También se incorporó un título con la conclusión principal y etiquetas de datos para facilitar la lectura. Finalmente, se utilizó un color de acento para destacar el mes con mayor producción.

## 6. Conclusión
En el conjunto de ejemplo, la producción pasó de 820 unidades en enero a 980 en junio. El rediseño permite comunicar esta evolución de manera más clara, precisa y visualmente honesta.

## 7. Archivos incluidos
- `produccion_ejemplo.csv`: datos de ejemplo.
- `redisenio_grafico.py`: código para generar los gráficos.
- `imagenes/01_grafico_antes.png`: gráfico original.
- `imagenes/02_grafico_despues.png`: gráfico rediseñado.

**Nota:** Los datos son simulados. No deben presentarse como registros reales de una empresa.
