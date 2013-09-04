from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import svg


def home(request):
    return render(request, 'home.html')


@csrf_exempt
def svg(request):
    text = request.POST['text']
    svg_text = svg.text(text)
    response = HttpResponse(svg_text, content_type="image/svg+xml")
    response['Content-Disposition'] = 'attachment; filename=test.svg'
    response['Content-Length'] = len(svg_text)
    return response
