from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .forms import ResForm, MenuForm

from .models import Customer, Restaurants, Menu, Cart

# Create your views here.
def index(request):
    return render(request, 'delivery/index.html')

def sign_in(request):
    return render(request, 'delivery/sign_in.html')

def sign_up(request):
    return render(request, 'delivery/sign_up.html')

def handle_signin(request):
    li = Restaurants.objects.all()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            cus = Customer.objects.get(username = username, password = password)
            if(username == "admin"):
                return render(request, 'delivery/success.html')
            else:
                return render(request, 'delivery/cusdisplay_res.html', {'username':username, 'li':li})
        except:
            return render(request, 'delivery/failure.html')
   
    
def handle_signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')      
        try:
            cus = Customer.objects.get(username = username, password = password)
        except:
            cus = Customer(username = username, password = password, email = email, mobile = mobile, address = address)
            cus.save()
        return render(request, 'delivery/sign_in.html')
    else:
        return HttpResponse('Invalid Request')
    
def add_res(request):
    form = ResForm(request.POST or None)
    if form.is_valid():
        res_name = request.POST.get('Res_name')
        try:
            res = Restaurants.objects.get(Res_name = res_name)
        except:
            form.save()
            return redirect('delivery:display_res')
    return render(request, 'delivery/add_res.html', {'form':form}) 

def display_res(request):
    li = Restaurants.objects.all()
    return render(request, 'delivery/display_res.html', {'li':li})

def cusdisplay_res(request,username):
    customer = Customer.objects.get(username=username)
    li = Restaurants.objects.all()
    return render(request, 'delivery/cusdisplay_res.html', {'li':li, 'username':username})

def view_menu(request, id):
    res = Restaurants.objects.get(pk=id)
    menu = Menu.objects.filter(res=res)
    return render(request, 'delivery/view_menu.html', {'res':res, 'menu':menu})

def cusview_menu(request, id,username):
    res = Restaurants.objects.get(pk=id)
    menu = Menu.objects.filter(res=res)
    return render(request, 'delivery/cusview_menu.html', {'res':res, 'menu':menu, 'username':username})

def add_menu(request, id):
    restaurant = Restaurants.objects.get(pk=id)
    form = MenuForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            menu_item = form.save(commit=False)
            menu_item.res = restaurant
            menu_item.save()
            return redirect('delivery:view_menu', id)
    return render(request, 'delivery/menu_form.html', {'form': form, 'id': id})


def delete_menu(request, id):
    item = Menu.objects.get(pk=id)
    res_id=item.res.id
    item.delete()
    return redirect('delivery:view_menu', res_id)



def update_restaurant(request, id):
    restaurant = get_object_or_404(Restaurants, pk=id)
    form = ResForm(request.POST or None, instance=restaurant)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('delivery:display_res')
    return render(request, 'delivery/update_restaurant.html', {'form': form, 'restaurant': restaurant})

def delete_restaurant(request, id):
    restaurant = get_object_or_404(Restaurants, pk=id)
    restaurant.delete()
    return redirect('delivery:display_res')

def show_cart(request, username):
    customer = Customer.objects.get(username=username)
    cart = Cart.objects.filter(customer= customer).first()
    items = cart.items.all() if cart else []
    total_price = cart.total_price() if cart else 0
    return render(request, 'delivery/show_cart.html', {'items':items, 'total_price':total_price,'username':username})