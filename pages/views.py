from django.shortcuts import render

# Create your viewwwwas here.

def index(request):

          context = {
               'title':"E-commerce"
          }
          return render(request,'pages/index.html',context)



