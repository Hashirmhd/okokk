from pyrogram import Client, filters


@Client.on_message(filters.command(["help"]))
async def start(client, message):
    helptxt = f"Use Download button,IF You Not See That Click /start"
    await message.reply_text(helptxt)
