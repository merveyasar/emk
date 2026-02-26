from django.urls import path
from . import views

urlpatterns = [
    path('/', views.dashboard, name='dashboard'),
    path('organizasyonlar/sb/', views.sb, name='sb'),
    path('organizasyonlar/kale/', views.kale, name='kale'),
    path('organizasyonlar/sirket-gunleri/', views.sirket_gunleri, name='sirket_gunleri'),
    path('organizasyonlar/teknik-gezi/', views.teknik_gezi, name='teknik_gezi'),
    path('organizasyonlar/egitim-seminerleri/', views.egitim_seminerleri, name='egitim_seminerleri'),
    path('organizasyonlar/gdkg/', views.gdkg, name='gdkg'),
    path('organizasyonlar/col/', views.col, name='col'),
    path('organizasyonlar/mentorship/', views.mentorship, name='mentorship'),
    path('hakkimizda/', views.hakkimizda, name='hakkimizda'), 
    path('ekibimiz/', views.ekibimiz, name='ekibimiz'), 
    path('edergi/', views.edergi, name='edergi'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('tuzuk/', views.tuzuk, name='tuzuk'),
]