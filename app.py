import streamlit as st

# Configuração da Página
st.image("LOGO_BANNER.jpg", width=800)

# Estilização Customizada CORRIGIDA
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Topo do Site
st.title("🛠️ OGNET Resolve")
st.subheader("O seu guia interativo para instalação das borrachas")
st.write("---")

# Passo 1: Identificação do Perfil
st.markdown("### 1. Identifique seu modelo pelo visual:")

# Cria 3 colunas lado a lado
col1, col2, col3 = st.columns(3)

with col1:
    st.image("encaixe.jpg", caption="Modelo de Encaixe")
    if st.button("Selecionar Encaixe"):
        st.session_state.tipo = "Encaixe"

with col2:
    st.image("aba.jpg", caption="Modelo de Aba")
    if st.button("Selecionar Aba"):
        st.session_state.tipo = "Aba"

with col3:
    st.image("colado.jpg", caption="Modelo Colado")
    if st.button("Selecionar Colado"):
        st.session_state.tipo = "Colado"

# Lógica para mostrar as dúvidas após o clique
if 'tipo' in st.session_state:
    st.info(f"Você selecionou: Borracha de {st.session_state.tipo}")
    # Aqui entra o restante do seu código de dúvidas...
    
    # Passo 2: Diagnóstico do Problema
    st.markdown(f"### 2. Qual esta sendo o seu problema ? Ou qual sua duvida na insstalação da {tipo_perfil}?")
    
    opcoes_problema = {
        "Borracha de Encaixe (Canaleta/Pressão)": [
            "A borracha parece ser maior que a porta, ficou sobrando na lateral ou comprimento",
            "A borracha não para dentro da canaleta (fica saindo)",
            "Ficou uma fresta, tem vãos ou aberturas (o ímã não encosta na geladeira)",
            "A borracha veio com dobras, amassada ou esta enrugada",
            "A borracha nao pega pressão, a porta nao fica fechada",
            "A porta ficou difícil de fechar"
        ],
        "Borracha de Aba (Parafuso ou Rebite)": [
            "A borracha está repuxando nos cantos",
            "A porta ficou difícil de fechar ou nao para fechada",
            "A borracha nao tem furos, como montar na porta"
            "A borracha parece ser maior que a porta",
            "A borracha não para dentro da canaleta (fica saindo)",
            "Ficou uma fresta, tem vãos ou aberturas (o ímã não encosta na geladeira)",
            "A borracha veio com dobras, amassada ou esta enrugada",
            "A borracha nao pega pressão, a porta nao fica fechada"
        ],
        "Borracha Colada": [
            "A cola não está aderindo",
            "A borracha está desalinhada"
            "A porta ficou difícil de fechar ou nao para fechada",
            "A borracha nao tem furos, como montar na porta"
            "A borracha parece ser maior que a porta",
            "A borracha não para dentro da canaleta (fica saindo)",
            "Ficou uma fresta, tem vãos ou aberturas (o ímã não encosta na geladeira)",
            "A borracha veio com dobras, amassada ou esta enrugada",
            "A borracha nao pega pressão, a porta nao fica fechada"
        ]
    }
    
    problema_selecionado = st.radio("Selecione o sintoma:", opcoes_problema[tipo_perfil])
    
    st.write("---")
    st.markdown("### 💡 Solução Recomendada:")

    # Lógicas de Solução
    if "maior que a porta" in problema_selecionado:
        st.success("**Técnica dos 4 Cantos:**")
        st.image("4cantos.jpg", caption="Comece sempre pelos cantos")
        st.write("Não corte a borracha! Encaixe primeiro os 4 cantos e depois os centros, em modelos de encaixe é muito comum o cliente instalar um canto e ir esticando a borracha pro outro lado isso faz com que a borracha estique e fique sobrando tanto no comprimento quanto na largura. Caso a sua ja tenha esticado, basta refazer a instalacao colocando os 4 cantos e depois pressionar o centros.")
        
    elif "fresta" in problema_selecionado or "amassada" in problema_selecionado:
        st.warning("**Ajuste Térmico:**")
        st.write("Use um secador de cabelo para aquecer a borracha e moldá-la até o gabinete.")

    else:
        st.info("Siga as instruções padrão de limpeza e pressão para garantir a aderência.")
        
# Rodapé de Suporte
st.write("---")
col1, col2 = st.columns(2)
with col1:
    st.write("Ainda precisa de ajuda?")
with col2:
    # Substitua pelo seu número real do WhatsApp
    link_whatsapp = "https://wa.me/5511994251306?text=OGNET BORRACHAS me ajude a instalar a minha borracha!!!!!"
    st.link_button("Falar com Técnico no WhatsApp", link_whatsapp)

st.caption("OGNET-BORRACHAS Resolve - Facilitando sua instalação.")












