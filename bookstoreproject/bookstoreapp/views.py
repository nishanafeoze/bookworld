from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def demo(request):
    return render(request, "hi.html")
# def about(request):
#     return render(request, "about.html")
# def contact(request):
#     return render(request,"contact.html")
# def bookdetail(request):
#     return render(request,"bookdetail.html")
# def thanks(request):
#     return render(request,"thanks.html")
def index(request):
    return render(request, "index.html")
#
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res = x+y
#     sub = x - y
#     mul = x * y
#     div = x / y
#     return render(request, 'result.html', {'result' : res,'sub':sub,'mul':mul,'div':div })

# Create your views