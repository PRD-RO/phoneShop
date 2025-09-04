from django.db.models import Sum
from .models import Cart 

def CartTotal(request):
    total=Cart.objects.aggregate(total=Sum("quantity"))["total"]or 0
    return {"CartTotal":total}

