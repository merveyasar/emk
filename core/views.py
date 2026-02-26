from django.shortcuts import render
from .models import Event, News, OrganizationSurvey,Magazine

def dashboard(request):
    # En son eklenen 3 etkinliÄŸi ve 4 duyuruyu Ã§ekiyoruz (SayÄ±yÄ± deÄŸiÅŸtirebilirsin)
    events = Event.objects.all().order_by('-date')
    news_list = News.objects.filter(is_active=True).order_by('-created_at')[:4]
    
    context = {
        'events': events,
        'news_list': news_list,
    }
    return render(request, 'core/dashboard.html', context)

def sb(request):
    return render(request, 'core/organizasyonlar/sb.html')

def kale(request):
    return render(request, 'core/organizasyonlar/kale.html')

def sirket_gunleri(request):
    return render(request, 'core/organizasyonlar/sirket_gunleri.html')

def teknik_gezi(request):
    return render(request, 'core/organizasyonlar/teknik_gezi.html')

def egitim_seminerleri(request):
    return render(request, 'core/organizasyonlar/egitim_seminerleri.html')

def gdkg(request):
    return render(request, 'core/organizasyonlar/gdkg.html')

def col(request):
    return render(request, 'core/organizasyonlar/col.html')

def mentorship(request):
    return render(request, 'core/organizasyonlar/mentorship.html')

def hakkimizda(request):
    return render(request, 'core/hakkimizda.html')

def ekibimiz(request):
    return render(request, 'core/ekibimiz.html')

def edergi(request):
    magazines = Magazine.objects.all().order_by('-published_date')
    return render(request, 'core/edergi.html', {'magazines': magazines})


def iletisim(request):
    return render(request, 'core/iletisim.html')

def tuzuk(request):
    return render(request, 'core/tuzuk.html')