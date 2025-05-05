from decouple import config
import os


DB_NAME=os.environ.get('DB_NAME', config('DB_NAME'))
DB_USR=os.environ.get('DB_USR', config('DB_USR'))
DB_PASS=os.environ.get('DB_PASS', config('DB_PASS'))
DB_PORT=os.environ.get('DB_PORT', config('DB_PORT'))
DB_HOST=os.environ.get('DB_HOST', config('DB_HOST', default='localhost'))
SECRET_KEY =os.environ.get('SECRET_KEY', config('SECRET_KEY'))
DEBUG=os.environ.get('DEBUG', config('DEBUG', default=True))