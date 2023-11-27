from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpResponse
from.models import Orders 
from .forms import OnlineStatusForm


# Create your views here.

# here we create a function home which will be called when a user searches the home page
# it takes a request the gives a response(must be in response format) eg return HttpResponse("Hello world")
# to use response you need to import it

def firstPage(request):
    return render(request,'firstPage.html')

def home(request):
    return render(request,'home.html');

def sender(request):
    return render(request,'sender.html');

def transporter(request):
    # getting Orders
    if request.method == 'POST':
        goods_value = request.POST.get('goods_value')
        deliver_before = request.POST.get('delivery_before', None)
        distance_to = request.POST.get('distance_to')
        transport_fee = request.POST.get('transport_fee')
        service_fee = request.POST.get('service_fee')
        
        Orders.objects.create(goods_value=goods_value,deliver_before=deliver_before,distance_to=distance_to,transport_fee=transport_fee,service_fee=service_fee)
        return redirect('/')

    return render(request, 'transporter.html')

def orders(request):
    # we create our objects here, pass objects.
    orders= Orders.objects.all()
    return render(request,"orders.html", {'orders':orders})

def workerPage(request):
    return render(request,'workerPage.html')

# getting details on a pending order.
def order_details(request, order_id):
    order = get_object_or_404(Orders, pk=order_id)
    return render(request, 'order_details.html', {'order': order})

def your_view(request, object_id):
    print(f"Received object_id: {object_id}")
    obj = get_object_or_404(YourModel, pk=object_id)
    return render(request, 'your_template.html', {'obj': obj})

# going online function

def update_online_status(request):
    if request.method == 'POST':
        form = OnlineStatusForm(request.POST)
        if form.is_valid():
            # Get the current user's profile
            user_profile = UserProfile.objects.get(user=request.user)

            # Update online status and location based on form data
            user_profile.is_online = form.cleaned_data['set_online']
            if user_profile.is_online:
                # Get latitude and longitude from the request or another source
                user_profile.latitude = request.POST.get('latitude')
                user_profile.longitude = request.POST.get('longitude')

            user_profile.save()

            return redirect('map')  # Redirect to the map view or any other page
    else:
        form = OnlineStatusForm(initial={'set_online': False})

    return render(request, 'workerPage.html', {'form': form})


def map(request):
    return render(request, 'map.html')
