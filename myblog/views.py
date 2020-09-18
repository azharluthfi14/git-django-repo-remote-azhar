from django.shortcuts import render


def my_view(request):
    context = {
        'title': "hello word",
    }
    return render(request, "index.html", context)
