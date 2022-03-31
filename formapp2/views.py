from django.shortcuts import render, redirect

from formapp2.models import Message


def message_list(request):
    messages = Message.objects.all()

    return render(
        request,
        'formapp2/message_list.html',
        context={
            'messages': messages
        }
    )


# Formularz HMTL
def contact1(request):
    if request.method == "POST":
        data = request.POST

        Message.objects.create(
            name=data.get('name'),
            email=data.get('email'),
            category=data.get('category'),
            subject=data.get('subject'),
            body=data.get('body')
        )

        return redirect('formapp2:message-list')

    return render(
        request,
        'formapp2/form1.html'
    )