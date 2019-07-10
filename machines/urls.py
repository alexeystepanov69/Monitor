from django.conf.urls import url, include
from django.urls import path
from . import views
from machines import views
from rest_framework import routers
from .views import RawDataViewSet, EquipmentWorksDetailView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'^api/rawdata', RawDataViewSet, base_name='RawData')

urlpatterns = [
                  url(r'^$', views.EqipmentFilteredListView.as_view(), name='equipment-list'),
				  url(r'^accounts/', include('django.contrib.auth.urls')),
				  url(r'^newdata/', views.RawDataUploadView.as_view()),
                  url(r'graph', views.APIGraphData.as_view(), name='graph-data'),
				  url(r'^register/$', views.register, name='register'),
				  url(r'^edit/$', views.edit, name='edit'),
                  path('works/<int:pk>/', views.EquipmentWorksDetailView.as_view(), name='works-detail'),
              ] + router.urls
