from django.contrib import admin
from .models import Event, News

admin.site.register(Event)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    # Admin formunu özelleştireceğimiz template
    change_form_template = "admin/news_preview_change_form.html"
    
    list_display = ('title', 'is_active', 'created_at')

    class Media:
        # Statik dosyalarına bu isimlerle ekleyeceğiz
        js = ('js/admin_news_preview.js',)
        css = {
            'all': ('css/admin_news_preview.css',)
        }