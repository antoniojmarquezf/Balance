import streamlit as st

# Lista original de duraciones
durations = [5, 1, 7, 6, 2, 7, 4, 3, 6, 3, 4]

# Convertir en ítems únicos con IDs
activities = [(i, d) for i, d in enumerate(durations)]

# Guardar en session_state
if "remaining" not in st.session_state:
    st.session_state.remaining = activities
if "days" not in st.session_state:
    st.session_state.days = {f"Día {i+1}": [] for i in range(6)}

st.title("Juego de Programación de Mantenimiento")

# Selección de día
day = st.selectbox("Selecciona un día:", list(st.session_state.days.keys()))

# Selección de actividad (mostrar valor, pero guardar ID)
options = [f"ID{i}: {d}h" for i, d in st.session_state.remaining]
choice = st.selectbox("Selecciona una actividad:", options)

if st.button("Asignar"):
    if choice:
        idx = options.index(choice)
        act_id, act_val = st.session_state.remaining.pop(idx)  # quitar solo esa actividad
        st.session_state.days[day].append((act_id, act_val))

# Mostrar asignaciones
st.subheader("Distribución actual")
for d, acts in st.session_state.days.items():
    horas = sum(v for _, v in acts)
    st.write(f"**{d}** ({horas}h): {', '.join(str(v) for _, v in acts)}")

st.subheader("Actividades restantes")
st.write([v for _, v in st.session_state.remaining])
