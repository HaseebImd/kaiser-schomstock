from django.shortcuts import render
from django.http.response import JsonResponse
from django.views import View
from .models import ZipCodeLatLong
def Home(request):
    return render(request, 'Home.html')


class Test(View):
    
    def get(self, request):
        return render(request, 'Test.html')

    def post(self, request):
        images=request.FILES.getlist('images')
        for img in images:
            print(img)
        return render(request, 'Test.html')

class AllZipCodes(View):
    def get(self, request):
        resp=ZipCodeLatLong.objects.values('zipCode','lat','long')
        resp = list(resp) 
        return JsonResponse({'resp': resp})