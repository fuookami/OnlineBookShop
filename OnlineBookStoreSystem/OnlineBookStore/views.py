from django.shortcuts import render

# Create your views here.


def go_to_index(request):
    return render(request, '../WebRoot/index.html')


def go_to_about(request):
    return render(request, '../WebRoot/about.html')


def go_to_store(request):
    return render(request, '../WebRoot/store.html')


def go_to_check_book_detail(request):
    return render(request, '../WebRoot/check_book_detail.html')


def go_to_register_used_book(request):
    return render(request, '../WebRoot/register_used_book.html')


def go_to_trolley(request):
    return render(request, '../WebRoot/trolley.html')


def go_to_user_center(request):
    return render(request, '../WebRoot/user_center.html')


def go_to_login(request):
    return render(request, '../WebRoot/login.html')


def go_to_register_account(request):
    return render(request, '../WebRoot/register_account.html')
