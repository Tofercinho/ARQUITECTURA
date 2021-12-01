from django.contrib import admin
from .models import newProduct, user, usercontact, informe, terrenocrud
# Register your models here.


class useredit(admin.ModelAdmin):
    list_display = ["name", "username", "email", "password"]
    list_editable = ["username"]
    search_fields = ["name"]

class userscontact(admin.ModelAdmin):
    list_display = ["name", "email", "msn", "obser"]
    search_fields = ["nom"]

class adminproducts(admin.ModelAdmin):
    list_display = ["name", "type", "gender", "size", "brand", "price", "img"]
    search_fields = ["brand"]

class adterrenocrud(admin.ModelAdmin):
    list_display = ["personal", "nomtec", "asunto", "nomempresa", "anteceden", "observacion", "observacion1"]
    search_fields = ["personal"]


admin.site.register(user, useredit)
admin.site.register(usercontact, userscontact)
admin.site.register(newProduct, adminproducts)
admin.site.register(terrenocrud,adterrenocrud)
