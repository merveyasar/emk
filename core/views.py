from django.shortcuts import render
from .models import OrganizationEvent, TeamMember,PageContent,Magazine, Announcement
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

def dashboard(request):
    content, _ = PageContent.objects.get_or_create(path='/')
    latest_announcement = Announcement.objects.filter(is_active=True).first()
    
    # Tüm organizasyonların aktiflik durumunu modelden çekiyoruz
    # Sidebar'dan bir OrganizationEvent'i "is_active=True" yaptığında burası otomatik güncellenir
    active_orgs = OrganizationEvent.objects.filter(is_active=True).values_list('type', flat=True)
    
    return render(request, 'core/dashboard.html', {
        'page_data': content.data,
        'announcement': latest_announcement,
        'active_orgs': list(active_orgs) # ['KALE', 'COL', 'SG'...] şeklinde döner
    })

def sb(request):
    # Sayfa genel içerikleri (Başlıklar, Sayaç Tarihi, İstatistikler)
    content, _ = PageContent.objects.get_or_create(path=request.path)
    
    # Tüm SB Etkinlikleri (Arşiv Galerisi için)
    # extra_data içinde: {"sectors": ["Otomotiv", "FMCG"], "gallery": ["url1", "url2"]}
    sb_archives = OrganizationEvent.objects.filter(type='SB').order_by('-year')
    
    # Şu anki aktif SB (is_active=True olan)
    active_sb = sb_archives.filter(is_active=True).first()

    return render(request, 'core/organizasyonlar/sb.html', {
        'page_data': content.data,
        'active_sb': active_sb,
        'archives': sb_archives,
    })
def kale(request):
    content, _ = PageContent.objects.get_or_create(path=request.path)
    
    # Tüm KALE Etkinlikleri (Yıl bazlı arşiv için)
    # extra_data içinde: {"slogan": "...", "images": ["url1", "url2"]}
    kale_archives = OrganizationEvent.objects.filter(type='KALE').order_by('-year')
    
    # Şu anki aktif KALE (is_active=True olan)
    active_kale = kale_archives.filter(is_active=True).first()

    return render(request, 'core/organizasyonlar/kale.html', {
        'page_data': content.data,
        'active_kale': active_kale,
        'archives': kale_archives,
    })

def sirket_gunleri(request):
    # Sayfa genel ayarları (Hero metni, Sayaç Tarihi vb.)
    content, _ = PageContent.objects.get_or_create(path=request.path)
    
    # Tüm Şirket Günleri Arşivi (SG Tipi)
    # extra_data: {"logos": ["url1", "url2"], "stat_firms": "45+", "stat_visitors": "2500+"}
    sg_archives = OrganizationEvent.objects.filter(type='SG').order_by('-year')
    
    # Şu anki aktif Şirket Günleri
    active_sg = sg_archives.filter(is_active=True).first()

    return render(request, 'core/organizasyonlar/sirket_gunleri.html', {
        'page_data': content.data,
        'active_sg': active_sg,
        'archives': sg_archives,
    })
    
def teknik_gezi(request):
    # Sayfa genel ayarları (Hero metni, İstatistikler)
    content, _ = PageContent.objects.get_or_create(path=request.path)
    
    # Tüm Teknik Gezi Dönemleri (TG Tipi)
    # extra_data: {"factories": [{"name": "Hyundai", "desc": "...", "img": "..."}], "next_trip": "Ford Otosan"}
    tg_archives = OrganizationEvent.objects.filter(type='TG').order_by('-year')
    
    # Şu anki aktif gezi periyodu
    active_tg = tg_archives.filter(is_active=True).first()

    return render(request, 'core/organizasyonlar/teknik_gezi.html', {
        'page_data': content.data,
        'active_tg': active_tg,
        'archives': tg_archives,
    })
    
def egitim_seminerleri(request):
    # Sayfa genel ayarları (Başlıklar, Görseller vb.)
    content, _ = PageContent.objects.get_or_create(path=request.path)
    
    # Tüm Eğitimler (OrganizationEvent modelinden ES tipi)
    # is_active olanlar 'Kayıtları Açık' olarak en üstte görünür
    all_trainings = OrganizationEvent.objects.filter(type='ES').order_by('-is_active', '-year')

    return render(request, 'core/organizasyonlar/egitim_seminerleri.html', {
        'page_data': content.data,
        'trainings': all_trainings
    })

def gdkg(request):

    content, _ = PageContent.objects.get_or_create(path=request.path)
    
    # Kütüphane Arşivi (OrganizationEvent modelinden GDKG tipi)
    # extra_data içinde: {"city": "Mardin", "summary": "...", "img_url": "..."}
    libraries = OrganizationEvent.objects.filter(type='GDKG').order_by('-year')

    return render(request, 'core/organizasyonlar/gdkg.html', {
        'page_data': content.data,
        'libraries': libraries
    })

