from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from poly import sum_polynom


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
    await update.message.reply_text(f'Сложить полиномы 1 и 2 из файла: /calc poly')


async def get_calc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    with open("polynom/polynom_0.txt") as file:
        data = file.read()
    with open("polynom/polynom_1.txt") as file:
        data1 = file.read()
    await update.message.reply_text(f'Полином 1: {data}')
    await update.message.reply_text(f'Полином 2: {data1}')
    await update.message.reply_text(f'Результат: {sum_polynom(data, data1)}')


my_token = "input token here"
app = ApplicationBuilder().token(my_token).build()
app.add_handler(CommandHandler("start", hello))
app.add_handler(CommandHandler("calc", get_calc))
app.run_polling()

