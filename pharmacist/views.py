from django.shortcuts import render,get_object_or_404
from .models import Medicinemaster, Medicineissued
from django.http import HttpResponse
def getSize():
	count_medicine_rows = Medicinemaster.objects.count()
	return count_medicine_rows
def populatePharmacistDB():
	ws_med_name=['Paracetamol','Crocin','Disprin']
	ws_price=[73,20,50]
	ws_stock_qty=[90,100,30]
	for i in range(len(ws_med_name)):
		addStock = Medicinemaster()
		addStock.ws_med_name=ws_med_name[i]
		addStock.ws_stock_qty=ws_stock_qty[i]
		addStock.ws_price=ws_price[i]
		addStock.save()
def getMedicineList(ws_pat_id):
	medicineissuedobj = Medicineissued.objects.filter(ws_pat_id=ws_pat_id)
	medicineDict = {}
	i=0
	for meds in medicineissuedobj:
		priceObj = get_object_or_404(Medicinemaster,ws_med_id=meds.ws_med_id)
		print(priceObj.ws_med_id)
		medicineDict[i]= [priceObj.ws_med_name,meds.ws_qty,priceObj.ws_price*meds.ws_qty]
		i+=1
	return medicineDict
def pharmacistHome(request):
	return render(request,"pharmacist/pharmacistHome.html")

def issueMedicine(request):
	return render(request,'pharmacist/issuemedicine.html')