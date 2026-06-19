# app.py

import streamlit as st
import pandas as pd
import joblib

# ============================
# CONFIGURACIÓN
# ============================

st.set_page_config(
    page_title="Predicción de Viviendas",
    page_icon="🏠",
    layout="wide"
)

# ============================
# CARGA DEL MODELO
# ============================

modelo = joblib.load("modelo.pkl")

# ============================
# TÍTULO
# ============================

st.title("🏠 Predicción del Valor de Vivienda")

st.markdown("""
Ingrese las características de la zona y la vivienda para estimar
el valor medio de una propiedad.
""")

# ============================
# SIDEBAR
# ============================

st.sidebar.header("Características")

longitud = st.sidebar.slider(
    "Longitud",
    min_value=-124.35,
    max_value=-114.31,
    value=-118.49,
    step=0.01
)

latitud = st.sidebar.slider(
    "Latitud",
    min_value=32.54,
    max_value=41.95,
    value=34.26,
    step=0.01
)

edad_mediana_vivienda = st.sidebar.slider(
    "Edad mediana vivienda",
    min_value=1,
    max_value=52,
    value=29
)

total_habitaciones = st.sidebar.number_input(
    "Total habitaciones",
    min_value=1,
    value=2127
)

total_dormitorios = st.sidebar.number_input(
    "Total dormitorios",
    min_value=1,
    value=435
)

poblacion = st.sidebar.number_input(
    "Población",
    min_value=1,
    value=1166
)

hogares = st.sidebar.number_input(
    "Hogares",
    min_value=1,
    value=409
)

ingreso_mediano = st.sidebar.slider(
    "Ingreso mediano",
    min_value=0.5,
    max_value=15.0,
    value=3.54,
    step=0.01
)

proximidad_oceano = st.sidebar.selectbox(
    "Proximidad al océano",
    [
        "<1H OCEAN",
        "INLAND",
        "NEAR OCEAN",
        "NEAR BAY",
        "ISLAND"
    ]
)

# ============================
# DATAFRAME DE ENTRADA
# ============================

entrada = pd.DataFrame({
    "longitud": [longitud],
    "latitud": [latitud],
    "edad_mediana_vivienda": [edad_mediana_vivienda],
    "total_habitaciones": [total_habitaciones],
    "total_dormitorios": [total_dormitorios],
    "poblacion": [poblacion],
    "hogares": [hogares],
    "ingreso_mediano": [ingreso_mediano],
    "proximidad_oceano": [proximidad_oceano]
})

# ============================
# BOTÓN DE PREDICCIÓN
# ============================

if st.button("Realizar Predicción"):

    prediccion = modelo.predict(entrada)[0]

    st.success("Predicción completada")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Valor estimado de la vivienda",
            f"${prediccion:,.0f}"
        )

    with col2:
        st.metric(
            "Ingreso mediano",
            f"{ingreso_mediano:.2f}"
        )

    st.subheader("Datos ingresados")

    st.dataframe(
        entrada,
        use_container_width=True
    )

# ============================
# INFORMACIÓN
# ============================

with st.expander("Información del modelo"):
    st.write("""
    Este modelo estima el valor medio de una vivienda utilizando:

    - Ubicación geográfica
    - Edad de las viviendas
    - Habitaciones y dormitorios
    - Población
    - Hogares
    - Ingreso mediano
    - Proximidad al océano
    """)
