#!/usr/bin/env python3
"""
Dashboard - Framework de Carreira Data & IA
Visualização interativa do framework de carreira

Deploy: Streamlit Cloud
Uso local: streamlit run app.py
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path

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
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 2rem;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 1.1rem;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Carrega todos os CSVs necessários."""
    base_path = Path(__file__).parent / "data"
    
    df_niveis = pd.read_csv(base_path / "niveis.csv")
    df_expectativas = pd.read_csv(base_path / "expectativas.csv")
    df_skills = pd.read_csv(base_path / "skills.csv")
    df_valores = pd.read_csv(base_path / "valores_gupy.csv")
    
    return df_niveis, df_expectativas, df_skills, df_valores

def create_radar_chart(df_expectativas, df_niveis, nivel_selecionado, comparar_com=None):
    """Cria gráfico radar de expectativas."""
    nivel_id = df_niveis[df_niveis['nome'] == nivel_selecionado]['id'].values[0]
    df_nivel = df_expectativas[df_expectativas['nivel_id'] == nivel_id]
    
    fig = go.Figure()
    
    # Nível principal
    fig.add_trace(go.Scatterpolar(
        r=df_nivel['nota_esperada'].tolist(),
        theta=df_nivel['dimensao'].tolist(),
        fill='toself',
        name=nivel_selecionado,
        line=dict(color='#667eea', width=3),
        fillcolor='rgba(102, 126, 234, 0.3)'
    ))
    
    # Nível de comparação (se selecionado)
    if comparar_com:
        comp_id = df_niveis[df_niveis['nome'] == comparar_com]['id'].values[0]
        df_comp = df_expectativas[df_expectativas['nivel_id'] == comp_id]
        fig.add_trace(go.Scatterpolar(
            r=df_comp['nota_esperada'].tolist(),
            theta=df_comp['dimensao'].tolist(),
            fill='toself',
            name=comparar_com,
            line=dict(color='#f093fb', width=3),
            fillcolor='rgba(240, 147, 251, 0.3)'
        ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 5],
                tickmode='linear',
                tick0=0,
                dtick=1,
                gridcolor='#e0e0e0'
            ),
            angularaxis=dict(
                gridcolor='#e0e0e0'
            )
        ),
        showlegend=True,
        title=dict(
            text=f"Expectativas: {nivel_selecionado}" + (f" vs {comparar_com}" if comparar_com else ""),
            x=0.5,
            xanchor='center',
            font=dict(size=18)
        ),
        height=550,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.15,
            xanchor="center",
            x=0.5
        )
    )
    
    return fig

