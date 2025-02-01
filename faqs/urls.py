from django.urls import path
from .views import faq_list
from .views import create_faq,faq_page,add_fag_page

urlpatterns = [
    path("faqs/", faq_list, name="faq-list"),
    path('create_faq/', create_faq, name='create_faq'),
    path("faq/", faq_page, name="faq"),
    path('add_faq/', add_fag_page, name='add_faq'),
]
