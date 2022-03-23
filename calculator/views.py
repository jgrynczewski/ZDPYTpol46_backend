from django.shortcuts import render, redirect


def add(request):
    value_1 = request.POST.get("value_1")
    value_2 = request.POST.get("value_2")

    if value_1 and value_2:
        res = int(value_1) + int(value_2)
        return redirect('calculator:result', res=res)

    return render(
        request,
        'calculator/add.html',
    )


def result(request, res):
    return render(
        request,
        'calculator/result.html',
        context={
            'res': res
        }
    )
