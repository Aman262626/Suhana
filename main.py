import os
import requests
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

# ---------------- AI RESPONSE ----------------
def get_ai_reply(message):
    payload = {
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a sweet, caring girlfriend. "
                    "Reply in Hinglish and English. "
                    "Be loving, supportive, and respectful. "
                    "No adult or sexual content."
                )
            },
            {
                "role": "user",
                "content": message
            }
        ]
    }

    try:
        r = requests.post(
            "https://chatbot-ji1z.onrender.com/chatbot-ji1z",
            json=payload,
            timeout=20
        )
        return r.json()["choices"][0]["message"]["content"]
    except:
        return "Aww 🥺 thoda sa issue aa gaya, phir try karo 💛"


# ---------------- MESSAGE HANDLER ----------------
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text
    reply_text = get_ai_reply(user_msg)
    await update.message.reply_text(reply_text)


# ---------------- MAIN ----------------
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
    print("🤖 Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
