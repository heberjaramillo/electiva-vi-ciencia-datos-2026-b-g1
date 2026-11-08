# Semana 14 – Medidas DAX para Taller RPM'S

**Estudiante:** Heber Armando Jaramillo Sanchez  
**Programa:** Ingeniería Mecatrónica  
**Asignatura:** Ciencia de Datos  
**Proyecto integrador:** Análisis de órdenes de trabajo de Taller RPM'S

## 1. Problema que se analiza

En un taller se necesita saber cuántas motocicletas ya fueron entregadas y qué proporción representan frente a todas las órdenes recibidas. Esto ayuda a revisar el flujo de trabajo y detectar acumulación de órdenes pendientes, en reparación o canceladas.

## 2. Datos utilizados

Se utiliza la misma base maestra del proyecto: `ordenes_trabajo_RPM.csv`, con 240 registros simulados. Incluye motocicletas Bajaj, Yamaha y AKT; mecánica rápida, técnica y avanzada; fechas, servicios, estados y valores.

**Nota:** los datos son simulados para fines académicos y no corresponden a facturas ni órdenes reales.

## 3. Preparación en Power BI

1. Abrir Power BI Desktop.
2. Seleccionar **Obtener datos → Texto/CSV**.
3. Importar `ordenes_trabajo_RPM.csv`.
4. En Power Query, comprobar que `fecha_ingreso` y `fecha_entrega` sean fechas, y que `horas_tecnico`, `mano_obra_cop`, `repuestos_cop` y `total_cop` sean numéricos.
5. Cargar los datos.
6. En el panel de campos, cambiar el nombre de la tabla a `OrdenesRPM`.
7. Seleccionar **Modelado → Nueva medida** y crear las dos medidas de abajo.

## 4. Medidas DAX

### Medida 1: órdenes entregadas

```dax
Ordenes Entregadas =
CALCULATE(
    COUNTROWS(OrdenesRPM),
    OrdenesRPM[estado_orden] = "Entregada"
)
```

Cuenta las filas de la tabla cuyo estado es “Entregada”. En el conjunto simulado actual, el resultado es **156 órdenes**.

### Medida 2: porcentaje de órdenes entregadas

```dax
Porcentaje Ordenes Entregadas =
DIVIDE(
    [Ordenes Entregadas],
    COUNTROWS(OrdenesRPM),
    0
)
```

Divide las órdenes entregadas entre el total de órdenes. En la base actual, el resultado es **65 %** (156 de 240). En Power BI, seleccionar la medida y darle formato de porcentaje.

## 5. Antes y después: mejora aplicada

**Enfoque menos conveniente:** crear una columna calculada que repita una marca de 1 o 0 por cada registro y luego sumar esa columna para contar las entregadas. Para el porcentaje, también se podría guardar otro cálculo fila por fila.

**Enfoque utilizado:** crear medidas DAX. `CALCULATE` aplica el filtro de estado al momento de consultar; `COUNTROWS` cuenta las filas bajo ese filtro y `DIVIDE` calcula el porcentaje de forma segura cuando el denominador es cero.

**¿Por qué es mejor para este caso?** Las medidas se calculan según los filtros y segmentadores del informe (por ejemplo, marca, tipo de mecánica o fecha). No se almacena una columna adicional para estos dos indicadores. `DIVIDE` evita un error de división por cero.

## 6. Cómo comprobar los resultados

Crear dos tarjetas en la vista Informe:
- Tarjeta 1: `Ordenes Entregadas` → debe mostrar **156**.
- Tarjeta 2: `Porcentaje Ordenes Entregadas` → debe mostrar **65,0 %**.

Se pueden agregar segmentadores para `marca`, `tipo_servicio` y `fecha_ingreso` para explorar los resultados por marca, área de trabajo y periodo.

## 7. Conclusión

Las dos medidas permiten conocer el volumen de órdenes que ya fueron entregadas y su proporción frente al total registrado. Esto aporta una lectura sencilla del flujo de trabajo de Taller RPM'S y permite analizarlo por marca, tipo de mecánica y fecha.

## 8. Archivos

- `ordenes_trabajo_RPM.csv`: base de datos maestra simulada.
- `medidas_rpms.dax`: fórmulas DAX de la actividad.
- `README.md`: explicación y pasos de desarrollo.
