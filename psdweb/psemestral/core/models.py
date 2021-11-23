from django.db import models


# Create your models here.

class user(models.Model):
    # verbose_name='nombre'
    name = models.CharField( max_length=50)
    username = models.CharField( max_length=50)
    email = models.EmailField(('email address'), unique=True)
    password = models.CharField( max_length=50)

    def __str__(self):
        return self.nom

class usercontact(models.Model):

    name = models.CharField( max_length=50)
    email = models.CharField( max_length=50)
    msn = models.CharField( max_length=300)
    obser = models.CharField( max_length=300)

    def __str__(self):
        return self.name


#productos

typeProduct = [
    [0, 'poleras'],
    [1, 'pantalones'],
    [2, 'camisas'],
    [3, 'polerones'],
    [4, 'vestidos'],
    [5, 'zapatillas']
]
genders = [
    [0, 'Masculino'],
    [1, 'Femenino'],
]
brands = [
    [0, 'nike'],
    [1, 'adidas'],
    [2, 'rebook'],
    [3, 'levis'],
    [4, 'lacoste'],
    [5, 'supreme'],
    [6, 'gucci']
]

class newProduct(models.Model):  

    gender = models.IntegerField(choices = genders)
    name = models.CharField( max_length=50)
    size = models.CharField( max_length=5)
    type = models.IntegerField(choices = typeProduct)
    brand = models.IntegerField(choices = brands)
    price = models.IntegerField()
    img = models.ImageField(upload_to='productos', null=True, blank=True)

    def __str__(self):
        return self.name
        