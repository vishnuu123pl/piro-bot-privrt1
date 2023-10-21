import random
import re, asyncio, time, shutil, psutil, os, sys
from pyrogram import Client, filters, enums
from pyrogram.types import *
from info import BOT_START_TIME, ADMINS
from utils import humanbytes  

CMD = ["/", "."]

@Client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    await message.reply_text("𝖡𝗎𝖽𝖽𝗒 𝖨𝖺𝗆 𝖠𝗅𝗂𝗏𝖾 :) 𝖧𝗂𝗍 /start \n\n𝖧𝗂𝗍 /help 𝖥𝗈𝗋 𝖧𝖾𝗅𝗉 ;)\n\n\n𝖧𝗂𝗍 /ping 𝖳𝗈 𝖢𝗁𝖾𝖼𝗄 𝖡𝗈𝗍 𝖯𝗂𝗇𝗀 😁")

@Client.on_message(filters.command("help", CMD))
async def help(_, message):
    await message.reply_text("𝖧𝗂𝗍 /series 𝖥𝗈𝗋 series 𝖲𝖾𝖺𝗋𝖼𝗁 𝖱𝗎𝗅𝖾𝗌 📃\n\n𝖧𝗂𝗍 /movie 𝖥𝗈𝗋 movie 𝖲𝖾𝖺𝗋𝖼𝗁 𝖱𝗎𝗅𝖾𝗌 📃\n\n\n𝖧𝗂𝗍 /tutorial 𝖥𝗈𝗋 𝖯𝗋𝗈𝗉𝖾𝗋 𝖳𝗎𝗍𝗈𝗋𝗂𝖺𝗅 𝖵𝗂𝖽𝖾𝗈𝗌 🤗")


@Client.on_message(filters.command("movie", CMD))
async def movie(_, message):
    await message.reply_text("⚠️❗️ 𝙈𝙊𝙑𝙄𝙀𝙎 𝙉𝙊𝙏 𝘼𝙑𝘼𝙄𝙇𝘼𝘽𝙇𝙀 ❗️⚠️\n\n📝 𝘔𝘰𝘷𝘪𝘦 𝘈𝘷𝘢𝘪𝘭𝘢𝘣𝘭𝘦 𝘉𝘖𝘛𝘡 🚦 \n\n  🚧 @EVAMARIA_v_Bot \n  🚧 @Ultramoviesearch_bot")

@Client.on_message(filters.command("series", CMD))
async def series(_, message):
    await message.reply_text("⚠️❗️ 𝗦𝗲𝗿𝗶𝗲𝘀 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗙𝗼𝗿𝗺𝗮𝘁 ❗️⚠️\n\n🗣 𝖲𝖾𝗋𝗂𝖾𝗌 𝖭𝖺𝗆𝖾, 𝘚𝘦𝘳𝘪𝘦𝘴 𝘥𝘢𝘵𝘦 (𝘞𝘩𝘪𝘤𝘩 𝘋𝘢𝘵𝘦 𝘦𝘱𝘴𝘰𝘥𝘦 𝘺𝘰𝘶 𝘸𝘢𝘯𝘵) 🧠\n\n🖇𝐄𝐱𝐚𝐦𝐩𝐥𝐞: \n\n• 𝘎𝘦𝘦𝘵𝘩𝘢 𝘎𝘰𝘷𝘪𝘯𝘥𝘢𝘮 20✅ \n• 𝘚𝘸𝘢𝘯𝘥𝘢𝘯𝘢𝘮 28✅ \n• 𝘚𝘶𝘯𝘥𝘢𝘳𝘪 21✅ \n• 𝘒𝘶𝘥𝘶𝘮𝘣𝘢𝘴𝘳𝘦𝘦 𝘚𝘢𝘳𝘢𝘥𝘢 2✅ \n• Bavana S02✅\n\n [𝗗𝗼𝗻𝘁 𝗨𝘀𝗲 𝘄𝗼𝗿𝗱𝘀 𝗟𝗶𝗸𝗲 𝗦𝗲𝗮𝘀𝗼𝗻/𝗘𝗽𝗶𝘀𝗼𝗱𝗲/𝗦𝗲𝗿𝗶𝗲𝘀 , . : - 𝗲𝘁𝗰] ❌")

@Client.on_message(filters.command("tutorial", CMD))
async def tutorial(_, message):
    await message.reply_text("𝖢𝗁𝖾𝖼𝗄𝗈𝗎𝗍 @Asianet_serial_HPM 𝖥𝗈𝗋 𝖳𝗎𝗍𝗈𝗋𝗂𝖺𝗅𝗌 😎")

@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...........")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"𝖯𝗂𝗇𝗀!\n{time_taken_s:.3f} ms")

@Client.on_message(filters.command("status"))          
async def stats(bot, update):
    currentTime = time.strftime("%Hh%Mm%Ss", time.gmtime(time.time() - BOT_START_TIME))
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    ms_g = f"""<b>⚙️ 𝖡𝗈𝗍 𝖲𝗍𝖺𝗍𝗎𝗌</b>

🕔 𝖴𝗉𝗍𝗂𝗆𝖾: <code>{currentTime}</code>
🛠 𝖢𝖯𝖴 𝖴𝗌𝖺𝗀𝖾: <code>{cpu_usage}%</code>
🗜 𝖱𝖠𝖬 𝖴𝗌𝖺𝗀𝖾: <code>{ram_usage}%</code>
🗂 𝖳𝗈𝗍𝖺𝗅 𝖣𝗂𝗌𝗄 𝖲𝗉𝖺𝖼𝖾: <code>{total}</code>
🗳 𝖴𝗌𝖾𝖽 𝖲𝗉𝖺𝖼𝖾: <code>{used} ({disk_usage}%)</code>
📝 𝖥𝗋𝖾𝖾 𝖲𝗉𝖺𝖼𝖾: <code>{free}</code> """

    msg = await bot.send_message(chat_id=update.chat.id, text="__𝖯𝗋𝗈𝖼𝖾𝗌𝗌𝗂𝗇𝗀...__", parse_mode=enums.ParseMode.MARKDOWN)         
    await msg.edit_text(text=ms_g, parse_mode=enums.ParseMode.HTML)

@Client.on_message(filters.command("restart") & filters.user(ADMINS))
async def stop_button(bot, message):
    msg = await bot.send_message(text="**𝖡𝗈𝗍 𝖨𝗌 𝖱𝖾𝗌𝗍𝖺𝗋𝗍𝗂𝗇𝗀...🪄**", chat_id=message.chat.id)       
    await asyncio.sleep(3)
    await msg.edit("**𝖡𝗈𝗍 𝖱𝖾𝗌𝗍𝖺𝗋𝗍𝖾𝖽 𝖲𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅𝗅𝗒 ! 𝖱𝖾𝖺𝖽𝗒 𝖳𝗈 𝖬𝗈𝗏𝖾 𝖮𝗇 💯**")
    os.execl(sys.executable, sys.executable, *sys.argv)
