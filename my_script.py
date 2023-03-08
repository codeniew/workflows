import os

token = os.getenv('TOKEN')
print(f"The token is {token}")
if token=='abc':
  print('TOKEN正确')
