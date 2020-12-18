from flask import Flask
from pathlib import Path

UPLOAD_FOLDER = Path("C:/Users/elton/Documents/durham docs/1002 - AI algorithms/project/uploads")

app = Flask(__name__)
app.secret_key = "secret123"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER