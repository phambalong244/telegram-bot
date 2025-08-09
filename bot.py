from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# ===== Danh sách câu hỏi - câu trả lời =====
qa_dict = {
    "xin chào": "Chào bạn! Mình là bot của bạn đây.",
    "bạn tên gì": "Mình tên là Trợ Lý Ảo do bạn tạo.",
    "hôm nay ngày mấy": "Bạn tự xem lịch đi 😄",
}

# ===== Xử lý tin nhắn =====
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    reply = qa_dict.get(text, "Mình chưa biết trả lời câu này.")
    await update.message.reply_text(reply)

# ===== Chạy bot =====
def main():
    TOKEN = "8390674333:AAEU2EbREEdOZ1LVW-OvM12BR55sLWUFWCw"  # <-- Thay token bot của bạn vào đây
    app = Application.builder().token(TOKEN).build()

    # Nhận tin nhắn text và xử lý
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot đang chạy...")
    app.run_polling()

if __name__ == "__main__":
    main()
