
import os
import sys  
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import discord
from discord.ext import commands
from task_manager_bot.database import TaskDatabase
from task_manager_bot.config import token

intents = discord.Intents.default()
intents.message_content = True  # Mesaj içeriğine erişim izni
bot = commands.Bot(command_prefix='!', intents=intents)

db = TaskDatabase()

@bot.event
async def on_ready():
    print(f'Bot giriş yaptı: {bot.user}')

@bot.command(name='add_task')
async def add_task(ctx, *, description: str):
    """Yeni görev ekler."""
    task_id = db.add_task(description)  # Artık task_id döndürülüyor
    await ctx.send(f'✅ Görev eklendi. ID: {task_id}, Açıklama: "{description}"')
    print(f"[LOG] Görev eklendi: {description}")

@bot.command(name='delete_task')
async def delete_task(ctx, task_id: int):
    """Veritabanından belirli bir görevi siler."""
    task_db = TaskDatabase(db_path='tasks.db')  # Veritabanını başlat
    task_db.delete_task(task_id)  # Görevi sil
    await ctx.send(f"🗑️ Görev {task_id} başarıyla silindi.")  # Kullanıcıya mesaj gönder
    print(f"[LOG] Görev silindi: ID {task_id}")

@bot.command(name='show_tasks')
async def show_tasks(ctx):
    tasks = db.get_all_tasks()

    if not tasks:
        await ctx.send("📭 Gösterilecek görev yok.")
        print("[LOG] Kullanıcı görev listesini istedi. Hiç görev bulunamadı.")
        return

    message = "📋 Görev Listesi:\n"
    completed_count = 0

    for task in tasks:
        task_id, description, completed = task
        status = "✅" if completed else "❌"
        message += f"ID: {task_id}, Açıklama: {description}, Durum: {status}\n"
        if completed:
            completed_count += 1

    await ctx.send(message)

    total = len(tasks)
    print(f"[LOG] Görev listesi gösterildi. Toplam: {total}, Tamamlanan: {completed_count}")


@bot.command(name='complete_task')
async def complete_task(ctx, task_id: int):
    """Görevi tamamlanmış olarak işaretler."""
    tasks = db.get_all_tasks()
    task_ids = [task[0] for task in tasks]  # ID'leri al

    if task_id not in task_ids:
        await ctx.send(f'❌ Bu ID ile bir görev bulunamadı: {task_id}')
        return

    db.complete_task(task_id)
    await ctx.send(f'🎉 Görev tamamlandı olarak işaretlendi. ID: {task_id}')
    print(f"[LOG] Görev tamamlandı: ID {task_id}")
    
@bot.command(name='completed_tasks')
async def completed_tasks(ctx):
    """Tamamlanmış görevleri gösterir."""
    tasks = db.get_completed_tasks()
    if not tasks:
        await ctx.send("✅ Tamamlanmış görev bulunmuyor.")
        return

    response = "📋 **Tamamlanmış Görevler:**\n"
    for task_id, desc in tasks:
        response += f"- ID: {task_id}, Açıklama: {desc}\n"

    await ctx.send(response)
    print(f"[LOG] Görev tamamlandı: ID {task_id}")

    
bot.run(token)
