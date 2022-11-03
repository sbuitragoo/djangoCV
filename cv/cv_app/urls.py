from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name = 'cv_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('menu', views.menu, name='menu'),
    path('cv', views.complete_cv, name='complete_cv'),
    path('info/personal', views.personal_info, name='personal_info'),
    path('studies', views.studies, name='studies'),
    path('work/experience', views.work_experience, name='work_experience'),
    path('info/additional', views.additional_info, name='additional_info'),
    path('db/fill', views.db_filling, name='db_filling'),
]

urlpatterns += staticfiles_urlpatterns()
