from django.shortcuts import render , HttpResponse
import fuzzywuzzy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
# Create your views here.

def home(request):
    return render(request,'webpage/index.html')

def similarity(request):
    if request.method == "GET":
        return render(request, 'webpage/similar.html')

    if request.method == "POST":
        text1 = request.POST['uname1']
        text2 = request.POST['uname2']

        ratio = fuzz.ratio(text1,text2)

        context = {
            'answer': str(ratio) + "%"

        }
        return render(request, 'webpage/similar.html', context)