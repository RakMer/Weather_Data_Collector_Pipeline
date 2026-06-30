import pandas as pd
import redis
import json
from sqlalchemy import create_engine

#docker exec -it dataStorage redis-cli   LLEN weather_queue

redis_connector = redis.Redis(host='queue',port=6379, db=0)

veri_paketi = redis_connector.rpop('raw_weather_queue')

if veri_paketi:
    veri_paketi = veri_paketi.decode('utf-8')

    veri_paketi = json.loads(veri_paketi)

    df_ham = pd.json_normalize(veri_paketi['list'])

    print(df_ham.head(5))

    df_temiz = df_ham[['dt_txt', 'main.temp_min', 'main.temp_max', 'main.humidity']].copy()

    # 3. ADIM: Matematiksel Dönüşüm (Kelvin'den Celsius'a geçiş)
    df_temiz['main.temp_min'] = (df_temiz['main.temp_min'] - 273.15).round(2)
    df_temiz['main.temp_max'] = (df_temiz['main.temp_max'] - 273.15).round(2)

    # 4. ADIM: Sütun başlıklarını senin istediğin gibi kurumsal ve Türkçe yapıyoruz
    df_temiz.columns = ['tarih', 'min_sicaklik', 'max_sicaklik', 'nem']

    # Sonucu görelim
    print("🚀 --- PANDAS MOTORUNDAN ÇIKAN TERTEMİZ TABLO ---")
    print(df_temiz.head(5))  # İlk 5 satırı yazdıralım

    engine = create_engine(('postgresql://mert:scretpassword@database:5432/deneme'))

    df_temiz.to_sql('beykoz_hava_durumu', engine, if_exists='append', index=False)


else:
    print("Redis'de veri yok.")