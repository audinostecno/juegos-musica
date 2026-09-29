import streamlit as st
import os
import random

# Configuración de la página
st.set_page_config(page_title="Juegos Musicales - LAC", page_icon="🎮", layout="centered")

# --- LÓGICA FLUIDA DEL MEMOTEST (Sin botones de reinicio) ---
def procesar_giro(idx):
    # Si ya hay 2 cartas dadas vuelta (que no coincidieron), las ocultamos y damos vuelta la nueva
    if len(st.session_state.memo_flipped) == 2:
        st.session_state.memo_flipped = [idx]
    else:
        # Si había 0 o 1, simplemente la damos vuelta
        st.session_state.memo_flipped.append(idx)
        # Verificamos si al dar vuelta esta carta se formó el par
        if len(st.session_state.memo_flipped) == 2:
            c1, c2 = st.session_state.memo_flipped[0], st.session_state.memo_flipped[1]
            if st.session_state.memo_deck[c1]['id'] == st.session_state.memo_deck[c2]['id']:
                # ¡Coinciden! Las guardamos como resueltas y limpiamos la mesa para seguir
                st.session_state.memo_matched.extend([c1, c2])
                st.session_state.memo_flipped = []

# Inyectar CSS para diseño de imágenes y cartas
st.markdown("""
    <style>
    img {
        background-color: white;
        border-radius: 10px;
        padding: 10px;
    }
    .stButton>button {
        width: 100%;
        height: 60px;
        font-size: 18px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Cabecera
col1, col2 = st.columns([1, 4])
with col1:
    if os.path.exists("juan_cartoon.png"):
        st.image("juan_cartoon.png", width=120)
with col2:
    st.title("🎮 Sala de Juegos - LAC Música")
    st.write("¡Poné a prueba lo que aprendimos en clase!")

# --- BANCOS DE PREGUNTAS ---
banco_pentagrama = [
    {"img": "clave_de_sol_nota_do.png", "opciones": ["Do", "Re", "Mi"], "correcta": "Do"},
    {"img": "clave_de_sol_nota_re.png", "opciones": ["Re", "Fa", "Sol"], "correcta": "Re"},
    {"img": "clave_de_sol_nota_dosostenido.png", "opciones": ["Do", "Do sostenido", "Re bemol"], "correcta": "Do sostenido"},
    {"img": "clave_de_sol_nota_mib.png", "opciones": ["Mi", "Re sostenido", "Mi bemol"], "correcta": "Mi bemol"},
    {"img": "clave_de_sol_nota_fa.png", "opciones": ["Fa", "La", "Si"], "correcta": "Fa"},
    {"img": "clave_de_sol_nota_sol.png", "opciones": ["Fa", "Sol", "La"], "correcta": "Sol"},
    {"img": "clave_de_sol_nota_la.png", "opciones": ["Sol", "La", "Si"], "correcta": "La"},
    {"img": "clave_de_sol_nota_lasostenido.png", "opciones": ["La", "La sostenido", "Si bemol"], "correcta": "La sostenido"},
    {"img": "clave_de_sol_nota_sib.png", "opciones": ["Si", "Si bemol", "La sostenido"], "correcta": "Si bemol"},
    {"img": "clave_de_fa_nota_re.png", "opciones": ["Fa", "Re", "Si"], "correcta": "Re"},
    {"img": "clave_de_fa_nota_fa.png", "opciones": ["Re", "Fa", "La"], "correcta": "Fa"}
]

banco_intervalos = [
    {"pregunta": "¿Qué distancia hay entre Re y Sol?", "opciones": ["Tercera", "Cuarta", "Quinta"], "correcta": "Cuarta"},
    {"pregunta": "¿Qué distancia hay entre Do y Mi?", "opciones": ["Segunda", "Tercera", "Cuarta"], "correcta": "Tercera"},
    {"pregunta": "¿Qué distancia hay entre Mi y Si?", "opciones": ["Cuarta", "Quinta", "Sexta"], "correcta": "Quinta"},
    {"pregunta": "¿Qué distancia hay entre Fa y Sol?", "opciones": ["Primera", "Segunda", "Tercera"], "correcta": "Segunda"},
    {"pregunta": "¿Qué distancia hay entre Do y el siguiente Do?", "opciones": ["Sexta", "Séptima", "Octava"], "correcta": "Octava"}
]

banco_ritmos = [
    {"audio": "corto corto largo audio.mp3", "img_correcta": "corto corto largo imagen.png"},
    {"audio": "corto largo corto audio.mp3", "img_correcta": "corto largo corto imagen.png"},
    {"audio": "corto largo corto corto audio.mp3", "img_correcta": "corto largo corto corto imagen.png"}
]

instrumentos_memotest = ["violin", "trompeta", "piano", "flauta_traversa"]

banco_alturas = [
    {"grave": "tuba", "agudo": "flauta_traversa"},
    {"grave": "contrabajo", "agudo": "violin"},
    {"grave": "trombon", "agudo": "trompeta"}
]

# --- INICIALIZAR MEMORIA Y ESTADOS ---
if 'puntaje' not in st.session_state:
    st.session_state.puntaje = 0
if 'juegos_completados' not in st.session_state:
    st.session_state.juegos_completados = []

if 'preguntas_n3' not in st.session_state:
    st.session_state.preguntas_n3 = random.sample(banco_pentagrama, 3)
if 'preguntas_n5' not in st.session_state:
    st.session_state.preguntas_n5 = random.sample(banco_intervalos, 3)
if 'pregunta_n6' not in st.session_state:
    st.session_state.pregunta_n6 = random.choice(banco_ritmos)
if 'pregunta_n8' not in st.session_state:
    st.session_state.pregunta_n8 = random.choice(banco_alturas)

# --- INICIALIZAR MEMOTEST ---
if 'memo_deck' not in st.session_state:
    deck = []
    for inst in instrumentos_memotest:
        deck.append({"id": inst, "tipo": "img", "valor": f"{inst}.png"})
        deck.append({"id": inst, "tipo": "texto", "valor": inst.upper()})
    random.shuffle(deck)
    st.session_state.memo_deck = deck
    st.session_state.memo_flipped = []
    st.session_state.memo_matched = []

# Menú lateral
st.sidebar.title("📌 Menú de Desafíos")
juego_actual = st.sidebar.radio("Elegí un nivel:", 
    ["1. Historia y Orígenes", 
     "2. La Escalera de Notas", 
     "3. El Pentagrama Visual", 
     "4. Sonido, Eco y Figuras", 
     "5. Calculadora de Intervalos",
     "6. 📝 Dictado Rítmico",
     "7. 🃏 Memotest de Instrumentos",
     "8. ⚖️ Batalla: Grave vs Agudo"])

st.sidebar.markdown("---")
st.sidebar.title(f"🏆 Puntaje total: {st.session_state.puntaje}")
if st.sidebar.button("Jugar de nuevo (Mezclar todo)"):
    st.session_state.clear()
    st.rerun()

# ==================================
# JUEGOS CLÁSICOS (1 AL 5)
# ==================================
if juego_actual == "1. Historia y Orígenes":
    st.header("📜 Nivel 1: Historia de las Notas")
    q1 = st.radio("1. ¿Dónde se encontró la partitura más antigua?", ["Egipto", "Roma", "Siria", "Grecia"], index=None)
    q2 = st.radio("2. ¿Qué monje ideó los nombres de las notas?", ["San Juan", "Guido D'Arezzo", "Papa Gregorio"], index=None)
    q3 = st.radio("3. ¿Por qué se reemplazó 'Ut' por 'Do'?", ["Porque Do era más fácil de pronunciar", "Sobraba una letra"], index=None)
    if st.button("Corregir"):
        if "nivel1" not in st.session_state.juegos_completados:
            puntos = (q1 == "Siria")*10 + (q2 == "Guido D'Arezzo")*10 + (q3 == "Porque Do era más fácil de pronunciar")*10
            st.session_state.puntaje += puntos
            st.session_state.juegos_completados.append("nivel1")
            st.success(f"Sumaste {puntos} puntos.")
        else: st.warning("Nivel ya completado.")

elif juego_actual == "2. La Escalera de Notas":
    st.header("🪜 Nivel 2: Grados Conjuntos")
    q1 = st.radio("1. Notas vecinas de SOL:", ["Do y Mi", "Fa y La", "La y Si"], index=None)
    q2 = st.radio("2. Notas vecinas de RE:", ["Do y Mi", "Fa y Sol", "Si y Do"], index=None)
    q3 = st.radio("3. Notas vecinas de DO:", ["Mi y Fa", "Sol y La", "Si y Re"], index=None)
    if st.button("Corregir"):
        if "nivel2" not in st.session_state.juegos_completados:
            puntos = (q1 == "Fa y La")*10 + (q2 == "Do y Mi")*10 + (q3 == "Si y Re")*10
            st.session_state.puntaje += puntos
            st.session_state.juegos_completados.append("nivel2")
            st.success(f"Sumaste {puntos} puntos.")
        else: st.warning("Nivel ya completado.")

elif juego_actual == "3. El Pentagrama Visual":
    st.header("🎼 Nivel 3: El Pentagrama")
    respuestas_n3 = []
    for i, q in enumerate(st.session_state.preguntas_n3):
        st.markdown(f"**Pregunta {i+1}:**")
        if os.path.exists(q['img']): st.image(q['img'], width=200)
        resp = st.radio("¿Qué nota ves?", q['opciones'], key=f"n3_{i}", index=None)
        respuestas_n3.append((resp, q['correcta']))
    if st.button("Corregir"):
        if "nivel3" not in st.session_state.juegos_completados:
            puntos = sum(10 for r, c in respuestas_n3 if r == c)
            st.session_state.puntaje += puntos
            st.session_state.juegos_completados.append("nivel3")
            st.success(f"Sumaste {puntos} puntos.")
        else: st.warning("Nivel ya completado.")

elif juego_actual == "4. Sonido, Eco y Figuras":
    st.header("🔊 Nivel 4: Cualidades")
    q1 = st.radio("Diferencia Eco y Reverberación:", ["Eco repite claro, reverberación alarga el sonido", "Son lo mismo"], index=None)
    q2 = st.radio("Cualidad Fuerte/Suave:", ["Altura", "Intensidad", "Timbre"], index=None)
    q3 = st.radio("Figura más larga:", ["Negra", "Corchea", "Redonda"], index=None)
    if st.button("Corregir"):
        if "nivel4" not in st.session_state.juegos_completados:
            puntos = (q1 == "Eco repite claro, reverberación alarga el sonido")*10 + (q2 == "Intensidad")*10 + (q3 == "Redonda")*10
            st.session_state.puntaje += puntos
            st.session_state.juegos_completados.append("nivel4")
            st.success(f"Sumaste {puntos} puntos.")
        else: st.warning("Nivel ya completado.")

elif juego_actual == "5. Calculadora de Intervalos":
    st.header("🥁 Nivel 5: Intervalos")
    q_compas = st.radio("¿6/8 es simple o compuesto?", ["Simple", "Compuesto"], index=None)
    respuestas_n5 = []
    for i, q in enumerate(st.session_state.preguntas_n5):
        resp = st.radio(q['pregunta'], q['opciones'], key=f"n5_{i}", index=None)
        respuestas_n5.append((resp, q['correcta']))
    if st.button("Corregir"):
        if "nivel5" not in st.session_state.juegos_completados:
            puntos = (q_compas == "Compuesto")*10 + sum(10 for r, c in respuestas_n5 if r == c)
            st.session_state.puntaje += puntos
            st.session_state.juegos_completados.append("nivel5")
            st.success(f"Sumaste {puntos} puntos.")
        else: st.warning("Nivel ya completado.")

# ==================================
# NUEVOS JUEGOS INTELIGENTES
# ==================================
elif juego_actual == "6. 📝 Dictado Rítmico":
    st.header("📝 Nivel 6: Correspondencia Rítmica")
    ritmo_actual = st.session_state.pregunta_n6
    
    if os.path.exists(ritmo_actual['audio']):
        st.audio(ritmo_actual['audio'])
    else: st.error(f"Falta el audio: {ritmo_actual['audio']}")
        
    st.write("¿Cuál de estos ritmos acaba de sonar?")
    opciones_visuales = [r['img_correcta'] for r in banco_ritmos]
    random.shuffle(opciones_visuales)
    
    colA, colB, colC = st.columns(3)
    with colA:
        if os.path.exists(opciones_visuales[0]): st.image(opciones_visuales[0], caption="Opción A")
    with colB:
        if os.path.exists(opciones_visuales[1]): st.image(opciones_visuales[1], caption="Opción B")
    with colC:
        if os.path.exists(opciones_visuales[2]): st.image(opciones_visuales[2], caption="Opción C")
        
    q6 = st.radio("Seleccioná la correcta:", ["Opción A", "Opción B", "Opción C"], index=None)
    if st.button("Corregir Nivel 6"):
        if "nivel6" not in st.session_state.juegos_completados:
            if q6:
                idx_seleccionado = int(q6.split(" ")[1].replace('A','0').replace('B','1').replace('C','2'))
                if opciones_visuales[idx_seleccionado] == ritmo_actual['img_correcta']:
                    st.session_state.puntaje += 20
                    st.session_state.juegos_completados.append("nivel6")
                    st.success("¡Excelente oído rítmico! 20 puntos.")
                    st.balloons()
                else: st.error("Ese no es el ritmo. ¡Intentá escuchar de nuevo!")
        else: st.warning("Ya completaste este nivel.")

elif juego_actual == "7. 🃏 Memotest de Instrumentos":
    st.header("🃏 Nivel 7: Memotest")
    st.write("Encontrá los pares uniendo la **imagen** con su **nombre**.")
    if len(st.session_state.memo_flipped) == 2:
        st.error("No coinciden... Hacé clic en cualquier otra carta para continuar.")
    
    cols = st.columns(4)
    for i in range(8):
        with cols[i % 4]:
            if i in st.session_state.memo_matched:
                st.success("✔️ Pareja")
                if st.session_state.memo_deck[i]['tipo'] == 'img' and os.path.exists(st.session_state.memo_deck[i]['valor']):
                    st.image(st.session_state.memo_deck[i]['valor'])
                else: st.markdown(f"**{st.session_state.memo_deck[i]['valor']}**")
            elif i in st.session_state.memo_flipped:
                st.info("👀")
                if st.session_state.memo_deck[i]['tipo'] == 'img' and os.path.exists(st.session_state.memo_deck[i]['valor']):
                    st.image(st.session_state.memo_deck[i]['valor'])
                else: st.markdown(f"**{st.session_state.memo_deck[i]['valor']}**")
            else:
                dorso = "logo_audinos_abreviado_color_sin_letras.png"
                if os.path.exists(dorso): st.image(dorso)
                # EL BOTÓN MAGICO QUE LLAMA A LA FUNCIÓN AL HACER CLIC
                st.button("Girar", key=f"btn_{i}", on_click=procesar_giro, args=(i,))
                
    if len(st.session_state.memo_matched) == 8 and "nivel7" not in st.session_state.juegos_completados:
        st.session_state.puntaje += 30
        st.session_state.juegos_completados.append("nivel7")
        st.success("¡Completaste el Memotest! Sumaste 30 puntos.")
        st.balloons()

elif juego_actual == "8. ⚖️ Batalla: Grave vs Agudo":
    st.header("⚖️ Nivel 8: Batalla de Alturas")
    st.write("Escuchá estos dos instrumentos y decidí cuál suena más **Grave**.")
    
    batalla = st.session_state.pregunta_n8
    if 'orden_n8' not in st.session_state:
        opciones = [batalla['grave'], batalla['agudo']]
        random.shuffle(opciones)
        st.session_state.orden_n8 = opciones
        
    opciones = st.session_state.orden_n8
    
    colA, colB = st.columns(2)
    with colA:
        st.write("**Instrumento A**")
        audio_a = f"{opciones[0]} 2.mp3" if not os.path.exists(f"{opciones[0]}.mp3") else f"{opciones[0]}.mp3"
        if os.path.exists(audio_a): st.audio(audio_a)
        else: st.write(f"*(Falta audio {opciones[0]})*")
        
    with colB:
        st.write("**Instrumento B**")
        audio_b = f"{opciones[1]} 2.mp3" if not os.path.exists(f"{opciones[1]}.mp3") else f"{opciones[1]}.mp3"
        if os.path.exists(audio_b): st.audio(audio_b)
        else: st.write(f"*(Falta audio {opciones[1]})*")
        
    q8 = st.radio("¿Cuál tiene el registro más GRAVE?", ["Instrumento A", "Instrumento B"], index=None)
    if st.button("Corregir Nivel 8"):
        if "nivel8" not in st.session_state.juegos_completados:
            if q8:
                seleccionado = opciones[0] if q8 == "Instrumento A" else opciones[1]
                if seleccionado == batalla['grave']:
                    st.session_state.puntaje += 20
                    st.session_state.juegos_completados.append("nivel8")
                    st.success(f"¡Exacto! El {batalla['grave'].replace('_', ' ')} es mucho más grave. 20 puntos.")
                    st.balloons()
                else: st.error("Ups, ese era el más agudo. ¡Prestá atención a las frecuencias bajas!")
        else: st.warning("Ya completaste este nivel.")
