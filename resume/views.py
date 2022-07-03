from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
# Create your views here.

firstname=''

def build(request):
    return render(request,'index.html')

def generate(request):
    firstname=request.POST.get('firstName')
    lastname=request.POST.get('lastName')
    email=request.POST.get('email')
    mnumber=request.POST.get('mnumber')
    dob=request.POST.get('dob')
    linkedin=request.POST.get('linkedin')
    summary=request.POST.get('summary')
    path=request.get_full_path()
    path='http://127.0.0.1:8000'+path
    educationdetails = []
    professionaldetails = []
    skills = []
    personaldetails = []

    personaldetails={'firstname':firstname,'lastname':lastname,'email':email,'mnumber':mnumber,'dob':dob,'linkedin':linkedin,'summary':summary}
    print(personaldetails)
    if 'val' in request.POST:
        val=request.POST.get('val')
        if val !='':
            val=int(val)
            
            for i in range(1,val+1):
                courseduration=request.POST.get('courseduration'+str(i))
                standard=request.POST.get('standard'+str(i))
                college=request.POST.get('college'+str(i))
                cgpa=request.POST.get('cgpa'+str(i))
                educationdetails.append({'courseduration':courseduration,'standard':standard,'college':college,'cgpa':cgpa})
                #print(educationdetails)
    if 'val1' in request.POST:
        val1=request.POST.get('val1')
        if val1 !='':
            val1=int(val1)
            
            for i in range(1,val1+1):
                projectduration=request.POST.get('projectduration'+str(i))
                role=request.POST.get('role'+str(i))
                projectname=request.POST.get('projectname'+str(i))
                projectdescription=request.POST.get('projectdescription'+str(i))
                professionaldetails.append({'projectduration':projectduration,'projectname':projectname,'role':role,'projectdescription':projectdescription})
                #print(professionaldetails)
    if 'val2' in request.POST:
        val2=request.POST.get('val2')
        if val2!='':
            val2=int(val2)
            
            for i in range(1,val2+1):
                skill=request.POST.get('skill'+str(i))
                skills.append(skill)
            #print(skills)
    #print(personaldetails, educationdetails,professionaldetails,skills)
    return render(request,'srt-resume.html',{'personaldetails':personaldetails,'educationdetails':educationdetails,'professionaldetails':professionaldetails,'skills':skills})

def download(request):
    import pdfkit
    url=request.get_full_path()
    url+='/generate'
    filename=firstname+'.pdf'
    # configuring pdfkit to point to our installation of wkhtmltopdf
    config = pdfkit.configuration(wkhtmltopdf=r"F:\\android\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")

    # converting html file to pdf file
    pdfkit.from_url('http://127.0.0.1:8000/generate',filename, configuration=config)
    return HttpResponse('D:\django projects\env\resumebuilder\out',content_type='application/pdf')
