import os

from app import app
from config import DATABASE_NAME


if __name__ == '__main__':
    app.debug = True
    app.config['DATABASE_NAME'] = DATABASE_NAME
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)
