import requests

# Hacer una solicitud GET a la API para obtener un chiste aleatorio
response = requests.get('https://api.chucknorris.io/jokes/random')

# Extraer el chiste de la respuesta en formato JSON
data = response.json()
joke = data['value']

# Mostrar el chiste
print(joke)
