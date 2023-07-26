import traceback
from app.routes import app
from app import config
from src.logger import SetupLogging


app_log = SetupLogging()

if __name__ == '__main__':
    app_log.log.info("Application Started")
    try:
        app.run(host=config.HOST, port=config.PORT)
    except Exception:
        app_log.log.error(f"Exception occured:\n{traceback.format_exc()}")
