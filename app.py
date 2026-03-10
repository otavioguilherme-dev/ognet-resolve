import streamlit as st
import os

# Configuração da Página
st.set_page_config(page_title="OGNET Resolve", page_icon="✅", layout="centered")

# --- CONFIGURAÇÕES DO WHATSAPP ---
NUMERO_WHATSAPP = "5511994251306"
MENSAGEM_PADRAO = "Olá! Usei o OGNET Resolve mas ainda preciso de ajuda com minha borracha."

# 1. Primeiro CRIAMOS as colunas (Definição)
# O esquema [1, 4, 1] dá muito mais espaço para a imagem no meio
col_esq, col_meio, col_dir = st.columns([1, 4, 1])

# 2. Depois USAMOS a coluna criada (Execução)
with col_meio:
    if os.path.exists(ARQUIVO_LOGO):
        # Para aumentar o tamanho, usamos width. Tente 500 ou 600.
        st.image(ARQUIVO_LOGO, width=800)
    else:
        st.info("Aguardando upload do arquivo LOGO_BANNER.jpg")

# Títulos centralizados logo abaixo do banner
st.markdown("<h1 style='text-align: center;'>OGNET Resolve</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>O seu guia interativo para instalação de borrachas</p>", unsafe_allow_html=True)
st.write("---")

# --- BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    if os.path.exists(ARQUIVO_LOGO):
        st.image(ARQUIVO_LOGO, use_container_width=True)
    
    st.title("Suporte OGNET")
    if st.sidebar.button("🔄 Reiniciar Guia"):
        st.session_state.tipo = None
        st.rerun()

    st.write("---")
    st.write("Precisa de atendimento humano?")
    link_wa_sidebar = f"https://wa.me/{NUMERO_WHATSAPP}?text=OGNET%20RESOLVE,%20PRECISO%20DE%20AJUDA!!!"
    st.sidebar.link_button("Falar com Especialista", link_wa_sidebar)

# --- CONTEÚDO CENTRAL ---
# Centralizando o Logo no topo
col_esq, col_meio, col_dir = st.columns([1, 2, 1])
with col_meio:
    if os.path.exists(ARQUIVO_LOGO):
        st.image(ARQUIVO_LOGO, use_container_width=True)

st.markdown("<h1 style='text-align: center;'>OGNET Resolve</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>O seu guia interativo para instalação de borrachas</p>", unsafe_allow_html=True)
st.write("---")

# Inicializa a memória da escolha (Session State)
if 'tipo' not in st.session_state:
    st.session_state.tipo = None

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

    # Dicionário corrigido (adicionado vírgulas faltantes)
    opcoes_problema = {
        "Encaixe": [
            "A borracha parece ser maior que a porta",
            "A borracha não para dentro da canaleta (fica saindo)",
            "Ficou uma fresta, tem vãos ou aberturas",
            "A borracha veio com dobras ou amassada",
            "A borracha nao pega pressão/porta nao fecha",
            "A porta ficou difícil de fechar"
        ],
        "Aba": [
            "A borracha está repuxando nos cantos",
            "A porta ficou difícil de fechar",
            "A borracha nao tem furos, como montar",
            "A borracha parece ser maior que a porta",
            "Ficou uma fresta ou vãos de abertura"
        ],
        "Colado": [
            "A cola não está aderindo",
            "A borracha está desalinhada",
            "A porta ficou difícil de fechar",
            "Ficou uma fresta ou vão"
        ]
    }
    
    problema = st.radio("Selecione o sintoma:", opcoes_problema[tipo_selecionado])
    
    st.divider()
    st.markdown("### 💡 Solução OGNET:")

    if "maior que a porta" in problema:
        st.success("**Técnica dos 4 Cantos:**")
        st.write("Não corte! Encaixe os 4 cantos primeiro e depois empurre o meio para as pontas.")
        
    
    elif "fresta" in problema or "amassada" in problema or "vãos" in problema:
        st.warning("**Ajuste Térmico:**")
        st.write("Use um secador de cabelo para aquecer e moldar a borracha até encostar no metal. Feche a porta e aguarde esfriar.")
        
    
    else:
        st.info("Certifique-se de que a superfície esteja limpa e aplique pressão uniforme por toda a extensão.")

    # BOTÃO WHATSAPP NO FINAL DA SOLUÇÃO
    st.write("---")
    st.write("A solução acima não resolveu seu caso?")
    link_wa = f"https://wa.me/5511994251306?text=OGNET RESOLVE PRECISO DE AJUDA!!!!!"
    st.link_button("🆘 Chamar Técnico no WhatsApp", link_wa)












