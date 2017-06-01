# _*_ encoding:utf-8 _*_
from django.views.generic.base import View
from django.shortcuts import render
from django.http import HttpResponse
import json
import MySQLdb


# Create your views here.
class MedicineOperation(View):
    def get(self, request):
        return render(request, "medicine-operation.html")


class PrescriptionReceive(View):
    def post(self, request):
        print 'PrescriptionReceive...'
        diseaseName = request.POST.get('diseaseName')
        patientContent = request.POST.get('patientContent')
        contentVec = request.POST.get('contentVec')
        prescriptionName = request.POST.get('prescriptionName')
        prescriptions = request.POST.get('prescriptions')
        prescriptionsReason = request.POST.get('prescriptionsReason')
        sourceFrom = request.POST.get('sourceFrom')
        if diseaseName == '' or patientContent == '' or prescriptionName == '' or prescriptions == '' or prescriptionsReason == '' or sourceFrom == '':
            print '带星号的为必填项'
            return HttpResponse('{"result":"带星号的为必填项"}', content_type="application/json")
        elif diseaseName == None or patientContent == None or prescriptionName == None or prescriptions == None or prescriptionsReason == None or sourceFrom == None:
            print '数据异常，提交失败'
            return HttpResponse('{"result":"数据异常，提交失败"}', content_type="application/json")
        host = "127.0.0.1"

        user = "root"

        pwd = "w1020392881"

        db = "candyonline"
        sql = 'insert into prescription_operation(diseaseName, patientContent, contentVec, prescriptionName, prescriptions, prescriptionsReason, sourceFrom) VALUES(%s,%s,%s,%s,%s,%s,%s) '
        data = (diseaseName, patientContent, contentVec, prescriptionName, prescriptions, prescriptionsReason, sourceFrom)
        lis = []
        try:
            conn = MySQLdb.connect(host, user, pwd, db, use_unicode=True, charset="utf8")
            lis.append(data)
            cursor = conn.cursor()
            res = cursor.executemany(sql, lis)
            conn.commit()
        except BaseException, e:
            print e.message
        finally:
            conn.rollback()
            cursor.close()
            conn.close()
        if res == 1:
            return HttpResponse('{"result":"提交成功"}', content_type="application/json")
        else:
            return HttpResponse('{"result":"数据异常，提交失败"}', content_type="application/json")
