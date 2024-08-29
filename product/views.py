from .models import Product
from django.shortcuts import render , HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all().values('name', 'description', 'price', 'provider')
        return JsonResponse(list(products), safe=False)
    return HttpResponse("Only GET method is allowed.", status=405)



@csrf_exempt
def create_product(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        product = Product.objects.get(id=body ,name=body['name'], price=body['price'])
        product.objects.create(
            name= body['input_name'],
            price= body['input_price'],
        )
        product.save()
        return HttpResponse("new product reserved and factor made")
    else:
        return HttpResponse("BAD REQUEST")
    