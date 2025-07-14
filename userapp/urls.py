from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'wheel-specifications',WheelSpecificationViewset,basename='wheel-specifications')
router.register(r'bogie-checksheet',BogieCheckSheetViewset,basename='bogie-checksheet')


urlpatterns = [
    path('',include(router.urls)),
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('profile/',UserProfileView.as_view(),name='profile'),
    path('users/',AllUserView.as_view(),name='users')
]
