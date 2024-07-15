from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


# Create your views here.
@require_http_methods(["GET"])
@csrf_exempt
def authorize(request):
    try:
        code = request.GET["code"]
        print(code)
        return JsonResponse({}, status=200)
    except Exception as e:
        return JsonResponse({"err": str(e)})
