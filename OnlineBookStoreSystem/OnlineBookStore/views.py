from django.shortcuts import render

# Create your views here.


def go_to_index(request):
    return render(request, '../WebRoot/index.html')
