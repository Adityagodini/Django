from django.shortcuts import render

# Create your views here.
def index(request):
    name="Devaratha"
    animal="Dinasour"
    place="Khansar"
    food="Biriyani"
    movie="Salaar"

    ctx={
        'name':name,
        'animal':animal,
        'place':place,
        'food':food,
        'movie':movie

    }

    return render(request,'my.html',ctx)