"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from students import views
from group import views as group_views
from teachers import views as teachers_views



urlpatterns = [
    path('admin/', admin.site.urls),
    # students
    path('', views.index),
    path('students/', views.get_students),
    path('students/<int:student_id>/', views.get_student),
    path('students/create/<int:age>/', views.create_students),
    path('students/generate_students/', views.generate_students),
    # groups
    path('groups/', group_views.get_groups),
    # teacher
    path('teachers/', teachers_views.get_teachers),

]

