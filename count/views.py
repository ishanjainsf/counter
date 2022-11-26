from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from count.models import Counter

@csrf_exempt
def get_current_counter(request):
    try:
        # data = list(Counter.objects.all().values_list())
        # print(data)
        return JsonResponse({"data": 1}, safe=False, status=200)
    except:
        return JsonResponse({"message":"Error in getting the current count value"}, status=500)


@csrf_exempt
def increment_counter(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        res = {}
        curr_value = data["curr_val"]
        res["updated_value"] = curr_value + 1
        return JsonResponse(res, status=200, safe=False)
    except:
        return JsonResponse({"message":"Error in incrementing the counter"}, status=500)