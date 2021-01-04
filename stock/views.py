from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Tag,Category,Product, Customer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def getStatus(request):
    if request.session.get('username') is not None:
        usr = User.objects.get(username=request.session.get('username'))
        try:
            customer = Customer.objects.get(user=usr)
            print(customer)
            return True
        except:
            return False

def getName(request):
    if request.session.get('username') is not None:
        usr = User.objects.get(username=request.session.get('username'))
        try:
            customer = Customer.objects.get(user=usr)
            print(customer)
            return customer
        except:
            return False


def dashboard(request):
    print(request.session.get('username'))
    if request.session.get('username') is not None:
        return render(request, 'stock/dashboard.html')
    else:
        return render(request, 'stock/register.html')

def loggin(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            print(user)
            login(request, user)
            request.session['username'] = username
            return redirect(to='stock')
            # return render(request,'stock/login.html', {'success': 'success'})
        else:
            # messages.info(request, 'Username or Password is incorrect')
            return render(request,'stock/login.html', {'error': 'Username or Password is incorrect'})
    return render(request, 'stock/login.html')

def logoutPage(request):
    request.session['username'] = None
    logout(request)
    return redirect(to='stock')

def userprofile(request):
    return render (request,'stock/userprofile.html')

def alluserprofile(request):
    alluser=User.objects.all()
    return render (request,'stock/alluserprofile.html',{'user':alluser})

def register(request):
    if request.method =='POST':
        if request.POST['password1'] == request.POST['password2']:
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            try:
                user = User.objects.get(username=username)
                return render(request, 'stock/register.html', {'error': 'Username has already existed'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=username, password=password1, email=email)
                Customer.objects.create(user=user, name=username, email=email)
                login(request, user)

                # return redirect(to='register')
                return render(request, 'stock/login.html', {'success': 'success'})
        else:
            return render(request, 'stock/register.html', {'error': 'Password does not match'})

    return render(request,'stock/register.html')


def categoryAdd(request):
    category_model=Category
    if getStatus(request):
        if request.method =='POST':
            category_name=request.POST['category_name']
            category_save=category_model.objects.create(category_name=category_name, customer=getName(request))
            category_save.save()
            return redirect(to='category')
        return render(request,'stock/category.html')
    else:
        return redirect(to='stock')

def categoryView(request):
    if request.session.get('username') is not None:
        category_model = Category
        # category_view=category_model.objects.all()
        usr = User.objects.get(username=request.session.get('username'))
        try:
            customer = Customer.objects.get(user=usr)
        except:
            return redirect(to='stock')
        category_view=category_model.objects.filter(customer=customer)
        return render(request, 'stock/category_view.html', {'category_views': category_view})
    return redirect(to='stock')

def categoryEdit(request,id):
    if request.session.get('username') is not None:

        usr = User.objects.get(username=request.session.get('username'))
        try:
            customer = Customer.objects.get(user=usr)
        except:
            return redirect(to='stock')

        category_model=Category.objects.get(id=id)
        return render(request,'stock/category_edit.html',{'edit':category_model})
    else:
        return redirect(to='stock')


def categoryUpdate(request,id):
    category_model = Category.objects.get(id=id)
    if request.method =='POST':
        category_model.category_name=request.POST['categoryname']
        category_model.save()
        return redirect(to='view')
        # category_update=
    return render(request,'stock/category_edit.html',{'update':category_model})


def categoryDelete(request,id):
    category_model=Category.objects.get(id=id)
    category_model.delete()
    return redirect(to='view')



def tagAdd(request):
    if getStatus(request):
        if request.method =='POST':
            tag_name=request.POST['tag_name']
            tag_save=Tag.objects.create(tag_name=tag_name, customer=getName(request))
            tag_save.save()
            return redirect(to='tag')
        return render(request,'stock/tag.html')
    else:
        return redirect(to='stock')

def tagView(request):
    if getStatus(request):
        # tag_view=Tag.objects.all()
        tag_view=Tag.objects.filter(customer=getName(request))
        print(tag_view)
        return render(request, 'stock/tag_view.html', {'tag_views': tag_view})
    return redirect(to='stock')

def tagEdit(request,id):
    category_model=Tag.objects.get(id=id)
    return render(request,'stock/tag_edit.html',{'edit':category_model})


def tagUpdate(request,id):
    tag_model = Tag.objects.get(id=id)
    if request.method =='POST':
        tag_model.tag_name=request.POST['tagname']
        tag_model.save()
        return redirect(to='tagview')
        # category_update=
    return render(request,'stock/tag_edit.html',{'update':tag_model})


def tagDelete(request,id):
    tag_model=Tag.objects.get(id=id)
    tag_model.delete()
    return redirect(to='tagview')



def productAdd(request):
    # product_model=Product
    if getStatus(request):
        category_model = Category.objects.all()
        # tags_model = Tag.objects.all()
        tags_model = Tag.objects.filter(customer=getName(request))
        if request.method =='POST' and request.FILES['product_image']:

            category_id=request.POST['category']
            category_name=Category.objects.get(id=category_id)
            print(category_name)

            product_name=request.POST['product_name']
            print(product_name)

            product_image=request.FILES['product_image']
            print(product_image)

            tag_names=[x.tag_name for x in Tag.objects.all()]
            tag_ids=[]
            for y in tag_names:
                tag_ids.append(request.POST.get(y))
                print(tag_ids)
            # tag_ids=request.POST['tag_name']
            description=request.POST['description']
            print(description)


            # tag_id=request.POST['tags']
            # tags=Tag.objects.filter(id=tag_id)
            # print(tags)

            product_save=Product.objects.create(category_name=category_name,
                                                 product_name=product_name,
                                                 product_image=product_image,
                                                 customer=getName(request),
                                                 description=description
                                                       )


            # product_save.save()
            for j in [i for i in tag_ids if i]:
                product_save.tags.add(int(j))


            return redirect(to='product')
        return render(request,'stock/product.html',{'category_model':category_model,'tags_model':tags_model})
    else:
        return redirect(to='stock')

def productView(request):
    if getStatus(request):
        # product_view=Product.objects.all()
        product_view=Product.objects.filter(customer=getName(request))
        print(product_view)
        return render(request, 'stock/product_view.html', {'product_views': product_view})
    else:
        return redirect(to='stock')


def productEdit(request,id):
    tags_model = Tag.objects.filter(customer=getName(request))
    product_model=Product.objects.get(id=id)
    category_model = Category.objects.filter(customer=getName(request))
    return render(request,'stock/product_edit.html',{'edit':product_model, 'tags_model':tags_model, 'category_model':category_model})


def productUpdate(request,id):
    product_model = Product.objects.get(id=id)

    category_model = Category.objects.all()
    tags_model = Tag.objects.all()
    if request.method == 'POST':
        category_id = request.POST['category']
        category_name = Category.objects.get(id=category_id)

        product_name = request.POST['product_name']
        # print(request.FILES)
        print(request.FILES['product_image'])

        tag_names = [x.tag_name for x in Tag.objects.all()]
        tag_ids = []
        for y in tag_names:
            tag_ids.append(request.POST.get(y))
            print(tag_ids)

        description = request.POST['description']
        product_update = Product.objects.filter(id=id).update(category_name=category_name, product_name=product_name,
                                                               product_image=request.FILES['product_image'], description=description)
        print(tag_ids)
        product_update_tag = Product.objects.get(id=id)
        for j in [i for i in tag_ids if i]:
            product_update_tag.tags.add(int(j))
        return redirect(to='productview')
    # return render(request, 'stock/product.html', {'category_model': category_model, 'tags_model': tags_model})
    return render(request,'stock/product_edit.html',{'edit':product_model, 'tags_model':tags_model, 'category_model':category_model})


def productDelete(request,id):
    product_model=Product.objects.get(id=id)
    product_model.delete()
    return redirect(to='productview')