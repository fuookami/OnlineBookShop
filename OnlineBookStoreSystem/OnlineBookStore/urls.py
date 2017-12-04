from django.conf.urls import url, include

from . import views
from . import tests
from .AccountHandler.views import *
from .MessageHandler.views import *
from .BookHandler.views import *

urlpatterns = [
    url(r'^index$', views.go_to_index),
    url(r'^about$', views.go_to_about),
    url(r'^store$', views.go_to_store),
    url(r'^trolley$', views.go_to_trolley),
    url(r'^user_center$', views.go_to_user_center),

    url(r'^account/register$', registered_account_request),
    url(r'^account/register/activation_token=(\S[^;]+)$', activate_account_request),
    url(r'^account/login$', login_request),

    url(r'^message/get_messages_count$', get_message_count_request),
    url(r'^message/get_messages$', get_message_request),

    url(r'^book/search_book$', get_search_book_request),
    url(r'^book/get_book_detail$', get_book_detail_request),
    url(r'^book/get_server_fee$', get_server_fee_request),
    url(r'^book/register_used_book$', register_used_book_request)

    # for test
    # url(r'^test/token1=(\w+);token2=(\w+)$', tests.test_pattern),
    # url(r'^test/server$', tests.test_server_ip),
    # url(r'^test/register$', tests.test_register)
]
