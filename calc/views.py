from django.http import HttpResponse


def add(request):
    print('111')
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    c = int(a) + int(b)
    return HttpResponse(c)


def add2(request, a, b):
    print(a)
    c = int(a) + int(b)
    return HttpResponse(c)
