from django.conf.urls import url, include
from django.urls import path
from . import views
from machines import views
from rest_framework import routers
from .views import RawDataViewSet, EquipmentWorksDetailView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'^api/rawdata', RawDataViewSet, base_name='RawData')

urlpatterns = [
                  url(r'^$', views.EqipmentFilteredListView.as_view(), name='equipment-list'),
				  url(r'^accounts/', include('django.contrib.auth.urls')),
				  url(r'^newdata/', views.RawDataUploadView.as_view()),
                  url(r'graph', views.APIGraphData.as_view(), name='graph-data'),
				  url(r'^register/$', views.register, name='register'),
				  url(r'^edit/$', views.edit, name='edit'),
				  url(r'^validate/$', views.validate, name='validate'),
				  url(r'^not_validate/$', views.not_validate, name='not_validate'),
				  url(r'^validate_phone/$', views.validate_phone, name='validate_phone'),
                  path('works/<int:pk>/', views.EquipmentWorksDetailView.as_view(), name='works-detail'),
              ] + router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)