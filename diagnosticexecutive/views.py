from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Diagnosticmaster,Diagnostictest
from deskexecutive.models import Userstore
def diagnosticHome(request):
	return render(request,"diagnostic/diagnosisHome.html")

def populateDiagnosticDB():
	ws_test_name=['ECG','Blood Test','MRI','CCTA','ECHO']
	ws_price=[700, 150, 1500,3200, 700]

	for i in range(len(ws_test_name)):
		addTest = Diagnosticmaster()
		addTest.ws_test_name=ws_test_name[i]
		addTest.ws_charge=ws_price[i]
		addTest.save()
def getDiagnosisList(ws_pat_id):
	diagnosisObj = Diagnostictest.objects.filter(ws_pat_id=ws_pat_id)
	diagnosisDict = {}
	i=0
	for tests in diagnosisObj:
		testObj = get_object_or_404(Diagnosticmaster,ws_test_id=tests.ws_test_id)
		print(testObj.ws_test_id)
		diagnosisDict[i]= [testObj.ws_test_name,testObj.ws_charge]
		i+=1
	return diagnosisDict


def addDiagnosis(request):
     if request.method == 'POST':
        testName = request.POST['testid']
        charges = request.POST['charge']
        ob = Diagnosticmaster()
        ob.ws_charge=charges
        ob.ws_test_name=testName
        ob.save()
        return render(request,'add.html',{"msg":"Test Added Succesfully"})
     else:   
        return render(request,'add.html')

def fetchData(request):
	if request.method == "POST":
		ws_pat_id = request.POST['uid']
		patientobj= get_object_or_404(Userstore,pk=ws_pat_id)
		patientDetails={
		'patientId' : ws_pat_id,
		'patientName': patientobj.ws_pat_name,
		'patientSSN' : patientobj.ws_ssn,
		'patientAge' : patientobj.ws_pat_age,
		'patientCity': patientobj.ws_city,
		'patientState': patientobj.ws_state,
		'patientAdrs' : patientobj.ws_adrs,
		'patientStatus': patientobj.ws_status,
		'patientRtype' : patientobj.ws_rtype,
		'patientDOJ' : str(patientobj.prettyTime)
		}
	return HttpResponse(json.dumps(patientDetails))

def testDiagnose(request):
	if request.method == 'POST':
		p_id = request.POST['pid']
		testId = request.POST['testid']
		patients = Patients.objects.all()
		if Diagnosticmaster.objects.filter(ws_test_id=testId).exists():
			ob = Diagnosticmaster.objects.filter(ws_test_id=testId)
			dt = DiagnosticTest()
			dt.ws_pat_id = patient.p_id
			dt.ws_test_id = diagnos.ws_test_id
			dt.save()
			return render(request,'testdiagnose.html',{'message':'Test Added Succesfully'})
		else:
			return render(request,'testdiagnose.html',{'message':"Test doesn't exists"})
	else:
		return render(request,'testdiagnose.html')