from django.urls import path
from . import views
urlpatterns=[
	path('',views.diagnosticHome,name="diagnosticHome"),
	path('adddiagnosis/',views.addDiagnosis,name="addDiagnosticTest"),
	path('testdiagnose/',views.testDiagnose,name="testDiagnose"),
	path('testdiagnose/fetchdata',views.fetchData,name="fetchData"),
]