# Semana 12 – Rediseña un gráfico | Taller RPM'S

**Estudiante:** Heber Armando Jaramillo Sanchez  
**Programa:** Ingeniería Mecatrónica  
**Asignatura:** Ciencia de Datos  
**Proyecto integrador:** Análisis de órdenes de trabajo del Taller RPM'S

## 1. Objetivo
Rediseñar una visualización para comunicar con claridad cómo se distribuyen las órdenes de trabajo según el tipo de servicio.

## 2. Datos utilizados
Se utiliza la base maestra `ordenes_trabajo_RPM.csv`, con 240 registros simulados. No son órdenes reales ni representan ingresos reales del taller.

| Tipo de servicio | Órdenes | Porcentaje |
|---|---:|---:|
| Mecánica rápida | 72 | 30 % |
| Mecánica técnica | 96 | 40 % |
| Mecánica avanzada | 72 | 30 % |
| **Total** | **240** | **100 %** |

## 3. Gráfico antes
Archivo: `01_grafico_antes.png`

Se presenta un gráfico circular con efectos visuales y separación de sectores. Aunque permite ver proporciones, dificulta comparar con precisión las cantidades y no destaca una conclusión.

## 4. Gráfico después
Archivo: `02_grafico_despues.png`

Se utiliza un gráfico de barras horizontales. El eje de cantidades comienza en cero, se muestran los valores y porcentajes y el título comunica el hallazgo principal.

## 5. Justificación del rediseño (3–4 líneas)
Se reemplazó el gráfico circular con efectos por barras horizontales, porque facilitan comparar las cantidades entre categorías.  
La escala comienza en cero para representar las diferencias de forma honesta.  
Se añadieron etiquetas con cantidad y porcentaje, y un título que comunica la conclusión principal: la mecánica técnica representa el 40 % de las órdenes.  
Se mantuvo un diseño limpio para que la información sea fácil de leer.

## 6. Código para reproducir los gráficos
El archivo `redisenar_grafico.py` genera las dos imágenes a partir del CSV. Requiere Python, pandas y matplotlib.

## 7. Conclusión
En esta base simulada, la mecánica técnica es la categoría con mayor participación (40 %), mientras que mecánica rápida y avanzada representan cada una el 30 %. Esta visualización permite identificar rápidamente dónde se concentra la mayor cantidad de órdenes.

---
**Nota académica:** todos los registros son simulados y se usan únicamente con fines educativos.
