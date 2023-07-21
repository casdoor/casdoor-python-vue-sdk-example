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

from functools import wraps

from flask import redirect, request, session, jsonify


def authz_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'casdoorUser' in session.keys():
            return f(*args, **kwargs)
        else:
            return jsonify({'status': 'error', 'msg': 'casdoorUser session key does not exist'})

    return wrapper
