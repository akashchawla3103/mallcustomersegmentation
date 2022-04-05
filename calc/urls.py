from django.urls import path
from . import views
from  akash import settings
from django.conf.urls.static import static

urlpatterns = [
   path('',views.index, name='index'),
    path('aut_user',views.aut_user, name='aut_user'),
    path('home',views.home, name='home'),
    path('check',views.check, name='check'),
    path('upload',views.upload,name='upload'),
    path('cleandata',views.cleandata,name='cleandata'),
    path('segmentdata',views.segmentdata,name='segmentdata'),
    path('send_email',views.send_email,name='send_email'),
    path('mail_page',views.mail_page,name='mail_page'),
    path('analytics',views.analytics,name='analytics'),
    path('offer',views.offer,name='offer'),
    path('logoutUser',views.logoutUser,name='logoutUser'),
    path('segment_email',views.segment_email,name='segment_email'),
    path('seg_generate_rand',views.seg_generate_rand,name='seg_generate_rand'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
 