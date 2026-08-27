from django.urls import path
from . import views
urlpatterns=[
    path('person/',views.person),
    path('person/<int:id>',views.getPerson),
    path('student/',views.Student.as_view()),
    path('student/<int:id>',views.StudentDetails.as_view()),
    path('car/',views.Cars.as_view()),
     path('car/<int:id>',views.CarDetail.as_view())
]