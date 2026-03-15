import streamlit as st
import os

# 1. CONFIGURAÇÃO DA PÁGINA (Sempre o primeiro comando Streamlit)
st.set_page_config(page_title="Bem vindo a OGNET Resolve", page_icon="✅", layout="centered")

# 2. DEFINIÇÃO DAS VARIÁVEIS (Defina o nome do arquivo AQUI)
# Isso evita o NameError nas linhas abaixo
ARQUIVO_LOGO = "LOGO_BANNER.jpg" 
NUMERO_WHATSAPP = "5511994251306"

# 3. CONTEÚDO DA BARRA LATERAL (SIDEBAR)
with st.sidebar:
    if os.path.exists(ARQUIVO_LOGO):
        st.image(ARQUIVO_LOGO, use_container_width=True)
    
    st.title("FALAR COM SUPORTE OGNET BORRACHAS")
    # ... resto do código da sidebar ...

# 4. CONTEÚDO CENTRAL (BANNER)
col_esq, col_meio, col_dir = st.columns([1, 4, 1])
with col_meio:
    # Agora o Python já sabe o que é ARQUIVO_LOGO porque definimos no passo 2
    if os.path.exists(ARQUIVO_LOGO):
        st.image(ARQUIVO_LOGO, width=1000) 
    else:
        st.info("Aguardando upload do arquivo LOGO_BANNER.jpg")
  

    st.write("---")

    link_wa_sidebar = f"https://wa.me/{NUMERO_WHATSAPP}?text=OGNET%20RESOLVE,%20PRECISO%20DE%20AJUDA!!!"
    st.sidebar.link_button("Falar com Especialista", link_wa_sidebar)
st.markdown("<h1 style='text-align: center;'>OGNET Resolve</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Bem vindo a OGNET Resolve o seu instalador on line de Borrachas</p>", unsafe_allow_html=True)
st.write("---")

# Inicializa a memória da escolha (Session State)
if 'tipo' not in st.session_state:
    st.session_state.tipo = None

# 1. Menu Visual de Modelos
st.markdown("### 1. Identifique seu modelo pelo visual:")
col1, col2, col3 = st.columns(3)

with col1:
    if os.path.exists("ENCAIXE.jpg"):
        st.image("ENCAIXE.jpg", caption="Modelo de Encaixe")
    else:
        st.info("📸 Foto: Encaixe")
    if st.button("Modelo Encaixe", key="btn_encaixe"):
        st.session_state.tipo = "Encaixe"

with col2:
    if os.path.exists("PARAFUSADO.jpg"):
        st.image("PARAFUSADO.jpg", caption="Modelo de Aba")
    else:
        st.info("📸 Foto: Aba")
    if st.button("Modelo Aba", key="btn_aba"):
        st.session_state.tipo = "Aba"

with col3:
    if os.path.exists("INJETADO.jpg"):
        st.image("INJETADO.jpg", caption="Modelo Colado")
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
            "A borracha parece ser maior que a porta ou ficou sobrando ?",
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
        st.write("""
       Este erro é muito comum de acontecer, a borracha estica na hora da instalação ou quando e removida da caixa, mas fique tranquilo isso não é um problema que não possa ser corrigido!

Seguindo a risca nossas orientações iremos fazer a nova borracha voltar pra medida padrão e assim poderemos reinstalar!",

1 - Desliguea geladeira e inicie o processo de deixar a borracha aberta ao sol por cerca de 1 ou 2 horas, ate ela ficar bem mole(maleável) Caso não tenha sol você pode usar um secador dou soprador de calor ou ainda coloca-la em um balde com agua morna.

2 - retirar do sol e colocar no piso frio pra esfriar (com esse processo ela vai dilatar com o calor e no piso frio ela esfria e encolhe, voltando a medida padrão de fabrica, deixar 1 a 3 horas no chão frio).

3 - A instalação deve ser feita SEMPRE encaixando os 4 cantos (os 2 de cima e os 2 baixo) e somente depois de encaixar os CANTOS deve-se pressionar o meio da borracha, isso evita que ela estique e fique de 1 a 2 cm maior. Após encaixar os 4 cantos, iremos fixar o meio da borracha, agora e só ir passando os dedos e ir pressionando a borracha, caso fique alguma “barriga” não se preocupe assim que você religar a geladeira a temperatura baixa vai fazer com que ela se ajuste a porta.
""") 
    
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


















