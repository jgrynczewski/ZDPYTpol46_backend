from django.shortcuts import render, HttpResponse
from django import views


# function-based view
def hello(request):
    return HttpResponse("Hello, world!")


# class-based view
class HelloView(views.View):
    def get(self, request):
        return HttpResponse("Hello, world!")


# A szablony ?
# function-based view
def hello_template(request):
    return render(
        request,
        'viewapp/hello.html'
    )


# class-based view
class HelloClassView(views.View):
    def get(self, request):
        return render(
            request,
            'viewapp/hello.html'
        )
