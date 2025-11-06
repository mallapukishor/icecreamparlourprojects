from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from icreamapp import models

# Create your views here.
def home(request):
    print(request.COOKIES)
    d = {
        'page':'Home Page',
        'title':'HOME'
    }
    return render(request, 'home.html', d)

def about(request):
    d = {
        'page':'About Page',
        'title':'ABOUT'
    }
    return render(request, 'about.html', d)

def contact(request):
    d = {
        'page':'Contact Page',
        'title':'CONTACT'
    }
    return render(request, 'contact.html', d)

@login_required(login_url='login')
def menu(request):
    objs = models.menu.objects.all()
    d = {
        'page':'Menu Page',
        'title':'MENU',
        'records':objs
    }
    return render(request, 'menu.html', d)

@login_required(login_url='login')
def insert(request):
    return render(request, 'insert.html')

@login_required(login_url='login')
def save(request):    
    # 1. create object 
    obj = models.menu()
    # 2. insert data to object
    if request.method == 'POST':
        obj.name = request.POST['name']
        obj.brand = request.POST['brand']
        obj.price = request.POST['price']
        # 3. save data as a record
        obj.save()
        # return HttpResponse('Record Inserted Successfully')
        return redirect(menu)
    else:
        return HttpResponse('Record Insertion Failed')

@login_required(login_url='login')
def edit(request,id):
    obj = models.menu.objects.get(id=id)
    d = {'record':obj}
    return render(request, 'update.html', d)

@login_required(login_url='login')
def update(request):
    
    if request.method == "GET":
        # 1. get record object based on id
        obj = models.menu.objects.get(id= request.GET['id'])
        # 2. modify record data
        obj.name = request.GET['name']
        obj.brand = request.GET['brand']
        obj.price = request.GET['price']
        # 3. update record
        obj.save()
    #return HttpResponse('Record Updated Successfully')
    return redirect(menu)

@login_required(login_url='login')
def delete(request, id):
    # 1. get record object based on id
    obj = models.menu.objects.get(id=id)
    # 2. delete record from menu table
    obj.delete()
    #return HttpResponse('Record Deleted Successfully')
    return redirect(menu)

@login_required(login_url='login')
def read(request):
    # 1. get all the records from menu table
    objs = models.menu.objects.all()
    for obj in objs:
        print(f'name:{obj.name}, brand:{obj.brand}, price:{obj.price}')
    return HttpResponse('Records extracted successfully')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username = username, password = password)
        if user != None:
            login(request, user)
            return redirect(home)
    return render(request,'login.html')

@login_required(login_url='login')
def signout(request):
    logout(request)
    return redirect(home)