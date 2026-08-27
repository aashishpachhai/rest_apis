from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('employee',views.EmployeeViewset,basename='employee')

urlpatterns=[
    path('person/',views.person),
    path('person/<int:id>',views.getPerson),
    path('student/',views.Student.as_view()),
    path('student/<int:id>',views.StudentDetails.as_view()),
    path('car/',views.Cars.as_view()),
    path('car/<int:id>',views.CarDetail.as_view()),
    path('house/',views.Houses.as_view()),
    path('house/<int:id>',views.HouseDetail.as_view()),
    path('',include(router.urls))
]