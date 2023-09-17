import logging
from telegram.ext import Updater, CommandHandler
from pytube import YouTube

# Configura el token de tu bot de Telegram
TOKEN = '6675505705:AAHujQAMvbbrVq3XyU7k8xkrQLbbR6ZPwpc'

# Configura la carpeta donde se guardarán los videos descargados
DOWNLOAD_PATH = '/path/to/save/videos'

# Configura el nivel de registro del bot
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(name)

def start(update, context):
    """Handler para el comando /start"""
    update.message.reply_text('¡Hola! Envíame el enlace de un video de YouTube y lo descargaré por ti.')

def download_video(update, context):
    """Handler para manejar el enlace de descarga"""
    # Obtiene el enlace del mensaje de texto enviado por el usuario
    video_link = update.message.text

    try:
        # Descarga el video utilizando la biblioteca pytube
        youtube = YouTube(video_link)
        video = youtube.streams.get_highest_resolution()
        video.download(DOWNLOAD_PATH)

        # Envía un mensaje de confirmación al usuario
        update.message.reply_text('¡Video descargado correctamente!')
    except Exception as e:
        # Manejo de errores
        logger.error('Error al descargar el video: %s', str(e))
        update.message.reply_text('No se pudo descargar el video. Por favor, verifica el enlace e intenta nuevamente.')

def main():
    """Función principal del bot"""
    # Crea la instancia de Updater con el token de tu bot
    updater = Updater(TOKEN, use_context=True)

    # Obtiene el despachador para registrar los controladores de comandos
    dp = updater.dispatcher

    # Registra un controlador para el comando /start
    dp.add_handler(CommandHandler("start", start))

    # Registra un controlador para cualquier mensaje de texto
    dp.add_handler(CommandHandler("link", download_video))

    # Inicia el bot
    updater.start_polling()

    # Ejecuta el bot hasta que se presione Ctrl-C para detenerlo
    updater.idle()

if name == 'main':
    main()
