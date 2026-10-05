# C2 Activity — Modelo, consulta y limpieza de datos

**Estudiante:** Heber Jaramillo  
**Caso de estudio:** Taller de Motos RPM  
**Corte:** 2  
**Semana:** 9

## 1. ERD

El modelo de datos representa la operación básica de un taller de motocicletas. Se definieron cinco entidades: `CLIENTE`, `VEHICULO`, `ORDEN_TRABAJO`, `DIAGNOSTICO` y `REPARACION`.

Las relaciones principales son:

- Cliente 1:N Vehículo.
- Vehículo 1:N Orden de trabajo.
- Orden de trabajo 1:1 Diagnóstico.
- Orden de trabajo 1:N Reparación.

El diagrama completo se encuentra en [`erd/erd.md`](erd/erd.md).

## 2. Dataset y limpieza

Se utilizó un dataset **simulado** de 31 registros de órdenes de servicio correspondientes a septiembre de 2026. El dataset contiene fecha, tipo de servicio, marca, modelo, kilometraje, costo e identificación del mecánico.

### Antes y después

| Métrica | Antes | Después |
|---|---:|---:|
| Filas | 32 | 31 |
| Valores nulos | 2 | 0 |
| Duplicados | 1 | 0 |

### Procesos realizados

1. Se cargó el CSV utilizando `pandas`.
2. Se revisaron dimensiones, tipos, valores nulos y duplicados.
3. Se transformó `fecha` al tipo `datetime`.
4. Se convirtieron `kilometraje` y `costo` a valores numéricos.
5. Se estandarizaron los formatos de texto y nombres.
6. Los valores numéricos faltantes se imputaron utilizando la mediana.
7. El mecánico faltante se identificó como `No Registrado`.
8. Se eliminó el registro duplicado.
9. Se volvió a validar el dataset después de la limpieza.

## 3. Preguntas y consultas

### Pregunta 1

**¿Qué tipo de servicio generó mayores ingresos durante septiembre de 2026?**

Se utilizó una agrupación por `tipo_servicio` y una suma del campo `costo`.

**Resultado:** el tipo de servicio con mayor ingreso fue **Motor**, con aproximadamente **$2,125,000**.

### Pregunta 2

**¿Qué mecánico atendió más órdenes y cuál fue su ingreso promedio?**

Se agrupó por `mecanico`, contando órdenes y calculando el promedio de `costo`.

**Resultado:** **Carlos** atendió más órdenes, con **11 órdenes** y un ingreso promedio aproximado de **$118,636**.

---

## Data & cleaning

The dataset contains simulated motorcycle workshop service records from September 2026. It includes the service date, service type, motorcycle brand and model, mileage, service cost, and mechanic. The dataset was loaded into Python using pandas and inspected for missing values, duplicated records, incorrect data types, and inconsistent text formats. Missing numeric values were imputed using the median, while a missing mechanic value was replaced with a descriptive category. Duplicate records were removed and dates, numbers, and text fields were standardized. Two questions were answered using pandas filters, grouping, counting, and aggregation to identify the service type with the highest revenue and the mechanic with the highest number of orders.

## 4. Archivos

- `data/produccion_septiembre.csv` — dataset original con problemas de calidad simulados.
- `data/produccion_septiembre_limpio.csv` — dataset limpio.
- `notebooks/c2_activity.ipynb` — código completo en pandas.
- `erd/erd.md` — ERD y cardinalidades.

## 5. Conclusión

El ejercicio demuestra un flujo básico de ciencia de datos: modelar el dominio, cargar datos, detectar problemas de calidad, limpiar los registros y realizar consultas mediante agregaciones. El resultado permite obtener información útil para la gestión de un taller.
