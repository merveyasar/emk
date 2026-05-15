import json
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.files.storage import default_storage

from .models import (
    OrganizationEvent, OrganizationArchive, 
    TeamMember, PageContent, Magazine, 
    Announcement, Sponsor, Mentor
)

def sb(request):
    event, _ = OrganizationEvent.objects.get_or_create(
        slug='sb', 
        defaults={'name': 'Sektöre Büyüteç', 'description': 'SB Etkinlik Açıklaması'}
    )
    content, _ = PageContent.objects.get_or_create(path=request.path)
    
    archives = event.archives.all().order_by('-year')
    # Benzersiz yılları filtreleme menüsü için çekiyoruz
    years = event.archives.values_list('year', flat=True).distinct().order_by('-year')
    
    active_sb = archives.first()
    all_archives = archives # Filtreleme için tüm liste

    return render(request, 'core/organizasyonlar/sb.html', {
        'page_data': content.data,
        'active_sb': active_sb,
        'all_archives': all_archives,
        'years': years,
    })
      
def kale(request):
    event, _ = OrganizationEvent.objects.get_or_create(
        slug='kale', 
        defaults={'name': 'KALE - Liderlik Kampı', 'description': 'Liderlik kampı detayları...'}
    )
    
    content, _ = PageContent.objects.get_or_create(path=request.path)
    
    # KALE'ye ait tüm arşivlenmiş dönemleri çekiyoruz
    archives = event.archives.all().order_by('-year')

    return render(request, 'core/organizasyonlar/kale.html', {
        'page_data': content.data,
        'archives': archives,
    })

def sirket_gunleri(request):
    event, _ = OrganizationEvent.objects.get_or_create(
        slug='sg', 
        defaults={'name': 'Şirket Günleri', 'description': 'Kariyer ve istihdam odaklı dev fuar.'}
    )
    content, _ = PageContent.objects.get_or_create(path=request.path)
    
    # Şirket Günleri arşivleri (Yıllara göre)
    archives = event.archives.all().order_by('-year')
    years = event.archives.values_list('year', flat=True).distinct().order_by('-year')

    return render(request, 'core/organizasyonlar/sirket_gunleri.html', {
        'page_data': content.data,
        'archives': archives,
        'years': years,
    })
    
def teknik_gezi(request):
    event, _ = OrganizationEvent.objects.get_or_create(
        slug='teknik-gezi', 
        defaults={'name': 'Teknik Geziler', 'description': 'Teorik bilginin pratikle buluştuğu saha yolculukları.'}
    )
    content, _ = PageContent.objects.get_or_create(path=request.path)
    
    # Teknik gezi arşivleri
    archives = event.archives.all().order_by('-year')
    years = event.archives.values_list('year', flat=True).distinct().order_by('-year')

    return render(request, 'core/organizasyonlar/teknik_gezi.html', {
        'page_data': content.data,
        'archives': archives,
        'years': years,
    })

def egitim_seminerleri(request):
    # Sayfa genel içerikleri (Hero vs.)
    event, _ = OrganizationEvent.objects.get_or_create(
        slug='egitim-seminerleri', 
        defaults={'name': 'Eğitim ve Seminerler', 'description': 'Eğitim ve seminer etkinliklerimiz.'}
    )
    
    content, _ = PageContent.objects.get_or_create(path=request.path)
    
    # Aktif Duyurular/Eğitimler (Modelin is_active ise filtrele)
    # Burada Announcement modelini veya özel bir Education modelini kullanabilirsin
    egitimler = Announcement.objects.filter(category='EGITIM', is_active=True).order_by('-created_at')

    from datetime import datetime
    bugun = datetime.now().date()
    for edu in egitimler:
        deadline_str = edu.extra_data.get('deadline')
        if deadline_str:
            try:
                # String'i gerçek tarih objesine çeviriyoruz
                deadline_date = datetime.strptime(deadline_str, '%Y-%m-%d').date()
                
                print(f"Deadline: {deadline_date}, Bugün: {bugun}") # Debug için
                edu.is_expired = deadline_date < bugun
            except ValueError:
                # Eğer tarih formatı bozuksa güvenlik için süresi dolmuş sayalım
                edu.is_expired = True
        else:
            # Deadline girilmemişse her zaman açık kalsın
            edu.is_expired = False
    archives = event.archives.all().order_by('-year')
    years = event.archives.values_list('year', flat=True).distinct().order_by('-year')

    return render(request, 'core/organizasyonlar/egitim_seminerleri.html', {
        'page_data': content.data,
        'egitimler': egitimler,
        'archives': archives,
        'years': years,
    })
    
