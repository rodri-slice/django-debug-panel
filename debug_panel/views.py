from django.http import HttpResponse
from debug_panel.cache import cache
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def debug_data(request, cache_key):
    html = cache.get(cache_key)

    if html is None:
        return render(request, 'debug-data-unavailable.html', {})

    return HttpResponse(html, content_type="text/html; charset=utf-8")
