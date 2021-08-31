from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from .form import *
from .models import *
from django.contrib.auth.decorators import login_required


def index(reguest):
    instance = product.objects.all()
    context = {
        'obj_list': instance
    }
    return render(reguest, "home.html",context)


def index2(reguest):
    return render(reguest, "index-2.html")


def blog_view(reguest):
    data=blog.objects.all()


    return render(reguest, "blog.html",{'data':data})


def blogdetails(reguest):
    return render(reguest, "blog_details.html")


def checkout(reguest):
    instance=order.objects.filter(createdby=reguest.user.username)
    amt=0
    datalist=[]
    data3=product.objects.all()
    i=1
    for data2 in instance:
        amt +=data2.total
        data_username = CustomUser.objects.all()

        if data_username:

            for data_username in data_username:

                print('1',data_username.username)
                print('2',data2.addedby)
                if data2.addedby==data_username.username:

                    print('iiiii',i)
                    i +=1
                    print('true data')
                    ad=data2.addedby
                    if data2.status!=True:
                        profile.objects.create(username=data2.addedby,
                                               productname=data2.name,
                                               quantity=data2.quantity,
                                               status='sold',
                                               price=data2.price,
                                               totalamount=data2.total)
                        data2.status = True
                        data2.save()

            '''
            for data3 in data3:
                print('data',data2.addedby)
                print('data3',data3.addedby)
                if data2.addedby==data3.addedby:
                    print('added',data3.addedby)
                    profile.objects.create(username=data3.addedby,
                                          productname=data3.name,
                                          quantity=data2.quantity,
                                          status='sold',
                                          price=data2.price,
                                          totalamount=data2.total)
        #user_data=CustomUser.objects.get(reguest.user.username)
        for instance1 in instance:
            amt +=instance1.total
        '''

    if reguest.method == 'POST':
        for instance1 in instance:
            instance1.delete()
        print("post")
        form =checkout_form(reguest.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.totalamount = amt
            form.addedby=ad
            form.save()



            return redirect('index')
    else:
        print("else")
        form =checkout_form()

    context ={
        'obj_list':instance,
        'form':form,
        'amount':amt
    }
    return render(reguest, "checkout.html",context)


def contact(reguest):
    return render(reguest, "contact.html")


def shopdetails(reguest):
    return render(reguest, "shop_details.html")


def shop(reguest):
    instance = product.objects.all()
    context = {
        'obj_list': instance
    }
    return render(reguest, "shop.html", context)


def shopingcart(reguest):
    return render(reguest, "shoping_cart.html")


def signup(reguest):
    if reguest.method == 'POST':
        print("post")
        form = CustomerUserCreationForm(reguest.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.save()
            return redirect('login')
    else:
        print("else")
        form = CustomerUserCreationForm()
    return render(reguest, "signup.html", {'form': form})



def shopgrid(reguest):
    return render(reguest, "shoping_grid.html")

def productview(reguest,id=None):
    instance=product.objects.get(id=id)
    context = {
        'obj_list': instance
    }
    return render(reguest, "shop_details.html", context)

def cartview(reguest,id=None):
    instance=product.objects.get(id=id)

    instance=cart.objects.create(image=instance.image,name=instance.name,price=instance.price,createdby=reguest.user.username,total=instance.price,quantity=1,addedby=instance.addedby)
    return redirect('cartdata')
def cartdata(request):
    instance=cart.objects.filter(createdby=request.user.username)
    amt=0
    for instance1 in instance:
        amt +=instance1.total

    context={
        'obj_list':instance,
        'total_amount':amt
    }
    return render(request,"shoping_cart.html",context)
def add(request,id=None):

    instance=cart.objects.get(id=id)
    price1=instance.price
    print(price1)
    q=instance.quantity
    if q:
        pass
    else:
        q=0
    print(q)
    total=instance.total
    q +=1
    print(q)
    total +=price1

    instance.total=total
    instance.quantity=q
    instance.save()
    return  redirect('cartdata')

def sub(reguest,id=None):
    instance = cart.objects.get(id=id)
    price1 = instance.price
    print(price1)
    q = instance.quantity
    if q:
        pass
    else:
        q = 0
    print(q)
    total = instance.total
    q -= 1
    print(q)
    total -= price1

    instance.total = total
    instance.quantity = q
    instance.save()
    return redirect('cartdata')
def cancel(request,id=None):
    instance= cart.objects.get(id=id)
    instance.delete()
    return  redirect('cartdata')

def order_product(request):
    instance=cart.objects.filter(createdby=request.user.username)
    for instance in instance:
        print('add',instance.addedby)
        order.objects.create(name=instance.name,image=instance.image,price=instance.price,quantity=instance.quantity,total=instance.total,createdby=instance.createdby,addedby=instance.addedby)
        instance.delete()
    return redirect('checkout')
@login_required
def product_reg(reguest):
    if reguest.method=='POST':
        print('post')
        form=product_regform(reguest.POST,reguest.FILES)
        if form.is_valid():
            form=form.save(commit=False)
            form.addedby=reguest.user.username
            form.save()
            return redirect('index')
        else:
            form=product_regform()
    return render(reguest,'registration.html')

@login_required
def profile1(reguest):
    instance = profile.objects.filter(username=reguest.user.username)
    amt=0
    for instance1 in instance:
        amt +=instance1.price
    #instance=profile.objects.create(username=reguest.user.username,productname=)
    context={
        'instance':instance,
        'amount':amt
    }
    return render(reguest, 'profile.html',context)

def search(request):
    name=request.GET['srch']
    #data=product.objects.get(name=name)
    #data=get_object_or_404(product,name=name)
    data=product.objects.filter(name=name)

    print('name',name)
    context={
        'obj_list':data,
    }
    return render(request,'shop_details1.html',context)


def search1(request,data=None):
    #data=product.objects.get(name=name)
    #data=get_object_or_404(product,name=name)
    data=product.objects.filter(name=data)

    print('name',data)
    context={
        'obj_list':data,
    }
    return render(request,'shop_details1.html',context)