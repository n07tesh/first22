from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord



# Create your views here.
def index(request):


    my_dict = {'insert_me':''}
    return render (request,'first_app/index.html',context=my_dict)
def index2(request):

    # Example for MTV in Django_LV2
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpage_list}


    return  render(request, 'first_app/index2.html',context=date_dict)
