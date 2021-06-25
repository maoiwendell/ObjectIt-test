from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from carDearlership.models import CarForm, Car


def home(request):

    all_cars = Car.objects.all()
    carpaginator = Paginator(all_cars , 10)
    page = request.GET.get('page')
    try:
        cars= carpaginator.page(page)
    except PageNotAnInteger:
        cars= carpaginator.page(1)
    except EmptyPage:
        cars= carpaginator.page(carpaginator.num_pages)
    return render(request, 'home.html',{'all_car':cars})


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
