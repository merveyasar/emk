import os
import django

# Django ayarlarını yüklüyoruz
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'emk_web.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Buradaki bilgileri kendine göre güncelle kanka
username = 'merve'
email = ''
password = 'merve123..!!'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Süper kullanıcı '{username}' başarıyla oluşturuldu!")
else:
    print(f"Kullanıcı '{username}' zaten mevcut.")