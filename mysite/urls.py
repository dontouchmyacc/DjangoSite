
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# from .news.views import ArticlesAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('news/', include('news.urls')),
    # path('api/v1/newslist/', ArticlesAPIView.as_view()),
    path('valute/', include('valute.urls')),
    path('accounts/', include('allauth.urls'))
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
