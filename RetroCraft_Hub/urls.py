"""
URL configuration for RetroCraft_Hub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from. import views
from producer import views as views2
from freelancer import views as views3

urlpatterns = [
    ### common functions
    path('admin/', admin.site.urls),
    # path("producer/",include('producer.urls')),
    path("",views.login,name="login"),
    path("signup/",include("authentication.urls")),
    path("home/",views.home,name="home"),
    path("home/<id>",views.homeview,name="homeview"),
    path("notifications/",views.notifications,name="notifications"),

    
    ### All Recruiter's functionalities
    path("newjob/",views2.newjob,name="new_job"),
    path("deletejob/<id>/",views2.delete_job,name="deletejob"),
    path("editprofile/",views2.edit_profile,name="editprofile"),
    path("jobpage/<id>/",views2.jobpage,name="jobpage"),
    path("freelancerlist/",views2.freelancer_list,name="freelancerlist"),
    
    
    
    ### All Freelancer's functionalities
    path("joblist/",views3.job_list,name="joblist"),
    path("jobviewpage/<id>/",views3.jobviewpage,name="jobviewpage"),
    path("interest/<id>/",views3.addinterest,name="addinterest"),
    path("leavejob/<id>/",views3.leavejob,name="leavejob"),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        
urlpatterns += staticfiles_urlpatterns()



