import streamlit as st

# Lista original de duraciones
durations = [5, 1, 7, 6, 2, 7, 4, 3, 6, 3, 4]
horas_por_dia = 8
num_dias = 6

# Convertir en ítems únicos con IDs
activities = [(i, d) for i, d in enumerate(durations)]

# Guardar en session_state
if "remaining" not in st.session_state:
    st.session_state.remaining = activities
if "days" not in st.session_state:
    st.session_state.days = {f"Día {i+1}": [] for i in range(num_dias)}

st.title("🎮 Juego de Programación de Mantenimiento")

# Selección de día
day = st.selectbox("📅 Selecciona un día:", list(st.session_state.days.keys()))

# Selección de actividad (mostrar valor, pero guardar ID)
options = [f"ID{i}: {d}h" for i, d in st.session_state.remaining]
choice = st.selectbox("🔧 Selecciona una actividad:", options)

# Botón asignar
if st.button("Asignar"):
    if choice:
        idx = options.index(choice)
        act_id, act_val = st.session_state.remaining[idx]

        # Verificar horas acumuladas en ese día
        horas_usadas = sum(v for _, v in st.session_state.days[day])
        if horas_usadas + act_val <= horas_por_dia:
            # Se puede asignar
            st.session_state.remaining.pop(idx)  # quitar solo esa actividad
            st.session_state.days[day].append((act_id, act_val))
            st.success(f"✅ Actividad de {act_val}h asignada a {day}")
        else:
            st.error(f"❌ No se puede asignar {act_val}h a {day}, superaría las {horas_por_dia}h")

# Mostrar asignaciones
st.subheader("📊 Distribución actual")
total_libres = 0
for d, acts in st.session_state.days.items():
    horas_usadas = sum(v for _, v in acts)
    horas_libres = horas_por_dia - horas_usadas
    total_libres += horas_libres
    st.write(f"**{d}** → {horas_usadas}h usadas, {horas_libres}h libres")
    st.write(f"Actividades: {', '.join(str(v) for _, v in acts) if acts else 'Ninguna'}")

# Mostrar actividades restantes
st.subheader("⏳ Actividades restantes")
restantes = [v for _, v in st.session_state.remaining]
st.write(restantes)
st.write(f"Suma total de actividades sin programar: {sum(restantes)}h")

# Resumen general
st.subheader("📌 Resumen")
st.write(f"Total de horas libres en los {num_dias} días: {total_libres}h")
