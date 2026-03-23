# app.py
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Consumo Consciente IA", layout="wide")

st.title("🌱 Consumo Consciente IA")
st.write("Avalie seu consumo de água 💧 e energia ⚡ com base em dados reais.")

# ----------------------
# 💧 ENTRADA - ÁGUA
# ----------------------
st.header("💧 Consumo de Água")

col1, col2 = st.columns(2)

with col1:
    tempo_banho = st.slider("Tempo médio de banho (min)", 1, 30, 10)
    banhos_dia = st.slider("Banhos por dia", 1, 4, 1)
    descargas = st.slider("Descargas por dia", 0, 20, 5)

with col2:
    torneira_cozinha = st.slider("Uso torneira cozinha (min/dia)", 0, 60, 10)
    torneira_banheiro = st.slider("Uso torneira banheiro (min/dia)", 0, 30, 5)
    maquina_lavar = st.slider("Máquina de lavar (vezes/semana)", 0, 14, 3)

# ----------------------
# ⚡ ENTRADA - ENERGIA
# ----------------------
st.header("⚡ Consumo de Energia (horas por dia)")

consumo_aparelhos = {
    "TV": 0.1,
    "Video Game": 0.15,
    "TV Box": 0.05,
    "Soundbar": 0.05,
    "Ar Condicionado": 1.5,
    "Geladeira": 0.15,
    "Forno Elétrico": 2.0,
    "Cooktop": 1.5,
    "Micro-ondas": 1.2,
    "Lava Louça": 1.0,
    "Air Fryer": 1.4,
    "Máquina de Lavar": 0.5,
    "Máquina de Lavar e Secar": 1.0,
    "Computador": 0.2,
    "Notebook": 0.05,
    "Smartphone": 0.01
}

horas = {}

for aparelho in consumo_aparelhos:
    horas[aparelho] = st.slider(aparelho, 0, 24, 1)

# ----------------------
# 🚀 BOTÃO
# ----------------------
if st.button("Analisar consumo"):

    # 💧 Cálculo água
    agua_total = 0
    agua_total += tempo_banho * 9 * banhos_dia
    agua_total += descargas * 6
    agua_total += torneira_cozinha * 8
    agua_total += torneira_banheiro * 6
    agua_total += maquina_lavar * 100 / 7

    # ⚡ Cálculo energia
    energia_total = 0
    consumo_individual = {}

    for aparelho in consumo_aparelhos:
        consumo = horas[aparelho] * consumo_aparelhos[aparelho]
        consumo_individual[aparelho] = consumo
        energia_total += consumo

    # ----------------------
    # 📊 CLASSIFICAÇÃO
    # ----------------------
    def classificar_agua(consumo):
        if consumo < 120:
            return "🟢 Baixo"
        elif consumo <= 180:
            return "🟡 Médio"
        else:
            return "🔴 Alto"

    def classificar_energia(consumo):
        if consumo < 4:
            return "🟢 Baixo"
        elif consumo <= 7:
            return "🟡 Médio"
        else:
            return "🔴 Alto"

    # ----------------------
    # 📊 RESULTADO
    # ----------------------
    st.header("📊 Resultado")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("💧 Água")
        st.write(f"Consumo: {agua_total:.1f} L/dia")
        st.write("Média Brasil: 150 L/dia")
        st.write(classificar_agua(agua_total))

    with col2:
        st.subheader("⚡ Energia")
        st.write(f"Consumo: {energia_total:.2f} kWh/dia")
        st.write("Média Brasil: 6 kWh/dia")
        st.write(classificar_energia(energia_total))

    # ----------------------
    # 📈 GRÁFICO
    # ----------------------
    st.subheader("📈 Consumo por aparelho")

    nomes = list(consumo_individual.keys())
    valores = list(consumo_individual.values())

    fig, ax = plt.subplots()
    ax.barh(nomes, valores)
    st.pyplot(fig)

    # ----------------------
    # 🧠 FEEDBACK
    # ----------------------
    st.subheader("🧠 Sugestões inteligentes")

    if tempo_banho > 15:
        st.write("🚿 Reduza o banho para até 10 minutos.")
    if energia_total > 7:
        st.write("⚡ Reduza o uso de aparelhos de alto consumo.")
    if horas["Ar Condicionado"] > 8:
        st.write("❄️ Use o ar-condicionado com moderação.")

    # ----------------------
    # 🏢 IMPACTO COLETIVO
    # ----------------------
    st.subheader("🏢 Impacto no condomínio")

    moradores = st.slider("Número de moradores", 1, 500, 50)

    st.write(f"💧 Total: {agua_total * moradores:.0f} L/dia")
    st.write(f"⚡ Total: {energia_total * moradores:.2f} kWh/dia")

# requirements.txt
# streamlit
# matplotlib

# README.md
# Consumo Consciente IA
# Projeto para análise de consumo sustentável com IA leve.
# Deploy via Streamlit Cloud.
