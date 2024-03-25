from django.shortcuts import render
from .models import Sushi, Sets

def food_page(request):
    foodSushi = Sushi.objects.all()
    foodSets = Sets.objects.all()
    context = {
        'foodSushi': foodSushi,
        'foodSets': foodSets
    }
    return render(request, "./foods_page.html", context)
