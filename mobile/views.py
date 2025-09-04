from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.shortcuts import loader
from .models import category,products,Cart
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login 
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
import random
from .models import Cart, Order, OrderItem
from django.contrib.auth.models import User 
# Create your views here.

def Welcom(request):
    return HttpResponse('اهلا بكم في دروس جانقو')

def LandPage(request):
    Category=category.objects.all()
    context={
       'data':Category
    }
    return render(request,'landPage.html',context)
  

def GetData(request):
   data={
      'name':'احمد',
      'age':25,
      'skills':['python','django','HTML'],
   }
   return JsonResponse(data)

def datasend(request,name):
   return HttpResponse(name)
def Add(request,d1,d2):
  return HttpResponse(d1+d2)

def runindex(request):
   template=loader.get_template('index.html')
   return HttpResponse(template.render())

def AbouUs(request):
   template=loader.get_template('aboutUs.html')
   return HttpResponse(template.render())

def invoice(request, order_id):
    order = Order.objects.get(id=order_id)
    order_items = order.items.all()
    grand_total = sum(item.quantity * item.price for item in order_items)

    return render(request, 'invoice.html', {
        'order': order,
        'order_items': order_items,
        'grand_total': grand_total,
    })

def blog(request):
   template=loader.get_template('blog.html')
   return HttpResponse(template.render())

def phonemenue(request):
   phon_id=request.GET.get("id")
   product=products.objects.filter(category_id=phon_id)
   context={
      'product':product
   }
   return render(request,"phoneMenue.html",context)

def details(request):
   phone_id=request.GET.get("id")
   product=products.objects.filter(id=phone_id)
   context={
      'product':product
   }
   return render(request,"detailes.html",context)

def addToCart(request):
   product=request.GET.get("id")
   if not product:
        # Fail gracefully
        return render(request, "detailes.html", {"error": "No product selected."})
   cart_item,created=Cart.objects.get_or_create(
      user=request.user,
      product_id=product ,
      defaults={'quantity':1}
   )     
   if not created:
    cart_item.quantity +=1
    cart_item.save()
    
   product=products.objects.filter(id=product)
   context={
       "product":product
   }
   return render(request,"detailes.html",context)

@login_required(login_url='authLogin')
def checkout(request):
    cart = Cart.objects.select_related('product').filter(user=request.user)
    grand_total = sum(item.product.price * item.quantity for item in cart)

    if request.method == "POST":
        order = Order.objects.create(user=request.user)
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        cart.delete()        
        order_items = OrderItem.objects.select_related('product').filter(order=order)

        return render(request, 'invoice.html', {
            'order': order,
            'order_items': order_items,
            'grand_total': sum(item.quantity * item.price for item in order_items),
        })

    return render(request, 'checkOut.html', {
        'cart': cart,
        'grand_total': grand_total,
    })

def authLogin(request):
 if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("checkout")  
        else:
    
            return render(request, "auth/auth_login.html", {
                "error": "اسم المستخدم أو كلمة السر غير صحيحة"
            })
 return render(request, "auth/auth_login.html")

def authRegister(request):
  if request.method == "POST":
    form=UserCreationForm(request.POST)
    if form.is_valid():
       form.save()
       return redirect('authLogin')
  else:
    form=UserCreationForm()
  
  return render(request,'auth/auth_register.html',{'form':form})

def authLogout(request):
   logout(request)
   return redirect('authLogin')    

def Account(request):
   user=request.user
   return render(request, 'Account.html',{'user':user})