# frontend/urls.py

from django.urls import re_path
from .views import FrontendAppView

urlpatterns = [
    # Catch-all URL that directs to the React app
    re_path(r'^.*$', FrontendAppView.as_view(), name='frontend'),
]
