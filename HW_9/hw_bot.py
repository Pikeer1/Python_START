from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from task_calc import calculator
from negafib import negafibon


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
    await update.message.reply_text(f'Вычислить выражение: /calc 3+10/2')
    await update.message.reply_text(f'Перевести в двоичную систему: /bin 8')
    await update.message.reply_text(f'Вывод чисел НегаФибоначчи: /nfib 8')


async def get_calc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    inp_num = update.message.text.split(' ', 1)[1]
    await update.message.reply_text(f'Результат: {inp_num} = {calculator(inp_num)}')


async def binary(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    number = update.message.text.split(' ', 1)[1]
    await update.message.reply_text("Результат: {0:b}".format(int(number)))


async def get_nfib(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    inp_number = update.message.text.split(' ', 1)[1]
    await update.message.reply_text(f'Результат: {inp_number} = {negafibon(inp_number)}')


my_token = "input token here"
app = ApplicationBuilder().token(my_token).build()
app.add_handler(CommandHandler("start", hello))
app.add_handler(CommandHandler("calc", get_calc))
app.add_handler(CommandHandler("bin", binary))
app.add_handler(CommandHandler("nfib", get_nfib))
app.run_polling()
