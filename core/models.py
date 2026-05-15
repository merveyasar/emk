from django.db import models

class PageContent(models.Model):
    path = models.CharField(max_length=255, unique=True)
    data = models.JSONField(default=dict) 

    def __str__(self):
        return self.path
    
    
class TeamMember(models.Model):
    RANKS = [('ALFA', 'Alfa'), ('BETA', 'Beta'), ('GAMA', 'Gama')]
    TEAMS = [('DIS', 'Dış Organizasyonlar'), ('IC', 'İç Organizasyonlar'), 
             ('IK', 'İnsan Kaynakları'), ('FIN', 'Finans'), ('GAMA', 'Gama Kurulu')]

    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    rank = models.CharField(max_length=10, choices=RANKS)
    team = models.CharField(max_length=10, choices=TEAMS)
    image = models.ImageField(upload_to='team/', default='team/default.png')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'name'] # Otomatik sıralama ekledik

    def __str__(self):
        return self.name
    
    
class Magazine(models.Model):
    title = models.CharField(max_length=255, verbose_name="Dergi Başlığı")
    issue_number = models.PositiveIntegerField(verbose_name="Sayı No")
    release_date = models.DateField(verbose_name="Yayın Tarihi")
    description = models.TextField(verbose_name="Kısa Açıklama")
    cover_image = models.ImageField(upload_to='magazines/covers/', verbose_name="Kapak Resmi")
    read_link = models.URLField(verbose_name="Okuma Linki (Issuu vb.)")
    pdf_file = models.FileField(upload_to='magazines/pdfs/', null=True, blank=True, verbose_name="PDF Dosyası")
    is_active = models.BooleanField(default=True, verbose_name="Yayında mı?")

    class Meta:
        verbose_name = "Dergi"
        verbose_name_plural = "Dergiler"
        ordering = ['-release_date']

    def __str__(self):
        return f"Sayı {self.issue_number}: {self.title}"
    

class Announcement(models.Model):
    CATEGORY_CHOICES = [
        ('ANLIK', 'Anlık Duyuru'),
        ('KULUP', 'Kulüpsel Gelişmeler'),
        ('ETKINLIK', 'Etkinlik Haberi'),
    ]
    
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='ANLIK')
    title = models.CharField(max_length=200, verbose_name="Duyuru Başlığı")
    text = models.TextField(verbose_name="Duyuru İçeriği")
    link = models.URLField(blank=True, verbose_name="Detay Linki (Opsiyonel)")
    is_active = models.BooleanField(default=True, verbose_name="Aktif mi?")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Duyuru"
        verbose_name_plural = "Duyurular"
        ordering = ['-created_at']

    def __str__(self):
        return f"[{self.category}] {self.title}"
    
    
class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    logo = models.FileField(upload_to='sponsors/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
          

class OrganizationEvent(models.Model):
    name = models.CharField(max_length=100, unique=True) 
    slug = models.SlugField(unique=True) 
    description = models.TextField()

class OrganizationArchive(models.Model):
    event = models.ForeignKey(OrganizationEvent, on_delete=models.CASCADE, related_name='archives')
    year = models.PositiveIntegerField()
    motto = models.CharField(max_length=255, verbose_name="Dönem Mottosu / Sloganı")
    description = models.TextField(verbose_name="Dönem Özeti")
    cover_image = models.ImageField(upload_to='org/covers/')
    
    extra_data = models.JSONField(default=dict, blank=True)

    class Meta:
        ordering = ['-year']
        verbose_name = "Organizasyon Arşivi"
