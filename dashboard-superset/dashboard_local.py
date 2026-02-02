#!/usr/bin/env python3
"""
Dashboard Local - Framework de Carreira Data & IA
Visualização interativa dos dados do framework

Uso:
    streamlit run dashboard_local.py
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import psycopg2
from dotenv import load_dotenv
import os

# Configuração da página
st.set_page_config(
    page_title="Framework de Carreira - Data & IA",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #555;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 1.1rem;
    }
</style>
""", unsafe_allow_html=True)

# Carregar variáveis de ambiente
load_dotenv()

@st.cache_resource
def get_connection():
    """Cria conexão com banco de dados."""
    return psycopg2.connect(
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )

@st.cache_data
def load_niveis():
    """Carrega dados dos níveis."""
    conn = get_connection()
    query = "SELECT * FROM niveis ORDER BY ordem"
    df = pd.read_sql(query, conn)
    return df

@st.cache_data
def load_expectativas():
    """Carrega expectativas por nível."""
    conn = get_connection()
    query = """
        SELECT n.id, n.nome, n.ordem, e.dimensao, e.nota_esperada
        FROM niveis n
        LEFT JOIN expectativas e ON n.id = e.nivel_id
        WHERE e.subdimensao IS NULL
        ORDER BY n.ordem, e.dimensao
    """
    df = pd.read_sql(query, conn)
    return df

@st.cache_data
def load_skills():
    """Carrega skills por trilha."""
    conn = get_connection()
    query = """
        SELECT n.nome as nivel, n.ordem, s.trilha, s.categoria, 
               s.skill, s.nivel_esperado, s.detalhes
        FROM skills s
        JOIN niveis n ON s.nivel_id = n.id
        ORDER BY n.ordem, s.trilha, s.categoria
    """
    df = pd.read_sql(query, conn)
    return df

@st.cache_data
def load_valores():
    """Carrega valores Gupy."""
    conn = get_connection()
    query = """
        SELECT n.nome as nivel, n.ordem, v.valor, v.manifestacao
        FROM valores_gupy v
        JOIN niveis n ON v.nivel_id = n.id
        ORDER BY n.ordem, v.ordem
    """
    df = pd.read_sql(query, conn)
    return df

def create_radar_chart(df_expectativas, nivel_selecionado, comparar_com=None):
    """Cria gráfico radar de expectativas."""
    df_nivel = df_expectativas[df_expectativas['nome'] == nivel_selecionado]
    
    fig = go.Figure()
    
    # Nível principal
    fig.add_trace(go.Scatterpolar(
        r=df_nivel['nota_esperada'].tolist(),
        theta=df_nivel['dimensao'].tolist(),
        fill='toself',
        name=nivel_selecionado,
        line=dict(color='#1f77b4', width=2),
        fillcolor='rgba(31, 119, 180, 0.3)'
    ))
    
    # Nível de comparação (se selecionado)
    if comparar_com:
        df_comp = df_expectativas[df_expectativas['nome'] == comparar_com]
        fig.add_trace(go.Scatterpolar(
            r=df_comp['nota_esperada'].tolist(),
            theta=df_comp['dimensao'].tolist(),
            fill='toself',
            name=comparar_com,
            line=dict(color='#ff7f0e', width=2),
            fillcolor='rgba(255, 127, 14, 0.3)'
        ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 5],
                tickmode='linear',
                tick0=0,
                dtick=1
            )
        ),
        showlegend=True,
        title=dict(
            text=f"Expectativas: {nivel_selecionado}" + (f" vs {comparar_com}" if comparar_com else ""),
            x=0.5,
            xanchor='center'
        ),
        height=500
    )
    
    return fig

