"""clinik URL Configuration

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
from django.urls import path
from app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('patientadd/',views.patientadd,name='patientadd'),
    path('patientdetails/',views.patientdetails,name='patientdetails'),
    path('delete<int:id>/',views.pdelete,name='pdelete'),
    path('pupdate<int:id>/', views.pupdate,name='update'),


    path('medicineadd/',views.medicineadd,name='medicineadd'),
    path('medicinedetails/',views.medicinedetails,name='medicinedetails'),
    path('mdelete<int:id>/',views.mdelete,name='mdelete'),
    path('mupdate<int:id>/', views.mupdate,name='mupdate'),


    path('rprint/', views.receiptprint,name='rprint'),
    path('bill/', views.billprint,name='bill'),
    path('printrecipt/', views.print,name='receipt'),
    path('history/', views.history,name='history'),





    path('searchp/', views.search_patient,name='searchp'),
    path('searchm/', views.search_medicine,name='searchm'),
    path('searchb/', views.search_bloodcamp,name='searchb'),
    path('searchn/', views.search_notes,name='searchn'),
    path('searchcp/', views.search_criticalpatient,name='searchcp'),
    path('searchh/', views.pres_history,name='searchh'),



    path('bd/', views.blood,name='bd'),
    path('bd1/', views.bddetails,name='bd1'),
    path('bdelete<int:id>/',views.bdelete,name='bdelete'),
    path('bupdate<int:id>/', views.bupdate,name='updateb'),


    path('notes/',views.note,name='notes'),
    path('addnotes/',views.add_note,name='addnotes'),
    path('ndelete<int:id>/',views.ndelete,name='ndelete'),
    path('nupdate<int:id>/', views.nupdate,name='nupdate'),

    

    path('cpatientadd/',views.criticalpatientadd,name='cpatientadd'),
    path('cpatientdetails/',views.criticalpatientdetails,name='cpatientdetails'),
    path('cpdelete<int:id>/',views.cpdelete,name='cpdelete'),
    path('cpupdate<int:id>/', views.cpupdate,name='cpupdate'),


]
