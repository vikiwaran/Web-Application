from django.shortcuts import render
from django.shortcuts import HttpResponse
from reportlab.pdfgen import canvas
from django.views.generic import View
from wsgiref.util import FileWrapper
from django.template.loader import render_to_string
from io import BytesIO
from xhtml2pdf import pisa
from django.db import connection
from .models import Faculty_information
from faculty.models import Book_published
from faculty.models import Chapters19_20
from faculty.models import Chapters
from faculty.models import Conference
from faculty.models import Journals




def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request,'dashboard.html')

def faculty_info(request):
    return render(request,'faculty_info.html')

def results(request):
    return render(request,'results.html')

def book_pub(request):
    return render(request,'book_pub.html')

def book_cha(request):
    return render(request,'book_cha.html')

def about(request):
    return render(request,'about.html')

def chapter(request):
    result1=()
    result2=()
    result3=()
    result4=()
    F_Name=''
    cursor = connection.cursor()
    p=request.POST.getlist('checks []')
    if(p.count('2017')>0):
        cursor.execute("SELECT * FROM Chapters WHERE F_Id ='"+request.POST.get('faculty')+"' and Year ='2017'")
        result1 = cursor.fetchall()
        if(len(result1)!=0):
            F_Name=result1[0][1]

    if(p.count('2018')>0):
        cursor.execute("SELECT * FROM Chapters WHERE F_Id ='"+request.POST.get('faculty')+"' and Year ='2018'")
        result2 = cursor.fetchall()
        if(len(result2)!=0):
            F_Name=result2[0][1]

    if(p.count('2019')>0):
        cursor.execute("SELECT * FROM Chapters WHERE F_Id ='"+request.POST.get('faculty')+"' and Year ='2019'")
        result3 = cursor.fetchall()
        if(len(result3)!=0):
            F_Name=result3[0][1]

    if(p.count('2020')>0):
        cursor.execute("SELECT * FROM Chapters WHERE F_Id ='"+request.POST.get('faculty')+"' and Year ='2020'")
        result4 = cursor.fetchall()
        if(len(result4)!=0):
            F_Name=result4[0][1]
    data={'data1':result1,'data2':result2,'data3':result3,'data4':result4,'F_Name':F_Name}
    print(result3)
    return render(request,'chapter.html',{'data': data})





def paper(request):
        result1=()
        result2=()
        result3=()
        result4=()
        F_Name=''
        cursor = connection.cursor()
        p=request.POST.getlist('checks []')
        r=request.POST.getlist('checks')
        if(p.count('2017')>0 and r.count('1')>0 ):
            cursor.execute("SELECT * FROM Journals WHERE F_Id ='"+request.POST.get('faculty')+"' and Year ='2017'")
            result1 = cursor.fetchall()
            if(len(result1)!=0):
                F_Name=result1[0][1]

        if(p.count('2018')>0 and r.count('1')>0):
            cursor.execute("SELECT * FROM Journals WHERE F_Id ='"+request.POST.get('faculty')+"' and Year ='2018'")
            result2 = cursor.fetchall()
            if(len(result2)!=0):
                F_Name=result2[0][1]

        if(p.count('2019')>0 and r.count('1')>0):
            cursor.execute("SELECT * FROM Journals WHERE F_Id ='"+request.POST.get('faculty')+"' and Year ='2019'")
            result3 = cursor.fetchall()
            if(len(result3)!=0):
                F_Name=result3[0][1]

        if(p.count('2020')>0 and r.count('1')>0):
            cursor.execute("SELECT * FROM Journals WHERE F_Id ='"+request.POST.get('faculty')+"' and Year ='2020'")
            result4 = cursor.fetchall()
            if(len(result4)!=0):
                F_Name=result4[0][1]


        result11=()
        result21=()
        result31=()
        result41=()
        cursor = connection.cursor()
        if(p.count('2017')>0 and r.count('2')>0 ):
            cursor.execute("SELECT * FROM Conference WHERE F_Id ='"+request.POST.get('faculty')+"' and Year ='2017'")
            result11 = cursor.fetchall()
            if(len(result11)!=0):
                F_Name=result11[0][1]

        if(p.count('2018')>0 and r.count('2')>0):
            cursor.execute("SELECT * FROM Conference WHERE F_Id ='"+request.POST.get('faculty')+"' and Year ='2018'")
            result21 = cursor.fetchall()
            if(len(result21)!=0):
                F_Name=result21[0][1]

        if(p.count('2019')>0 and r.count('2')>0):
            cursor.execute("SELECT * FROM Conference WHERE F_Id ='"+request.POST.get('faculty')+"' and Year ='2019'")
            result31 = cursor.fetchall()
            if(len(result31)!=0):
                F_Name=result31[0][1]

        if(p.count('2020')>0 and r.count('2')>0):
            cursor.execute("SELECT * FROM Conference WHERE F_Id ='"+request.POST.get('faculty')+"' and Year ='2020'")
            result41 = cursor.fetchall()
            if(len(result41)!=0):
                F_Name=result41[0][1]
        data={'data1':result1,'data2':result2,'data3':result3,'data4':result4,'data11':result11,'data21':result21,'data31':result31,'data41':result41,'F_Name':F_Name}
        return render(request,'paper.html',{'data': data})







def book(request):
    print(request.POST.get('book'))
    posts= Book_published.objects.raw("SELECT * FROM Book_published WHERE B_Id='"+request.POST.get('book')+"'")
    return render(request,'book.html',{'data': posts})


def show(request):
    print(request.POST.get('faculty'))

    posts = Faculty_information.objects.raw("SELECT * FROM Faculty_information WHERE F_Id='"+request.POST.get('faculty')+"'")
    return render(request,'show.html',{'data': posts})
