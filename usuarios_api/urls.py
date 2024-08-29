from django.urls import path, include
from rest_framework.routers import DefaultRouter
from usuarios_api import views


router = DefaultRouter()
router.register('users', views.UserProfileViewSet)
router.register('subjects', views.SubjectViewSet)
router.register('assignments', views.AssignmentViewSet)
router.register('grades', views.GradeViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
