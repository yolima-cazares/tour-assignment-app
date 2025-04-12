import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Configuración de página
st.set_page_config(layout="wide")
st.title("Asignador de Grupos desde el Mapa")

# Inicializamos los datos si es la primera vez que se abre la app
if "puntos" not in st.session_state:
    st.session_state.puntos = pd.DataFrame({
        "Nombre": ["Punto A", "Punto B", "Punto C", "Punto D"],
        "Lat": [46.8, 46.81, 46.82, 46.83],
        "Lon": [7.6, 7.61, 7.62, 7.63],
        "Grupo": [0, 0, 0, 0]  # Grupo 0 = sin asignar
    })

# Diccionario de colores por grupo
colores = {
    0: "gray", 1: "red", 2: "blue", 3: "green", 4: "purple",
    5: "orange", 6: "darkred", 7: "lightblue", 8: "lightgreen",
    9: "pink", 10: "cadetblue", 11: "darkpurple", 12: "beige",
    13: "darkblue", 14: "black", 15: "lightgray"
}

# Crear el mapa centrado en el promedio de las coordenadas
lat_center = st.session_state.puntos["Lat"].mean()
lon_center = st.session_state.puntos["Lon"].mean()
m = folium.Map(location=[lat_center, lon_center], zoom_start=13)

# Añadir los marcadores al mapa
for _, row in st.session_state.puntos.iterrows():
    folium.Marker(
        location=[row["Lat"], row["Lon"]],
        popup=row["Nombre"],
        icon=folium.Icon(color=colores[row["Grupo"]])
    ).add_to(m)

# Mostrar el mapa interactivo
map_data = st_folium(m, width=700, height=500)

# Si el usuario hizo clic en algún punto
if map_data and map_data.get("last_object_clicked"):
    click = map_data["last_object_clicked"]
    st.success(f"Hiciste clic en coordenadas: {click}")

    # Identificar el punto más cercano al clic
    df = st.session_state.puntos.copy()
    df["distancia"] = ((df["Lat"] - click["lat"])**2 + (df["Lon"] - click["lng"])**2)
    idx_cercano = df["distancia"].idxmin()
    nombre_punto = df.loc[idx_cercano, "Nombre"]

    st.markdown(f"**Punto seleccionado:** `{nombre_punto}`")
    grupo_nuevo = st.selectbox("Asigna a grupo (1–15):", list(range(1, 16)))
    if st.button("Guardar grupo"):
        st.session_state.puntos.at[idx_cercano, "Grupo"] = grupo_nuevo
        st.experimental_rerun()

# Mostrar tabla con asignaciones actuales
st.write("Asignaciones actuales:")
st.dataframe(st.session_state.puntos.drop(columns="distancia", errors="ignore"))
