# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('home/', views.home, name='home'),
#     path('show/', views.list_students, name='show'),
#     path('edit/', views.edit_students, name='edit'),
#     path('delete/', views.delete_students, name='delete'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # تغيير من index إلى home
    path('index/', views.index, name='index'),  # إضافة هذا إذا كنت تريد الاحتفاظ بصفحة index
    path('show/', views.list_students, name='show'),
    path('add/', views.add_student, name='add'),
    path('edit/<int:student_id>/', views.edit_student, name='edit'),
    path('delete/<int:student_id>/', views.delete_student, name='delete'),
    path('highlight-demo/', views.highlight_demo, name='highlight_demo'),
]