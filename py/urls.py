#las URLS para importar algun que otro objeto
from django.urls import path
from .views import productos, producto
from .viewsLogin import login
from . import views

urlpatterns = [
  path('Proyecto-semestral-desarollo-web/productos.html/', views.productos.html),
  path('royecto-semestral-desarollo-web/nosotros.html/', views.nosotros.html),
  path('royecto-semestral-desarollo-web/ropa-hombre.html/', views.ropahombre.html),
  path('royecto-semestral-desarollo-web/ropa-mujer.html/', views.ropamujer.html),
  path('royecto-semestral-desarollo-web/ropa-nina.html/', views.ropanina.html),
  path('royecto-semestral-desarollo-web/ropa-nino.html/', views.ropanino.html),
  path('producto/', productos, name="productos"),
  path('productos/<pk>', producto, name="producto"),
  path('login/', login, name='login')
]
