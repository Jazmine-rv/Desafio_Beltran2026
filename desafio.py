import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Configuración de la página
st.set_page_config(
    page_title="Diagnóstico de Accesibilidad - Avellaneda",
    page_icon="♿",
    layout="wide"
)

# Estilos personalizados
st.markdown("""
    <style>
    .main-header {
        font-family: Georgia, serif;
        font-size: 2.5rem;
        color: #1B2A3D;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1rem;
        color: #4A5A6E;
        margin-bottom: 2rem;
    }
    .kpi-card {
        background-color: #1B2A3D;
        padding: 1.5rem;
        border-radius: 8px;
        color: white;
    }
    .kpi-number {
        font-family: Georgia, serif;
        font-size: 3.2rem;
        font-weight: bold;
        line-height: 1;
    }
    .kpi-label {
        font-size: 0.9rem;
        color: #CBD5D9;
        margin-top: 0.3rem;
    }
    .metric-card {
        background-color: white;
        padding: 1.2rem 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #2E6E68;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08);
    }
    .metric-number {
        font-family: Georgia, serif;
        font-size: 1.8rem;
        font-weight: bold;
        color: #1B2A3D;
    }
    .metric-desc {
        font-size: 0.85rem;
        color: #4A5A6E;
        margin: 0.2rem 0 0;
    }
    .metric-sub {
        font-size: 0.75rem;
        color: #8A9AAC;
        font-style: italic;
        margin: 0.3rem 0 0;
    }
    .source-box {
        border-left: 4px solid #C4802E;
        background-color: white;
        padding: 1rem 1.5rem;
        border-radius: 0 6px 6px 0;
        font-size: 0.85rem;
        color: #4A5A6E;
    }
    .footer {
        border-top: 1px solid #D8D2C4;
        padding-top: 1.2rem;
        font-size: 0.75rem;
        color: #8A9AAC;
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
    }
    .badge {
        background-color: #2E6E68;
        color: white;
        padding: 0.25rem 1rem;
        border-radius: 999px;
        font-size: 0.7rem;
        font-weight: 600;
        letter-spacing: 0.04em;
        text-transform: uppercase;
        display: inline-block;
    }
    </style>
""", unsafe_allow_html=True)

# ============================================
# HEADER
# ============================================
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown('<p style="font-size:0.75rem; font-weight:700; color:#1E4A46; letter-spacing:0.04em; text-transform:uppercase;">DESAFÍO BELTRÁN 2026 — DIAGNÓSTICO </p>', unsafe_allow_html=True)
    st.markdown('<h1 class="main-header">Accesibilidad urbana en Avellaneda</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Estimación de la población con discapacidad o movilidad reducida, construida a partir de fuentes públicas oficiales (INDEC, Censo 2022).</p>', unsafe_allow_html=True)
with col2:
    st.markdown('<div style="text-align:right; margin-top:1.5rem;"><span class="badge">Conurbano Sur 2030</span></div>', unsafe_allow_html=True)

# ============================================
# KPIS PRINCIPALES
# ============================================
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-number">37.858</div>
            <div class="kpi-label">Personas estimadas con discapacidad en Avellaneda</div>
            <div style="font-size:0.8rem; color:#CBD5D9; margin-top:0.5rem;">Prevalencia regional: 10,3% · Población total: 367.554 hab.</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div style="background-color:white; padding:1.5rem; border-radius:8px; border:1px solid #D8D2C4; height:100%; display:flex; flex-direction:column; justify-content:center;">
            <div style="font-size:0.8rem; color:#4A5A6E;">Usuarios potenciales de la app</div>
            <div style="font-family:Georgia, serif; font-size:2.8rem; color:#1B2A3D; line-height:1;">~25.000</div>
            <div style="font-size:0.8rem; color:#4A5A6E;">Personas que podrían beneficiarse directamente<br><span style="font-size:0.7rem; color:#8A9AAC;">(estimación conservadora: 2/3 de la población con discapacidad)</span></div>
        </div>
    """, unsafe_allow_html=True)

st.divider()

# ============================================
# MÉTRICAS DE IMPACTO
# ============================================
st.markdown('<p style="font-size:0.7rem; font-weight:700; color:#1E4A46; text-transform:uppercase; letter-spacing:0.04em;">MÉTRICAS DE IMPACTO PROPUESTAS</p>', unsafe_allow_html=True)
st.markdown('<h2 style="font-family:Georgia, serif; font-size:1.4rem; margin-top:0;">Cómo mediremos el éxito del sistema</h2>', unsafe_allow_html=True)

cols = st.columns(4)
metrics = [
    {"number": "-30%", "desc": "Reducción de reportes en zonas críticas", "sub": "A 6 meses, en los 3 barrios con mayor concentración"},
    {"number": "+20%", "desc": "Aumento en percepción de accesibilidad", "sub": "Medido mediante encuestas a usuarios (basal vs. post)"},
    {"number": "85%", "desc": "Tasa de resolución de incidentes", "sub": "Reportes con respuesta/derivación en 30 días"},
    {"number": "+40%", "desc": "Incremento en reportes ciudadanos", "sub": "Aumento esperado durante el primer año"}
]

for i, col in enumerate(cols):
    with col:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-number">{metrics[i]['number']}</div>
                <div class="metric-desc">{metrics[i]['desc']}</div>
                <div class="metric-sub">{metrics[i]['sub']}</div>
            </div>
        """, unsafe_allow_html=True)

st.divider()

# ============================================
# MAPA DE CALOR - VERSIÓN CON NOMBRES COMPLETOS
# ============================================
st.markdown('<p style="font-size:0.7rem; font-weight:700; color:#1E4A46; text-transform:uppercase; letter-spacing:0.04em;">VISUALIZACIÓN DE DATOS</p>', unsafe_allow_html=True)
st.markdown('<h2 style="font-family:Georgia, serif; font-size:1.4rem; margin-top:0;">Reportes de accesibilidad por barrio — Simulación</h2>', unsafe_allow_html=True)

# Datos simulados con valores realistas
datos_barrios = pd.DataFrame({
    'Barrio': ['Dock Sud', 'Sarandí', 'Villa Domínico', 'Piñeyro', 'Avellaneda', 'Gerli', 'Wilde'],
    'Reportes': [25, 18, 15, 12, 8, 6, 4],
    'Rampas rotas': [10, 7, 6, 5, 3, 2, 1],
    'Veredas dañadas': [8, 6, 5, 4, 3, 2, 2],
    'Semáforos sin funcionar': [4, 3, 2, 2, 1, 1, 0],
    'Falta de rampas': [3, 2, 2, 1, 1, 1, 1]
})

# Clasificar densidad
def clasificar_densidad(valor):
    if valor >= 15:
        return 'Alta'
    elif valor >= 8:
        return 'Media'
    elif valor >= 1:
        return 'Baja'
    else:
        return 'Sin reportes'

datos_barrios['Densidad'] = datos_barrios['Reportes'].apply(clasificar_densidad)

# Color map
color_map = {
    'Alta': '#B34141',
    'Media': '#D98C3A',
    'Baja': '#4A9E96',
    'Sin reportes': '#D5CDBC'
}

# Gráfico de barras con colores de densidad
fig_barrios = px.bar(
    datos_barrios,
    x='Barrio',
    y='Reportes',
    color='Densidad',
    color_discrete_map=color_map,
    text='Reportes',
    title='Reportes de barreras de accesibilidad por barrio (simulación)',
    labels={'Reportes': 'Cantidad de reportes', 'Barrio': ''}
)

fig_barrios.update_layout(
    height=350,
    margin=dict(l=20, r=20, t=50, b=20),
    showlegend=True
)

fig_barrios.update_traces(textposition='outside')

st.plotly_chart(fig_barrios, use_container_width=True)

# Tabla resumen
st.dataframe(
    datos_barrios[['Barrio', 'Reportes', 'Rampas rotas', 'Veredas dañadas', 'Semáforos sin funcionar', 'Falta de rampas', 'Densidad']],
    use_container_width=True,
    hide_index=True
)

# Leyenda
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('🔴 **Alta** (>15 reportes)')
with col2:
    st.markdown('🟠 **Media** (8-15 reportes)')
with col3:
    st.markdown('🟢 **Baja** (1-7 reportes)')
with col4:
    st.markdown('⚪ **Sin reportes** (0 reportes)')

st.caption("📊 **Interpretación:** Dock Sud y Sarandí concentran la mayor cantidad de reportes, siendo las zonas con más barreras de accesibilidad. Estos barrios serían prioritarios para la intervención.")

st.divider()

