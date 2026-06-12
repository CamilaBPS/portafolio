import streamlit as st
import time

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="CP | Cloud Security Specialist", page_icon="⚡", layout="wide")

# --- CSS AVANZADO: DISEÑO TECH/JUVENIL/PREMIUM ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');

    /* Fondo Base con gradiente sutil estilo Cyber */
    .main {
        background: radial-gradient(circle at top right, #1e293b, #0f172a, #020617);
        color: #f8fafc;
        font-family: 'Inter', sans-serif;
    }

    /* Barra Lateral Estilo Cyber-Consola */
    [data-testid="stSidebar"] {
        background-color: rgba(15, 23, 42, 0.8);
        border-right: 1px solid #1e293b;
        backdrop-filter: blur(10px);
    }

    /* Tarjetas con efecto Glassmorphism */
    .glass-card {
        background: rgba(30, 41, 59, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.05);
        padding: 2rem;
        border-radius: 16px;
        backdrop-filter: blur(12px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        margin-bottom: 20px;
        transition: transform 0.3s ease, border 0.3s ease;
    }

    .glass-card:hover {
        transform: translateY(-5px);
        border: 1px solid #38bdf8;
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.2);
    }

    /* Títulos con Gradiente */
    .hero-text {
        background: linear-gradient(90deg, #38bdf8, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem;
        font-weight: 800;
        margin-bottom: 0;
    }

    /* Botones Estilo Terminal/Tech */
    .stButton>button {
        background: linear-gradient(135deg, #2563eb 0%, #7c3aed 100%);
        color: white;
        border: none;
        padding: 10px 24px;
        border-radius: 12px;
        font-weight: 600;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        text-transform: uppercase;
        font-size: 0.8rem;
    }

    .stButton>button:hover {
        box-shadow: 0 0 25px rgba(124, 58, 237, 0.6);
        transform: scale(1.02);
    }

    /* Etiquetas de tecnología */
    .tech-tag {
        display: inline-block;
        background: rgba(56, 189, 248, 0.1);
        color: #38bdf8;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        margin: 4px;
        border: 1px solid rgba(56, 189, 248, 0.3);
    }

    /* Inputs y Selectores */
    .stNumberInput input, .stSelectbox div {
        background-color: #1e293b !important;
        color: white !important;
        border-radius: 8px !important;
        border: 1px solid #334155 !important;
    }

    hr { border: 0.5px solid #1e293b; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVEGACIÓN ---
with st.sidebar:
    st.markdown("<h2 style='color: #38bdf8;'>SYSTEM OPS</h2>", unsafe_allow_html=True)
    section = st.radio("MENU_ROOT:", ["CORE", "TECH_STACK", "DEPLOYMENTS"])
    st.markdown("---")
    st.markdown("🤖 `Status: Online`")

# --- SECCIÓN 1: INICIO (HERO) ---
if section == "CORE":
    st.markdown('<p class="hero-text">Camila Paredes Suárez</p>', unsafe_allow_html=True)
    st.markdown("<h3 style='margin-top:-10px; color: #818cf8;'>Cloud Security Engineer</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div class="glass-card">
        Ingeniera en Informática con experiencia en soporte técnico y transformación digital enfocada en la eficiencia operativa. Actualmente especializándome en 
        Ciberseguridad, Ciberdefensa y Arquitectura Cloud (AWS), con el objetivo de fusionar la continuidad operativa con la protección de activos en la nube. 
        Experiencia en la implementación de estándares de seguridad de la información y apasionada por el diseño de infraestructuras cloud resilientes, seguras y 
        escalables. 
        Enfocada en resolver la brecha entre la infraestructura Cloud y las necesidades críticas del negocio moderno.
        </div>
        """, unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        c1.markdown("🔗 [**LinkedIn**](https://www.linkedin.com/in/camila-paredes-su%C3%A1rez-647799224/)")
        c2.markdown("🐙 [**GitHub**](https://github.com/CamilaBPS?tab=repositories)")

# --- SECCIÓN 2: MATRIZ DE COMPETENCIAS ---
elif section == "TECH_STACK":
    st.markdown("<h2 style='color: #f8fafc;'>[MATRIX_RECON] // Expertise & Stack</h2>", unsafe_allow_html=True)
    st.write("Estructura de competencias alineada a la ingeniería de software, protección de infraestructuras críticas y entornos Cloud.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="glass-card" style="height: 100%;">
        <h3>Cloud Architecture & IA</h3>
        <p>Implementación y despliegue seguro de microservicios e infraestructura elástica en nubes públicas.</p>
        <span class="tech-tag">AWS re/Start</span>
        <span class="tech-tag">Amazon Bedrock</span>
        <span class="tech-tag">AWS Lambda</span>
        <span class="tech-tag">Amazon S3</span>
        <span class="tech-tag">IAM / Cloud Security Sec</span>
        <span class="tech-tag">Integración de IA Generativa</span>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="glass-card" style="height: 100%;">
        <h3>Cybersecurity & Defense</h3>
        <p>Gestión de vulnerabilidades, análisis de riesgos informáticos y endurecimiento de plataformas digitales.</p>
        <span class="tech-tag">Diplomado Ciberseguridad</span>
        <span class="tech-tag">Ciberdefensa</span>
        <span class="tech-tag">Seguridad WordPress (Wordfence)</span>
        <span class="tech-tag">Auditoría de Activos</span>
        <span class="tech-tag">Protección perimetral</span>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="glass-card" style="height: 100%;">
        <h3>Core Engineering</h3>
        <p>Fundamentos sólidos de desarrollo de software, automatización de tareas y control de versiones.</p>
        <span class="tech-tag">Ingeniería en Informática</span>
        <span class="tech-tag">Python (Scripting)</span>
        <span class="tech-tag">SQL (Bases de datos)</span>
        <span class="tech-tag">Git / GitHub</span>
        <span class="tech-tag">Linux Bash</span>
        </div>
        """, unsafe_allow_html=True)

# --- SECCIÓN 3: PROYECTOS (MÓDULO DE SEGURIDAD AUDIT) ---
elif section == "DEPLOYMENTS":
    st.markdown("<h2 style='color: #f8fafc;'>Active Deployments</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="glass-card">
    <h2 style='color: #38bdf8; font-size: 1.5rem;'>[EVALUACIÓN_CLOUD] // Monitor de Vulnerabilidades</h2>
    <p>Script automatizado desarrollado en Python para la detección temprana de brechas de seguridad, políticas IAM laxas y vulnerabilidades perimetrales en infraestructuras Cloud.</p>
    <a href='https://github.com' style='color:#818cf8; text-decoration:none;'>SRC_CODE -> REPOSITORY_ACCESS</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Módulo de Simulación: Analizador de Vulnerabilidades")
    st.write("Simulación del motor de análisis de políticas de seguridad y vulnerabilidades basándose en reglas heurísticas:")
    
    with st.container():
        c1, c2 = st.columns(2)
        with c1:
            puertos_abiertos = st.number_input("Puertos críticos expuestos", min_value=0, value=0, step=1)
            usuarios_sin_mfa = st.number_input("Identidades (IAM) sin autenticación MFA", min_value=0, value=0, step=1)
        with c2:
            entorno = st.selectbox("Target_Environment:", ["AWS Production", "AWS Staging", "WordPress Web Server"])
            
        if st.button("RUN_SECURITY_SCAN"):
            with st.status("Initializing Scan Engine...", expanded=True) as status:
                time.sleep(0.8)
                st.write(f"Evaluating {entorno} assets...")
                time.sleep(1.0)
                st.write("Checking IAM policy compliance and open endpoints...")
                status.update(label="Scan Complete", state="complete", expanded=False)
            
            # Lógica de decisión adaptada a ciberseguridad
            if puertos_abiertos == 0 and usuarios_sin_mfa == 0:
                st.balloons()
                st.markdown(f"""
                <div style="background: rgba(34, 197, 94, 0.1); border: 1px solid #22c55e; padding: 20px; border-radius: 12px;">
                <h4 style="color: #22c55e; margin:0;">SUCCESS: SECURE_BASELINE_COMPLIANT</h4>
                <p style="color: white; margin-top:10px;">Entorno evaluado: <b>{entorno}</b><br><br>
                <b>SEC_REPORT:</b> No se detectaron vectores de riesgo críticos inmediatos. Las configuraciones de los Security Groups, políticas de privilegios mínimos (IAM) y accesos perimetrales cumplen con los estándares de hardening recomendados.</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="background: rgba(239, 68, 68, 0.1); border: 1px solid #ef4444; padding: 20px; border-radius: 12px;">
                <h4 style="color: #ef4444; margin:0;">WARNING: VULNERABILITIES_DETECTED</h4>
                <p style="color: white; margin-top:10px;">Entorno evaluado: <b>{entorno}</b><br>
                Alertas críticas: Se registraron {puertos_abiertos} endpoints expuestos a la WAN pública y {usuarios_sin_mfa} cuentas sin doble factor de autenticación.<br><br>
                <b>REMEDIAL_ACTION:</b> Se requiere aplicar parches de mitigación. Restringir el tráfico no autorizado en los Security Groups, forzar políticas organizacionales para exigir MFA obligatorio y aplicar el principio de mínimos privilegios inmediatamente.</p>
                </div>
                """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #475569; font-size: 0.8rem;'>CAMILA PAREDES SUÁREZ // PORTAFOLIO // 2026</p>", unsafe_allow_html=True)