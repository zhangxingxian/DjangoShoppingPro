from django.shortcuts import render


def testquery(request):
    return render(request, 'test.html')
