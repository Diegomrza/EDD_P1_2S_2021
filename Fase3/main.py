from datetime import time
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import time, asyncio

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origin":"*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
    while True:
        time.sleep(3.0)
        print('3 seconds')



if __name__ == '__main__':
    app.run(threaded = True,port = 3000, debug = True)
    
