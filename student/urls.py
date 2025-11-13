from django.urls import path
from student.views import add_student,edit_student,delete_student,Student_list
urlpatterns=[
    path('',Student_list,name='student_list'),
    path('add/',add_student,name='add_student'),
    path('edit/<int:id>/',edit_student,name='edit_student'),
    path('delete/<int:id>/',delete_student,name='delete_student')
]