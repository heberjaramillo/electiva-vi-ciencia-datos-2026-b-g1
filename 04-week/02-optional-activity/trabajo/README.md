# Actividad Semana 4 - Diagnóstico de datos de un proceso

## Ciencia de Datos

**Estudiante:** Heber Jaramillo  
**Asignatura:** Electiva VI - Ciencia de Datos  
**Actividad:** Diagnóstico de datos de un proceso  
**Caso de estudio:** Taller de Motos RPM  

---

## 1. Problema y pregunta de datos

### Problema

El Taller de Motos RPM genera diariamente información relacionada con las ventas de repuestos, servicios de mantenimiento, clientes, motocicletas e inventario.

Actualmente, esta información puede encontrarse en diferentes registros y formatos, lo que dificulta identificar rápidamente cuáles son los servicios y repuestos con mayor demanda.

Por esta razón, se propone utilizar Ciencia de Datos para analizar la información del taller y apoyar la toma de decisiones.

El objetivo principal es mejorar la gestión del inventario, planificar las compras de repuestos y conocer el comportamiento de los servicios realizados.

### Pregunta de datos

**¿Cuáles son los servicios y repuestos con mayor demanda en el Taller de Motos RPM y cómo puede utilizarse esta información para mejorar el inventario y la planificación de compras?**

---

## 2. Inventario de datos

Para realizar el análisis se pueden utilizar diferentes fuentes de información generadas durante las actividades del taller.

| Fuente o dato | Ejemplo | Tipo de dato |
|---|---|---|
| Registro de ventas | Fecha, producto, cantidad, precio | Estructurado |
| Registro de servicios | Tipo de servicio, fecha, costo, motocicleta | Estructurado |
| Información de clientes | Nombre, teléfono, vehículo | Semiestructurado |
| Información de motocicletas | Marca, modelo, placa, cilindraje | Estructurado |
| Inventario de repuestos | Producto, cantidad disponible, precio | Estructurado |
| Fotografías de motocicletas | Fotos antes y después del servicio | No estructurado |
| Facturas en PDF | Información de la venta y del servicio | No estructurado |
| Comentarios de clientes | Opiniones y observaciones sobre el servicio | No estructurado |

### Explicación

Los datos estructurados son aquellos que pueden organizarse fácilmente en tablas, como las ventas, el inventario y los registros de servicios.

Los datos semiestructurados tienen una organización parcial mediante etiquetas o campos, como la información almacenada en archivos JSON.

Los datos no estructurados no tienen una estructura tabular definida, como fotografías, documentos PDF y comentarios escritos por los clientes.

---

## 3. Tipo de analítica

Para este proyecto se pueden aplicar diferentes tipos de analítica de datos.

### Analítica descriptiva

La analítica descriptiva permite conocer qué ha ocurrido en el taller.

Por ejemplo:

- Identificar los repuestos más vendidos.
- Identificar los servicios más realizados.
- Conocer las ventas por periodo.
- Conocer cuáles son las motocicletas que reciben más servicios.
- Analizar el comportamiento histórico del inventario.

### Analítica diagnóstica

La analítica diagnóstica permite investigar por qué ocurrió determinado comportamiento.

Por ejemplo, se puede analizar por qué un repuesto tiene una demanda mayor que otro o por qué determinados servicios aumentan durante ciertos periodos.

### Analítica predictiva

La analítica predictiva puede utilizarse para estimar la demanda futura de repuestos y servicios.

Por ejemplo, utilizando los registros históricos se podría estimar qué repuestos tendrán mayor demanda durante las próximas semanas o meses.

### Analítica prescriptiva

La analítica prescriptiva puede utilizar los resultados anteriores para apoyar la toma de decisiones.

Por ejemplo, puede ayudar a determinar:

- Qué repuestos deberían comprarse.
- Cuántas unidades deberían mantenerse en inventario.
- Qué productos necesitan reposición.
- Cómo planificar mejor las compras.

### Analítica seleccionada

Para este proyecto se propone utilizar principalmente **analítica descriptiva y predictiva**, debido a que primero se necesita conocer el comportamiento histórico del taller y posteriormente estimar la demanda futura.

---

## 4. ¿Es un caso de Big Data?

El proyecto puede crecer hacia un escenario de Big Data si el taller comienza a almacenar grandes cantidades de información durante largos periodos y recibe información de diferentes fuentes.

Las principales características o "V" que pueden aparecer son:

### Volumen

El taller puede generar una gran cantidad de registros de ventas, servicios, clientes, motocicletas e inventario a medida que aumenta el número de operaciones.

### Velocidad

Los datos se generan continuamente durante la operación diaria del taller, especialmente con cada venta, servicio o actualización del inventario.

### Variedad

Se pueden encontrar diferentes tipos de información:

- Tablas de ventas.
- Registros de inventario.
- Archivos JSON.
- Fotografías.
- Facturas PDF.
- Comentarios de clientes.

### Veracidad

Es necesario verificar que los datos sean correctos, eliminando registros duplicados, corrigiendo errores y evitando información incompleta.

### Valor

El análisis de estos datos puede generar información útil para mejorar las compras, controlar el inventario, identificar los servicios más solicitados y apoyar las decisiones del negocio.

### Conclusión sobre Big Data

En su estado actual, el proyecto puede considerarse principalmente un proyecto de análisis de datos de un negocio pequeño. Sin embargo, puede evolucionar hacia Big Data si aumenta significativamente el volumen, velocidad y variedad de los datos almacenados.

---

## 5. Ciclo de vida del proyecto de datos

El ciclo de vida propuesto para este proyecto es:

**Pregunta → Obtener → Limpiar → Analizar → Visualizar → Decidir**

### Aplicación del ciclo

**Pregunta:** identificar cuáles son los servicios y repuestos con mayor demanda.

**Obtener:** recopilar los registros de ventas, servicios, clientes, motocicletas e inventario.

**Limpiar:** corregir errores, eliminar registros duplicados y organizar los datos.

**Analizar:** utilizar estadísticas y técnicas de análisis para encontrar patrones y tendencias.

**Visualizar:** representar los resultados mediante gráficos, tablas e indicadores.

**Decidir:** utilizar los resultados para mejorar las compras, el inventario y la planificación de los servicios.

### Diagrama del ciclo

```text
┌───────────────┐
│    PREGUNTA   │
│ ¿Qué queremos │
│   conocer?    │
└───────┬───────┘
        ↓
┌───────────────┐
│    OBTENER     │
│ Ventas, datos  │
│ e inventario   │
└───────┬───────┘
        ↓
┌───────────────┐
│    LIMPIAR     │
│ Corregir datos │
│ y duplicados   │
└───────┬───────┘
        ↓
┌───────────────┐
│    ANALIZAR    │
│ Encontrar      │
│ patrones       │
└───────┬───────┘
        ↓
┌───────────────┐
│  VISUALIZAR    │
│ Gráficos y     │
│ estadísticas   │
└───────┬───────┘
        ↓
┌───────────────┐
│    DECIDIR     │
│ Mejorar        │
│ inventario     │
└───────────────┘
---

## 6. Problem & data

The Taller de Motos RPM needs to analyze its business data to improve services and inventory management.

The data includes sales records, customer information, motorcycle information, service orders, inventory records, photographs, PDF invoices, and customer comments.

Some of these data are structured, while others are semi-structured or unstructured.

Descriptive analytics can be used to understand the services and spare parts with the highest demand.

Predictive analytics can be used to estimate future demand for spare parts and services.

The results can help the workshop make better decisions about inventory, purchasing, and customer service.
---

## 7. Conclusión

El análisis de datos aplicado al Taller de Motos RPM permite transformar los registros generados diariamente en información útil para la toma de decisiones.

Mediante la analítica descriptiva se puede conocer el comportamiento histórico del negocio, mientras que la analítica predictiva permite estimar posibles comportamientos futuros.

La información obtenida puede utilizarse para mejorar la gestión del inventario, planificar las compras de repuestos, identificar los servicios con mayor demanda y mejorar la atención de los clientes.

Este proyecto representa una aplicación práctica de la Ciencia de Datos en un proceso real de negocio.
