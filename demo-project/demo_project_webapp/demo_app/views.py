from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    print(request.method)
    for item in request.headers:
        print(item)
    return HttpResponse("Hello!, This is the Welcome Home for DemoApp")


def drinks(request, drink_name):

    drink = {
        'mocha': 'type of coffee',
        'tea' : 'type of beverage',
        'lemonade' : 'type of refreshment',
    }
    choice_of_drink = drink[drink_name]

    return HttpResponse(f"<h2> {drink_name} </h2>" + choice_of_drink)

