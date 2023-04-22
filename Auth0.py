# # auth0.py
# from functools import wraps
# from auth0.v3.authentication import GetToken
# from django.conf import settings
# from jose import jwt
# import requests
# import json


# def auth0_required(function):
#     @wraps(function)
#     def wrap(request, *args, **kwargs):
#         token = None
#         if 'Authorization' in request.headers:
#             token = request.headers['Authorization']
#             if token.startswith('Bearer '):
#                 token = token[7:]

#         if not token:
#             return json.dumps({'error': 'Authorization header missing'})

#         try:
#             jwt.decode(
#                 token,
#                 settings.AUTH0_CLIENT_SECRET,
#                 audience=settings.API_IDENTIFIER,
#                 algorithms=['HS256']
#             )
#         except jwt.ExpiredSignatureError:
#             return json.dumps({'error': 'Token expired'})
#         except jwt.InvalidTokenError:
#             return json.dumps({'error': 'Invalid token'})

#         return function(request, *args, **kwargs)

#     return wrap