def gdkg(request):
    event, _ = OrganizationEvent.objects.get_or_create(
        slug='gdkg', 
        defaults={'name': 'Gülümseyen Düşler Kitaplardan Geçer', 'description': 'Köy okullarına kütüphane ve umut taşıyan sosyal sorumluluk projesi.'}
    )
    content, _ = PageContent.objects.get_or_create(path=request.path)
    
    # GDKG arşivleri
    archives = event.archives.all().order_by('-year')
    years = event.archives.values_list('year', flat=True).distinct().order_by('-year')

    return render(request, 'core/organizasyonlar/gdkg.html', {
        'page_data': content.data,
        'archives': archives,
        'years': years,
    })

def col(request):
    event, _ = OrganizationEvent.objects.get_or_create(
        slug='col', 
        defaults={'name': 'CaseOfLegends', 'description': 'En prestijli vaka analizi yarışması.'}
    )
    content, _ = PageContent.objects.get_or_create(path=request.path)
    
    archives = event.archives.all().order_by('-year')
    years = event.archives.values_list('year', flat=True).distinct().order_by('-year')

    return render(request, 'core/organizasyonlar/col.html', {
        'page_data': content.data,
        'archives': archives,
        'years': years,
    })

def mentorship(request):
    event, _ = OrganizationEvent.objects.get_or_create(
        slug='menti-mentor', 
        defaults={'name': 'Menti-Mentör Programı', 'description': 'Tecrübenin genç vizyonla buluştuğu gelişim yolculuğu.'}
    )
    content, _ = PageContent.objects.get_or_create(path=request.path)
    
    # Mentör portföyü ve galeri verilerini içeren arşiv nesnelerini çekiyoruz
    archives = event.archives.all().order_by('-year')
    mentors = Mentor.objects.filter(is_active=True).order_by('-id') # Tüm aktif mentörler (son eklenen üstte)

    return render(request, 'core/organizasyonlar/mentorship.html', {
        'page_data': content.data,
        'archives': archives,
        'mentors': mentors,
    })

def get_all_mentors(request):
    """Editör panelindeki listeleme için"""
    mentors = Mentor.objects.all().order_by('-id')
    data = [{
        'id': m.id,
        'name': m.name,
        'company': m.company,
        'title': m.title,
        'image': m.image # URLField olarak tuttuğunu varsayıyorum
    } for m in mentors]
    return JsonResponse(data, safe=False)

def get_mentor_detail(request, pk):
    """Düzenleme formu açıldığında verileri doldurmak için"""
    m = get_object_or_404(Mentor, pk=pk)
    return JsonResponse({
        'id': m.id,
        'name': m.name,
        'company': m.company,
        'title': m.title,
        'image': m.image
    })

@csrf_exempt
@require_POST
def add_mentor(request):
    try:
        Mentor.objects.create(
            name=request.POST.get('name'),
            company=request.POST.get('company'),
            title=request.POST.get('title'),
            image=request.FILES.get('image') # URL değil, dosya objesi aldık
        )
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})

@csrf_exempt
@require_POST
def update_mentor(request, pk):
    try:
        m = get_object_or_404(Mentor, pk=pk)
        m.name = request.POST.get('name')
        m.company = request.POST.get('company')
        m.title = request.POST.get('title')
        
        # Eğer yeni bir görsel seçildiyse güncelle
        if 'image' in request.FILES:
            m.image = request.FILES['image']
            
        m.save()
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})
    
@csrf_exempt
@require_POST
def delete_mentor(request, pk):
    """Mentör Silme"""
    try:
        m = get_object_or_404(Mentor, pk=pk)
        m.delete()
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})
  

