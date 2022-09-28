from django.shortcuts import render, redirect

from .models import ContactForm
from django.contrib import messages




def teamform(request):
    if  request.method =='POST':

        fullname=request.POST['fullname']
        phone=request.POST['phone']
        email=request.POST['email']
        company_name=request.POST['company_name']
        subject=request.POST['subject']
        detail_msg=request.POST['detail_msg']
        user_id = request.POST['user_id']
        
       

        teamform =ContactForm(fullname=fullname, phone=phone, email=email, company_name=company_name, subject=subject, detail_msg=detail_msg, user_id =user_id)

        teamform.save()
        messages.success(request, 'Thanks for reaching out!')
        return redirect('youtubers')
