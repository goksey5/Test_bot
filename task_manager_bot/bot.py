# bot.py
import sys
import discord
from discord.ext import commands
from database import TaskDatabase
from config import token
sys.path.append(r'C:\Users\gokse\OneDrive\Masaüstü\task_manager_bot')


intents = discord.Intents.default()
intents.message_content = True  # Mesaj içeriğine erişim izni
bot = commands.Bot(command_prefix='!', intents=intents)

db = TaskDatabase()

@bot.event
async def on_ready():
    print(f'Bot giriş yaptı: {bot.user}')

@bot.command(name='add_task')
async def add_task(ctx, *, description: str):
    task_id = db.add_task(description)
    await ctx.send(f'✅ Görev eklendi. ID: {task_id}, Açıklama: "{description}"')

@bot.command(name='delete_task')
async def delete_task(ctx, task_id: int):
    db.delete_task(task_id)
    await ctx.send(f'🗑️ Görev silindi. ID: {task_id}')

@bot.command(name='show_tasks')
async def show_tasks(ctx):
    tasks = db.get_all_tasks()
    if not tasks:
        await ctx.send("📭 Henüz görev bulunmuyor.")
        return

    task_list = ""
    for task in tasks:
        status = "✅" if task[2] else "❌"
        task_list += f"ID: {task[0]}, Açıklama: {task[1]}, Durum: {status}\n"
    await ctx.send(f"📋 Görev Listesi:\n{task_list}")

@bot.command(name='complete_task')
async def complete_task(ctx, task_id: int):
    tasks = db.get_all_tasks()
    task_ids = [task[0] for task in tasks]  # ID'leri al

    if task_id not in task_ids:
        await ctx.send(f'❌ Bu ID ile bir görev bulunamadı: {task_id}')
        return

    db.complete_task(task_id)
    await ctx.send(f'🎉 Görev tamamlandı olarak işaretlendi. ID: {task_id}')
    
@bot.command(name='completed_tasks')
async def completed_tasks(ctx):
    tasks = db.get_completed_tasks()
    if not tasks:
        await ctx.send("✅ Tamamlanmış görev bulunmuyor.")
        return

    response = "📋 **Tamamlanmış Görevler:**\n"
    for task_id, desc in tasks:
        response += f"- ID: {task_id}, Açıklama: {desc}\n"

    await ctx.send(response)


bot.run(token)
