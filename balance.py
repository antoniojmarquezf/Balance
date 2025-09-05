import streamlit as st

# Datos de entrada
duraciones = [5, 1, 7, 6, 2, 7, 4, 3, 6, 3, 4]
horas_por_dia = 8
dias = 6

st.title("Planificador de Actividades en 6 días de 8 horas")

# Inicializar contenedores para los días
agenda = [[] for _ in range(dias)]
horas_usadas = [0] * dias

# Copia de las duraciones para ir asignando
pendientes = duraciones.copy()

# Algoritmo sencillo: colocar cada actividad en el primer día donde quepa
for d in duraciones:
    asignado = False
    for i in range(dias):
        if horas_usadas[i] + d <= horas_por_dia:
            agenda[i].append(d)
            horas_usadas[i] += d
            asignado = True
            break
    if asignado:
        pendientes.remove(d)

# Calcular resultados
horas_libres = [horas_por_dia - h for h in horas_usadas]
total_horas_libres = sum(horas_libres)

# Mostrar resultados
for i in range(dias):
    st.subheader(f"Día {
