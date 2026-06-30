# Weather Data Collector Pipeline

Bu proje, OpenWeather tabanlı bir hava durumu API'sinden veri çekip Redis kuyruğuna yazan, ardından bu veriyi Pandas ile temizleyerek PostgreSQL veritabanına aktaran basit bir veri toplama hattıdır.

## Ne Yapar?

Pipeline şu sırayla çalışır:

1. `api_collector.py` hava durumu verisini API'den alır.
2. Ham veri `raw_weather_queue` adlı Redis kuyruğuna eklenir.
3. `data_procces.py` kuyruğu okur ve JSON verisini tabloya dönüştürür.
4. Sıcaklık değerleri Kelvin'den Celsius'a çevrilir.
5. Temizlenmiş veri PostgreSQL'deki `beykoz_hava_durumu` tablosuna yazılır.

## Teknolojiler

- Python
- Redis
- PostgreSQL
- Pandas
- SQLAlchemy
- dotenv
- Docker
- Docker Compose

## Proje Yapısı

- `api_collector.py`: API'den veri çekip Redis'e yazar.
- `data_procces.py`: Redis'ten veriyi alır, temizler ve veritabanına kaydeder.
- `docker-compose.yml`: Redis, PostgreSQL ve uygulama servislerini başlatır.
- `Dockerfile`: Python imajını oluşturur.
- `requirements.txt`: Python bağımlılıklarını içerir.
- `.env`: PostgreSQL için ortam değişkenlerini tutar.

## Gereksinimler

Projeyi çalıştırmak için sisteminizde aşağıdakiler kurulu olmalıdır:

- Docker
- Docker Compose

## Kurulum

1. Proje klasörüne girin.
2. Gerekirse `.env` dosyasının içeriğini kontrol edin.

Örnek `.env` içeriği:

```env
POSTGRES_DB=deneme
POSTGRES_USER=mert
POSTGRES_PASSWORD=scretpassword
```

## Çalıştırma

Container'ları başlatmak için:

```bash
docker compose up --build
```

Bu komut Redis ve PostgreSQL servislerini ayağa kaldırır, ardından hava durumu verisini toplar ve işlenmiş veriyi veritabanına yazar.

## Veritabanı Bilgileri

Varsayılan PostgreSQL ayarları:

- Veritabanı: `deneme`
- Kullanıcı: `mert`
- Şifre: `scretpassword`
- Host: `database`
- Port: `5432`

Oluşturulan tablo adı:

- `beykoz_hava_durumu`

## Bağımlılıklar

`requirements.txt` içinde yer alan paketler:

- `pandas`
- `redis`
- `sqlalchemy`
- `psycopg2-binary`
- `dotenv`

## Beklenen Sonuç

Pipeline başarıyla çalıştığında:

- ham veri Redis kuyruğuna eklenir,
- temizlenmiş hava durumu tablosu hazırlanır,
- veriler PostgreSQL'deki `beykoz_hava_durumu` tablosuna kaydedilir.

