from django.shortcuts import render


# Zapis ciasteczka
def set_cookie(request):
    res = render(
        request,
        'stateapp/cookie.html',
        context={
            'msg': "Ustawiono ciasteczko 'user'"
        }
    )

    # print(res)
    # print(dir(res))  # set_cookie / delete_cookie

    res.set_cookie('user', 'John')
    return res


# Odczyt ciasteczka
def show_cookie(request):
    # print(request)
    # print(dir(request))  # COOKIES
    print(request.COOKIES)

    return render(
        request,
        'stateapp/show_cookie.html',
        context={
            'cookies': request.COOKIES,
        }
    )


# Usunięcie ciasteczka
def delete_cookie(request):
    res = render(
        request,
        'stateapp/cookie.html',
        context={
            'msg': "Usunięto ciasteczko 'user'"
        }
    )

    res.delete_cookie('user')
    return res


# Zapis danych do sesji
def set_session(request):
    # print(dir(request))
    # print(request.session)
    # print(dir(request.session))  # keys, values, items, has_key ... -> like a dict

    request.session['counter'] = 0

    return render(
        request,
        'stateapp/session.html',
        context={
            'msg': 'Ustawiono sesję',
        }
    )


# Odczyt danych z sesji
def show_session(request):
    if request.session.has_key('counter'):
        request.session['counter'] += 1

    return render(
        request,
        'stateapp/show_session.html',
        context={
            'session': request.session
        }
    )


# Usunięcie danych z sesji
def delete_session(request):
    if request.session.has_key('counter'):
        del request.session['counter']

    return render(
        request,
        'stateapp/session.html',
        context={
            'msg': 'Z sesji usunięto dane pod kluczem counter'
        }
    )
