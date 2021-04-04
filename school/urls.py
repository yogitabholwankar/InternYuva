from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	# path('account/', include('accounts.urls')),
 #    path('', include('dprocess.urls')),
	# path('', include('classroom.urls')),
	path('accounts/', include('accounts.urls')),
    path('', include('dprocess.urls')),
	path('', include('classroom.urls')),
	path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)