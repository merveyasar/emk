from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('organizasyonlar/sb/', views.sb, name='sb'),
    path('organizasyonlar/kale/', views.kale, name='kale'),
    path('organizasyonlar/sirket-gunleri/', views.sirket_gunleri, name='sirket_gunleri'),
    path('organizasyonlar/teknik-gezi/', views.teknik_gezi, name='teknik_gezi'),
    path('organizasyonlar/egitim-seminerleri/', views.egitim_seminerleri, name='egitim_seminerleri'),
    path('organizasyonlar/gdkg/', views.gdkg, name='gdkg'),
    path('organizasyonlar/col/', views.col, name='col'),
    path('organizasyonlar/mentorship/', views.mentorship, name='mentorship'),
    
    path('editor/get-org-event/<int:pk>/', views.get_org_event, name='get_org_event'),
    
    # Ekle (pk olmadan)
    path('editor/save-org-event/', views.save_org_event, name='add_org_event'),
    
    # Güncelle (pk ile)
    path('editor/save-org-event/<int:pk>/', views.save_org_event, name='update_org_event'),
    
    # Sil
    path('editor/delete-org-event/<int:pk>/', views.delete_org_event, name='delete_org_event'),
    
    path('hakkimizda/', views.hakkimizda, name='hakkimizda'), 
    path('ekibimiz/', views.ekibimiz, name='ekibimiz'), 
    path('editor/add-member/', views.add_member, name='add_member'),
    path('editor/get-member/<int:pk>/', views.get_member_detail, name='get_member_detail'),
    path('editor/delete-member/<int:pk>/', views.delete_member, name='delete_member'),
    path('editor/update-member/<int:pk>/', views.update_member, name='update_member'),

    path('edergi/', views.edergi, name='edergi'),
    
    # Dergi İşlemleri
    path('editor/get-magazine/<int:pk>/', views.get_magazine, name='get_magazine'),
    path('editor/update-magazine/<int:pk>/', views.update_magazine, name='update_magazine'),
    path('editor/add-magazine/', views.add_magazine, name='add_magazine'),
    
    path('iletisim/', views.iletisim, name='iletisim'),
    path('tuzuk/', views.tuzuk, name='tuzuk'),
    
    path('editor/universal-save/', views.universal_save, name='universal_save'),
    
    
]