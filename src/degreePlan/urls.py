"""degreePlan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

#here is where we import the urls that we have created
from degrees.views import allDegreesView, degreeClassesView, degreeTimeline, addADegree, editDegree
from transferCredits.views import transferCreditView, addTransferCredit
from home.views import homeView

#make sure to add the path to the to the url patters below
#**** don't forget the comma !!!
urlpatterns = [
    path('', homeView),
    path('admin/', admin.site.urls),
    path('degrees/', allDegreesView, name='degrees'),
    path('degree/', degreeClassesView, name='degreePlan'),
    path('timeline/', degreeTimeline, name='timeline'),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('transferCreditList/', transferCreditView, name='transferCreditList'),
    path('addDegree/', addADegree, name="addDegree"),
    path('editDegree/', editDegree, name="editDegree"),
    #path('degrees/', allDegreesView, name='transferCreditList')
    path('addTransferCredit/', addTransferCredit, name="addTransferCredit"),

]

