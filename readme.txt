Weather Data Collector Pipeline

Bu proje, OpenWeather tabanlı bir hava durumu API'sinden veri çekip Redis kuyruğuna yazan, ardından bu veriyi Pandas ile temizleyerek PostgreSQL veritabanına aktaran basit bir veri toplama hattıdır.

## Proje Akışı

1. `api_collector.py` hava durumu verisini API'den alır.
2. Ham veri `raw_weather_queue` adlı Redis kuyruğuna eklenir.
3. `data_procces.py` kuyruğu okur, JSON verisini `pandas` ile tabloya dönüştürür.
4. Sıcaklık değerleri Kelvin'den Celsius'a çevrilir.
5. Temizlenmiş veri PostgreSQL'deki `beykoz_hava_durumu` tablosuna yazılır.

## Kullanılan Teknolojiler

- Python
- Redis
- PostgreSQL
- Pandas
- SQLAlchemy
- Docker / Docker Compose

## Dosyalar

- `api_collector.py`: API'den veri çekip Redis'e yazar.
- `data_procces.py`: Redis'ten veriyi alır, temizler ve veritabanına kaydeder.
- `docker-compose.yml`: Redis, PostgreSQL ve uygulama servislerini başlatır.
- `Dockerfile`: Python imajını oluşturur.
- `requirements.txt`: Python bağımlılıklarını içerir.

## Kurulum

Proje Docker ile çalıştırılmak üzere hazırlanmıştır. Bilgisayarınızda Docker ve Docker Compose kurulu olmalıdır.

Bağımlılıklar:

- `redis`
- `pandas`
- `sqlalchemy`
- `psycopg2-binary`

## Çalıştırma

1. Proje klasörüne girin.
2. Container'ları başlatın:

```bash
docker compose up --build
```

Bu komut sırasıyla Redis ve PostgreSQL servislerini ayağa kaldırır, ardından hava durumu verisini toplar ve işlenmiş veriyi veritabanına yazar.

## Veritabanı Ayarları

Docker Compose içinde varsayılan PostgreSQL bilgileri şöyledir:

- Veritabanı: `deneme`
- Kullanıcı: `mert`
- Şifre: `scretpassword`
- Host: `database`
- Port: `5432`

Tablo adı:

- `beykoz_hava_durumu`

## Notlar

- API anahtarı şu anda kod içinde sabit tanımlı. Daha güvenli kullanım için ortam değişkenine taşınması önerilir.
- `data_procces.py` dosya adında yazım farkı var; istenirse daha sonra daha anlaşılır bir isimle düzenlenebilir.
- Redis kuyruğunda veri yoksa işlem `Redis'de veri yok.` mesajı verir.

## Beklenen Çıktı

Pipeline başarıyla çalıştığında:

- ham veri Redis kuyruğuna eklenir,
- temizlenmiş hava durumu tablosu oluşturulur,
- veriler PostgreSQL'deki `beykoz_hava_durumu` tablosuna eklenir.

