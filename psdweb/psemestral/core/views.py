from django.http.request import HttpRequest
from django.http.response import Http404
from django.shortcuts import render, redirect
from .models import user, usercontact, newProduct, informe, terrenocrud
from .forms import contactForm, registroUser, addProduct, CustomUserCreationForm, registroInforme, terrenocrudForm
from .util import render_pdf
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.generic import ListView, View
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

def addinforme(request): #agregar

    msnform = terrenocrudForm()
    data = {'cform' : msnform}
    
    if request.method == 'POST':
        msnform = contactForm(data = request.POST) 
        if msnform.is_valid():
            msnform.save()
        else:
            data["cform"] = msnform
        
        print("Mensaje enviado Correctamente")
        mensaje = "Mensaje enviado Correctamente"
        messages.success(request, mensaje)
    else:
        print("No se puedo enviar el mensaje, revisa los datos")
        #mensaje = "No se puedo enviar el mensaje, revisa los datos"
        #messages.error(request, mensaje)

    return render(request, 'web/creacionInformeTerreno.html', data)


class informeFinalpdfView(View):

    def link_callback(self, uri, rel):
        """
        Convert HTML URIs to absolute system paths so xhtml2pdf can access those
        resources
        """
        # use short variable names
        sUrl = settings.STATIC_URL  # Typically /static/
        sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL  # Typically /static/media/
        mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

        # convert URIs to absolute system paths
        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri  # handle absolute uri (ie: http://some.tld/foo.png)

        # make sure that file exists
        if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
        return path

    def get(self, request, *args, **kwargs):
        try:
            template = get_template('web/informeFinal.html')
            asis= newProduct.objects.all()
            visi= usercontact.objects.all()
            context= {
                'asistentes': newProduct.objects.all(),
                'visitas': usercontact.objects.all(),
                'numasistentes': asis.count(),
                'numvisitas': visi.count(),

                'icon': '{}{}'.format(settings.STATIC_URL, 'app/img/Iconos/LOGUITO.png'),
                'icono': '{}{}'.format(settings.STATIC_URL, 'app/img/pngw.png')
            }
            html= template.render(context)
            response = HttpResponse(content_type='application/pdf')
            pisaStatus=pisa.CreatePDF(
                html, dest=response, link_callback=self.link_callback)
            return response
        except:
            pass
        return HttpResponse('Hehe Algo fallo')


class ListacertificadoListView(ListView):
    model=addProduct
    template_name="web/certificado.html"
    contexto="form"

class certificadopdfView(View):
    def link_callback(self, uri, rel):
        """
        Convert HTML URIs to absolute system paths so xhtml2pdf can access those
        resources
        """
        # use short variable names
        sUrl = settings.STATIC_URL  # Typically /static/
        sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL  # Typically /static/media/
        mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

        # convert URIs to absolute system paths
        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri  # handle absolute uri (ie: http://some.tld/foo.png)

        # make sure that file exists
        if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
        return path

    def get(self, request, *args, **kwargs):
        try:
            template = get_template('web/certificadopdf.html')
            context= {
                'form': newProduct.objects.get(id=self.kwargs['idproduct']),
                'icon': '{}{}'.format(settings.STATIC_URL, 'app/img/Iconos/LOGUITO.png'),
                'icono': '{}{}'.format(settings.STATIC_URL, 'app/img/pngw.png')
            }
            html= template.render(context)
            response = HttpResponse(content_type='application/pdf')
            pisaStatus=pisa.CreatePDF(
                html, dest=response, link_callback=self.link_callback)
            return response
        except:
            pass
        return HttpResponse('Hehe Algo fallo')


# Create your views here.

def index(request):
    return render(request, 'web/index.html')

# funciones para el contacto
def contacto(request): #agregar

    msnform = contactForm()
    data = {'cform' : msnform}
    
    if request.method == 'POST':
        msnform = contactForm(data = request.POST) 
        if msnform.is_valid():
            msnform.save()
        else:
            data["cform"] = msnform;
        
        print("Mensaje enviado Correctamente")
        mensaje = "Mensaje enviado Correctamente"
        messages.success(request, mensaje)
    else:
        print("No se puedo enviar el mensaje, revisa los datos")
        #mensaje = "No se puedo enviar el mensaje, revisa los datos"
        #messages.error(request, mensaje)

    return render(request, 'web/contacto.html', data)


def contactcrud(request): #listar
    contacts = usercontact.objects.all()
    users = user.objects.all()
    products = newProduct.objects.all()
    numproducts = products.count()
    numusers = users.count()
    numcontacts = contacts.count()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(products, 10)
        products = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity' : contacts, 'nusers' : numusers, 'ncontacts' : numcontacts, 'nproducts' : numproducts,
        'paginator' : paginator
    }
    return render(request, 'web/contactcrud.html', data)

def lcontdel(request, iduserc): #eliminar
    contacts = usercontact.objects.get(id=iduserc)

    try:
        usercontact.delete(contacts)
        print("Eliminado Correctamente")
        mensaje = "Eliminado Correctamente"
        messages.success(request, mensaje)
        
    except:
        print("No se puedo eliminar, revisa los datos")
        mensaje = "No se puedo eliminar, revisa los datos"
        messages.error(request, mensaje)
        
    return redirect('contactcrud')

# End funciones para el coontacto

def modelo(request):
    return render(request, 'web/modelo.html')

