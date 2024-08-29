from django.shortcuts import render , HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from provider.models import Provider


@csrf_exempt
def signup(request) :
    if request.method == 'POST' :
        body = json.loads(request.body)
        Provider.objects.create(
            name= body['name_inp'] , 
            email = body['email_inp'] , 
            phone_number = body['phone_number_inp'] ,
        )
        return HttpResponse("new provider added")
    else : 
        return HttpResponse("bad request!")
