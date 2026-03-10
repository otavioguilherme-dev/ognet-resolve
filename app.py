import streamlit as st
import os

# Configuração da Página
st.set_page_config(page_title="OGNET Resolve", page_icon="✅", layout="centered")

# --- CONFIGURAÇÕES DO WHATSAPP ---
NUMERO_WHATSAPP = "5511994251306"  # COLOQUE SEU NÚMERO AQUI (com DDD e sem espaços)
MENSAGEM_PADRAO = "Olá! Usei o OGNET Resolve mas ainda preciso de ajuda com minha borracha."

# Inicializa a memória da escolha (Session State)
if 'tipo' not in st.session_state:
    st.session_state.tipo = None

st.title("🛠️ OGNET Resolve")
st.subheader("O seu guia interativo para instalação de borrachas")
st.write("---")

# 1. Menu Visual de Modelos
st.markdown("### 1. Identifique seu modelo pelo visual:")
col1, col2, col3 = st.columns(3)

with col1:
    if os.path.exists("encaixe.jpg"):
        st.image("encaixe.jpg", caption="Modelo de Encaixe")
    else:
        st.info("📸 Foto: Encaixe")
    if st.button("Modelo Encaixe", key="btn_encaixe"):
        st.session_state.tipo = "Encaixe"

with col2:
    if os.path.exists("aba.jpg"):
        st.image("aba.jpg", caption="Modelo de Aba")
    else:
        st.info("📸 Foto: Aba")
    if st.button("Modelo Aba", key="btn_aba"):
        st.session_state.tipo = "Aba"

with col3:
    if os.path.exists("colado.jpg"):
        st.image("colado.jpg", caption="Modelo Colado")
    else:
        st.info("📸 Foto: Colado")
    if st.button("Modelo Colado", key="btn_colado"):
        st.session_state.tipo = "Colado"

st.write("---")

# 2. Só mostra as dúvidas SE o cliente escolheu um tipo
if st.session_state.tipo is not None:
    tipo_selecionado = st.session_state.tipo
    st.markdown(f"### 2. Qual o problema ou dúvida na instalação da borracha de **{tipo_selecionado}**?")

    opcoes_problema = {
        "Encaixe": [
            "A borracha parece ser maior que a porta, ficou sobrando na lateral ou comprimento",
            "A borracha não para dentro da canaleta (fica saindo)",
            "Ficou uma fresta, tem vãos ou aberturas (o ímã não encosta na geladeira)",
            "A borracha veio com dobras, amassada ou esta enrugada",
            "A borracha nao pega pressão, a porta nao fica fechada",
            "A porta ficou difícil de fechar"
        ],
        "Aba": [
            "A borracha está repuxando nos cantos",
            "A porta ficou difícil de fechar ou nao para fechada",
            "A borracha nao tem furos, como montar na porta"
            "A borracha parece ser maior que a porta",
            "A borracha não para dentro da canaleta (fica saindo)",
            "Ficou uma fresta, tem vãos ou aberturas (o ímã não encosta na geladeira)",
            "A borracha veio com dobras, amassada ou esta enrugada",
            "A borracha nao pega pressão, a porta nao fica fechada"
        ],
        "Colado": [
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
    
    problema = st.radio("Selecione o sintoma:", opcoes_problema[tipo_selecionado])
    
    st.divider()
    st.markdown("### 💡 Solução OGNET:")

    if "maior que a porta" in problema:
        st.success("**Técnica dos 4 Cantos:**")
        st.write("Não corte! Encaixe os 4 cantos primeiro e depois empurre o meio para as pontas.")
    
    elif "fresta" in problema or "amassada" in problema:
        st.warning("**Ajuste Térmico:**")
        st.write("Use um secador de cabelo para aquecer e moldar a borracha até encostar no metal.")
    
    # BOTÃO WHATSAPP NO FINAL DA SOLUÇÃO
    st.write("---")
    st.write("A solução acima não resolveu seu caso?")
    link_wa = f"https://wa.me/{NUMERO_WHATSAPP}?text={MENSAGEM_PADRAO}"
    st.link_button("🆘 Chamar Técnico no WhatsApp", link_wa)

# --- BARRA LATERAL (SIDEBAR) ---
st.sidebar.title("Suporte OGNET")
if st.sidebar.button("🔄 Reiniciar Guia"):
    st.session_state.tipo = None
    st.rerun()

st.sidebar.write("---")
st.sidebar.write("Precisa de atendimento humano?")
link_wa_sidebar = f"https://wa.me/5511994251306?text=OGNET RESOLVE, PRECISO DE AJUDA!!!"
st.sidebar.link_button("Falar com Especialista VIA WhatsApp", link_wa_sidebar)













