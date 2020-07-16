
import os

FLASK_LOG_TYPE = os.getenv('FLASK_LOG_TYPE', 'stream')
FLASK_LOG_LEVEL = os.getenv('FLASK_LOG_LEVEL', 'INFO')
FLASK_LOG_DIR = os.getenv('FLASK_LOG_DIR', '')