from django.shortcuts import render
from django.views import View
from .models import Customer, Product, cart, OrderPlaced
from .forms import CustomerRegistrationForm
from django.contrib import messages
from django.contrib.auth.views import LogoutView
# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
 def get(self, request):
  topwears = Product.objects.filter(category = 'TW')
  bottomwears = Product.objects.filter(category = 'BW')
  mobiles = Product.objects.filter(category = 'M')
  return render(request, 'app/home.html', {'topwears':topwears, 'bottomwears':bottomwears, 'mobiles':mobiles})

# def product_detail(request):
#  return render(request, 'app/productdetail.html')

class ProductDetailView(View):
 def get(self, request, pk):
  product = Product.objects.get(pk=pk)
  return render(request, 'app/productdetail.html', {'product' :product})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

# def change_password(request):
#  return render(request, 'app/changepassword.html')

def mobile(request, data=None):
 if data == None:
  mobiles = Product.objects.filter(category = 'M')
 elif data == 'Redmi' or data == 'Samsung':
  mobiles = Product.objects.filter(category = 'M').filter(brand=data)

#  elif data == 'below':
#   mobiles = Product.objects.filter(category = 'M').filter(discounted_price_lt=1000)

#  elif data == 'above':
#    mobiles = Product.objects.filter(category = 'M').filter(discounted_price_gt=1000)

 elif data == 'below':
  mobiles = Product.objects.filter(category='M').filter(discounted_price__lt=1000)

 elif data == 'above':
  mobiles = Product.objects.filter(category='M').filter(discounted_price__gt=1000)


 
 return render(request, 'app/mobile.html',{'mobiles': mobiles})

# def login(request):
#  return render(request, 'app/login.html')

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')

class CustomerRegistrationView(View):
 def get(self, request):
  form = CustomerRegistrationForm()
  return render(request, 'app/customerregistration.html',{'form':form})
 
 def post(self, request):
  form =CustomerRegistrationForm(request.POST)
  if form.is_valid():
   messages.success(request, 'Congratulations!! Registered Sucessfully')
   form.save()
 
  return render(request, 'app/customerregistration.html',{'form':form})
class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
 


 

def checkout(request):
 return render(request, 'app/checkout.html')
