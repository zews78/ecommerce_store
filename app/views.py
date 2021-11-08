from django import views
from django.http.response import JsonResponse
from django.views.generic.edit import CreateView
from django.shortcuts import redirect, render
from django.views import View
from .models import Category_Choices, Product,Customer,Cart,OrderPlaced, Reviews
from .forms import CustomerRegistration,CustomerProfile,ReviewForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ProductView(View):
    def get(self,request):
        totalitem=0
        PlayStation=Product.objects.filter(category='PS')
        Xbox=Product.objects.filter(category='XB')
        Nintendo=Product.objects.filter(category='NI')
        PC=Product.objects.filter(category='PC')
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
        return render(request,'app/home.html',{'PlayStation':PlayStation,'Xbox':Xbox,'Nintendo':Nintendo,'PC':PC,'totalitem':totalitem})

#def home(request):
 #return render(request, 'app/home.html')
class ProductDetail(View):
    def get(self, request, pk):
        totalitem=0
        product=Product.objects.get(pk=pk)
        itemincart=False
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
            itemincart=Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
        return render(request, 'app/productdetail.html',{'product':product,'itemincart':itemincart,'totalitem':totalitem})

def product_detail(request):
 return render(request, 'app/productdetail.html')

@login_required
def add_to_cart(request):
    user=request.user
    productid=request.GET.get('prod_id')
    product=Product.objects.get(id=productid)
    Cart(user=user,product=product).save()
    return redirect('/cart')

@login_required
def show_cart(request):
    totalitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
        user=request.user
        cart=Cart.objects.filter(user=user)
        #print(cart)
        amount=0.0
        shippingamount=100.0
        totalamount=0.0
        cartproduct=[p for p in Cart.objects.all() if p.user==user]
        #print(cartproduct)
        if cartproduct:
            for p in cartproduct:
                tempamount=(p.quantity*p.product.selling_price)
                amount+=tempamount
                totalamount=amount+shippingamount
            return render(request, 'app/addtocart.html',{'cart':cart,'totalamount':totalamount,'amount':amount,'totalitem':totalitem})
        else:
            return render(request,'app/emptycart.html',{'totalitem':totalitem})

def pluscart(request):
    if request.method=='GET':
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount=0.0
        shippingamount=100.0
        cartproduct=[p for p in Cart.objects.all() if p.user==request.user]
        for p in cartproduct:
            tempamount=(p.quantity*p.product.selling_price)
            amount+=tempamount

        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':amount+shippingamount
            }
        return JsonResponse(data)

def minuscart(request):
    if request.method=='GET':
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        amount=0.0
        shippingamount=100.0
        cartproduct=[p for p in Cart.objects.all() if p.user==request.user]
        for p in cartproduct:
            tempamount=(p.quantity*p.product.selling_price)
            amount+=tempamount

        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':amount+shippingamount
            }
        return JsonResponse(data)


def removecart(request):
    if request.method=='GET':
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount=0.0
        shippingamount=100.0
        cartproduct=[p for p in Cart.objects.all() if p.user==request.user]
        for p in cartproduct:
            tempamount=(p.quantity*p.product.selling_price)
            amount+=tempamount

        data={
            'amount':amount,
            'totalamount':amount+shippingamount
            }
        return JsonResponse(data)
         
        

@login_required
def buy_now(request):
    user=request.user
    productid=request.GET.get('prod_id')
    product=Product.objects.get(id=productid)
    Cart(user=user,product=product).save()
    return redirect('/checkout')

@login_required
def address(request):
    totalitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    address=Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html',{'address':address,'active':'btn-danger','totalitem':totalitem})


@login_required
def orders(request):
    totalitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    orderplaced=OrderPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html',{'orderplaced':orderplaced,'totalitem':totalitem})

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

@login_required
def checkout(request):
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    user=request.user
    address=Customer.objects.filter(user=user)
    cartitem=Cart.objects.filter(user=user)
    amount=0.0
    shippingamount=100.0
    totalamount=0.0
    cartproduct=[p for p in Cart.objects.all() if p.user==request.user]
    if cartproduct:
        for p in cartproduct:
            tempamount=(p.quantity*p.product.selling_price)
            amount+=tempamount
    totalamount=amount+shippingamount
    return render(request, 'app/checkout.html',{'address':address,'totalamount':totalamount,'cartitem':cartitem,'totalitem':totalitem})