def main():
    # Header
    st.markdown('<div class="main-header">📊 Framework de Carreira - Data & IA</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Dashboard Interativo de Exploração</div>', unsafe_allow_html=True)
    
    # Carregar dados
    try:
        df_niveis = load_niveis()
        df_expectativas = load_expectativas()
        df_skills = load_skills()
        df_valores = load_valores()
    except Exception as e:
        st.error(f"❌ Erro ao conectar ao banco de dados: {e}")
        st.info("💡 Verifique se o arquivo .env está configurado corretamente.")
        return
    
    # Métricas principais
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("📈 Níveis", len(df_niveis))
    with col2:
        st.metric("🎯 Dimensões", df_expectativas['dimensao'].nunique())
    with col3:
        st.metric("🛠️ Skills", len(df_skills))
    with col4:
        st.metric("💎 Valores", df_valores['valor'].nunique())
    
    st.markdown("---")
    
    # Tabs principais
    tab1, tab2, tab3, tab4 = st.tabs(["🎯 Radar de Expectativas", "🛠️ Skills por Trilha", "📊 Comparação de Níveis", "💎 Valores Gupy"])
    
    # TAB 1: Radar de Expectativas
    with tab1:
        st.subheader("🎯 Visualização Radar por Nível")
        
        col1, col2 = st.columns([2, 1])
        
        with col2:
            st.markdown("### Configurações")
            
            nivel_selecionado = st.selectbox(
                "Selecione o nível:",
                df_niveis['nome'].tolist(),
                index=2  # Default: SE III
            )
            
            comparar = st.checkbox("Comparar com outro nível")
            comparar_com = None
            
            if comparar:
                nivel_atual_ordem = df_niveis[df_niveis['nome'] == nivel_selecionado]['ordem'].values[0]
                opcoes_comparacao = df_niveis[df_niveis['ordem'] != nivel_atual_ordem]['nome'].tolist()
                comparar_com = st.selectbox(
                    "Comparar com:",
                    opcoes_comparacao,
                    index=min(1, len(opcoes_comparacao)-1)
                )
            
            # Mostrar detalhes do nível
            st.markdown("### Detalhes do Nível")
            nivel_info = df_niveis[df_niveis['nome'] == nivel_selecionado].iloc[0]
            st.markdown(f"**Tipo:** {nivel_info['tipo']}")
            if pd.notna(nivel_info['escopo']):
                st.markdown(f"**Escopo:** {nivel_info['escopo']}")
            if pd.notna(nivel_info['alcance_colaborativo']):
                st.markdown(f"**Alcance:** {nivel_info['alcance_colaborativo']}")
        
        with col1:
            fig = create_radar_chart(df_expectativas, nivel_selecionado, comparar_com)
            st.plotly_chart(fig, use_container_width=True)
            
            # Tabela de notas
            st.markdown("### 📋 Notas Detalhadas")
            df_nivel_detalhes = df_expectativas[df_expectativas['nome'] == nivel_selecionado][['dimensao', 'nota_esperada']]
            df_nivel_detalhes.columns = ['Dimensão', 'Nota Esperada']
            st.dataframe(df_nivel_detalhes, hide_index=True, use_container_width=True)
    
    # TAB 2: Skills por Trilha
    with tab2:
        st.subheader("🛠️ Skills Técnicas por Trilha")
        
        col1, col2 = st.columns([1, 3])
        
        with col1:
            trilha_selecionada = st.selectbox(
                "Selecione a trilha:",
                df_skills['trilha'].unique().tolist()
            )
            
            nivel_skill = st.selectbox(
                "Filtrar por nível:",
                ["Todos"] + df_niveis['nome'].tolist(),
                key="nivel_skill"
            )
        
        with col2:
            df_skills_filtrado = df_skills[df_skills['trilha'] == trilha_selecionada]
            
            if nivel_skill != "Todos":
                df_skills_filtrado = df_skills_filtrado[df_skills_filtrado['nivel'] == nivel_skill]
            
            # Agrupar por categoria
            categorias = df_skills_filtrado['categoria'].unique()
            
            for categoria in categorias:
                with st.expander(f"📦 {categoria}", expanded=True):
                    df_cat = df_skills_filtrado[df_skills_filtrado['categoria'] == categoria]
                    
                    for _, skill in df_cat.iterrows():
                        st.markdown(f"**{skill['skill']}** - *{skill['nivel']}*")
                        if pd.notna(skill['nivel_esperado']):
                            st.markdown(f"↳ Nível esperado: `{skill['nivel_esperado']}`")
                        if pd.notna(skill['detalhes']) and skill['detalhes'] != '':
                            st.markdown(f"↳ {skill['detalhes']}")
                        st.markdown("")
    
    # TAB 3: Comparação de Níveis
    with tab3:
        st.subheader("📊 Comparação Entre Níveis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            nivel_base = st.selectbox(
                "Nível atual:",
                df_niveis['nome'].tolist(),
                index=1,
                key="nivel_base"
            )
        
        with col2:
            nivel_alvo = st.selectbox(
                "Nível alvo:",
                df_niveis['nome'].tolist(),
                index=2,
                key="nivel_alvo"
            )
        
        if nivel_base != nivel_alvo:
            # Comparação de expectativas
            st.markdown("### 🎯 Gap de Expectativas")
            
            df_base = df_expectativas[df_expectativas['nome'] == nivel_base][['dimensao', 'nota_esperada']]
            df_alvo = df_expectativas[df_expectativas['nome'] == nivel_alvo][['dimensao', 'nota_esperada']]
            
            df_comparacao = df_base.merge(df_alvo, on='dimensao', suffixes=('_atual', '_alvo'))
            df_comparacao['gap'] = df_comparacao['nota_esperada_alvo'] - df_comparacao['nota_esperada_atual']
            df_comparacao.columns = ['Dimensão', 'Nota Atual', 'Nota Alvo', 'Gap']
            
            st.dataframe(df_comparacao, hide_index=True, use_container_width=True)
            
            # Gráfico de barras do gap
            fig = px.bar(
                df_comparacao,
                x='Dimensão',
                y='Gap',
                title=f"Gap de Crescimento: {nivel_base} → {nivel_alvo}",
                color='Gap',
                color_continuous_scale='RdYlGn'
            )
            st.plotly_chart(fig, use_container_width=True)
    
    # TAB 4: Valores Gupy
    with tab4:
        st.subheader("💎 Valores Gupy por Nível")
        
        df_valores_nivel = df_valores[df_valores['nivel'] == nivel_valores]
        
        for _, row in df_valores_nivel.iterrows():
            with st.expander(f"💎 {row['valor']}", expanded=True):
                st.markdown(row['manifestacao'])
    
    # Footer
    st.markdown("---")
    st.markdown("🚀 **Dashboard Local** - Framework de Carreira Data & IA")

if __name__ == "__main__":
    main()

