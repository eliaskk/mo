# _*_ encoding:utf-8 _*_
from django.views.generic.base import View
from django.shortcuts import render
from django.http import HttpResponse
import simplejson

from medicineDialectic import rank4Medicine
from scrapMedicine import prescriptionTreatment
# Create your views here.


class SavePrescription(View):
    def get(self, request):
        return render(request, "prescription.html")


class ReceivePrescription(View):
    def post(self, request):
        print "ReceivePrescription come in..."
        content = request.POST.get("content")
        content = unicode.decode(content, 'utf-8')
        lis = rank4Medicine(content, '')

        result = simplejson.dumps(lis)
        return HttpResponse(result, content_type='application/json')


class Test(View):
    def get(self, request):
        fileName = 'G:\myfile\myWorkSpace\prescription.txt'
        prescriptionTreatment(fileName)
        return render(request, "prescription.html")


class MedicineReasoning(View):
    def get(self, request):
        return render(request, "medicine-reasoning.html")


class PrescriptionMatch(View):
    def post(self, request):
        print "PrescriptionMatch........"
        free_text = request.POST.get('free_text')
        lis = ['数据1', '数据2', '数据3', '数据4', '数据5', '数据6',
               '数据7', '数据8', '数据9', '数据10', '数据11', '数据12', '数据13']
        return HttpResponse('{"status":"success", "lis":'+simplejson.dumps(lis)+'}', content_type='application/json')