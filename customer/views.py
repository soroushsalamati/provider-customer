from django.shortcuts import render , HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from customer.models import Customer


@csrf_exempt
def signup(request) :
    if request.method == 'POST' :
        body = json.loads(request.body)
        Customer.objects.create(
            name= body['name_inp'] , 
            phone_number = body['phone_number_inp'] ,
            wallet = body['wallet_inp'] ,
        )
        return HttpResponse("new Customer added")
    else : 
        return HttpResponse("bad request!")
