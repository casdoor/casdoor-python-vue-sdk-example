# Copyright 2022 The Casdoor Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask import Flask, send_from_directory
from flask_cors import CORS
from api import api_blueprint
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(api_blueprint)
CORS(app, supports_credentials=True)


@app.route('/')
def index():
    return send_from_directory('../web/dist', 'index.html')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_static(path):
    if not path.startswith('api'):
        dist_dir = os.path.abspath(os.path.join(os.getcwd(), '../web/dist'))
        if os.path.exists(os.path.join(dist_dir, path)):
            return send_from_directory(dist_dir, path)
        else:
            return send_from_directory(dist_dir, 'index.html')
    else:
        return api_blueprint


if __name__ == '__main__':
    app.run(debug=True)
