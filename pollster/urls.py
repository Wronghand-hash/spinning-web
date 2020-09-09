from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="homepage"),
    path('polls/', include('polls.urls')),
    path('todo/', include('ToDO.urls')),
    path('blog/', include('blog.urls')),
]
