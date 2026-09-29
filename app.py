import streamlit as st
import os
import random
import time

# Configuración de la página
st.set_page_config(page_title="Juegos Musicales - LAC", page_icon="🎮", layout="centered")

# Inyectar CSS para poner fondo blanco a las imágenes transparentes
st.markdown("""
    <style>
    img {
        background-color: white;
        border-radius: 10px;
        padding: 10px;
    }
    .stButton>button {
        width: 100%;
        height: 100px;
        font-size: 20px;
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

# --- BANCOS DE PREGUNTAS (1 al 5) ---
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
    {"pregunta": "¿Qué distancia hay entre Do y el siguiente Do?", "opciones": ["Sexta", "Séptima", "Octava"], "correcta": "Octava"},
    {"pregunta": "¿Qué distancia hay entre La y Do (agudo)?", "opciones": ["Segunda", "Tercera", "Cuarta"], "correcta": "Tercera"}
]

# --- DATOS PARA NUEVOS JUEGOS ---
banco_ritmos = [
    {"audio": "corto corto largo audio.mp3", "img_correcta": "corto corto largo imagen.png", "nombre": "Corto Corto Largo"},
    {"audio": "corto largo corto audio.mp3", "img_correcta": "corto largo corto imagen.png", "nombre": "Corto Largo Corto"},
    {"audio": "corto largo corto corto audio.mp3", "img_correcta": "corto largo corto corto imagen.png", "nombre": "Corto Largo Corto Corto"}
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

# --- ESTADO DEL MEMOTEST ---
if 'memo_deck' not in st.session_state:
    # Crear pares: 4 imágenes y 4 nombres
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
    st.session_state.clear() # Limpia todo y reinicia
    st.rerun()

# --- NIVELES 1 al 5 (Mantenidos igual que tu versión) ---
if juego_actual == "1. Historia y Orígenes":
    st.header("📜 Nivel 1: Historia de las Notas")
    q1 = st.radio("1. ¿Dónde se encontró la partitura musical más antigua hace 3400 años?", ["Egipto", "Roma", "Siria", "Grecia"], index=None)
    q2 = st.radio("2. ¿Qué monje italiano ideó los nombres de las notas en el siglo XI?", ["San Juan", "Guido D'Arezzo", "Papa Gregorio"], index=None)
    q3 = st.radio("3. ¿Por qué se reemplazó la sílaba 'Ut' por la nota 'Do'?", ["Porque sobraba una letra", "Porque era el nombre de una diosa", "Porque Do era más fácil de pronunciar"], index=None)
    
    if st.button("Corregir Nivel 1"):
        if "nivel1" not in st.session_state.juegos_completados:
            puntos = (q1 == "Siria")*10 + (q2 == "Guido D'Arezzo")*10 + (q3 == "Porque Do era más fácil de pronunciar")*10
            st.session_state.puntaje += puntos
            st.session_state.juegos_completados.append("nivel1")
            st.success(f"¡Excelente! Sumaste {puntos} puntos.")
        else: st.warning("Ya completaste este nivel.")

elif juego_actual == "2. La Escalera de Notas":
    st.header("🪜 Nivel 2: Grados Conjuntos")
    q1 = st.radio("1. ¿Cuáles son las notas vecinas de SOL?", ["Do y Mi", "Fa y La", "La y Si"], index=None)
    q2 = st.radio("2. ¿Cuáles son las notas vecinas de RE?", ["Do y Mi", "Fa y Sol", "Si y Do"], index=None)
    q3 = st.radio("3. ¿Cuáles son las notas vecinas de DO?", ["Mi y Fa", "Sol y La", "Si y Re"], index=None)

    if st.button("Corregir Nivel 2"):
        if "nivel2" not in st.session_state.juegos_completados:
            puntos = (q1 == "Fa y La")*10 + (q2 == "Do y Mi")*10 + (q3 == "Si y Re")*10
            st.session_state.puntaje += puntos
            st.session_state.juegos_completados.append("nivel2")
            st.success(f"¡Bien ahí! Sumaste {puntos} puntos.")
        else: st.warning("Ya completaste este nivel.")

elif juego_actual == "3. El Pentagrama Visual":
    st.header("🎼 Nivel 3: El Pentagrama")
    respuestas_n3 = []
    for i, q in enumerate(st.session_state.preguntas_n3):
        st.markdown(f"**Pregunta {i+1}:**")
        if os.path.exists(q['img']): st.image(q['img'], width=200)
        resp = st.radio("¿Qué nota ves arriba?", q['opciones'], key=f"n3_{i}", index=None)
        respuestas_n3.append((resp, q['correcta']))
        st.write("---")

    if st.button("Corregir Nivel 3"):
        if "nivel3" not in st.session_state.juegos_completados:
            puntos = sum(10 for seleccion, correcta in respuestas_n3 if seleccion == correcta)
            st.session_state.puntaje += puntos
            st.session_state.juegos_completados.append("nivel3")
            st.success(f"¡Genial! Sumaste {puntos} puntos.")
        else: st.warning("Ya completaste este nivel.")

elif juego_actual == "4. Sonido, Eco y Figuras":
    st.header("🔊 Nivel 4: Cualidades y Figuras")
    q1 = st.radio("1. ¿Qué diferencia hay entre el Eco y la Reverberación?", ["El eco repite la palabra clara, la reverberación alarga el sonido", "Son exactamente lo mismo"], index=None)
    q2 = st.radio("2. ¿Qué cualidad del sonido nos permite distinguir si es Fuerte o Suave?", ["Altura", "Intensidad", "Timbre"], index=None)
    q3 = st.radio("3. ¿Cuál de estas figuras musicales dura más tiempo?", ["Negra", "Corchea", "Redonda", "Blanca"], index=None)

    if st.button("Corregir Nivel 4"):
        if "nivel4" not in st.session_state.juegos_completados:
            puntos = (q1 == "El eco repite la palabra clara, la reverberación alarga el sonido")*10 + (q2 == "Intensidad")*10 + (q3 == "Redonda")*10
            st.session_state.puntaje += puntos
            st.session_state.juegos_completados.append("nivel4")
            st.success(f"¡Súper! Sumaste {puntos} puntos.")
        else: st.warning("Ya completaste este nivel.")

elif juego_actual == "5. Calculadora de Intervalos":
    st.header("🥁 Nivel 5: Compases e Intervalos (Aleatorio)")
    q_compas = st.radio("1. ¿Un compás de 6/8 es simple o compuesto?", ["Simple", "Compuesto"], index=None)
    respuestas_n5 = []
    for i, q in enumerate(st.session_state.preguntas_n5[:2]):
        resp = st.radio(f"{i+2}. {q['pregunta']}", q['opciones'], key=f"n5_{i}", index=None)
        respuestas_n5.append((resp, q['correcta']))

    if st.button("Corregir Nivel 5"):
        if "nivel5" not in st.session_state.juegos_completados:
            puntos = (q_compas == "Compuesto")*10 + sum(10 for seleccion, correcta in respuestas_n5 if seleccion == correcta)
            st.session_state.puntaje += puntos
            st.session_state.juegos_completados.append("nivel5")
            st.success(f"¡Perfecto! Sumaste {puntos} puntos.")
        else: st.warning("Ya completaste este nivel.")

# --- NUEVOS NIVELES ---

elif juego_actual == "6. 📝 Dictado Rítmico":
    st.header("📝 Nivel 6: Correspondencia Rítmica")
    st.write("Escuchá el audio y elegí la imagen que representa esa duración.")
    
    ritmo_actual = st.session_state.pregunta_n6
    
    if os.path.exists(ritmo_actual['audio']):
        st.audio(ritmo_actual['audio'])
    else:
        st.error(f"Falta subir el audio: {ritmo_actual['audio']}")
        
    st.write("¿Cuál de estos ritmos acaba de sonar?")
    
    # Mostrar opciones visuales
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
                else:
                    st.error("Ese no es el ritmo. ¡Intentá escuchar de nuevo!")
        else: st.warning("Ya completaste este nivel.")

elif juego_actual == "7. 🃏 Memotest de Instrumentos":
    st.header("🃏 Nivel 7: Memotest")
    st.write("Encontrá los pares uniendo la **imagen del instrumento** con su **nombre**.")
    
    # Lógica del Memotest
    deck = st.session_state.memo_deck
    flipped = st.session_state.memo_flipped
    matched = st.session_state.memo_matched
    
    # Dibujar la grilla 4x2
    cols = st.columns(4)
    for i in range(8):
        with cols[i % 4]:
            if i in matched:
                st.success("✔️ Pareja")
                if deck[i]['tipo'] == 'img' and os.path.exists(deck[i]['valor']):
                    st.image(deck[i]['valor'])
                else:
                    st.write(f"**{deck[i]['valor']}**")
            elif i in flipped:
                if deck[i]['tipo'] == 'img' and os.path.exists(deck[i]['valor']):
                    st.image(deck[i]['valor'])
                else:
                    st.info(f"**{deck[i]['valor']}**")
            else:
                # Mostrar el dorso de la carta
                dorso = "logo_audinos_abreviado_color_sin_letras.png"
                if os.path.exists(dorso):
                    st.image(dorso)
                if st.button(f"Girar carta {i+1}", key=f"btn_{i}"):
                    if len(flipped) < 2:
                        st.session_state.memo_flipped.append(i)
                        st.rerun()
    
    # Lógica de comprobación
    if len(flipped) == 2:
        c1, c2 = flipped[0], flipped[1]
        if deck[c1]['id'] == deck[c2]['id']:
            st.session_state.memo_matched.extend([c1, c2])
            st.session_state.memo_flipped = []
            st.success("¡Pareja encontrada!")
            time.sleep(1)
            st.rerun()
        else:
            st.error("No coinciden...")
            if st.button("Ocultar cartas de nuevo"):
                st.session_state.memo_flipped = []
                st.rerun()
                
    if len(matched) == 8 and "nivel7" not in st.session_state.juegos_completados:
        st.session_state.puntaje += 30
        st.session_state.juegos_completados.append("nivel7")
        st.success("¡Completaste el Memotest! Sumaste 30 puntos.")
        st.balloons()

elif juego_actual == "8. ⚖️ Batalla: Grave vs Agudo":
    st.header("⚖️ Nivel 8: Batalla de Alturas")
    st.write("Escuchá estos dos instrumentos y decidí cuál suena más **Grave**.")
    
    batalla = st.session_state.pregunta_n8
    
    # Aleatorizar orden de A y B
    if 'orden_n8' not in st.session_state:
        opciones = [batalla['grave'], batalla['agudo']]
        random.shuffle(opciones)
        st.session_state.orden_n8 = opciones
        
    opciones = st.session_state.orden_n8
    
    colA, colB = st.columns(2)
    with colA:
        st.write("**Instrumento A**")
        audio_a = f"{opciones[0]} 2.mp3" if not os.path.exists(f"{opciones[0]}.mp3") else f"{opciones[0]}.mp3" # Intenta con o sin 2
        if os.path.exists(audio_a): st.audio(audio_a)
        else: st.write(f"*(Falta audio {opciones[0]})*")
        
    with colB:
        st.write("**Instrumento B**")
        audio_b = f"{opciones[1]} 2.mp3" if not os.path.exists(f"{opciones[1]}.mp3") else f"{opciones[1]}.mp3"
        if os.path.exists(audio_b): st.audio(audio_b)
        else: st.write(f"*(Falta audio {opciones[1]})*")
        
    q8 = st.radio("¿Cuál de los dos instrumentos tiene el registro más GRAVE?", ["Instrumento A", "Instrumento B"], index=None)
    
    if st.button("Corregir Nivel 8"):
        if "nivel8" not in st.session_state.juegos_completados:
            if q8:
                seleccionado = opciones[0] if q8 == "Instrumento A" else opciones[1]
                if seleccionado == batalla['grave']:
                    st.session_state.puntaje += 20
                    st.session_state.juegos_completados.append("nivel8")
                    st.success(f"¡Exacto! El {batalla['grave'].replace('_', ' ')} es mucho más grave. 20 puntos.")
                    st.balloons()
                else:
                    st.error("Ups, ese era el más agudo. ¡Prestá atención a las frecuencias bajas!")
        else: st.warning("Ya completaste este nivel.")
