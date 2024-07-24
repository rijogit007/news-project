from django.urls import path
from django.contrib import admin
from newsapp import views
from django.conf import settings
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # path('admin/', admin.site.urls),
    path('',views.Home.as_view(),name='home_view'),
    path('reg', views.Userregistrationview.as_view(),name='reg_view'),
    path('log',views.UserLoginview.as_view(),name='login_view' ),
    path('cat', views.CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', views.NewsListView.as_view(), name='news_list'),
    path('article/<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)