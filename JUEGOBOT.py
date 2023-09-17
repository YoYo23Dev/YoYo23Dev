import random
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Palabras para el juego del Ahorcado
palabras = ["abandonado", "abalanzarse", "abanderado", "abandonar", "abarcar", "abatido", "abiertamente", "abismo", "abogado", "abominable", "aborrecer", "abrasivo", "abstemio", "absorber", "abuelo", "abundancia", "acabar", "acceso", "accidente", "aceptar", "acero", "acierto", "aclamación", "acomodar", "acorde", "acostumbrado", "acrobacia", "actividad", "actual", "acuático", "adecuado", "adios", "admiración", "adolescente", "adquirir", "adulterado", "afable", "afectar", "aficionado", "agente", "agitar", "agotado", "agradable", "agresivo", "agua", "aguacate", "ahogado", "aire", "ajedrez", "ajuste", "alabanza", "alambre", "albañil", "alboroto", "alcalde", "aldea", "alegría", "alentar", "alergia", "alfabeto", "alga", "aliento", "alivio", "almendra", "alpaca", "altar", "altavoz", "alumno", "alzar", "amable", "amante", "amarillo", "ambición", "amistad", "amor", "análisis", "anciano", "ancla", "andar", "anémona", "angustia", "anillo", "anochecer", "antiguo", "anunciar", "añadir", "apagar", "aparecer", "apetito", "aplastar", "aplauso", "aplicar", "apoyar", "aprender", "apretado", "aprovechar", "aproximado", "árbol", "arcilla", "ardilla", "arena", "aroma", "arpa", "arquitecto", "arrancar", "arrebato", "arruga", "arte", "ascensor", "asiento", "asistir", "asombro", "aspirar", "astro", "atacar", "atención", "atleta", "atmósfera", "atraer", "augurio", "aumentar", "ausente", "avance", "aventura", "ave", "avería", "ávido", "avión", "ayuda", "azote", "azúcar", "azul", "acceder", "año", "ángel", "ángulo", "ánimo", "año nuevo", "árbol genealógico", "acuario", "ópera", "éxito", "étnico", "último", "útil""python", "programacion", "bot", "telegram", "juego", "diversion"]

# Función para manejar el comando /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="¡Bienvenido al juego del Ahorcado! ¡Adivina la palabra!")

# Función para manejar el comando /ayuda
def ayuda(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="¡Este es el juego del Ahorcado! Intenta adivinar la palabra letra por letra.")

# Función para manejar los mensajes recibidos
def mensaje_recibido(update, context):
    mensaje = update.message.text.lower()
    chat_id = update.effective_chat.id
    if mensaje.isalpha():
        letra = mensaje
        if letra in palabra_oculta:
            for i, l in enumerate(palabra_oculta):
                if l == letra:
                    palabra_mostrada[i] = letra
            if "_" not in palabra_mostrada:
                context.bot.send_message(chat_id=chat_id, text="¡Felicidades! Has adivinado la palabra: {}".format(palabra_oculta.upper()))
                iniciar_juego()
            else:
                context.bot.send_message(chat_id=chat_id, text="¡Correcto! Has acertado una letra.")
                context.bot.send_message(chat_id=chat_id, text="Palabra: {}".format(" ".join(palabra_mostrada)))
        else:
            context.bot.send_message(chat_id=chat_id, text="¡Incorrecto! Inténtalo de nuevo.")
    else:
        context.bot.send_message(chat_id=chat_id, text="Por favor, ingresa una letra válida.")

# Función para iniciar un nuevo juego
def iniciar_juego():
    global palabra_oculta, palabra_mostrada
    palabra_oculta = random.choice(palabras)
    palabra_mostrada = ["_" for _ in palabra_oculta]

# Configuración del bot y los comandos
updater = Updater(token="TU_TOKEN")
dispatcher = updater.dispatcher

start_handler = CommandHandler("start", start)
ayuda_handler = CommandHandler("ayuda", ayuda)
mensaje_recibido_handler = MessageHandler(Filters.text, mensaje_recibido)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(ayuda_handler)
dispatcher.add_handler(mensaje_recibido_handler)

# Iniciar el bot
updater.start_polling()
