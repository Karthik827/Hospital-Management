"""hospital_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from hospital_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="home"),
    path("contact/",views.contact,name="contact"),
    path("about/",views.about,name="about"),
    path('admin_login/',views.Login,name="login"),
    path("dashboard/",views.Index,name="dashboard"),
    path("admin_logout",views.logout_admin,name="admin_logout"),
    path("view_doctor/",views.View_doctor,name="viewdoctor"),
    path("delete_doctor(p?<int:pid>)/",views.delete_doctor,name="delete_doctor"),
    path("add_doctor/",views.add_doctor,name="add_doctor"),
    path("view_patient/",views.View_patient,name="viewpatient"),
    path("delete_patient(p?<int:pid>)/",views.delete_patient,name="delete_patient"),
    path("add_patient/",views.add_patient,name="add_patient"),
    path("view_appointment/",views.view_appointment,name="view_appointment"),
    path("delete_appointment(p?<int:pid>)/",views.delete_appointment,name="delete_appointment"),
    path("add_appointment/",views.add_appointment,name="add_appointment"),

]
