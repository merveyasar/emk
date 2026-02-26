#!/usr/bin/env bash
# Hata oluşursa dur
set -o errexit

# Kütüphaneleri kur
pip install -r requirements.txt

# Statik dosyaları topla
python manage.py collectstatic --no-input

# Veritabanını güncelle
python manage.py migrate