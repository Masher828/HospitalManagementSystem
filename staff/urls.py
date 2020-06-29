from django.urls import path
from . import views
app_name = "staff"
urlpatterns=[
	path('',views.loginStaff,name="staffHome"),
	path('addstaff/',views.addStaff,name="addStaff"),
	path('loginstaff/',views.loginStaff,name="loginStaff"),
]