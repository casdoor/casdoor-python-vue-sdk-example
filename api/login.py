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

from casdoor import CasdoorSDK
from flask import jsonify, redirect, current_app, request, session, make_response, render_template
from flask_restful import Resource, reqparse

from .utils import authz_required


class SignIn(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('code', required=True, location='args')
        parser.add_argument('state', required=True, location='args')
        args = parser.parse_args()
        code = args['code']
        state = args['state']

        sdk: CasdoorSDK = current_app.config.get('CASDOOR_SDK')
        token = sdk.get_oauth_token(code)
        user = sdk.parse_jwt_token(token)
        session['casdoorUser'] = user

        return jsonify({'status': 'ok'})


class SignOut(Resource):

    @authz_required
    def post(self):
        del session['casdoorUser']
        return jsonify({
            'status': 'ok'
        })


class ToLogin(Resource):

    def get(self):
        sdk: CasdoorSDK = current_app.config.get('CASDOOR_SDK')
        redirect_url = sdk.get_auth_link(redirect_uri=current_app.config.get('REDIRECT_URI'), state='app-built-in')
        return make_response(render_template('tologin.html', redirect_url=redirect_url))
