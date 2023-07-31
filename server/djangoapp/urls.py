from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL

    # path for about view

    # path for contact us view

    # path for registration

    server/djangoapp/views.py # path for signup

    server/djangoapp/views.py # path for login

    server/djangoapp/views.py # path for logout

    path(route='', view=views.get_dealerships, name='index'),

    # path for dealer reviews view

# route for get_dealerships

from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL
    path(route='', view=views.get_dealerships, name='index')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
