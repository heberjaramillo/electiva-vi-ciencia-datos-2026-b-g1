# Parcial Práctico – Corte 1
## Ciencia de Datos

**Estudiante:** Heber Jaramillo  
**Asignatura:** Electiva VI – Ciencia de Datos  
**Actividad:** Parcial práctico – Corte 1  
**Caso:** Taller de Motos RPM

---

## 1. Tipos de datos

Para este ejercicio se toma como caso de estudio un taller de motocicletas.

| Dato | Ejemplo | Tipo |
|---|---|---|
| Registro de ventas | Fecha, producto, cantidad, precio | Estructurado |
| Información de clientes en JSON | Nombre, teléfono, vehículo | Semiestructurado |
| Fotografías de motocicletas | Fotos de la moto antes y después del servicio | No estructurado |
| Facturas en PDF | Documento con información de la venta y del servicio | No estructurado |

### Explicación

**Datos estructurados:** tienen una organización definida en filas y columnas, como los registros de ventas.

**Datos semiestructurados:** tienen cierta organización mediante campos y etiquetas, como un archivo JSON.

**Datos no estructurados:** no tienen una estructura tabular definida, como fotografías y documentos PDF.

---

## 2. Preguntas de analítica

### Analítica descriptiva

**Pregunta:**  
¿Cuántas motocicletas fueron atendidas por el Taller de Motos RPM durante el último mes?

Esta pregunta corresponde a la **analítica descriptiva** porque busca conocer qué ocurrió en un período determinado utilizando datos históricos.

### Analítica predictiva

**Pregunta:**  
¿Cuántas motocicletas se espera que ingresen al taller durante el próximo mes?

Esta pregunta corresponde a la **analítica predictiva** porque utiliza los datos históricos para estimar un resultado futuro.

---

## 3. Diagrama del proceso de datos

```text
┌─────────────────────┐
│       FUENTE        │
│                     │
│ Ventas              │
│ Clientes            │
│ Órdenes de servicio │
│ Sensores / Fotos    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   ALMACENAMIENTO    │
│                     │
│ Base de datos       │
│ Archivos CSV/JSON   │
│ Fotografías         │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│       ANÁLISIS      │
│                     │
│ Limpieza de datos   │
│ Estadística         │
│ Analítica           │
│ Machine Learning    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    VISUALIZACIÓN    │
│                     │
│ Gráficos            │
│ Tableros            │
│ Informes            │
│ Indicadores         │
└─────────────────────┘
```

---

## 4. Difference between descriptive and predictive analytics

**Descriptive analytics explains what happened in the past using historical data.**

**Predictive analytics uses historical data to estimate what may happen in the future.**

---

## Conclusión

La ciencia de datos permite que un taller de motocicletas convierta diferentes tipos de datos en información útil para tomar decisiones. La analítica descriptiva ayuda a comprender lo que ha ocurrido, mientras que la analítica predictiva permite anticipar posibles situaciones futuras.
