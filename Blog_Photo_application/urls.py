
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Blog_Photo_App.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# from django.conf.urls import url
# # from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.views.static import serve

# # Serve static and media files from development server
# # urlpatterns += staticfiles_urlpatterns()
# urlpatterns += url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
# urlpatterns += url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),