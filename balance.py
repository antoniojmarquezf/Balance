import streamlit as st

st.set_page_config(page_title="Juego de Programación de Mantenimiento", layout="wide")

st.title("🛠️ Juego de Programación de Mantenimiento")
st.write("Distribuye las actividades en 6 días de 8 horas. Una vez uses una actividad, desaparecerá de las opciones siguientes.")

# Lista inicial de actividades
if "actividades" not in st.session_state:
    st.session_state.actividades = [2, 1, 5, 3, 2, 6, 5, 8, 7, 1, 3, 2, 3]

actividades = st.session_state.actividades.copy()

st.subheader("📋 Actividades disponibles (horas)")
st.write(", ".join(map(str, actividades)))

# Número de días
num_dias = st.slider("Selecciona el número de días a programar:", 1, 10, 6)

dias = {}
usadas = []

# Ciclo de asignación día por día
for i in range(1, num_dias + 1):
    # Calcular las opciones disponibles (excluyendo ya usadas)
    opciones_disponibles = [str(x) for x in actividades if x not in usadas or usadas.count(x) < actividades.count(x)]

    seleccion = st.multiselect(
        f"Día {i} (elige actividades, máximo 8h)", 
        opciones_disponibles,
        key=f"dia{i}"
    )
    seleccion = [int(x) for x in seleccion]
    dias[i] = seleccion
    usadas.extend(seleccion)

# Resultados
st.markdown("---")
st.subheader("📊 Resultados de tu programación")

total_sobrante = 0
total_usado = 0

for i, act in dias.items():
    if act:
        suma = sum(act)
        sobrante = 8 - suma if suma <= 8 else f"❌ Excedido en {suma-8}h"
        st.write(f"**Día {i}:** {suma} horas → Actividades: {act} (Sobran: {sobrante})")
        if isinstance(sobrante, int):
            total_sobrante += sobrante
        total_usado += suma

st.markdown("---")
st.success(f"✅ Total horas usadas: {total_usado}")
st.info(f"⏳ Total horas sobrantes: {total_sobrante}")

# Botón para reiniciar
if st.button("🔄 Reiniciar juego"):
    st.session_state.actividades = [2, 1, 5, 3, 2, 6, 5, 8, 7, 1, 3, 2]
    for key in list(st.session_state.keys()):
        if key.startswith("dia"):
            del st.session_state[key]
    st.experimental_rerun()

