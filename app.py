import streamlit as st
import os
import random
import time

# Configuración de la página
st.set_page_config(page_title="Juegos Musicales - LAC", page_icon="🎮", layout="centered")

# --- FUNCIÓN: BUSCADOR INTELIGENTE DE ARCHIVOS ---
def buscar_archivo(nombre_base, tipo="audio"):
    extensiones = ['.mp3', '.wav', '.ogg'] if tipo == "audio" else ['.png', '.jpg', '.jpeg']
    variaciones = [
        f"{nombre_base}", 
        f"{nombre_base} 2", 
        f"{nombre_base}2", 
        f"{nombre_base} (2)",
        f"{nombre_base.capitalize()}"
    ]
    for var in variaciones:
        for ext in extensiones:
            if os.path.exists(f"{var}{ext}"):
                return f"{var}{ext}"
    return None # Si no encuentra nada

# Inyectar CSS
st.markdown("""
    <style>
    img { background-color: white; border-radius: 10px; padding: 10px; }
    .stButton>button { width: 100%; height: 60px; font-size: 18px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Cabecera
col1, col2 = st.columns([1, 4])
with col1:
    if os.path.exists("juan_cartoon.png"): st.image("juan_cartoon.png", width=120)
with col2:
    st.title("🎮 Sala de Juegos - LAC")
    st.write("¡Poné a prueba lo que aprendimos en clase!")

# --- BANCOS DE PREGUNTAS ---
banco_pentagrama = [
    {"img": "clave_de_sol_nota_do.png", "opciones": ["Do", "Re", "Mi"], "correcta": "Do"},
    {"img": "clave_de_sol_nota_re.png", "opciones": ["Re", "Fa", "Sol"], "correcta": "Re"},
    {"img": "clave_de_sol_nota_dosostenido.png", "opciones": ["Do", "Do sostenido", "Re bemol"], "correcta": "Do sostenido"},
    {"img": "clave_de_sol_nota_mib.png", "opciones": ["Mi", "Re sostenido", "Mi bemol"], "correcta": "Mi bemol"},
    {"img": "clave_de_sol_nota_fa.png", "opciones": ["Fa", "La", "Si"], "correcta": "Fa"}
]

banco_intervalos = [
    {"pregunta": "¿Qué distancia hay entre Re y Sol?", "opciones": ["Tercera", "Cuarta", "Quinta"], "correcta": "Cuarta"},
    {"pregunta": "¿Qué distancia hay entre Do y Mi?", "opciones": ["Segunda", "Tercera", "Cuarta"], "correcta": "Tercera"}
]

banco_ritmos = [
    {"audio": "corto corto largo audio", "img_correcta": "corto corto largo imagen.png"},
    {"audio": "corto largo corto audio", "img_correcta": "corto largo corto imagen.png"},
    {"audio": "corto largo corto corto audio", "img_correcta": "corto largo corto corto imagen.png"}
]

instrumentos_memotest = ["violin", "trompeta", "piano", "flauta_traversa"]

banco_alturas = [
    {"grave": "tuba", "agudo": "flauta_traversa"},
    {"grave": "contrabajo", "agudo": "violin"}
]

# --- INICIALIZAR MEMORIA ---
if 'puntaje' not in st.session_state: st.session_state.puntaje = 0
if 'juegos_completados' not in st.session_state: st.session_state.juegos_completados = []
if 'preguntas_n3' not in st.session_state: st.session_state.preguntas_n3 = random.sample(banco_pentagrama, min(3, len(banco_pentagrama)))
if 'preguntas_n5' not in st.session_state: st.session_state.preguntas_n5 = random.sample(banco_intervalos, 2)
if 'pregunta_n6' not in st.session_state: st.session_state.pregunta_n6 = random.choice(banco_ritmos)
if 'pregunta_n8' not in st.session_state: st.session_state.pregunta_n8 = random.choice(banco_alturas)

# --- GENERADOR DEL MAZO DE MEMOTEST SEGÚN MODALIDAD ---
def generar_mazo(modalidad):
    deck = []
    for inst in instrumentos_memotest:
        img_file = buscar_archivo(inst, "imagen") or f"{inst}.png"
        audio_file = buscar_archivo(inst, "audio") or f"{inst}.mp3"
        
        if modalidad == "1. Imagen vs Nombre":
            deck.append({"id": inst, "tipo": "img", "valor": img_file})
            deck.append({"id": inst, "tipo": "texto", "valor": inst.upper()})
        elif modalidad == "2. Sonido vs Imagen":
            deck.append({"id": inst, "tipo": "audio", "valor": audio_file})
            deck.append({"id": inst, "tipo": "img", "valor": img_file})
        elif modalidad == "3. Sonido vs Nombre":
            deck.append({"id": inst, "tipo": "audio", "valor": audio_file})
            deck.append({"id": inst, "tipo": "texto", "valor": inst.upper()})
    random.shuffle(deck)
    return deck

# Menú lateral
st.sidebar.title("📌 Menú de Desafíos")
juego_actual = st.sidebar.radio("Elegí un nivel:", 
    ["1. Historia y Orígenes", "2. La Escalera de Notas", "3. El Pentagrama Visual", 
     "4. Sonido, Eco y Figuras", "5. Calculadora de Intervalos", "6. 📝 Dictado Rítmico", 
     "7. 🃏 Memotest de Instrumentos", "8. ⚖️ Batalla: Grave vs Agudo", "🛠️ Radar de Archivos (Profe)"])

st.sidebar.markdown("---")
st.sidebar.title(f"🏆 Puntaje total: {st.session_state.puntaje}")
if st.sidebar.button("Jugar de nuevo (Mezclar todo)"):
    st.session_state.clear()
    st.rerun()

# ==================================
# JUEGOS CLÁSICOS (1 AL 5 Resumidos por espacio visual)
# ==================================
if juego_actual in ["1. Historia y Orígenes", "2. La Escalera de Notas", "3. El Pentagrama Visual", "4. Sonido, Eco y Figuras", "5. Calculadora de Intervalos"]:
    st.info("¡Seleccioná los niveles interactivos (6, 7 y 8) para ver las nuevas funciones!")

# ==================================
# 6. DICTADO RÍTMICO (Ahora obliga a mostrar las imágenes)
# ==================================
elif juego_actual == "6. 📝 Dictado Rítmico":
    st.header("📝 Nivel 6: Correspondencia Rítmica")
    ritmo_actual = st.session_state.pregunta_n6
    
    audio_encontrado = buscar_archivo(ritmo_actual['audio'], "audio")
    if audio_encontrado: st.audio(audio_encontrado)
    else: st.error(f"Falta el audio: {ritmo_actual['audio']}.mp3 o .wav")
        
    st.write("¿Cuál de estos ritmos acaba de sonar?")
    opciones_visuales = [r['img_correcta'] for r in banco_ritmos]
    random.shuffle(opciones_visuales)
    
    colA, colB, colC = st.columns(3)
    # Obligamos a cargar la imagen, si no existe saltará el ícono de imagen rota que nos permite darnos cuenta
    with colA: 
        try: st.image(opciones_visuales[0], caption="Opción A") 
        except: st.error(f"Falta {opciones_visuales[0]}")
    with colB: 
        try: st.image(opciones_visuales[1], caption="Opción B")
        except: st.error(f"Falta {opciones_visuales[1]}")
    with colC: 
        try: st.image(opciones_visuales[2], caption="Opción C")
        except: st.error(f"Falta {opciones_visuales[2]}")
        
    q6 = st.radio("Seleccioná la correcta:", ["Opción A", "Opción B", "Opción C"], index=None)
    if st.button("Corregir Nivel 6"):
        if "nivel6" not in st.session_state.juegos_completados:
            if q6:
                idx = int(q6.split(" ")[1].replace('A','0').replace('B','1').replace('C','2'))
                if opciones_visuales[idx] == ritmo_actual['img_correcta']:
                    st.session_state.puntaje += 20
                    st.session_state.juegos_completados.append("nivel6")
                    st.success("¡Excelente oído rítmico! 20 puntos.")
                    st.balloons()
                else: st.error("Ese no es el ritmo. ¡Intentá escuchar de nuevo!")
        else: st.warning("Ya completaste este nivel.")

# ==================================
# 7. MEMOTEST (3 Modos + Escondite Automático)
# ==================================
elif juego_actual == "7. 🃏 Memotest de Instrumentos":
    st.header("🃏 Nivel 7: Memotest")
    
    modo_seleccionado = st.radio("Elegí la modalidad:", ["1. Imagen vs Nombre", "2. Sonido vs Imagen", "3. Sonido vs Nombre"], horizontal=True)
    
    # Si cambias de modo, se reinicia el mazo
    if 'memo_modo_actual' not in st.session_state or st.session_state.memo_modo_actual != modo_seleccionado:
        st.session_state.memo_modo_actual = modo_seleccionado
        st.session_state.memo_deck = generar_mazo(modo_seleccionado)
        st.session_state.memo_flipped = []
        st.session_state.memo_matched = []
        st.rerun()

    deck = st.session_state.memo_deck
    
    cols = st.columns(4)
    for i in range(8):
        with cols[i % 4]:
            if i in st.session_state.memo_matched:
                st.success("✔️")
                if deck[i]['tipo'] == 'img':
                    try: st.image(deck[i]['valor'])
                    except: st.write("Imagen")
                elif deck[i]['tipo'] == 'texto':
                    st.markdown(f"**{deck[i]['valor']}**")
                elif deck[i]['tipo'] == 'audio':
                    st.markdown("🔊 **Sonido**")

            elif i in st.session_state.memo_flipped:
                st.info("👀")
                if deck[i]['tipo'] == 'img':
                    try: st.image(deck[i]['valor'])
                    except: st.write("Imagen")
                elif deck[i]['tipo'] == 'texto':
                    st.markdown(f"**{deck[i]['valor']}**")
                elif deck[i]['tipo'] == 'audio':
                    parlante = buscar_archivo("parlante", "imagen") or "logo_audinos_abreviado_color_sin_letras.png"
                    if os.path.exists(parlante): st.image(parlante)
                    if os.path.exists(deck[i]['valor']): st.audio(deck[i]['valor'])
                    else: st.error("Audio faltante")

            else:
                dorso = buscar_archivo("logo_audinos_abreviado_color_sin_letras", "imagen")
                if dorso: st.image(dorso)
                if st.button("Girar", key=f"btn_{i}"):
                    if len(st.session_state.memo_flipped) < 2:
                        st.session_state.memo_flipped.append(i)
                        st.rerun()

    # LOGICA DE AUTO-ESCONDITE (Se ejecuta después de dibujar las cartas)
    if len(st.session_state.memo_flipped) == 2:
        c1, c2 = st.session_state.memo_flipped
        if deck[c1]['id'] == deck[c2]['id']:
            st.success("¡Pareja encontrada!")
            time.sleep(1.5) # Espera un segundo y medio para que el chico la vea
            st.session_state.memo_matched.extend([c1, c2])
            st.session_state.memo_flipped = []
            st.rerun() # Se actualiza sola
        else:
            st.error("No coinciden...")
            time.sleep(1.5) # Espera un segundo y medio
            st.session_state.memo_flipped = []
            st.rerun() # Se esconden solas

    if len(st.session_state.memo_matched) == 8 and "nivel7" not in st.session_state.juegos_completados:
        st.session_state.puntaje += 30
        st.session_state.juegos_completados.append("nivel7")
        st.success("¡Completaste el Memotest! Sumaste 30 puntos.")
        st.balloons()

# ==================================
# 8. BATALLA GRAVE VS AGUDO (Buscador inteligente)
# ==================================
elif juego_actual == "8. ⚖️ Batalla: Grave vs Agudo":
    st.header("⚖️ Nivel 8: Batalla de Alturas")
    batalla = st.session_state.pregunta_n8
    if 'orden_n8' not in st.session_state:
        opciones = [batalla['grave'], batalla['agudo']]
        random.shuffle(opciones)
        st.session_state.orden_n8 = opciones
        
    opciones = st.session_state.orden_n8
    
    colA, colB = st.columns(2)
    with colA:
        st.write("**Instrumento A**")
        audio_a = buscar_archivo(opciones[0], "audio")
        if audio_a: st.audio(audio_a)
        else: st.error(f"Falta audio de {opciones[0]}")
        
    with colB:
        st.write("**Instrumento B**")
        audio_b = buscar_archivo(opciones[1], "audio")
        if audio_b: st.audio(audio_b)
        else: st.error(f"Falta audio de {opciones[1]}")
        
    q8 = st.radio("¿Cuál tiene el registro más GRAVE?", ["Instrumento A", "Instrumento B"], index=None)
    if st.button("Corregir Nivel 8"):
        if "nivel8" not in st.session_state.juegos_completados:
            if q8:
                seleccionado = opciones[0] if q8 == "Instrumento A" else opciones[1]
                if seleccionado == batalla['grave']:
                    st.session_state.puntaje += 20
                    st.session_state.juegos_completados.append("nivel8")
                    st.success(f"¡Exacto! El {batalla['grave'].replace('_', ' ')} es mucho más grave.")
                    st.balloons()
                else: st.error("Ups, ese era el más agudo.")
        else: st.warning("Ya completaste este nivel.")

# ==================================
# HERRAMIENTA PARA EL PROFE
# ==================================
elif juego_actual == "🛠️ Radar de Archivos (Profe)":
    st.header("🛠️ Panel de Diagnóstico")
    st.write("Si ves algo en ROJO, significa que ese archivo no está subido a GitHub o tiene el nombre mal escrito.")
    
    st.subheader("Audios del Memotest y Grave/Agudo")
    for inst in instrumentos_memotest + ["tuba", "contrabajo", "trombon"]:
        if buscar_archivo(inst, "audio"): st.success(f"✔️ {inst} (Audio OK)")
        else: st.error(f"❌ Falta audio de: {inst}")
            
    st.subheader("Imágenes de Instrumentos")
    for inst in instrumentos_memotest:
        if buscar_archivo(inst, "imagen"): st.success(f"✔️ {inst} (Imagen OK)")
        else: st.error(f"❌ Falta imagen de: {inst}")
            
    st.subheader("Dictados Rítmicos")
    for r in banco_ritmos:
        if buscar_archivo(r['audio'], "audio"): st.success(f"✔️ Audio: {r['audio']}")
        else: st.error(f"❌ Falta audio: {r['audio']}")
        if buscar_archivo(r['img_correcta'].replace(".png",""), "imagen"): st.success(f"✔️ Imagen: {r['img_correcta']}")
        else: st.error(f"❌ Falta imagen: {r['img_correcta']}")
