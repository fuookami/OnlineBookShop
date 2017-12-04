from django.shortcuts import render

# Create your views here.


def go_to_index(request):
    return render(request, '../WebRoot/index.html')


def go_to_about(request):
    return render(request, '../WebRoot/about.html')


def go_to_store(request):
    return render(request, '../WebRoot/store.html')


def go_to_trolley(request):
    return render(request, '../WebRoot/trolley.html')


def go_to_user_center(request):
    return render(request, '../WebRoot/user_center.html')
