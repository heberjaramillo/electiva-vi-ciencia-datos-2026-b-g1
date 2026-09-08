# Actividad Calificable – Corte 1
## Diagnóstico de datos de un proceso

**Estudiante:** Heber Jaramillo  
**Asignatura:** Electiva VI – Ciencia de Datos  
**Caso de estudio:** Taller de Motos RPM  
**Corte:** 1

---

## 1. Problema y pregunta de datos

### Problema

El Taller de Motos RPM realiza diferentes servicios de mantenimiento y reparación de motocicletas. Durante el proceso se generan datos relacionados con clientes, motocicletas, órdenes de servicio, repuestos, ventas, diagnósticos y fotografías de los trabajos realizados.

Actualmente, estos datos pueden encontrarse en diferentes formatos y fuentes. Esto dificulta conocer con facilidad cuáles son los servicios más frecuentes, qué repuestos tienen mayor demanda y cuántas motocicletas se atienden durante determinados períodos.

Por esta razón, se propone utilizar Ciencia de Datos para organizar y analizar la información del taller y apoyar la toma de decisiones.

### Pregunta de datos

**¿Cuáles son los servicios y repuestos más utilizados en el Taller de Motos RPM y cuántas motocicletas se espera atender durante el próximo mes?**

Esta pregunta permite analizar información histórica del taller y posteriormente utilizarla para realizar predicciones sobre la demanda futura.

---

# 2. Inventario de datos

Para analizar el proceso se identifican diferentes fuentes y campos de información.

| Fuente o campo | Ejemplo | Tipo de dato |
|---|---|---|
| Registro de ventas | Fecha, producto, cantidad, precio | Estructurado |
| Registro de clientes | Nombre, teléfono, identificación | Estructurado |
| Registro de motocicletas | Placa, marca, modelo, kilometraje | Estructurado |
| Órdenes de servicio | Número de orden, diagnóstico, trabajo realizado | Semiestructurado |
| Información de clientes en JSON | Nombre, teléfono, vehículo y servicios | Semiestructurado |
| Fotografías de motocicletas | Fotos antes y después de la reparación | No estructurado |
| Facturas en PDF | Información de venta, cliente y servicio | No estructurado |
| Reportes de diagnóstico | Resultados de scanner y códigos de falla | Semiestructurado |

### Clasificación de los datos

### Datos estructurados

Son datos que tienen una organización definida en filas y columnas y pueden almacenarse fácilmente en una base de datos.

Ejemplos:

- Registro de ventas.
- Registro de clientes.
- Registro de motocicletas.

### Datos semiestructurados

Son datos que tienen una organización mediante campos, etiquetas o estructuras, pero no necesariamente están organizados en tablas tradicionales.

Ejemplos:

- Archivos JSON.
- Órdenes de servicio.
- Reportes de diagnóstico.

### Datos no estructurados

Son datos que no tienen una estructura tabular definida.

Ejemplos:

- Fotografías de motocicletas.
- Facturas en PDF.

---

# 3. Tipo de analítica

Para este proyecto se pueden aplicar diferentes tipos de analítica de datos.

## Analítica descriptiva

La analítica descriptiva permite conocer qué ocurrió en el pasado utilizando los datos históricos del taller.

Ejemplo:

**¿Cuántas motocicletas fueron atendidas durante cada mes y cuáles fueron los servicios más realizados?**

Esta información permitiría conocer el comportamiento histórico del negocio.

---

## Analítica diagnóstica

La analítica diagnóstica permite buscar las razones o causas de determinados resultados.

Ejemplo:

**¿Por qué aumentaron las reparaciones de motocicletas durante determinados meses?**

Se podrían comparar variables como tipo de motocicleta, kilometraje, tipo de falla y servicio realizado.

---

## Analítica predictiva

La analítica predictiva utiliza información histórica para estimar posibles resultados futuros.

Ejemplo:

**¿Cuántas motocicletas se espera que ingresen al taller durante el próximo mes?**

Para responder esta pregunta se podrían utilizar los registros históricos de órdenes de servicio y la cantidad de motocicletas atendidas por mes.

---

## Analítica prescriptiva

La analítica prescriptiva permite utilizar los resultados obtenidos para apoyar la toma de decisiones y recomendar acciones.

Ejemplo:

**¿Qué cantidad de repuestos debería tener disponible el taller para atender la demanda esperada durante el próximo mes?**

Con esta información se podría mejorar la gestión del inventario y disminuir el riesgo de quedarse sin repuestos de alta demanda.

---

# 4. ¿Es un caso de Big Data?

En su estado actual, el Taller de Motos RPM puede comenzar como un proyecto de análisis de datos convencional y no necesariamente como Big Data.

Sin embargo, el proyecto podría convertirse en un caso de Big Data si el volumen de información aumenta considerablemente y se integran diferentes fuentes de datos.

Las principales características de Big Data se pueden analizar mediante las 5 V:

### Volumen

El taller puede acumular grandes cantidades de registros de ventas, clientes, motocicletas, órdenes de servicio, fotografías y diagnósticos.

### Velocidad

Los datos pueden generarse continuamente cada vez que se realiza una venta, se recibe una motocicleta o se registra un diagnóstico.

### Variedad

Se pueden manejar diferentes tipos de información:

- Bases de datos.
- Archivos CSV.
- Archivos JSON.
- Fotografías.
- Facturas PDF.
- Información de diagnósticos.

### Veracidad

Los datos deben ser correctos y confiables. Por ejemplo, una placa, precio o cantidad de repuestos incorrecta puede afectar los resultados del análisis.

### Valor

El análisis de estos datos puede ayudar al taller a tomar mejores decisiones sobre inventario, servicios, compras y atención de clientes.

### Conclusión sobre Big Data

**El proyecto no necesita ser considerado Big Data desde el inicio, pero puede evolucionar hacia un escenario de Big Data si aumenta significativamente el volumen, velocidad y variedad de los datos.**

---

# 5. Ciclo de vida del proyecto de datos

El ciclo de vida propuesto para el proyecto es:

```text
┌─────────────────────────────┐
│       1. PREGUNTA           │
│                             │
│ ¿Qué servicios y repuestos  │
│ tienen mayor demanda?       │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       2. OBTENER DATOS      │
│                             │
│ Ventas                      │
│ Clientes                    │
│ Motocicletas                │
│ Órdenes de servicio         │
│ Inventario                  │
│ Diagnósticos                │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       3. LIMPIAR DATOS      │
│                             │
│ Eliminar duplicados         │
│ Corregir errores            │
│ Completar datos faltantes   │
│ Organizar formatos          │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       4. ANALIZAR           │
│                             │
│ Estadística                 │
│ Analítica descriptiva       │
│ Analítica diagnóstica       │
│ Analítica predictiva        │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       5. VISUALIZAR         │
│                             │
│ Gráficos                    │
│ Tableros                    │
│ Indicadores                 │
│ Informes                    │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│         6. DECIDIR          │
│                             │
│ Mejorar inventario          │
│ Planificar compras          │
│ Organizar servicios         │
│ Mejorar la atención         │
└─────────────────────────────┘
