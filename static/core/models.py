from django.db import models

# Etkinlikler Tablosu
class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name="Etkinlik AdÄ±")
    description = models.TextField(verbose_name="Etkinlik AÃ§Ä±klamasÄ±")
    date = models.DateTimeField(verbose_name="Etkinlik Tarihi")
    location = models.CharField(max_length=200, verbose_name="Yer")
    image = models.ImageField(upload_to='events/', verbose_name="Kapak FotoÄŸrafÄ±")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Duyurular/Haberler Tablosu
class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Duyuru BaÅŸlÄ±ÄŸÄ±")
    content = models.TextField(verbose_name="Ä°Ã§erik")
    image = models.ImageField(upload_to='news/', blank=True, null=True, verbose_name="GÃ¶rsel (Opsiyonel)")
    is_active = models.BooleanField(default=True, verbose_name="YayÄ±nda mÄ±?")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class OrganizationSurvey(models.Model):
    location_preference = models.CharField(max_length=200, verbose_name="Yer Ã–nerisi")
    catering_preference = models.CharField(max_length=50, verbose_name="Ä°kram Tercihi")
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ã–neri - {self.submitted_at.strftime('%d/%m/%Y')}"

class Magazine(models.Model):
    title = models.CharField(max_length=200, verbose_name="Dergi AdÄ±")
    semester = models.CharField(max_length=100, verbose_name="DÃ¶nem (Ã–rn: 2024-2025 GÃ¼z)")
    cover_image = models.ImageField(upload_to='magazines/covers/', verbose_name="Kapak FotoÄŸrafÄ±")
    pdf_file = models.FileField(upload_to='magazines/pdfs/', verbose_name="PDF DosyasÄ±")
    published_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.semester}"