@login_required
def paymentdone(request):
    user=request.user
    custid=request.GET.get('custid')
    if not custid:
        messages.success(request,'Please Select an Address.')
        return redirect("checkout")
    customer=Customer.objects.get(id=custid)
    
    cart=Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user,customer=customer, product=c.product, quantity=c.quantity).save()
        c.delete()
    return redirect("orders")


def playstation(request,data=None):
    totalitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    if data==None:
        games=Product.objects.filter(category='PS')
    elif data=='below':
        games=Product.objects.filter(category='PS').filter(selling_price__lt=1000)
    elif data=='above':
        games=Product.objects.filter(category='PS').filter(selling_price__gt=1000)
    return render(request, 'app/playstation.html',{'games':games,'totalitem':totalitem})

def xbox(request,data=None):
    totalitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    if data==None:
        games=Product.objects.filter(category='XB')
    elif data=='below':
        games=Product.objects.filter(category='XB').filter(selling_price__lt=1500)
    elif data=='above':
        games=Product.objects.filter(category='XB').filter(selling_price__gt=1500)
    return render(request, 'app/xbox.html',{'games':games,'totalitem':totalitem})

def nintendo(request,data=None):
    totalitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    if data==None:
        games=Product.objects.filter(category='NI')
    elif data=='below':
        games=Product.objects.filter(category='NI').filter(selling_price__lt=4000)
    elif data=='above':
        games=Product.objects.filter(category='NI').filter(selling_price__gt=4000)
    return render(request, 'app/nintendo.html',{'games':games,'totalitem':totalitem})

def pc(request,data=None):
    totalitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    if data==None:
        games=Product.objects.filter(category='PC')
    elif data=='below':
        games=Product.objects.filter(category='PC').filter(selling_price__lt=600)
    elif data=='above':
        games=Product.objects.filter(category='PC').filter(selling_price__gt=600)
    return render(request, 'app/pc.html',{'games':games,'totalitem':totalitem})

def about(request):
    totalitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
    return render(request, 'app/about.html',{'totalitem':totalitem})

class CustomerRegistrationView(View):
    def get(self, request):
        form=CustomerRegistration()
        return render(request, 'app/signup.html',{'form':form})
    def post(self,request):
        form=CustomerRegistration(request.POST)
        if form.is_valid():
            messages.success(request,'Registration successful. Please head to the login page.')
            form.save()
        return render(request, 'app/signup.html',{'form':form})

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self,request):
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
        form=CustomerProfile()
        return render(request, 'app/profile.html',{'form':form,'active':'btn-danger','totalitem':totalitem})
    
    def post(self,request):
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
        form=CustomerProfile(request.POST)
        if form.is_valid():
            usr=request.user
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            state=form.cleaned_data['state']
            zipcode=form.cleaned_data['zipcode']
            reg=Customer(user=usr,name=name,locality=locality,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request, 'Profile updated succesfully')
        return render(request,'app/profile.html',{'form':form,'active':'btn-danger','totalitem':totalitem})


def search(request):
    if request.method=="POST":
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
        searched=request.POST['searched']   
        names=Product.objects.filter(name__contains=searched)
        return render(request,'app/search.html',{'searched':searched,'names':names,'totalitem':totalitem})
    else:
        totalitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
        return render(request,'app/search.html',{'totalitem':totalitem})
    
@method_decorator(login_required, name='dispatch')
class AddReviewView(CreateView):
    model=Reviews
    form_class=ReviewForm
    template_name='app/addreview.html'
    def form_valid(self, form):
        form.instance.product_id=self.kwargs['pk']
        return super().form_valid(form)
    def get_success_url(self):
<<<<<<< HEAD
        return reverse_lazy('productdetail', kwargs={'pk': self.kwargs['pk']})
=======
        return reverse_lazy('productdetail', kwargs={'pk': self.kwargs['pk']})

>>>>>>> 188199b0c779bce844f35f319a00cb288a8c15eb
