from django.shortcuts import render


def contact1(request):
    return render(
        request,
        'formapp2/form1.html'
    )