def col(request):
    # Sayfa genel içerikleri (Sayaç tarihi, Başvuru URL vb.)
    content, _ = PageContent.objects.get_or_create(path=request.path)
    
    # Arşiv verileri (OrganizationEvent modelinden COL tipindeki her şey)
    archive_events = OrganizationEvent.objects.filter(type='COL').order_by('-year')
    
    # Şu anki aktif yarışma (is_active=True olan)
    active_event = archive_events.filter(is_active=True).first()

    return render(request, 'core/organizasyonlar/col.html', {
        'page_data': content.data,
        'active_event': active_event,
        'archive_events': archive_events,
    })
    
    
def mentorship(request):
    content, _ = PageContent.objects.get_or_create(path=request.path)
    
    # Mentorship dönemleri (2024 Güz, 2025 Bahar vb.)
    # extra_data içinde mentör listesini tutacağız: {"mentors": [{"name": "...", "job": "..."}]}
    mentorship_periods = OrganizationEvent.objects.filter(type='MENT').order_by('-year')
    
    # Şu an başvuruya açık olan dönem
    active_period = mentorship_periods.filter(is_active=True).first()

    return render(request, 'core/organizasyonlar/mentorship.html', {
        'page_data': content.data,
        'active_period': active_period,
        'periods': mentorship_periods
    })

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import OrganizationEvent
import json

# 1. Veri Çekme (Edit Formu İçin)
def get_org_event(request, pk):
    event = get_object_or_404(OrganizationEvent, pk=pk)
    return JsonResponse({
        "id": event.id,
        "type": event.type,
        "year": event.year,
        "title": event.title,
        "extra_data": event.extra_data, # JSON verisi (winner, summary vb.)
        "is_active": event.is_active
    })

# 2. Ekleme ve Güncelleme (Hibrit View)
@csrf_exempt
def save_org_event(request, pk=None):
    if request.method == 'POST':
        try:
            # Eğer pk varsa güncelle, yoksa yeni oluştur
            if pk:
                event = get_object_or_404(OrganizationEvent, pk=pk)
            else:
                event = OrganizationEvent()

            # Temel Alanlar
            event.type = request.POST.get('type', event.type)
            event.year = request.POST.get('year', event.year)
            event.title = request.POST.get('title', event.title)
            event.is_active = request.POST.get('is_active') == 'true'

            # Dinamik JSON Verisi (Winner, Summary vb.)
            # Sidebar'dan gelen extra_data string'ini parse ediyoruz
            extra_json = request.POST.get('extra_data', '{}')
            event.extra_data = json.loads(extra_json)

            event.save()
            return JsonResponse({"status": "success", "id": event.id})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
    return JsonResponse({"status": "error", "message": "Geçersiz metod"})

# 3. Silme İşlemi
@csrf_exempt
def delete_org_event(request, pk):
    if request.method == 'POST':
        event = get_object_or_404(OrganizationEvent, pk=pk)
        event.delete()
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error"})


def hakkimizda(request):
    # Bu URL için PageContent kaydını getir veya yoksa oluştur
    content, created = PageContent.objects.get_or_create(path=request.path)
    
    # Template'e 'page_data' olarak JSON içeriğini gönderiyoruz
    return render(request, 'core/hakkimizda.html', {
        'page_data': content.data
    })
    
def ekibimiz(request):
    # 1. Mevcut URL yoluna göre (örn: /ekibimiz/) kaydı getir veya yoksa oluştur
    # 'path' modelimizde tanımladığımız alan adı
    content, created = PageContent.objects.get_or_create(path=request.path)
    
    # 2. Üyeleri çek (Sıralama modelde 'order' olarak tanımlıysa otomatik sıralar)
    members = TeamMember.objects.all().order_by('order', 'name')
    
    # 3. 'content.data' içindeki JSON verisini ve üyeleri template'e gönder
    return render(request, 'core/ekibimiz.html', {
        'page_data': content.data, # JSON olan içerik (Başlık, alt metin vb.)
        'members': members,
        'content': content # Gerekirse path vb. bilgiler için objenin kendisi
    })

def get_member_detail(request, pk):
    member = get_object_or_404(TeamMember, pk=pk)
    return JsonResponse({
        'name': member.name,
        'title': member.title,
        'rank': member.rank,
        'team': member.team,
        'order': member.order,
        'image_url': member.image.url
    })

