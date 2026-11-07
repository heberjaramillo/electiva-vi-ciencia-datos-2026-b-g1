# Semana 13 – Diseño de dashboard técnico | Taller RPM'S

**Estudiante:** Heber Armando Jaramillo Sanchez  
**Programa:** Ingeniería Mecatrónica  
**Asignatura:** Ciencia de Datos  
**Periodo:** 2026-B  
**Proceso:** Seguimiento técnico de órdenes de trabajo.

## 1. Proceso seleccionado
Control técnico de las órdenes de trabajo de motocicletas atendidas en Taller RPM'S. El tablero permite observar el volumen de órdenes cerradas, el tiempo promedio de reparación y el porcentaje de reparaciones terminadas dentro del tiempo objetivo.

## 2. Tres KPI y sus objetivos

| KPI | Fórmula | Resultado simulado | Objetivo |
|---|---|---:|---:|
| Órdenes cerradas | Conteo de órdenes con estado Cerrada | 34 | ≥ 34 en el periodo |
| Tiempo promedio de reparación | Promedio de horas de las órdenes cerradas | 3.40 h | ≤ 4,0 h |
| Reparaciones a tiempo | Órdenes cerradas dentro de horas objetivo / órdenes cerradas × 100 | 88.2% | ≥ 90% |

## 3. Boceto del dashboard
El tablero contiene tres tarjetas KPI en la parte superior, un gráfico de barras con órdenes recibidas por mes y un gráfico horizontal con el tiempo promedio por tipo de servicio. Incluye filtros propuestos de periodo, tipo de servicio y técnico.

![Dashboard técnico](imagenes/dashboard_tecnico_rpms.png)

## 4. Filtros
- Periodo: filtra por fecha de recepción.
- Tipo de servicio: mantenimiento preventivo, diagnóstico eléctrico, reparación de motor, frenos, transmisión o inyección electrónica.
- Técnico: permite revisar las órdenes asignadas a cada técnico.

Los tres filtros se pueden implementar en Power BI usando las columnas existentes del CSV.

## 5. Justificación de la jerarquía visual
Los KPI se ubican arriba porque resumen el estado técnico del taller de forma inmediata. El gráfico de órdenes por mes permite reconocer la carga de trabajo y su evolución. El gráfico de tiempo por servicio ayuda a identificar qué trabajos requieren más horas y dónde revisar procedimientos. Los filtros quedan en la parte superior para segmentar el análisis sin ocultar los indicadores principales.

## 6. Conclusión
En el conjunto simulado se cerraron 34 órdenes de trabajo. El tiempo promedio de reparación fue 3.40 horas y el 88.2% de las órdenes cerradas se terminó dentro del tiempo objetivo. Estos indicadores permiten estudiar carga de trabajo, duración y cumplimiento técnico.

**Nota:** Los registros y objetivos son simulados para fines académicos; no representan resultados reales de Taller RPM'S.
