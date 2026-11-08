from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

carpeta = Path(__file__).parent
df = pd.read_csv(carpeta / "ordenes_trabajo_RPM.csv")
df["fecha_ingreso"] = pd.to_datetime(df["fecha_ingreso"], errors="coerce")
df["horas_tecnico"] = pd.to_numeric(df["horas_tecnico"], errors="coerce")

total = len(df)
entregadas = int((df["estado_orden"] == "Entregada").sum())
porcentaje = entregadas / total * 100 if total else 0
promedio_horas = df["horas_tecnico"].mean()
por_tipo = df["tipo_servicio"].value_counts().reindex(
    ["Mecánica rápida", "Mecánica técnica", "Mecánica avanzada"], fill_value=0
)
por_estado = df["estado_orden"].value_counts()
por_mes = df.groupby(df["fecha_ingreso"].dt.to_period("M")).size()
por_mes.index = por_mes.index.astype(str)

fig = plt.figure(figsize=(13, 8), constrained_layout=True)
gs = GridSpec(3, 3, figure=fig, height_ratios=[0.6, 1.2, 1.3])
fig.suptitle("TALLER RPM'S | DASHBOARD DE ÓRDENES DE TRABAJO",
             fontsize=17, fontweight="bold")

for i, (titulo, valor, objetivo) in enumerate([
    ("Órdenes registradas", f"{total}", "Seguimiento del volumen"),
    ("Órdenes entregadas", f"{entregadas} ({porcentaje:.1f}%)", "Objetivo propuesto: ≥ 70 %"),
    ("Horas técnicas promedio", f"{promedio_horas:.2f} h", "Objetivo propuesto: ≤ 3.0 h"),
]):
    ax = fig.add_subplot(gs[0, i])
    ax.axis("off")
    ax.text(.5, .75, titulo, ha="center", fontweight="bold")
    ax.text(.5, .40, valor, ha="center", fontsize=20)
    ax.text(.5, .08, objetivo, ha="center", fontsize=8)

ax1 = fig.add_subplot(gs[1, :2])
ax1.plot(por_mes.index, por_mes.values, marker="o")
ax1.set_title("Órdenes ingresadas por mes")
ax1.set_ylabel("Cantidad de órdenes")
ax1.tick_params(axis="x", rotation=35)
ax1.grid(axis="y", alpha=.25)

ax2 = fig.add_subplot(gs[1, 2])
ax2.bar(por_estado.index, por_estado.values)
ax2.set_title("Órdenes por estado")
ax2.set_ylabel("Cantidad")
ax2.tick_params(axis="x", rotation=35)
ax2.grid(axis="y", alpha=.25)

ax3 = fig.add_subplot(gs[2, :])
barras = ax3.barh(por_tipo.index, por_tipo.values)
ax3.invert_yaxis()
ax3.set_title("Órdenes por tipo de servicio")
ax3.set_xlabel("Cantidad de órdenes")
ax3.grid(axis="x", alpha=.25)
for barra, valor in zip(barras, por_tipo.values):
    ax3.text(valor + 1, barra.get_y() + barra.get_height()/2, str(valor), va="center")
ax3.set_xlim(0, max(por_tipo.values) * 1.15)

fig.savefig(carpeta / "dashboard_semana13_rpms.png", dpi=180, bbox_inches="tight")
print("Dashboard generado correctamente.")
