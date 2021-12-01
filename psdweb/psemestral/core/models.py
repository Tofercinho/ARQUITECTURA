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

class terrenocrud(models.Model):
    
    personal = models.CharField( max_length=50)
    nomtec = models.CharField( max_length=50)
    asunto = models.CharField( max_length=255)
    nomempresa = models.CharField( max_length=255)
    anteceden = models.CharField( max_length=255)
    observacion = models.CharField( max_length=255)
    observacion1 = models.CharField( max_length=255)

    def __str__(self):
        return self.personal



#productos

typeProduct = [
    [0, 'Seguridad'],
    [1, 'Covid'],
    [2, 'Auto cuidado'],
    [3, 'Manejo de emociones'],
    [4, 'Psicologia de emergencia'],
    [5, 'Prevención y Manejo de Conflictos']
]
genders = [
    [0, 'Masculino'],
    [1, 'Femenino'],
    [2, 'No definido']
]
brands = [
    [0, 'SI'],
    [1, 'NO']
    
]

class newProduct(models.Model):  

    gender = models.IntegerField(choices = genders)
    name = models.CharField( max_length=50)
    size = models.CharField( max_length=256)
    type = models.IntegerField(choices = typeProduct)
    brand = models.IntegerField(choices = brands)
    price = models.IntegerField()
    img = models.ImageField(upload_to='productos', null=True, blank=True)

    def __str__(self):
        return self.name

class informe(models.Model):

    name: models.CharField(max_length=50)
    rut: models.IntegerField()   
    descripcion: models.TextField()
    empresa: models.CharField(max_length=60)
    def __str__(self):
        return self.name

