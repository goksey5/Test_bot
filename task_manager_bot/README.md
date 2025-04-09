# Task Manager Discord Bot

Bu proje, küçük ekipler için görevleri yönetmeye yardımcı olacak bir Discord botu oluşturur. Bot, görev ekleme, silme, görüntüleme ve tamamlanmış olarak işaretleme işlevlerine sahiptir. Tüm veriler SQLite veritabanında saklanır.

## Özellikler

- `!add_task <description>` - Bir görev ekler.
- `!delete_task <task_id>` - Belirtilen ID'ye sahip bir görevi siler.
- `!show_tasks` - Tüm görevlerin listesini gösterir.
- `!complete_task <task_id>` - Belirtilen ID'ye sahip bir görevi tamamlanmış olarak işaretler.

## Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki yazılımların yüklü olması gerekmektedir:

- Python 3.11 veya daha yüksek bir sürüm.
- discord.py kütüphanesi (Discord botları için Python kütüphanesi).
- SQLite (Veritabanı için).
  
Yüklemek için:

```bash
pip install discord.py

git clone https://github.com/goksey5/Test_bot.git
cd Test_bot
config.py dosyasındaki token değişkenini, Discord'dan aldığınız yeni bot token'ı ile güncelleyin. Bu token'ı .gitignore dosyasına ekleyerek güvenliğini sağlayın.
Botu çalıştırın:
python bot.py
