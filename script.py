import nest_asyncio
nest_asyncio.apply()

# Ваш код бота начинается здесь
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
TOKEN = '7358944803:AAG_dcaesr6mWKEegk7iRa1JRjxkaeG0TBU'

questions = [
    ("Какого цвета небо обычно в ясный день?", "синее"),
    ("Сколько лап у кошки?", "четыре"),
    ("Сколько недель в году?", "пятьдесят две"),
    ("Какое животное является символом мудрости?", "сова"),
    ("Что изобрел Александр Белл?", "телефон"),
    ("Какой самый большой океан на Земле?", "тихий"),
    ("Какой планеты не существует?", "земля"),
    ("Кто написал 'Гамлет'?", "шекспир"),
    ("Как называется столица Франции?", "париж"),
    ("Какой металл является самым легким?", "алюминий"),
    ("Кто изобрел лампочку?", "эдисон"),
    ("Какой газ необходим для дыхания человека?", "кислород"),
    ("Как называется наука о растениях?", "ботаника"),
    ("Сколько дней в високосном году?", "триста шестьдесят шесть"),
    ("Какой фрукт является самым популярным в мире?", "банан"),
    ("Кто нарисовал 'Мону Лизу'?", "да винчи"),
    ("Какой самый большой континент на Земле?", "азия"),
    ("Какой химический элемент обозначается символом O?", "кислород"),
    ("Какой цвет получается при смешивании красного и белого?", "розовый"),
    ("Как называется самая длинная река в мире?", "амазонка"),
    ("Какой планеты не существует?", "плутон"),
    ("Как называется твердая оболочка Земли?", "литосфера"),
    ("Какое животное является символом Австралии?", "кенгуру"),
    ("Кто написал 'Войну и мир'?", "толстой"),
    ("Как называется столица Японии?", "токио"),
    ("Какой из металлов является самым твердым?", "алмаз"),
    ("Кто изобрел радио?", "попов"),
    ("Какой газ вызывает парниковый эффект?", "углекислый газ"),
    ("Как называется наука о животных?", "зоология"),
    ("Сколько дней в феврале обычного года?", "двадцать восемь"),
    ("Какой овощ является самым популярным в мире?", "картофель"),
    ("Кто написал 'Преступление и наказание'?", "достоевский"),
    ("Какой самый маленький континент на Земле?", "австралия"),
    ("Какой химический элемент обозначается символом H?", "водород"),
    ("Какой цвет получается при смешивании синего и желтого?", "зеленый"),
    ("Как называется самая широкая река в мире?", "амазонка"),
    ("Какой планеты не существует?", "меркурий"),
    ("Как называется воздушная оболочка Земли?", "атмосфера"),
    ("Какое животное является символом России?", "медведь"),
    ("Кто написал 'Анну Каренину'?", "толстой"),
    ("Как называется столица Италии?", "рим"),
    ("Какой металл является самым благородным?", "золото"),
    ("Кто изобрел компьютер?", "тюринг"),
    ("Какой газ самый легкий?", "водород"),
    ("Как называется наука о природе?", "физика"),
    ("Сколько дней в марте?", "тридцать один"),
    ("Какой фрукт является самым витаминным?", "апельсин"),
    ("Кто написал 'Мастера и Маргариту'?", "булгаков"),
    ("Какой самый холодный континент на Земле?", "антарктида"),
]

class QuizBot:
    def __init__(self):
        self.current_question = None
        self.score = 0
        self.used_questions = set()
        self.question_count = 0

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        self.score = 0
        self.question_count = 0
        self.used_questions.clear()
        await update.message.reply_text('Добро пожаловать в викторину! Ответьте на 10 вопросов.')
        await self.ask_question(update)

    async def ask_question(self, update: Update) -> None:
        if self.question_count < 10:
            while True:
                question, answer = random.choice(questions)
                if question not in self.used_questions:
                    self.used_questions.add(question)
                    self.current_question = (question, answer)
                    break
            self.question_count += 1
            await update.message.reply_text(question)
        else:
            await update.message.reply_text(f'Викторина окончена! Вы ответили правильно на { self.score} из 10 вопросов.')

    async def check_answer(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user_answer = update.message.text.lower().strip()
        correct_answer = self.current_question[1].lower()

        if user_answer == correct_answer:
            self.score += 1
            await update.message.reply_text('Правильно!')
        else:
            await update.message.reply_text(f'Неправильно! Правильный ответ: { correct_answer}.')

        await self.ask_question(update)

async def main():
    bot = QuizBot()

    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", bot.start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, bot.check_answer))

    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())