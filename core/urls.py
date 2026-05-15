from django.urls import path
from . import views

urlpatterns = [
    
    path('organizasyonlar/sb/', views.sb, name='sb'),
    path('organizasyonlar/kale/', views.kale, name='kale'),
    path('organizasyonlar/sirket-gunleri/', views.sirket_gunleri, name='sirket_gunleri'),
    path('organizasyonlar/teknik-gezi/', views.teknik_gezi, name='teknik_gezi'),
    path('organizasyonlar/egitim-seminerleri/', views.egitim_seminerleri, name='egitim_seminerleri'),
    path('organizasyonlar/gdkg/', views.gdkg, name='gdkg'),
    path('organizasyonlar/col/', views.col, name='col'),
    path('organizasyonlar/mentorship/', views.mentorship, name='mentorship'),
    
    path('editor/get-all-mentors/', views.get_all_mentors, name='get_all_mentors'),
    path('editor/get-mentor/<int:pk>/', views.get_mentor_detail, name='get_mentor_detail'),
    path('editor/add-mentor/', views.add_mentor, name='add_mentor'),
    path('editor/update-mentor/<int:pk>/', views.update_mentor, name='update_mentor'),
    path('editor/delete-mentor/<int:pk>/', views.delete_mentor, name='delete_mentor'),
    
    
    path('editor/get-all-archives/<slug:slug>/', views.get_all_archives, name='get_all_archives'),
    path('editor/get-archive/<int:pk>/', views.get_archive_detail, name='get_archive_detail'),
    path('editor/save-archive/', views.save_archive, name='add_archive'),
    path('editor/save-archive/<int:pk>/', views.save_archive, name='update_archive'),
    path('editor/delete-archive/<int:pk>/', views.delete_archive, name='delete_archive'),
    
    path('', views.dashboard, name='dashboard'),
    
    path('editor/get-all-announcements/', views.get_all_announcements, name='get_all_announcements'),
    path('editor/get-announcement/<int:pk>/', views.get_announcement, name='get_announcement'),
    path('editor/add-announcement/', views.add_announcement, name='add_announcement'),
    path('editor/update-announcement/<int:pk>/', views.update_announcement, name='update_announcement'),
    path('editor/delete-announcement/<int:pk>/', views.delete_announcement, name='delete_announcement'),


    path('editor/get-all-sponsors/', views.get_all_sponsors, name='get_all_sponsors'),
    path('editor/add-sponsor/', views.add_sponsor, name='add_sponsor'),
    path('editor/delete-sponsor/<int:pk>/', views.delete_sponsor, name='delete_sponsor'),

    path('edergi/', views.edergi, name='edergi'),
    path('editor/get-magazine/<int:pk>/', views.get_magazine, name='get_magazine'),
    path('editor/update-magazine/<int:pk>/', views.update_magazine, name='update_magazine'),
    path('editor/add-magazine/', views.add_magazine, name='add_magazine'),
    path('editor/delete-magazine/<int:pk>/', views.delete_magazine, name='delete_magazine'),
    
    path('ekibimiz/', views.ekibimiz, name='ekibimiz'), 
    path('editor/add-member/', views.add_member, name='add_member'),
    path('editor/get-member/<int:pk>/', views.get_member_detail, name='get_member_detail'),
    path('editor/delete-member/<int:pk>/', views.delete_member, name='delete_member'),
    path('editor/update-member/<int:pk>/', views.update_member, name='update_member'),

    path('hakkimizda/', views.hakkimizda, name='hakkimizda'), 
    path('iletisim/', views.iletisim, name='iletisim'),
    path('tuzuk/', views.tuzuk, name='tuzuk'),
    
    path('editor/universal-save/', views.universal_save, name='universal_save'),
    
    
]