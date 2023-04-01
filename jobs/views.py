from django.shortcuts import render,redirect
from django.http.response import JsonResponse
from django.views import View
from .models import Jobs,JobImages
class AllJobs(View):
    
    def get(self, request):
        return render(request, 'jobs/allJobs.html')

    def post(self, request):
        images=request.FILES.getlist('images')
        for img in images:
            print(img)
        return render(request, 'Test.html')
        

class NewJob(View):
    
    def get(self, request):
        return render(request, 'jobs/newJob.html')

    def post(self, request):
        # print("In the Post")
        for i in request.POST:
            data=request.POST.get(i)
            print(i,data)
        city = request.POST.get('city')
        category = request.POST.get('category')
        postTitle = request.POST.get('postingtitle')
        Neighborhood = request.POST.get('neighborhood')
        postalCode = request.POST.get('postalcode')
        description = request.POST.get('description')
        employementType = request.POST.get('employementType')
        jobTitle = request.POST.get('jobTitle')
        compensation = request.POST.get('compensation')
        companyName = request.POST.get('companyName')
        email = request.POST.get('emailAddress')
        emailPrivacy = request.POST.get('emailPrivacy')
        phoneNumber = request.POST.get('phoneNumber')
        contactName = request.POST.get('contactName')
        streetName = request.POST.get('street')
        crossStreet = request.POST.get('crossStreet')
        cityAddress = request.POST.get('cityName')
        
        job=Jobs(city=city,category=category,postTitle=postTitle,Neighborhood=Neighborhood,postalCode=postalCode,description=description,employementType=employementType,
                 jobTitle=jobTitle,compensation=compensation,companyName=companyName,email=email,phoneNumber=phoneNumber,contactName=contactName,streetName=streetName,crossStreet=crossStreet,cityAddress=cityAddress
                 )
        job.direct_contact_recureters=True if request.POST.get('contact_by_rec') else False
        job.internship=True if request.POST.get('internship') else False
        job.non_prof_org=True if request.POST.get('non_profit_org') else False
        job.relo_ass_available=True if request.POST.get('relocation') else False
        job.telecommuting=True if request.POST.get('telecon') else False
        job.phoneCallOk=True if request.POST.get('phoneCalls') else False
        job.smsOk=True if request.POST.get('textSms') else False
        job.showPhoneNumber=True if request.POST.get('showPhoneNumber') else False
        job.showAddress=True if request.POST.get('showAddress') else False
        job.save()
        images=request.FILES.getlist('images')
        for img in images:
            print(img)
            image = JobImages(image=img, jobObject=job)
            image.save()
        return redirect('create-new-job')
        