import requests
class API:

    def __init__(self, url):
        self.url = url

    def mostrar_productos():

            url = "http://localhost:4000/products"
            response = requests.get(url)
            print(response)
            print(response.text)
            print(response.status_code)


    def mostrar_producto(name):
        url = f"http://localhost:4000/products/{name}"
        response = requests.get(url)
        response = response.json()     
        try:
            print(response)
        except:
            print('Error al intentar mostrar los datos')


    def crear_producto(name,price,quantity):
        headers = {'Content-Type': 'application/json'}
        url = "http://localhost:4000/products"
        data = "{\"name\":\"keyboard\",\"price\": 2000,\"quantity\": 5}"
        #data = f'{"name": "{name}","price": {price},"quantity": {quantity}}'
        response = requests.post(url, data=data, headers= headers)
        print(response.text)

    def actualizar_producto(name):
        headers = {'Content-Type': 'application/json'}
        url= f"http://localhost:4000/products/{name}" 
        data = "{\"name\":\"monitor\",\"price\": 3000,\"quantity\": 3}"   
        try:
            response = requests.put(url, data=data, headers=headers)
            response = response.json()
            print(response)
            # response.status_code == 200
            print('Datos actualizados correctamente')
        except:
            print('Error al actualizar los datos')

    def eliminar_producto(name):

        url= f"http://localhost:4000/products/{name}" 
        response = requests.delete(url)

        try:
            response.status_code == 204
            print('Datos eliminados correctamente')
        except:
            print('Error al eliminar los datos')


url = "http://localhost:4000/products"
#probando = API(url)
#probando.mostrar_productos()
API.mostrar_productos()
#API.crear_producto()
#API.actualizar_producto(input("Ingrese el nombre del producto que desea actualizar\n"))
#API.mostrar_productos()
#API.mostrar_producto(input("Ingrese el nombre del producto que desea ver\n"))
#API.eliminar_producto(input("Ingrese el nombre del producto que desea eliminar\n"))

