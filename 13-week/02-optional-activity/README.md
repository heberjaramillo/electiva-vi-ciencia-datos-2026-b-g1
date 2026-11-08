# Semana 13 – Diseña un dashboard | Taller RPM'S

**Estudiante:** Heber Armando Jaramillo Sanchez  
**Programa:** Ingeniería Mecatrónica  
**Asignatura:** Ciencia de Datos  
**Proyecto integrador:** Análisis de órdenes de trabajo del Taller RPM'S

## 1. Proceso seleccionado
Seguimiento de las órdenes de trabajo de motocicletas atendidas por Taller RPM'S. El tablero permite revisar el volumen de trabajo, el porcentaje de órdenes entregadas, el tiempo técnico utilizado y el comportamiento de las órdenes por mes, estado y tipo de servicio.

## 2. Indicadores KPI y objetivos

| KPI | Resultado en la base | Objetivo propuesto | Utilidad |
|---|---:|---:|---|
| Órdenes registradas | 240 | Seguimiento del volumen mensual | Conocer la carga de trabajo |
| Órdenes entregadas (%) | 156 (65.0%) | ≥ 70 % | Vigilar el cierre y entrega de trabajos |
| Horas técnicas promedio por orden | 3.03 h | ≤ 3.0 h | Controlar el tiempo técnico empleado |

Los objetivos son metas propuestas para el ejercicio académico, no metas históricas verificadas del taller.

## 3. Boceto del dashboard
Archivo: `dashboard_semana13_rpms.png`

- Fila superior: tres tarjetas KPI para mostrar primero el volumen, la proporción de entregas y el tiempo técnico promedio.
- Zona central: tendencia mensual de órdenes y distribución por estado.
- Zona inferior: comparación de órdenes por tipo de servicio.

## 4. Filtros propuestos
- Fecha de ingreso: permite analizar un periodo.
- Marca: permite comparar Bajaj, Yamaha y AKT.
- Tipo de servicio: mecánica rápida, técnica o avanzada.

## 5. Justificación de la jerarquía visual
Los KPI se ubican arriba porque resumen rápidamente el estado general del taller. En el centro se muestran la tendencia temporal y los estados para entender el comportamiento de las órdenes. Al final se compara el tipo de servicio para identificar dónde se concentra el trabajo.

## 6. Datos utilizados
Archivo: `ordenes_trabajo_RPM.csv`. Contiene 240 órdenes simuladas para fines académicos; no son registros reales del taller.

## 7. Cómo reproducir
El archivo `crear_dashboard.py` genera la imagen a partir del CSV. Requiere Python, pandas y matplotlib.

---
**Nota:** los resultados describen exclusivamente la base simulada utilizada en esta actividad.
