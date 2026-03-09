import streamlit as st

# Configuração da Página - Nome que aparece na aba do navegador
st.set_page_config(page_title="OGNET Resolve", page_icon="✅", layout="centered")

# Estilização Customizada (Opcional - Deixa o site com a cara da marca)
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    </style>
    """, unsafe_allow_input=True)

# Topo do Site
st.title("🛠️ OGNET Resolve")
st.subheader("O seu guia interativo para instalação de borrachas")
st.write("---")

# Passo 1: Identificação do Perfil
st.markdown("### 1. Qual modelo de borracha você recebeu?")
tipo_perfil = st.selectbox(
    "Selecione o tipo de encaixe:",
    ["Clique para selecionar...", "Borracha de Encaixe (Canaleta/Pressão)", "Borracha de Aba (Parafuso ou Rebite)", "Borracha Colada"]
)

if tipo_perfil != "Clique para selecionar...":
    
    # Passo 2: Diagnóstico do Problema
    st.markdown(f"### 2. O que está acontecendo na instalação da {tipo_perfil}?")
    
    opcoes_problema = {
        "Borracha de Encaixe (Canaleta/Pressão)": [
            "A borracha parece ser maior que a porta",
            "A borracha não para dentro da canaleta (fica saindo)",
            "Ficou uma fresta (o ímã não encosta na geladeira)",
            "A borracha veio com dobras ou amassada"
        ],
        "Borracha de Aba (Parafuso ou Rebite)": [
            "A borracha está repuxando nos cantos",
            "A porta ficou difícil de fechar",
            "Furos não alinham com os da porta"
        ],
        "Borracha Colada": [
            "A cola não está aderindo",
            "A borracha está desalinhada"
        ]
    }
    
    problema_selecionado = st.radio("Selecione o sintoma:", opcoes_problema[tipo_perfil])
    
    st.write("---")
    st.markdown("### 💡 Solução Recomendada:")

    # Lógica de Soluções para ENCAIXE
    if "maior que a porta" in problema_selecionado:
        st.success("**Técnica dos 4 Cantos:**")
        st.write("""
        Não corte a borracha! Ela apenas laceou no transporte. 
        1. Remova a borracha por completo.
        2. Encaixe primeiro os **4 ângulos (cantos)** da porta.
        3. Depois, pressione o centro de cada lateral.
        4. O 'excesso' sumirá conforme você pressiona do centro para as pontas.
        """)
        
    elif "fresta" in problema_selecionado or "amassada" in problema_selecionado:
        st.warning("**Ajuste Térmico (O Segredo da Vedação):**")
        st.write("""
        As borrachas novas precisam de memória térmica para vedar 100%.
        1. Use um **secador de cabelo** (médio) para aquecer a borracha onde há a fresta.
        2. Com a borracha morna, feche a porta e puxe-a levemente com os dedos até encostar no metal.
        3. Mantenha a porta fechada por 2 horas (use uma fita adesiva para manter a pressão se necessário).
        """)

    elif "não para dentro da canaleta" in problema_selecionado:
        st.info("**Limpeza e Verificação:**")
        st.write("""
        1. Verifique se há restos da borracha antiga ou gordura no trilho.
        2. Limpe a canaleta com um pano e álcool.
        3. Se o trilho estiver aberto (largo), você pode apertar levemente a canaleta com um alicate antes de encaixar.
        """)

# Rodapé de Suporte
st.write("---")
col1, col2 = st.columns(2)
with col1:
    st.write("Ainda precisa de ajuda?")
with col2:
    # Substitua pelo seu número real do WhatsApp
    link_whatsapp = "https://wa.me/5511994251306?text=OGNET BORRACHAS me ajuda a instalar a minha borracha!!!!!"
    st.link_button("Falar com Técnico no WhatsApp", link_whatsapp)

st.caption("OGNET-BORRACHAS Resolve - Facilitando sua instalação.")

