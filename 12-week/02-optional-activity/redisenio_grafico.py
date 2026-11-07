"""
SEMANA 12 - CIENCIA DE DATOS
Rediseño de un gráfico de producción industrial.

Los datos incluidos son SIMULADOS para demostrar el procedimiento.
Si se dispone de un CSV real, debe reemplazarse produccion_ejemplo.csv
manteniendo las columnas Mes y Unidades_producidas.
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("produccion_ejemplo.csv")

# Gráfico ANTES: eje vertical truncado, lo que exagera visualmente diferencias.
plt.figure(figsize=(10, 5.6))
plt.bar(df["Mes"], df["Unidades_producidas"], color="#4C78A8")
plt.ylim(800, 1000)
plt.title("Producción")
plt.xlabel("Mes")
plt.ylabel("Unidades")
plt.grid(axis="y", alpha=0.25)
plt.tight_layout()
plt.savefig("01_grafico_antes.png", dpi=180, bbox_inches="tight")
plt.show()

# Gráfico DESPUÉS: eje desde cero, título con conclusión y color para destacar junio.
colores = ["#9DB7C8"] * (len(df) - 1) + ["#168C83"]
plt.figure(figsize=(10, 5.6))
barras = plt.bar(df["Mes"], df["Unidades_producidas"], color=colores,
                 edgecolor="white", linewidth=0.8)
plt.ylim(0, max(df["Unidades_producidas"]) * 1.12)
plt.title(
    f"La producción aumentó de {df['Unidades_producidas'].iloc[0]} "
    f"a {df['Unidades_producidas'].iloc[-1]} unidades entre enero y junio",
    fontsize=13, weight="bold", pad=16
)
plt.xlabel("Mes")
plt.ylabel("Unidades producidas")
plt.grid(axis="y", linestyle="--", alpha=0.25)
plt.gca().set_axisbelow(True)

for barra, valor in zip(barras, df["Unidades_producidas"]):
    plt.text(barra.get_x() + barra.get_width()/2, valor + 18,
             str(valor), ha="center", va="bottom", fontsize=9)

plt.text(0.99, 0.94, "Junio: máximo del periodo",
         transform=plt.gca().transAxes, ha="right", va="top",
         color="#168C83", fontsize=9, weight="bold")
plt.tight_layout()
plt.savefig("02_grafico_despues.png", dpi=180, bbox_inches="tight")
plt.show()
