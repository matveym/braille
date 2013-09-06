from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import renderer


def home(request):
    return render(request, 'home.html')


@csrf_exempt
def svg(request):
    text = request.POST['text']
    svg_text = renderer.text(text)

    response = HttpResponse(svg_text, content_type="image/svg+xml")
    content_disposition = 'attachment; filename=image.svg'
    # content_disposition = 'attachment; filename=%s.svg' % _filename(text))
    response['Content-Disposition'] = content_disposition
    response['Content-Length'] = len(svg_text)
    return response

def _filename(text):
    result = text.replace('\r\n', ' ').replace('\r', ' ').replace('\n', ' ')
    result = result[:20]
    return result
