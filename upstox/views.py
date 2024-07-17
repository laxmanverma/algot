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


@require_http_methods(["GET"])
@csrf_exempt
def historical_data(request):
    try:
        symbol = request.GET["symbol"]
        interval = request.GET["interval"]
        to_date = request.GET["to_date"]
        from_date = request.GET["from_date"]
        from .service import fetch_historical_candle_data
        candle_data = fetch_historical_candle_data(symbol, interval, to_date, from_date)
        return JsonResponse(candle_data, status=200)
    except Exception as e:
        return JsonResponse({"err": str(e)})