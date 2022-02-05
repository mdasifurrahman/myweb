from django.shortcuts import render , HttpResponse
import fuzzywuzzy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
# Create your views here.
from django.core.files.storage import FileSystemStorage
import PyPDF2


def home(request):
    return render(request,'webpage/index.html')

def similarity(request):
    if request.method == "GET":
        return render(request, 'webpage/similar.html')

    if request.method == "POST":
        text1 = request.POST['uname1'].lower()
        text2 = request.POST['uname2'].lower()

        ratio = fuzz.ratio(text1,text2)

        context = {
            'answer': str(ratio) + "%"

        }
        return render(request, 'webpage/similar.html', context)


def upload(request):
    if request.method == "GET":
        return render(request, 'webpage/upload.html')

    if request.method == "POST":
        upload_file1 = request.FILES['document1']
        upload_file2 = request.FILES['document2']
        # print(upload_file.name)
        # print(upload_file.size)

        #document1
        fs = FileSystemStorage()
        filename1 = fs.save(upload_file1.name, upload_file1)
        uploaded_file_url1 = fs.url(filename1)

#document2
        filename2 = fs.save(upload_file2.name, upload_file2)
        uploaded_file_url2 = fs.url(filename2)

        pdffileobj1 = open(r"media\{}".format(filename1), 'rb')
        pdfreader1 = PyPDF2.PdfFileReader(pdffileobj1)
        pageobj1 = pdfreader1.getPage(0)
        arr1 = []
        arr1.append(pageobj1.extractText())

        pdffileobj2 = open(r"media\{}".format(filename2), 'rb')
        pdfreader2 = PyPDF2.PdfFileReader(pdffileobj2)
        pageobj2 = pdfreader2.getPage(0)
        arr2 = []
        arr2.append(pageobj2.extractText())
        ratio = fuzz.ratio(arr1,arr2)


        # print(pageobj1.extractText())

        context = {
                # 'uploaded_file_url1': uploaded_file_url1
            'answer' : ratio

        }
        # print(upload_file2.name)
        # print(upload_file2.size)
        return render(request,'webpage/upload.html', context)