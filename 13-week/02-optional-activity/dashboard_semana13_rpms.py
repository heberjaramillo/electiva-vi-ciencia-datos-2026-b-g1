"""
SEMANA 13 - CIENCIA DE DATOS
Dashboard técnico de Taller RPM'S.
Datos simulados para fines académicos.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Leer la base de órdenes de trabajo
df = pd.read_csv("ordenes_rpms.csv")

# Calcular indicadores usando únicamente órdenes cerradas
cerradas = df[df["estado"] == "Cerrada"]

ordenes_cerradas = len(cerradas)
tiempo_promedio = cerradas["horas_reparacion"].mean()
reparaciones_a_tiempo = (
    cerradas["horas_reparacion"] <= cerradas["horas_objetivo"]
).mean() * 100

print("DASHBOARD TÉCNICO - TALLER RPM'S")
print("--------------------------------")
print(f"Órdenes cerradas: {ordenes_cerradas}")
print(f"Tiempo promedio de reparación: {tiempo_promedio:.2f} horas")
print(f"Reparaciones a tiempo: {reparaciones_a_tiempo:.1f}%")

# Gráfico 1: órdenes recibidas por mes
df["fecha_recepcion"] = pd.to_datetime(df["fecha_recepcion"])
df["mes"] = df["fecha_recepcion"].dt.month

ordenes_mes = df.groupby("mes").size()
nombres_meses = {
    1: "Enero", 2: "Febrero", 3: "Marzo",
    4: "Abril", 5: "Mayo", 6: "Junio"
}
etiquetas = [nombres_meses[m] for m in ordenes_mes.index]

plt.figure(figsize=(9, 5))
plt.bar(etiquetas, ordenes_mes.values)
plt.title("Órdenes de trabajo recibidas por mes - Taller RPM'S")
plt.xlabel("Mes")
plt.ylabel("Cantidad de órdenes")
plt.ylim(0, max(ordenes_mes.values) + 2)
plt.grid(axis="y", alpha=0.25)
plt.tight_layout()
plt.savefig("ordenes_por_mes_rpms.png", dpi=160)
plt.show()

# Gráfico 2: tiempo promedio por tipo de servicio
tiempos_servicio = (
    cerradas.groupby("tipo_servicio")["horas_reparacion"].mean().sort_values()
)

plt.figure(figsize=(9, 5))
tiempos_servicio.plot(kind="barh")
plt.title("Tiempo promedio por tipo de servicio - Taller RPM'S")
plt.xlabel("Horas promedio")
plt.ylabel("Tipo de servicio")
plt.tight_layout()
plt.savefig("tiempo_por_servicio_rpms.png", dpi=160)
plt.show()