def main():
    # Header
    st.markdown('<div class="main-header">📊 Framework de Carreira - Data & IA</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Dashboard Interativo de Exploração</div>', unsafe_allow_html=True)
    
    # Carregar dados
    try:
        df_niveis, df_expectativas, df_skills, df_valores = load_data()
    except Exception as e:
        st.error(f"❌ Erro ao carregar dados: {e}")
        st.info("💡 Certifique-se de que a pasta 'data/' contém todos os CSVs necessários.")
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
    tab1, tab2, tab3, tab4 = st.tabs([
        "🎯 Radar de Expectativas", 
        "🛠️ Skills por Trilha", 
        "📊 Comparação de Níveis", 
        "💎 Valores Gupy"
    ])
    
    # TAB 1: Radar de Expectativas
    with tab1:
        st.subheader("🎯 Visualização Radar por Nível")
        
        col1, col2 = st.columns([3, 1])
        
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
            st.markdown("### Sobre este Nível")
            nivel_info = df_niveis[df_niveis['nome'] == nivel_selecionado].iloc[0]
            st.markdown(f"**Tipo:** {nivel_info['tipo']}")
            
            # Link para documentação completa
            st.markdown("---")
            st.markdown("📚 [Ver documentação completa](https://amandanery-o.github.io/framework-carreira-data-ia/)")
        
        with col1:
            fig = create_radar_chart(df_expectativas, df_niveis, nivel_selecionado, comparar_com)
            st.plotly_chart(fig, use_container_width=True)
            
            # Tabela de notas
            st.markdown("### 📋 Notas Detalhadas")
            nivel_id = df_niveis[df_niveis['nome'] == nivel_selecionado]['id'].values[0]
            df_nivel_detalhes = df_expectativas[df_expectativas['nivel_id'] == nivel_id][['dimensao', 'nota_esperada']]
            df_nivel_detalhes.columns = ['Dimensão', 'Nota Esperada (0-5)']
            st.dataframe(df_nivel_detalhes, hide_index=True, use_container_width=True)
    
    # TAB 2: Skills por Trilha
    with tab2:
        st.subheader("🛠️ Skills Técnicas por Trilha")
        
        col1, col2 = st.columns([1, 3])
        
        with col1:
            trilha_selecionada = st.selectbox(
                "Selecione a trilha:",
                sorted(df_skills['trilha'].unique().tolist())
            )
            
            nivel_skill = st.selectbox(
                "Filtrar por nível:",
                ["Todos os níveis"] + df_niveis['nome'].tolist(),
                key="nivel_skill"
            )
        
        with col2:
            df_skills_filtrado = df_skills[df_skills['trilha'] == trilha_selecionada].copy()
            
            if nivel_skill != "Todos os níveis":
                nivel_id = df_niveis[df_niveis['nome'] == nivel_skill]['id'].values[0]
                df_skills_filtrado = df_skills_filtrado[df_skills_filtrado['nivel_id'] == nivel_id]
            
            # Adicionar nome do nível
            df_skills_filtrado = df_skills_filtrado.merge(
                df_niveis[['id', 'nome']], 
                left_on='nivel_id', 
                right_on='id', 
                suffixes=('', '_nivel')
            )
            
            if len(df_skills_filtrado) == 0:
                st.info("Nenhuma skill encontrada para esta combinação.")
            else:
                # Agrupar por categoria
                categorias = df_skills_filtrado['categoria'].unique()
                
                for categoria in sorted(categorias):
                    with st.expander(f"📦 {categoria}", expanded=True):
                        df_cat = df_skills_filtrado[df_skills_filtrado['categoria'] == categoria]
                        
                        for _, skill in df_cat.iterrows():
                            nivel_badge = f"**{skill['nome']}**" if nivel_skill == "Todos os níveis" else ""
                            st.markdown(f"**{skill['skill']}** {nivel_badge}")
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
            
            base_id = df_niveis[df_niveis['nome'] == nivel_base]['id'].values[0]
            alvo_id = df_niveis[df_niveis['nome'] == nivel_alvo]['id'].values[0]
            
            df_base = df_expectativas[df_expectativas['nivel_id'] == base_id][['dimensao', 'nota_esperada']]
            df_alvo = df_expectativas[df_expectativas['nivel_id'] == alvo_id][['dimensao', 'nota_esperada']]
            
            df_comparacao = df_base.merge(df_alvo, on='dimensao', suffixes=('_atual', '_alvo'))
            df_comparacao['gap'] = df_comparacao['nota_esperada_alvo'] - df_comparacao['nota_esperada_atual']
            df_comparacao.columns = ['Dimensão', 'Nota Atual', 'Nota Alvo', 'Gap']
            
            # Adicionar emoji baseado no gap
            df_comparacao['Status'] = df_comparacao['Gap'].apply(
                lambda x: '🔥 Crescimento Significativo' if x >= 1 else '📈 Crescimento' if x > 0 else '✅ Mesmo Nível'
            )
            
            st.dataframe(df_comparacao, hide_index=True, use_container_width=True)
            
            # Gráfico de barras do gap
            fig = px.bar(
                df_comparacao,
                x='Dimensão',
                y='Gap',
                title=f"Gap de Crescimento: {nivel_base} → {nivel_alvo}",
                color='Gap',
                color_continuous_scale=['#f093fb', '#667eea'],
                text='Gap'
            )
            fig.update_traces(texttemplate='%{text:.1f}', textposition='outside')
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Selecione níveis diferentes para comparar.")
    
    # TAB 4: Valores Gupy
    with tab4:
        st.subheader("💎 Valores Gupy por Nível")
        
        nivel_valores = st.selectbox(
            "Selecione o nível:",
            df_niveis['nome'].tolist(),
            index=2,
            key="nivel_valores"
        )
        
        nivel_id = df_niveis[df_niveis['nome'] == nivel_valores]['id'].values[0]
        df_valores_nivel = df_valores[df_valores['nivel_id'] == nivel_id]
        
        if len(df_valores_nivel) == 0:
            st.info("Dados de valores ainda não disponíveis para este nível.")
        else:
            for _, row in df_valores_nivel.iterrows():
                with st.expander(f"💎 {row['valor']}", expanded=True):
                    st.markdown(row['manifestacao'])
    
    # Footer
    st.markdown("---")
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("🚀 **Framework de Carreira Data & IA** - Gupy")
    with col2:
        st.markdown("📚 [Documentação Completa](https://amandanery-o.github.io/framework-carreira-data-ia/)")

if __name__ == "__main__":
    main()