def update_member(request, pk):
    if request.method == 'POST':
        member = get_object_or_404(TeamMember, pk=pk)
        member.name = request.POST.get('name')
        member.title = request.POST.get('title')
        member.rank = request.POST.get('rank')
        member.team = request.POST.get('team')
        member.order = request.POST.get('order')
        
        if 'image' in request.FILES:
            member.image = request.FILES['image']
            
        member.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

def add_member(request):
    if request.method == 'POST':
        new_member = TeamMember.objects.create(
            name=request.POST.get('name'),
            title=request.POST.get('title'),
            rank=request.POST.get('rank'),
            team=request.POST.get('team'),
            order=request.POST.get('order', 0),
            image=request.FILES.get('image', 'team/default.png')
        )
        return JsonResponse({'status': 'success', 'id': new_member.id})
    return JsonResponse({'status': 'error'}, status=400)

def delete_member(request, pk):
    if request.method == 'POST':
        member = get_object_or_404(TeamMember, pk=pk)
        member.delete()
        return JsonResponse({'status': 'success'})    

from .models import Magazine

def edergi(request):
    magazines = Magazine.objects.filter(is_active=True)
    latest_mag = magazines.first() # ordering sayesinde en günceli verir
    archive = magazines[1:] if magazines.count() > 1 else [] # İlk hariç diğerleri arşivdir
    
    # Arşivdeki yılları filtreler (Frontend'deki butonlar için)
    years = magazines.dates('release_date', 'year', order='DESC')

    return render(request, 'core/edergi.html', {
        'latest': latest_mag,
        'archive': archive,
        'years': [y.year for y in years]
    })
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import PageContent, TeamMember, Magazine
import json

# --- MODEL BAZLI İŞLEMLER (Magazine / Member) ---

def get_magazine(request, pk):
    """Dergi verilerini JSON olarak döndürür"""
    mag = get_object_or_404(Magazine, pk=pk)
    data = {
        "title": mag.title,
        "issue_number": mag.issue_number,
        "description": mag.description,
        "read_link": mag.read_link,
        "cover_url": mag.cover_image.url if mag.cover_image else ""
    }
    return JsonResponse(data)

@csrf_exempt
def update_magazine(request, pk):
    """Dergi verilerini günceller"""
    if request.method == 'POST':
        mag = get_object_or_404(Magazine, pk=pk)
        mag.title = request.POST.get('title', mag.title)
        mag.issue_number = request.POST.get('issue_number', mag.issue_number)
        mag.description = request.POST.get('description', mag.description)
        mag.read_link = request.POST.get('read_link', mag.read_link)

        if 'cover_image' in request.FILES:
            mag.cover_image = request.FILES['cover_image']
        
        mag.save()
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error", "message": "Geçersiz istek"})


@csrf_exempt
def add_magazine(request):
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            issue_number = request.POST.get('issue_number')
            release_date = request.POST.get('release_date')
            description = request.POST.get('description')
            read_link = request.POST.get('read_link')
            cover_image = request.FILES.get('cover_image')

            new_mag = Magazine.objects.create(
                title=title,
                issue_number=issue_number,
                release_date=release_date,
                description=description,
                read_link=read_link,
                cover_image=cover_image
            )
            return JsonResponse({"status": "success", "id": new_mag.id})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
    return JsonResponse({"status": "error", "message": "Sadece POST isteği kabul edilir."})

def iletisim(request):
    # Bu path (/iletisim/) için veriyi getir veya oluştur
    content, created = PageContent.objects.get_or_create(path=request.path)
    return render(request, 'core/iletisim.html', {
        'page_data': content.data
    })

def tuzuk(request):
    content, created = PageContent.objects.get_or_create(path=request.path)
    # Maddeleri JSON içinden 'articles' anahtarıyla çekeceğiz
    # Eğer boşsa varsayılan 2-3 maddeyi biz tanımlayalım
    articles = content.data.get('articles', [
        {"title": "MADDE 1: Kulübün Adı", "content": "Kulübün adı Kocaeli Üniversitesi..."},
        {"title": "MADDE 2: Amacı", "content": "Endüstri Mühendisliği gelişimine..."}
    ])
    return render(request, 'core/tuzuk.html', {
        'page_data': content.data,
        'articles': articles
    })


import json
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import PageContent

@require_POST
def universal_save(request):
    path = request.POST.get('path') # Sayfanın adresi
    raw_data = request.POST.get('data') # Sayfadaki tüm editable alanlar
    
    try:
        json_data = json.loads(raw_data)
        
        # Bu path için kayıt varsa güncelle, yoksa yeni oluştur
        content, created = PageContent.objects.update_or_create(
            path=path,
            defaults={'data': json_data}
        )
        
        
        print(f"{'Oluşturuldu' if created else 'Güncellendi'}: {path} -> {json_data}")

        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    
    