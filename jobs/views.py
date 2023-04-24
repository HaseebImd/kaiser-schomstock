from django.shortcuts import render,redirect
from urllib.parse import urlencode
from django.urls import reverse
from geopy.geocoders import Nominatim
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.views import View
from .models import Jobs,JobImages
from Schomstock.models import ZipCodeLatLong
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
class AllJobs(View):
    
    def get(self, request):
        # zip_codes = [98052, 98092, 98115, 98103, 98003, 98023, 98105, 98042, 98034, 98133, 98118, 98125, 98058, 98031, 98122, 98033, 98032, 98004, 98059, 98001, 98006, 98056, 98030, 98155, 98168, 98117, 98002, 98198, 98038, 98029, 98027, 98109, 98074, 98144, 98007, 98040, 98072, 98146, 98011, 98107, 98106, 98188, 98008, 98178, 98108, 98075, 98028, 98112, 98119, 98055, 98053, 98102, 98022, 98126, 98116, 98005, 98121, 98199, 98177, 98166, 98136, 98045, 98077, 98101, 98057, 98065, 98104, 98019, 98148, 98014, 98354, 98070, 98010, 98024, 98051, 98047, 98151, 98251, 98134, 98039, 98195, 98158, 98154, 98161, 98174, 98068, 98256, 98288, 98050, 98132, 98171, 98184, 98054, 98164, 98181, 98224, 98191, 98009, 98013, 98015, 98025, 98035, 98041, 98062, 98064, 98063, 98071, 98073, 98083, 98089, 98093, 98111, 98113, 98114, 98124, 98127, 98131, 98129, 98139, 98138, 98141, 98145, 98160, 98165, 98170, 98175, 98185, 98190, 98194, 98471, 98481]
        # geolocator = Nominatim(user_agent='my_application')
        # for zip_code in zip_codes:
        #     location = geolocator.geocode(zip_code)
        #     print(zip_code, location.latitude, location.longitude)
        #     lat_long_zip = ZipCodeLatLong(zipCode=zip_code, lat=location.latitude, long=location.longitude)
        #     lat_long_zip.save()

        # return HttpResponse('Data inserted successfully')
        jobs=Jobs.objects.all().order_by('-id')
        for job in jobs:
            job_image = JobImages.objects.filter(jobObject=job).first()
            if job_image:
                image_path = job_image.image.path
                job.picture = job_image.image
        data = {}
        data['jobs'] = jobs
        return render(request, 'jobs/allJobs.html',data)

    def post(self, request):
        images=request.FILES.getlist('images')
        for img in images:
            print(img)
        return render(request, 'Test.html')
        

class NewJob(View):
    
    def get(self, request):
        return render(request, 'jobs/newJob.html')

    def post(self, request):
        try:
            # print("In the Post")
            # for i in request.POST:
            #     data=request.POST.get(i)
            #     print(i,data)
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
            # print(description)
            job.save()
            images=request.FILES.getlist('images')
            for img in images:
                print(img)
                image = JobImages(image=img, jobObject=job)
                image.save()
            return redirect('dashboard')
        except Exception as e:
            print(e)
            return render(request, 'jobs/newJob.html')


def PostDetails(request, id):
    try:
        job = Jobs.objects.get(id=id)
        images=JobImages.objects.filter(jobObject=job)
        latlong = ZipCodeLatLong.objects.filter(zipCode=job.postalCode).first()
        # for img in images:
        #     print(img.url)
        print(images)
        data = {}
        data['job'] = job
        data['images'] = images
        data['latlong'] = latlong
        return render(request, 'jobs/jobDetails.html',data)
    except Exception as e:
        print(e)
        return redirect('all-jobs')

def Dashboard(request):
    try:
        if "email" in request.session:
            cookiesEmail=request.session.get('email')
            userJobs = Jobs.objects.filter(email=cookiesEmail).order_by('-id')
            data = {}
            message = "Welcome back, "+cookiesEmail+"! Here are all your Posts."
            data['jobs'] = userJobs
            data['message'] = message
            return render(request, 'jobs/dashboard.html',data)
        else:
            return redirect('all-jobs')
    except:
        return redirect('all-jobs')
    

def Logout(request):
    request.session.clear()
    return redirect('/')


class JobPreview(View):
    def get(self, request,job_data):
        print(job_data)
        return render(request, 'jobs/previewJob.html', {'job_data': job_data})
    
class JobByCategory(View):
    def get(self, request,jobType):
        # print(jobType)
        jobs = Jobs.objects.filter(category=jobType)
        for job in jobs:
            job_image = JobImages.objects.filter(jobObject=job).first()
            if job_image:
                image_path = job_image.image.path
                job.picture = job_image.image
        data = {}
        data['jobs'] = jobs
        data['jobType'] = jobType
        return render(request, 'jobs/allJobs.html',data)

        
def JobSearch(request):
    try:
        query = request.POST.get('postalcode')
        print(query)
        jobs = Jobs.objects.filter(Q(postTitle__icontains=query) | Q(description__icontains=query))
        for job in jobs:
            job_image = JobImages.objects.filter(jobObject=job).first()
            if job_image:
                image_path = job_image.image.path
                job.picture = job_image.image
        data = {}
        data['jobs'] = jobs
        data['query'] = query
        
        return render(request, 'jobs/allJobs.html',data)
    except:
        return redirect('all-jobs')



def share_job(request, job_id):
    job = get_object_or_404(Jobs, id=job_id)
    if request.method == 'POST':
        share_url = request.POST.get('share_url')
        # implement your share functionality here
        return redirect('job_details', job_id=job.id)
    else:
        return render(request, 'jobs/share.html', {'job': job})