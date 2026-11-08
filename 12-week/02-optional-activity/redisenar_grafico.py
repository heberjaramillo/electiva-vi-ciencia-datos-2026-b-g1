import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

carpeta = Path(__file__).parent
df = pd.read_csv(carpeta / "ordenes_trabajo_RPM.csv")
conteos = df["tipo_servicio"].value_counts().reindex(
    ["Mecánica rápida", "Mecánica técnica", "Mecánica avanzada"]
)
porcentajes = conteos / len(df) * 100

# ANTES: gráfico circular con efectos visuales.
fig, ax = plt.subplots(figsize=(8, 5))
ax.pie(conteos.values, labels=conteos.index, autopct="%1.0f%%",
       startangle=140, explode=(0.08, 0.08, 0.08), shadow=True)
ax.set_title("Servicios del taller")
fig.tight_layout()
fig.savefig(carpeta / "01_grafico_antes.png", dpi=180, bbox_inches="tight")
plt.close(fig)

# DESPUÉS: barras horizontales con escala desde cero y etiquetas.
fig, ax = plt.subplots(figsize=(9, 5.2))
barras = ax.barh(conteos.index, conteos.values)
ax.invert_yaxis()
ax.set_xlim(0, max(conteos.values) * 1.18)
ax.set_xlabel("Cantidad de órdenes (de 240)")
ax.set_title("La mecánica técnica concentra el 40 % de las órdenes del taller", pad=16)
ax.grid(axis="x", alpha=0.25)
ax.set_axisbelow(True)
for barra, cantidad, porcentaje in zip(barras, conteos.values, porcentajes.values):
    ax.text(barra.get_width() + 2, barra.get_y() + barra.get_height()/2,
            f"{cantidad} órdenes ({porcentaje:.0f} %)", va="center")
fig.tight_layout()
fig.savefig(carpeta / "02_grafico_despues.png", dpi=180, bbox_inches="tight")
plt.close(fig)

print("Gráficos generados correctamente.")
