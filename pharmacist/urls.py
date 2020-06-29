from django.urls import path
from . import views
urlpatterns=[
	path('',views.pharmacistHome,name="pharmacistHome"),	
	path('issuemedicine/',views.issueMedicine, name="issueMedicine"),
]