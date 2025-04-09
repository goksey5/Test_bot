# bot.py

import discord
from discord.ext import commands
from database import TaskDatabase
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
    db.complete_task(task_id)
    await ctx.send(f'🎉 Görev tamamlandı olarak işaretlendi. ID: {task_id}')

# Botu başlatmak için aşağıdaki satırı kendi bot token'ınla birlikte aç:
bot.run(token)
