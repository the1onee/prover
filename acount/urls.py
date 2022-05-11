
from django.urls import path
from . import views
app_name='accounts'
urlpatterns = [
path('doctoer/',views.doctoer_list, name='doctoer_list'),
path('<slug:slug>/',views.doctoer_detail, name='doctoer_detail')
]
