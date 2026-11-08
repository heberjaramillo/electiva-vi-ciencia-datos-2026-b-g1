import pandas as pd
import matplotlib.pyplot as plt

# Leer la base de órdenes (debe estar en la misma carpeta)
df = pd.read_csv("ordenes_trabajo_RPM.csv")
df["fecha_ingreso"] = pd.to_datetime(df["fecha_ingreso"])

# Resample: contar órdenes al inicio de cada mes
serie = (df.set_index("fecha_ingreso")
           .resample("MS").size().rename("ordenes").to_frame())

# Media móvil de tres meses
serie["media_movil_3m"] = serie["ordenes"].rolling(3, min_periods=1).mean()
serie.to_csv("serie_temporal_mensual.csv", index_label="mes")

# Gráfico de evolución
ax = serie[["ordenes", "media_movil_3m"]].plot(marker="o", figsize=(10, 5))
ax.set_title("Las órdenes mensuales fluctúan; la media móvil suaviza los cambios")
ax.set_xlabel("Mes de ingreso")
ax.set_ylabel("Cantidad de órdenes")
ax.set_ylim(bottom=0)
ax.grid(axis="y", alpha=0.25)
plt.tight_layout()
plt.savefig("01_evolucion_temporal.png", dpi=180)
plt.close()

# Gráfico de comparación por tipo de servicio
comparacion = df.groupby("tipo_servicio").size().sort_values(ascending=False)
ax = comparacion.plot(kind="bar", figsize=(9, 5))
ax.set_title("El servicio técnico concentra la mayor cantidad de órdenes")
ax.set_xlabel("Tipo de servicio")
ax.set_ylabel("Cantidad de órdenes")
ax.set_ylim(bottom=0)
ax.grid(axis="y", alpha=0.25)
plt.tight_layout()
plt.savefig("02_comparacion_servicios.png", dpi=180)
plt.close()
