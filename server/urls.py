from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from meals import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'clients', views.ClientProfileViewSet)
router.register(r'client-conditions', views.ClientMedicalConditionViewSet)
router.register(r'client/checkins', views.ClientCheckinViewSet)
router.register(r'trainers', views.TrainerProfileViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'meals', views.MealViewSet)
router.register(r'foods', views.FoodViewSet)
router.register(r'inventory', views.FoodInventoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    #path('clients/', client_list, name='client-list'),
    #path('clients/<int:pk>/', client_detail, name='client-detail'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)