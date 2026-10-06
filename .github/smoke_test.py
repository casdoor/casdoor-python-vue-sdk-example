# Checks that the backend starts and its APIs answer, without signing in.
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

client = app.test_client()

response = client.get('/api/get-account')
assert response.json['status'] == 'error', response.json

response = client.get('/toLogin')
assert b'/login/oauth/authorize?client_id=' in response.data, response.data

response = client.post('/api/signin?code=invalid&state=state')
assert response.json['status'] == 'error', response.json

print('ok')
