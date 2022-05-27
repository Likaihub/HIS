from django.shortcuts import render

# Create your views here.
def patient_information(request):
    return render(request, 'index.html')
