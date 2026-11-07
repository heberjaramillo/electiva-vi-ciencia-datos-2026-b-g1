        "Órdenes de trabajo recibidas por mes - Taller RPM'S",
        fontsize=13,
        fontweight="bold",
    )
    ax.set_xlabel("Mes")
    ax.set_ylabel("Cantidad de órdenes")
    ax.set_ylim(0, max(meses_con_datos.values) * 1.20 + 1)
    ax.grid(axis="y", alpha=0.25)
    ax.set_axisbelow(True)

    for barra, valor in zip(barras, meses_con_datos.values):
        ax.text(
            barra.get_x() + barra.get_width() / 2,
            barra.get_height(),
            str(int(valor)),
            ha="center",
            va="bottom",
        )

    plt.xticks(rotation=25, ha="right")
    fig.tight_layout()
    ruta_salida = CARPETA_GRAFICOS / "ordenes_por_mes_rpms.png"
    fig.savefig(ruta_salida, dpi=160, bbox_inches="tight")
    plt.close(fig)
    print(f"Gráfico guardado en: {ruta_salida}")


# ------------------------------------------------------------
# 5. GRÁFICO 2: TIEMPO PROMEDIO POR TIPO DE SERVICIO
# ------------------------------------------------------------

def crear_grafico_tiempo_servicio(datos: pd.DataFrame) -> None:
    cerradas = datos[
        datos["estado"].str.casefold() == "cerrada"
    ].copy()

    cerradas = cerradas.dropna(
        subset=["tipo_servicio", "horas_reparacion"]
    )

    if cerradas.empty:
        print("No hay órdenes cerradas válidas para el gráfico por servicio.")
        return

    tiempos_servicio = (
        cerradas.groupby("tipo_servicio")["horas_reparacion"]
        .mean()
        .sort_values()
    )

    fig, ax = plt.subplots(figsize=(10, 6))
    barras = ax.barh(tiempos_servicio.index, tiempos_servicio.values)

    ax.set_title(
        "Tiempo promedio por tipo de servicio - Taller RPM'S",
        fontsize=13,
        fontweight="bold",
    )
    ax.set_xlabel("Horas promedio")
    ax.set_ylabel("Tipo de servicio")
    ax.grid(axis="x", alpha=0.25)
    ax.set_axisbelow(True)

    for barra, valor in zip(barras, tiempos_servicio.values):
        ax.text(
            valor,
            barra.get_y() + barra.get_height() / 2,
            f" {valor:.2f} h",
            va="center",
        )

    fig.tight_layout()
    ruta_salida = CARPETA_GRAFICOS / "tiempo_por_servicio_rpms.png"
    fig.savefig(ruta_salida, dpi=160, bbox_inches="tight")
    plt.close(fig)
    print(f"Gráfico guardado en: {ruta_salida}")


# ------------------------------------------------------------
# 6. PROGRAMA PRINCIPAL
# ------------------------------------------------------------

def main() -> None:
    try:
        datos = cargar_datos(ARCHIVO_DATOS)
        kpi = calcular_indicadores(datos)

        mostrar_indicadores(kpi)
        crear_grafico_ordenes_mes(datos)
        crear_grafico_tiempo_servicio(datos)

        # Guardar una tabla resumen con los indicadores.
        resumen = pd.DataFrame(
            [
                {"Indicador": "Órdenes registradas", "Resultado": kpi["total_ordenes"]},
                {"Indicador": "Órdenes cerradas", "Resultado": kpi["ordenes_cerradas"]},
                {"Indicador": "Órdenes en proceso", "Resultado": kpi["ordenes_en_proceso"]},
                {"Indicador": "Tiempo promedio (horas)", "Resultado": kpi["tiempo_promedio"]},
                {"Indicador": "Reparaciones a tiempo (%)", "Resultado": kpi["porcentaje_a_tiempo"]},
            ]
        )

        ruta_resumen = CARPETA_SALIDA / "resumen_kpi_rpms.csv"
        resumen.to_csv(ruta_resumen, index=False, encoding="utf-8-sig")

        print(f"\nResumen de KPI guardado en: {ruta_resumen}")
        print("Proceso terminado correctamente.")

    except (FileNotFoundError, ValueError, pd.errors.ParserError) as error:
        print(f"\nERROR: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
