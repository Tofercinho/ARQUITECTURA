#Serializers
from rest_framework import serializers
from core.models import productos

class productosSerializer(serializers.ModelSerializer):
    class Meta:
        model = productos
        fields = ['Ropa', 'Talla', 'Modelo', 'Categoria']
        email = serializers.EmailField()
        content = serializers.CharField(max_length=200)
        created = serializers.DateTimeField()

    def create(self, validated_data):
        return productos(**validated_data)

    def update(self, instance, validated_data):
        instance.model = validated_data.get('model', instance.model)
        instance.fields = validated_data.get('fields', instance.fields)
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        return instance

def new_func():
    productos = serializer.save()

    serializer = ProductosSerializer(data=data)

new_func()
