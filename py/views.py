#Api de los objetos
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def productos(request, pk):
      try:
            productos = productos.objects.get(ropa.pk)
      except:
            return response(status=status.HTTP_404_NOT_FOUND)

      if request.method == 'GET':
            {
                  "id": "<ID_PRODUCTO>", 
                  "summary": "<tipo de producto>",
                  "description" : "<Cualquier tipo de producto>"
            }

      elif request.method == 'POST':
            serializer = ProductosSerializer(productos)
            return Response(serializer.data)

      elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = ProductosSerializer(Productos, data=data)
            if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data)
            else:
                  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      elif request.method == 'DELETE':
            productos.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
      else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)           

#Importaciones
import requests

resp = requests.get('productos.html')
if resp.status_code != 200:
      raise ApiError('GET{}').format(resp.status_code))
for todo_item in resp.json():
      print('{} {}'.format(todo_item['id'], todo_item['summary']))      

#Decoradores
@permission_classes((IsAuthenticated,))
