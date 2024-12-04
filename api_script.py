import requests

url = "http://localhost:5000/libros"
response = requests.get(url)
if response.status_code == 200:
    print("Libros en la biblioteca:")
    print(response.json())
else:
    print("Error al obtener libros:", response.status_code)
