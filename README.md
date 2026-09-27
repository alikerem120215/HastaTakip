# 🏥 HastaTakip — Flask & SQLite Tabanlı Klinik Hasta Kayıt Sistemi

HastaTakip; klinikler, muayenehaneler ve doktorlar için tasarlanmış, hasta kayıtlarını, iletişim bilgilerini, tıbbi notları ve hasta evrak/fotoğraflarını yerel veritabanında güvenle saklayan pratik bir web yönetim sistemidir.

---

## 🌟 Temel Özellikler
- **Hasta Kayıt & Listeleme:** Yeni hasta profili oluşturma, isim, tanı ve iletişim bilgilerini kaydetme.
- **Evrak & Fotoğraf Yükleme:** Hastalara ait tahlil sonuçları, röntgen veya reçete fotoğraflarını yükleme ve arşivleme (`static/kayitlar`).
- **SQLite & SQLAlchemy:** Sunucu gerektirmeyen, hafif, taşınabilir ve hızlı yerel veritabanı altyapısı.
- **Responsive Arayüz:** Masaüstü ve tablet tarayıcılarıyla tam uyumlu sade Bootstrap tasarımı.

---

## 🚀 Başlarken

1. **Bağımlılıkları yükleyin:**
   ```bash
   pip install Flask Flask-SQLAlchemy
   ```

2. **Sunucuyu başlatın:**
   ```bash
   python3 main.py
   ```

3. Tarayıcınızda `http://127.0.0.1:5000` adresine gidin.
