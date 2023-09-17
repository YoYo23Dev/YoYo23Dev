import logging 
  
 from telegram import ForceReply, Update 
 from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters 
  
 # Enable logging 
 logging.basicConfig( 
     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO 
 ) 
 # set higher logging level for httpx to avoid all GET and POST requests being logged 
 logging.getLogger("httpx").setLevel(logging.WARNING) 
  
 logger = logging.getLogger(name) 
  
  
 # Define a few command handlers. These usually take the two arguments update and 
 # context. 
 async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: 
     """Send a message when the command /start is issued.""" 
     user = update.effective_user 
     await update.message.reply_html( 
         rf"Hi {user.mention_html()}!", 
         reply_markup=ForceReply(selective=True), 
     ) 
  
  
 async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: 
     """Send a message when the command /help is issued.""" 
     await update.message.reply_text("Help!") 
  
  
 async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: 
     """Echo the user message.""" 
     await update.message.reply_text(update.message.text) 
  
  
 def main() -> None: 
     """Start the bot.""" 
     # Create the Application and pass it your bot's token. 
     application = Application.builder().token("6675505705:AAHujQAMvbbrVq3XyU7k8xkrQLbbR6ZPwpc").build() 
  
     # on different commands - answer in Telegram 
     application.add_handler(CommandHandler("start", start)) 
     application.add_handler(CommandHandler("help", help_command)) 
  
     # on non command i.e message - echo the message on Telegram 
     def obtener_palabra_secreta():
    palabras = ["abandonado", "abalanzarse", "abanderado", "abandonar", "abarcar", "abatido", "abiertamente", "abismo", "abogado", "abominable", "aborrecer", "abrasivo", "abstemio", "absorber", "abuelo", "abundancia", "acabar", "acceso", "accidente", "aceptar", "acero", "acierto", "aclamación", "acomodar", "acorde", "acostumbrado", "acrobacia", "actividad", "actual", "acuático", "adecuado", "adios", "admiración", "adolescente", "adquirir", "adulterado", "afable", "afectar", "aficionado", "agente", "agitar", "agotado", "agradable", "agresivo", "agua", "aguacate", "ahogado", "aire", "ajedrez", "ajuste", "alabanza", "alambre", "albañil", "alboroto", "alcalde", "aldea", "alegría", "alentar", "alergia", "alfabeto", "alga", "aliento", "alivio", "almendra", "alpaca", "altar", "altavoz", "alumno", "alzar", "amable", "amante", "amarillo", "ambición", "amistad", "amor", "análisis", "anciano", "ancla", "andar", "anémona", "angustia", "anillo", "anochecer", "antiguo", "anunciar", "añadir", "apagar", "aparecer", "apetito", "aplastar", "aplauso", "aplicar", "apoyar", "aprender", "apretado", "aprovechar", "aproximado", "árbol", "arcilla", "ardilla", "arena", "aroma", "arpa", "arquitecto", "arrancar", "arrebato", "arruga", "arte", "ascensor", "asiento", "asistir", "asombro", "aspirar", "astro", "atacar", "atención", "atleta", "atmósfera", "atraer", "augurio", "aumentar", "ausente", "avance", "aventura", "ave", "avería", "ávido", "avión", "ayuda", "azote", "azúcar", "azul", "acceder", "año", "ángel", "ángulo", "ánimo", "año nuevo", "árbol genealógico", "acuario", "ópera", "éxito", "étnico", "último", "útil""python", "programacion", "juego", "computadora", "adivinar"]
    return random.choice(palabras)

def jugar_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_correctas = []
    intentos = 6
    
    print("¡Bienvenido al juego del Ahorcado!")
    print("------------------")
    
    while True:
        palabra_actual = ""
        for letra in palabra_secreta:
            if letra in letras_correctas:
                palabra_actual += letra
            else:
                palabra_actual += "_"
        
        print("Palabra actual:", palabra_actual)
        print("Intentos restantes:", intentos)
        
        if palabra_actual == palabra_secreta:
            print("¡Felicidades! ¡Has adivinado la palabra!")
            break
        
        if intentos == 0:
            print("Oh no, te has quedado sin intentos. ¡Perdiste!")
            print("La palabra secreta era:", palabra_secreta)
            break
        
        letra_ingresada = input("Ingresa una letra: ").lower()
        
        if letra_ingresada in letras_correctas:
            print("Ya has ingresado esa letra. ¡Intenta nuevamente!")
            continue
        
        if letra_ingresada.isalpha() == False or len(letra_ingresada) > 1:
            print("Por favor, ingresa una única letra válida.")
            continue
        
        if letra_ingresada in palabra_secreta:
            letras_correctas.append(letra_ingresada)
            print("¡Correcto! Has adivinado una letra.")
        else:
            intentos -= 1
            print("Incorrecto. Te queda(n)", intentos, "intentos restante(s).")
        
        print("------------------")

jugar_ahorcado()
  
     # Run the bot until the user presses Ctrl-C 
     application.run_polling(allowed_updates=Update.ALL_TYPES) 
  
  
 if name == "main": 
     main()
