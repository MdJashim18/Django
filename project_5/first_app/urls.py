from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = "homepage"),
    path('about/', views.about, name = "aboutpage"),
    path('submit_form/', views.submit_form, name = "submit_form"),
    path('DjangoForm/', views.DjangoForm, name = "DjangoForm"),
    path('StudentForm/', views.student_form_view, name="StudentForm"),
    path('passwordValidationProject/', views.passwordValidation, name="passwordValidationProject"),
]