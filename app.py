import streamlit as st
import pandas as pd

st.title("🌱 Consumo Consciente IA")

st.header("📋 Seus hábitos")

# 💧 Água
tempo_banho = st.slider("Tempo médio de banho (minutos)", 1, 30, 10)
banhos_dia = st.slider("Quantidade de banhos por dia", 1, 4, 1)
lavadora_semana = st.slider("Usos da máquina de lavar por semana", 0, 14, 3)
torneira_aberta = st.radio("Lava louça com torneira aberta?", ["Sim", "Não"])

# ⚡ Energia
horas_ocioso = st.slider("Horas de TV/PC ligados sem uso por dia", 0, 10, 2)
usa_led = st.radio("Usa lâmpadas LED?", ["Sim", "Não"])
luz_desnecessaria = st.radio("Deixa luz acesa sem necessidade?", ["Sim", "Não"])

if st.button("Analisar consumo"):
    
    # 💧 Cálculo de água (estimativa simples)
    agua_banho = tempo_banho * 9 * banhos_dia  # 9L por minuto
    agua_lavadora = lavadora_semana * 100 / 7
    agua_total = agua_banho + agua_lavadora
    
    if torneira_aberta == "Sim":
        agua_total *= 1.2
    
    # ⚡ Energia (estimativa simples)
    energia_total = horas_ocioso * 0.5
    
    if usa_led == "Não":
        energia_total *= 1.3
    
    if luz_desnecessaria == "Sim":
        energia_total *= 1.2

    # 🎯 Score
    score = 100

    if tempo_banho > 15:
        score -= 20
    if horas_ocioso > 3:
        score -= 15
    if usa_led == "Não":
        score -= 10
    if torneira_aberta == "Sim":
        score -= 10

    score = max(score, 0)

    # 📊 Resultado
    st.subheader("📊 Resultado")

    st.write(f"💧 Consumo estimado de água: {agua_total:.2f} L/dia")
    st.write(f"⚡ Consumo estimado de energia: {energia_total:.2f} kWh/dia")

    st.write(f"🎯 Score sustentável: {score}/100")

    if score >= 80:
        st.success("🟢 Sustentável")
    elif score >= 50:
        st.warning("🟡 Moderado")
    else:
        st.error("🔴 Alto consumo")

    # 🧾 Feedback inteligente
    st.subheader("🧠 Sugestões")

    if tempo_banho > 15:
        st.write("🚿 Reduza o banho para até 10 minutos.")
    if torneira_aberta == "Sim":
        st.write("🚰 Feche a torneira ao ensaboar a louça.")
    if usa_led == "Não":
        st.write("💡 Troque lâmpadas por LED.")
    if horas_ocioso > 3:
        st.write("🔌 Desligue aparelhos sem uso.")
        
import matplotlib.pyplot as plt

labels = ['Água', 'Energia']
valores = [agua_total, energia_total]

fig, ax = plt.subplots()
ax.bar(labels, valores)

st.pyplot(fig)        
