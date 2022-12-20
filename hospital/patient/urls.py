from django.urls import path
from.import views
urlpatterns=[
    path('',views.home,name='hm'),
    path('Booking',views.booking,name='bk'),
    path('Make an Appointment',views.departments,name='dpt'),
    path('About Us',views.about,name='abt'),
    path('Cancellation Policy',views.cancellation,name='cp'),
    path('CARDIOLOGY',views.cardiology,name='crd'),
    
    path('contactus',views.contactus,name='con'),
    path('dentalsurgery',views.dentalsurgery,name='dts'),
    path('Doctors',views.doctors,name='doct'),
    path('Department',views.departments,name='dpt'),
    path('emergencymedicine',views.emergencymedicine,name='em'),
    path('ENT',views.ent,name='ent'),
   
    
    path('Generalmedicine',views.generalmedicine,name='gm'),
    path('Privacy Policy',views.privacypolicy,name='pp'),
    path('Refund Policy',views.refundpolicy,name='rp'),

    path('Terms & Conditions',views.termsandconditions,name='tc'),
    path('search',views.searching,name='search_u'),

]