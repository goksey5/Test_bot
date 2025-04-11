
# 📝 Discord Görev Yöneticisi Botu

Bu proje, küçük ekiplerin görev yönetimini kolaylaştırmak için geliştirilmiş bir **Discord botudur**. Kullanıcılar görev ekleyebilir, silebilir, tamamlayabilir ve tüm görevleri listeleyebilir. Tüm veriler **SQLite veritabanı** ile saklanır.

## 🚀 Özellikler

- ✅ Görev ekleme: `!add_task <görev açıklaması>`
- ❌ Görev silme: `!delete_task <görev_id>`
- 📋 Tüm görevleri görüntüleme: `!show_tasks`
- ✔️ Görevi tamamlama: `!complete_task <görev_id>`
- 🎯 Tamamlanmış görevleri listeleme: `!completed_tasks`
- 🔐 Discord bot token'ı `config.py` dosyasında saklanır
- 🧪 Pytest ile test edilmiş sağlam altyapı

---

## 🛠️ Kurulum

```bash
# 1. Projeyi klonla
git clone https://github.com/kullanici_adi/task_manager_bot.git
cd task_manager_bot

# 2. Sanal ortam oluştur (isteğe bağlı)
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # macOS/Linux

# 3. Gerekli paketleri yükle
pip install -r requirements.txt
```

---

## ▶️ Başlatma

Botu çalıştırmak için:

```bash
python task_manager_bot/bot.py
```

**Not:** Botun çalışabilmesi için bir Discord bot token’ı gereklidir. Bu token `config.py` dosyasında şu şekilde tanımlanmalıdır:

```python
# config.py
TOKEN = "Senin Discord Bot Token'ın"
```

---

## 📂 Proje Yapısı

```
task_manager_bot/
│
├── bot.py               # Discord botu komutlarını içerir
├── database.py          # SQLite işlemleri
├── config.py            # Discord bot token'ı burada saklanır
├── requirements.txt     # Gerekli tüm kütüphaneler
├── tests/               # pytest test dosyaları
│   ├── test_add_task.py
│   ├── test_complete_task.py
│   ├── test_delete_task.py
│   ├── test_database.py
│   └── test_show_tasks.py
└── README.md            # Proje açıklaması
```

---

## ✅ Test Sonuçları

> Aşağıdaki sonuçlar pytest çalıştırılarak elde edilmiştir.

```
Platform   : win32
Python     : 3.11.2
Pytest     : 8.3.5
Toplam Test: 12
Başarılı   : ✅ 12 passed
Süre       : 4.54 saniye
```

| Test Dosyası               | Sonuç     |
|----------------------------|-----------|
| `test_add_task.py`         | ✅ Passed |
| `test_complete_task.py`    | ✅ Passed |
| `test_database.py`         | ✅ Passed |
| `test_delete_task.py`      | ✅ Passed |
| `test_show_tasks.py`       | ✅ Passed |

---

## 📦 Bağımlılıklar

Tüm bağımlılıklar `requirements.txt` dosyasında belirtilmiştir:

```
discord.py
pytest
```

Kurulum için:

```bash
pip install -r requirements.txt
```

---

## ✍️ Geliştirici

📌 **Adınız:** Gökhan 
💡 **Amaç:** Python becerilerini geliştirmek ve öğrencilere örnek proje sunmak.  

---

## 📜 Lisans

Bu proje MIT lisansı ile lisanslanmıştır.
