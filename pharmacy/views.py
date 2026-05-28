from django.shortcuts import render
from .models import Medicine, Stock

def search_medicine(request):
    query = request.GET.get("q", "")
    results = []

    if query:
        results = Stock.objects.filter(
            medicine__name__icontains=query,
            quantity__gt=0
        ).select_related("medicine", "pharmacy")

    return render(request, "search.html", {
        "results": results,
    })