def get_all_archives(request, slug):
    
    events = OrganizationEvent.objects.all()
    print([event.slug for event in events]) # Debug: Organizasyon etkinliklerini kontrol et
    # Belirli bir organizasyonun tüm yıllarını getirir
    event = get_object_or_404(OrganizationEvent, slug=slug)
    archives = event.archives.all().order_by('-year')
    data = [{
        'id': a.id,
        'year': a.year,
        'motto': a.motto,
        'cover_url': a.cover_image.url if a.cover_image else None
    } for a in archives]
    return JsonResponse(data, safe=False)

def get_archive_detail(request, pk):
    a = get_object_or_404(OrganizationArchive, pk=pk)
    return JsonResponse({
        'id': a.id,
        'year': a.year,
        'motto': a.motto,
        'description': a.description,
        'extra_data': a.extra_data, # Sektörler, Kazananlar, Mentörler burada
        'cover_url': a.cover_image.url if a.cover_image else None
    })

@csrf_exempt
@require_POST
def save_archive(request, pk=None):
    slug = request.POST.get('slug')
    event = get_object_or_404(OrganizationEvent, slug=slug)
    
    if pk:
        archive = get_object_or_404(OrganizationArchive, pk=pk)
    else:
        archive = OrganizationArchive(event=event)

    archive.year = request.POST.get('year')
    archive.motto = request.POST.get('motto')
    archive.description = request.POST.get('description')
    
    # Mevcut extra_data'yı al
    extra = archive.extra_data or {}

    # 1. ÇOKLU GÖRSEL İŞLEME
    gallery_paths = extra.get('images', []) 
    files = request.FILES.getlist('gallery_images')
    for f in files:
        # Dosya ismi çakışmaması için slug ve yıl ekleyerek kaydedebiliriz
        path = default_storage.save(f'org/gallery/{slug}_{archive.year}_{f.name}', f)
        gallery_paths.append(f'/media/{path}')
    
    extra['images'] = gallery_paths 
    
    # 2. EK VERİLERİ (Sektörler, Kazananlar vb.) GÜNCELLE
    extra_json = request.POST.get('extra_data_raw')
    if extra_json:
        # JSON'dan gelen veriyi mevcut extra_data ile birleştir
        # (Örn: winners veya sectors listesini günceller)
        new_data = json.loads(extra_json)
        extra.update(new_data)

    archive.extra_data = extra

    # 3. ANA KAPAK FOTOĞRAFI
    if 'cover_image' in request.FILES:
        archive.cover_image = request.FILES['cover_image']
            
    archive.save()
    return JsonResponse({'status': 'success'})

@csrf_exempt
@require_POST
def delete_archive(request, pk):
    """Sadece Arşiv Silen Özel View"""
    try:
        archive = get_object_or_404(OrganizationArchive, pk=pk)
        archive.delete()
        return JsonResponse({'status': 'success', 'message': 'Arşiv silindi.'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})


def dashboard(request):
    content, _ = PageContent.objects.get_or_create(path='/')
    
    # En güncel "Anlık Duyuru" (Hero altı için)
    latest_instant = Announcement.objects.filter(category='ANLIK', is_active=True).first()
    
    # Diğer tüm aktif duyurular (Grid için)
    other_announcements = Announcement.objects.filter(is_active=True).exclude(id=latest_instant.id if latest_instant else None)

    sponsors = Sponsor.objects.all().order_by('order')
    
    return render(request, 'core/dashboard.html', {
        'page_data': content.data,
        'latest_instant': latest_instant,
        'other_announcements': other_announcements,
        'sponsors': sponsors,
    })
    
def get_all_announcements(request):
    announcements = Announcement.objects.all() # ordering zaten modelde tanımlı [-created_at]
    data = [{
        'id': a.id, 
        'title': a.title, 
        'category': a.get_category_display(), 
        'is_active': a.is_active
    } for a in announcements]
    return JsonResponse(data, safe=False)

def get_announcement(request, pk):
    a = get_object_or_404(Announcement, pk=pk)
    return JsonResponse({
        'id': a.id,
        'category': a.category,
        'title': a.title,
        'text': a.text,
        'link': a.link,
        'extra_data': a.extra_data, # img_url, deadline gibi esnek veriler burada
        'is_active': a.is_active
    })

