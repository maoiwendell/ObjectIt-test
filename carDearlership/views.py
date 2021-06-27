from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from carDearlership.models import CarForm, Car, Sale, SaleForm
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail



#def home(request,order_by):
#    if order_by.is_invalid():
#        order_by = '-carMake'


def home(request):
#    if order_by.is_invalid():
#        order_by = '-carMake'
        order_by = request.GET.get('order_by', '-carMake')
        all_cars = Car.objects.all().order_by(order_by)

        carpaginator = Paginator(all_cars , 10)
        page = request.GET.get('page')
        try:
            cars= carpaginator.page(page)
        except PageNotAnInteger:
            cars= carpaginator.page(1)
        except EmptyPage:
            cars= carpaginator.page(carpaginator.num_pages)
        return render(request, 'home.html',{'cars':cars})




def list(request):
    form = CarForm()
    #return HttpResponse('list')
    #return render(request,'listCar.html',{'form':form})
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            save_form = form.save()
            return render(request,'thankYouPage.html',{'listID':save_form.id})
    else:
        form = CarForm()

    return render(request, 'listCar.html', {'form':form})

def sale(request,car_id):
    form = SaleForm()

    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():

            sale = form.save(commit=False)
            sale.car_id = car_id
            sale.save()
            car = sale.car
            import logging
            #logging.info
            body = f"Car {sale.car_id} has been sold " + \
                       f"Greetings see details below" + \
                       f"Make:  {car.carMake} "+ \
                       f"Model: {car.carModel} "+ \
                       f"Year:  {car.carYear} "+ \
                       f"Condition: {car.carCondition} "+  \
                       f"Seller Name: {car.sellerName} "+  \
                       f"Seller Contact info: {car.sellerNumber}"+ \
                       f"Price: {car.carPrice} "+ \
                       f"Buyer Name: {sale.buyerName} "+\
                       f"Buyer Contact info: {sale.buyerInfo} "+\
                       f"Commission: { (car.carPrice*0.05)} "+\
                       f"Net Amount: { (car.carPrice*0.95)} "
            send_mail(
                'A car has been sold',
                body,
                'from@example.com',
                ['to@example.com'],
                fail_silently=False
            )
        return render(request, 'saleSuccess.html')
    else:
        form = SaleForm()
        return render(request,'sale.html',{'form':form})

def available(request,car_id):
#    if(Sale.object.get(car_id=carListed_id)
    sales = Sale.objects.filter(car_id=car_id)
    if sales:
        sales.delete()

    #sale.delete()

#    availableCar = Sale.object.get(car=car_id)
#    availableCar
    return redirect('home')


    #if form.is_valid():
    #sale = form.save(commit=False)
#    sale.car_id = car_id
    #sale.save()