def nosotros(request):
    return render(request, 'web/nosotros.html')

def paginator(request):
    return render(request, 'web/paginator.html')

# CRUD Producto

def stockproduct(request): #listar producto en stock
    products = newProduct.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(products, 8)
        products = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity' : products,
        'paginator' : paginator

    }
    return render(request, 'web/stockproduct.html', data)

def addproducto(request): #AGREGAR PRODUCTO
    product = addProduct()
    data = {'proForm' : product}
    if request.method == 'POST':
        product = addProduct(request.POST, files = request.FILES) 
        if product.is_valid():
            product.save()
            print("Asistente Creado Correctamente")
            mensaje = "Asistente Creado Correctamente"
            messages.success(request, mensaje)
            return redirect('index')
        else:
            data["proForm"] = product;  
    else:
        print("No se puedo crear el Asistente, revisa los datos")
        mensaje = "No se puedo crear el Asistente, revisa los datos"
        messages.error(request, mensaje)
    return render(request, 'web/addproducto.html', data)

def productcrud(request): #listar producto en crud
    users = user.objects.all()
    contacts = usercontact.objects.all()
    products = newProduct.objects.all()
    numusers = users.count()
    numcontacts = contacts.count()
    numproducts = products.count()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(products, 4)
        products = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity' : products, 'nusers' : numusers, 'ncontacts' : numcontacts, 'nproducts' : numproducts,
        'paginator' : paginator
    }
    return render(request, 'web/productcrud.html', data)

def editproduct(request, idproduct): #editar producto desde un administrador
    eproduct = newProduct.objects.get(id=idproduct)
    data = {
    'form': addProduct(instance=eproduct) 
    }
    if request.method == 'POST':
        formulario_edit = addProduct(data=request.POST, instance=eproduct, files = request.FILES)
        if formulario_edit.is_valid:
            formulario_edit.save()
            data['mensaje'] = "Asistente editado correctamente"
            return redirect('productcrud')
        else:
            data["form"] = formulario_edit(instance=eproduct.object.get(id=idproduct));  
    return render(request, 'web/editproduct.html', data)

def deleteproduct(request, idproduct): #eliminar usuario desde un adminw
    product = newProduct.objects.get(id=idproduct)

    try:
        newProduct.delete(product)
        print("Asistente Eliminado Correctamente")
        mensaje = "Asistente Eliminado Correctamente"
        messages.success(request, mensaje)
        
    except:
        print('No se puedo eliminar, revisa los datos')
        mensaje = "No se puedo eliminar, revisa los datos"
        messages.error(request, mensaje)
        
    return redirect('productcrud') 


def ropahombre(request):
    products = newProduct.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(products, 8)
        products = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity' : products,
        'paginator' : paginator
    }
    return render(request, 'web/ropahombre.html', data)

def ropamujer(request):
    products = newProduct.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(products, 8)
        products = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity' : products,
        'paginator': paginator

    }
    return render(request, 'web/ropamujer.html', data)

def ropanina(request):
    products = newProduct.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(products, 20)
        products = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity' : products,
        'paginator': paginator
    }
    return render(request, 'web/ropanina.html', data)

def ropanino(request):
    products = newProduct.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(products, 20)
        products = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity' : products,
        'paginator': paginator
    }
    return render(request, 'web/ropanino.html', data)

def menus(request):
    return render(request, 'web/menus.html')

#login and register by user
#stock
def registro(request): #registro user

    data = {
        'form' : CustomUserCreationForm()
    }
    formulario = CustomUserCreationForm(data=request.POST)
    if request.method == 'POST':
        if formulario.is_valid():
            formulario.save()
            reguser = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, reguser)
            print("te has registrado correctamente")
            return redirect('index')
        else:
            data['form'] = formulario
    else:
        print('error en el formulario')
        
    return render(request, 'registration/register.html', data)

def loginuser(request):
    return render(request, 'web/login.html')

# End login and register by user

#funciones para el crud

def edituser(request, iduser): #editar usuario desde un administrador
    euser = User.objects.get(id=iduser)
    data = {
    'form': CustomUserCreationForm(instance=euser) 
    }
    if request.method == 'POST':
        formulario_edit = CustomUserCreationForm(data=request.POST, instance=euser)
        if formulario_edit.is_valid:
            formulario_edit.save()
            data['mensaje'] = "usuario editado correctamente"
            return redirect('userscrud')
        else:
            data["form"] = formulario_edit;  
    return render(request, 'web/edituser.html', data)

def eliminar(request, iduser): #eliminar usuario desde un adminw
    users = User.objects.get(id=iduser)

    try:
        User.delete(users)
        print("Eliminado Correctamente")
        mensaje = "Eliminado Correctamente"
        messages.success(request, mensaje)
        
    except:
        print('No se puedo eliminar, revisa los datos')
        mensaje = "No se puedo eliminar, revisa los datos"
        messages.error(request, mensaje)
        
    return redirect('userscrud')


def userscrud(request): #listar
    users = User.objects.all()
    contacts = usercontact.objects.all()
    products = newProduct.objects.all()
    numproducts = products.count()
    numusers = users.count()
    numcontacts = contacts.count()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(products, 10)
        products = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity' : users, 'nusers' : numusers, 'ncontacts' : numcontacts, 'nproducts' : numproducts,
        'paginator': paginator
    }
    return render(request, 'web/userscrud.html', data)

# fin funciones para el crud


#status

    


    