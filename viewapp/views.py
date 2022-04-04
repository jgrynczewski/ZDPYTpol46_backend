from django.shortcuts import render, HttpResponse
from django import views

from django.views.generic import TemplateView


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


# generic view
class HelloTemplateView(TemplateView):
    template_name = 'viewapp/hello.html'


# function-based view
def hello_template2(request):
    name = "Jan"
    return render(
        request,
        'viewapp/hello2.html',
        context={
            "name": name,
        }
    )


# class-based view
class HelloClassView2(views.View):
    def get(self, request):
        name = "Jan"
        return render(
            request,
            'viewapp/hello2.html',
            context={
                "name": name
            }
        )


# generic view
class HelloTemplateView2(TemplateView):
    template_name = 'viewapp/hello2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Jan"
        return context
