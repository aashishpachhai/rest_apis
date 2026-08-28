from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('employee',views.EmployeeViewset,basename='employee')
router.register('emp',views.EmployeesViewSet,basename='emp')

urlpatterns=[
    path('person/',views.person),
    path('person/<int:id>',views.getPerson),
    path('student/',views.Student.as_view()),
    path('student/<int:id>',views.StudentDetails.as_view()),
    path('car/',views.Cars.as_view()),
    path('car/<int:id>',views.CarDetail.as_view()),
    path('house/',views.Houses.as_view()),
    path('house/<int:id>',views.HouseDetail.as_view()),
    path('',include(router.urls)),
    path('blogs/',views.BlogsView.as_view()),
    path('comments/',views.CommentsView.as_view()),
    path('blogs/<int:pk>',views.BlogsViewDetails.as_view()),
    path('comments/<int:pk>',views. CommentsViewDetails.as_view())
]


