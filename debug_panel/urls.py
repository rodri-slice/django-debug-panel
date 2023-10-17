"""
URLpatterns for the debug panel.

These should not be loaded explicitly; It is used internally by the
debug-panel application.
"""
from .views import debug_data

from django.urls import path

_PREFIX = '__debug__'

urlpatterns = [
    path(r'^%s/data/(?P<cache_key>\d+\.\d+)/$' % _PREFIX, debug_data, name='debug_data'),
]
