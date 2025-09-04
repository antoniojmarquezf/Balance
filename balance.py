import streamlit as st

st.set_page_config(page_title="Juego de Programación de Mantenimiento", layout="wide")

st.title("🛠️ Juego de Programación de Mantenimiento")
st.write("Distribuye las actividades en días de 8 horas de modo que desperdicies la menor cantidad de tiempo posible.")

# Lista de actividades
actividades = [2, 1, 5, 3, 2, 6, 5, 8, 7, 1, 3, 2]

st.subheader("📋 Actividades disponibles (horas)")
st.write(", ".join(map(str, actividades)))

# Sección para que el estudiante asigne actividades
st.markdown("---")
st.subheader("📅 Asigna las actividades a cada día")

num_dias = st.slider("Selecciona el número de días a programar:", 1, 10, 6)

dias = {}
for i in range(1, num_dias + 1):
    seleccion = st.multiselect(
        f"Día {i}", 
        opciones := [str(x) for x in actividades], 
        key=f"dia{i}"
    )
    dias[i] = [int(x) for x in seleccion]

# Calcular resultados
st.markdown("---")
st.subheader("📊 Resultados de tu programación")

total_sobrante = 0
total_usado = 0

for i, act in dias.items():
    suma = sum(act)
    if suma > 0:
        sobrante = 8 - suma if suma <= 8 else f"❌ Excedido en {suma-8}h"
        st.write(f"**Día {i}:** {suma} horas (Sobran: {sobrante})")
        if isinstance(sobrante, int):
            total_sobrante += sobrante
        total_usado += suma

st.markdown("---")
st.success(f"✅ Total horas usadas: {total_usado}")
st.info(f"⏳ Total horas sobrantes: {total_sobrante}")

# Opción para enviar resultados
st.markdown("---")
st.subheader("📨 Enviar tu solución")
nombre = st.text_input("Escribe tu nombre completo")
if st.button("Enviar solución"):
    if nombre.strip() == "":
        st.error("Por favor ingresa tu nombre antes de enviar.")
    else:
        st.success(f"¡Gracias {nombre}! Tu solución ha sido registrada. (Aquí se puede conectar a Google Sheets o correo)")