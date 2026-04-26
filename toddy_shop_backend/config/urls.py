from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Toddy Shop Administration"
admin.site.index_title = "Apps and Services"
admin.site.site_title = "Toddy Shop"


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/v1/",
        include(
            [
                path("", include("core.urls"), name="core"),
                path("", include("shops.urls"), name="shops"),
            ]
        ),
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