def add_announcement(request):
    if request.method == 'POST':
        # extra_data'yı JSON olarak al
        extra_data = {}
        extra_data_raw = request.POST.get('extra_data_raw')
        if extra_data_raw:
            extra_data = json.loads(extra_data_raw)

        Announcement.objects.create(
            category=request.POST.get('category'),
            title=request.POST.get('title'),
            text=request.POST.get('text'),
            link=request.POST.get('link'),
            is_active=request.POST.get('is_active') == 'true',
            extra_data=extra_data # Modele kaydet
        )
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

def update_announcement(request, pk):
    if request.method == 'POST':
        a = get_object_or_404(Announcement, pk=pk)
        
        # extra_data güncellemesi
        extra_data_raw = request.POST.get('extra_data_raw')
        if extra_data_raw:
            a.extra_data = json.loads(extra_data_raw)

        a.category = request.POST.get('category')
        a.title = request.POST.get('title')
        a.text = request.POST.get('text')
        a.link = request.POST.get('link')
        a.is_active = request.POST.get('is_active') == 'true'
        a.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

def delete_announcement(request, pk):
    if request.method == 'POST':
        get_object_or_404(Announcement, pk=pk).delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

def get_all_sponsors(request):
    sponsors = Sponsor.objects.all().order_by('order')
    data = [{'id': s.id, 'name': s.name, 'logo_url': s.logo.url, 'order': s.order} for s in sponsors]
    return JsonResponse(data, safe=False)

def add_sponsor(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        order = request.POST.get('order', 0)
        logo = request.FILES.get('logo')
        
        if name and logo:
            Sponsor.objects.create(name=name, logo=logo, order=order)
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error', 'message': 'Eksik veri'}, status=400)

def delete_sponsor(request, pk):
    if request.method == 'POST':
        sponsor = get_object_or_404(Sponsor, pk=pk)
        sponsor.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

def edergi(request):
    all_magazines = Magazine.objects.filter(is_active=True)
    
    latest_mag = all_magazines.first() 
    
    years_queryset = all_magazines.dates('release_date', 'year', order='DESC')

    return render(request, 'core/edergi.html', {
        'latest': latest_mag,
        'all_magazines': all_magazines,  
        'years': [y.year for y in years_queryset]
    })

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

def delete_magazine(request, pk):
    if request.method == 'POST':
        magazine = get_object_or_404(Magazine, pk=pk)
        magazine.delete()
        return JsonResponse({'status': 'success'})   


def ekibimiz(request):
    content, created = PageContent.objects.get_or_create(path=request.path)
    
    members = TeamMember.objects.all().order_by('order', 'name')
    
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


def hakkimizda(request):
    content, created = PageContent.objects.get_or_create(path=request.path)
    
    return render(request, 'core/hakkimizda.html', {
        'page_data': content.data
    })
  
def iletisim(request):
    content, created = PageContent.objects.get_or_create(path=request.path)
    return render(request, 'core/iletisim.html', {
        'page_data': content.data
    })

def tuzuk(request):
    content, created = PageContent.objects.get_or_create(path=request.path)

    return render(request, 'core/tuzuk.html', {
        'page_data': content.data,
    })
  
@require_POST
def universal_save(request):
    path = request.POST.get('path') 
    # Frontend'de 'json_data' olarak append etmiştik
    raw_data = request.POST.get('json_data', '{}')
    
    try:
        new_data = json.loads(raw_data)
        
        # Mevcut kaydı getir veya oluştur
        content, created = PageContent.objects.get_or_create(path=path)
        
        # 1. Metin verilerini JSON içine güncelle
        if not content.data: content.data = {} # None hatasına karşı koruma
        content.data.update(new_data)
        
        # 2. Resim dosyaları (FILES) geldiyse onları kaydet ve URL'lerini JSON'a yaz
        if request.FILES:
            for key in request.FILES:
                file = request.FILES[key]
                # Dosyayı media/uploads altına kaydet
                file_path = default_storage.save(f'uploads/{file.name}', file)
                file_url = default_storage.url(file_path)
                # JSON verisindeki resim alanını gerçek URL ile güncelle
                content.data[key] = file_url
        
        # Django'ya JSON alanının değiştiğini söyle ve kaydet
        content.save()
        
        print(f"Başarılı: {path}")
        return JsonResponse({'status': 'success'})
        
    except Exception as e:
        print(f"Hata oluştu: {str(e)}")
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)