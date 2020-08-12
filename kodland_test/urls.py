from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from article.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    	path('article/<int:id>',article_detail,name='article_detail'),
  	  	path('', HomePageView.as_view(), name='home_page'),
        path('article/add/', AddArticleView.as_view(), name='add_article'),]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)