# ============================================
# GRÁFICO DE BARRAS - POBLACIÓN
# ============================================
st.markdown('<p style="font-size:0.7rem; font-weight:700; color:#1E4A46; text-transform:uppercase; letter-spacing:0.04em;">CONTEXTO DEMOGRÁFICO</p>', unsafe_allow_html=True)
st.markdown('<h2 style="font-family:Georgia, serif; font-size:1.4rem; margin-top:0;">Peso relativo dentro de la población de Avellaneda</h2>', unsafe_allow_html=True)

poblacion_data = pd.DataFrame({
    'Categoría': ['Población total', 'Adultos mayores (65+)', 'Con discapacidad (est.)', 'Potenciales usuarios app'],
    'Cantidad': [367554, 71580, 37858, 25000],
    'Color': ['#1B2A3D', '#C4802E', '#2E6E68', '#4A9E96']
})

fig2 = px.bar(
    poblacion_data,
    x='Categoría',
    y='Cantidad',
    color='Categoría',
    color_discrete_map={
        'Población total': '#1B2A3D',
        'Adultos mayores (65+)': '#C4802E',
        'Con discapacidad (est.)': '#2E6E68',
        'Potenciales usuarios app': '#4A9E96'
    },
    text='Cantidad',
    labels={'Cantidad': 'Personas', 'Categoría': ''}
)

fig2.update_layout(
    height=350,
    margin=dict(l=20, r=20, t=20, b=20),
    showlegend=False,
    yaxis=dict(tickformat=',')
)

fig2.update_traces(textposition='outside', texttemplate='%{text:,.0f}')

st.plotly_chart(fig2, use_container_width=True)

st.divider()

# ============================================
# DISTRIBUCIÓN POR TIPO DE DIFICULTAD
# ============================================
st.markdown('<p style="font-size:0.7rem; font-weight:700; color:#1E4A46; text-transform:uppercase; letter-spacing:0.04em;">COMPOSICIÓN POR TIPO DE DIFICULTAD</p>', unsafe_allow_html=True)
st.markdown('<h2 style="font-family:Georgia, serif; font-size:1.4rem; margin-top:0;">Distribución nacional por tipo (INDEC, 2018)</h2>', unsafe_allow_html=True)

tipo_data = pd.DataFrame({
    'Tipo': ['Solo motora', 'Solo visual', 'Solo auditiva', 'Solo mental-cognitiva', 'Dos dificultades o más', 'Solo certificado vigente'],
    'Porcentaje': [25.2, 13.7, 11.0, 7.5, 30.5, 10.5]
})

fig3 = px.bar(
    tipo_data,
    x='Tipo',
    y='Porcentaje',
    color='Tipo',
    color_discrete_sequence=['#2E6E68', '#4A9E96', '#6BAFAD', '#C4802E', '#D98C3A', '#8A9AAC'],
    text='Porcentaje',
    labels={'Porcentaje': '%', 'Tipo': ''}
)

fig3.update_layout(
    height=300,
    margin=dict(l=20, r=20, t=20, b=20),
    showlegend=False
)

fig3.update_traces(textposition='outside', texttemplate='%{text:.1f}%')

st.plotly_chart(fig3, use_container_width=True)

st.caption("Distribución a nivel nacional entre la población con dificultad. No existe desagregado por tipo a nivel de partido.")

st.divider()

# ============================================
# FUENTE Y METODOLOGÍA
# ============================================
st.markdown("""
    <div class="source-box">
        <p><strong>Fuentes:</strong> INDEC — Estudio Nacional sobre el Perfil de las Personas con Discapacidad (ENPD, 2018), en articulación con ANDIS; Censo Nacional de Población, Hogares y Viviendas 2022.</p>
        <p><strong>Cálculo:</strong> 367.554 habitantes (Avellaneda, Censo 2022) × 10,3% (prevalencia región Pampeana/GBA, INDEC) ≈ 37.858 personas.</p>
        <p>No existe un dato censal desagregado a nivel de partido: se trata de una estimación por proporción poblacional, no de un dato relevado directamente en Avellaneda.</p>
    </div>
""", unsafe_allow_html=True)

# ============================================
# FOOTER
# ============================================
st.markdown("""
    <div class="footer">
        <span>Instituto Tecnológico Beltrán </span>
    </div>
""", unsafe_allow_html=True)
