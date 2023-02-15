import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
print('Start program') 

# поиск токена для телеграмма 
def get_token(): 

    f = open('token.txt', "r") 
    token = f.read() 
    f.close() 

    return token

# Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Определяем константы этапов разговора
GENDER, AGE, PHOTO, LOCATION, BIO = range(5)

# функция обратного вызова точки входа в разговор
def start(update, _):
    # Список кнопок для ответа
    reply_keyboard = [['Boy', 'Girl']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    # Начинаем разговор с вопроса
    update.message.reply_text(
        'Меня зовут Бот, вот. Я проведу с вами беседу. '
        'Команда /cancel, чтобы прекратить разговор.\n\n'
        'Ты мальчик или девочка?',
        reply_markup=markup_key,)
    ## переходим к этапу `GENDER`, это значит, что ответ
    ## отправленного сообщения в виде кнопок будет список 
    ## обработчиков, определенных в виде значения ключа `GENDER`
    return GENDER
  
# Обрабатываем пол пользователя
def gender(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал пол пользователя
    logger.info("Пол %s: %s", user.first_name, update.message.text)
    # Следующее сообщение с удалением клавиатуры `ReplyKeyboardRemove`
    update.message.reply_text(
        'Хорошо, спасибо! А сколько лет тебе, скажи, а? '
        ' Если не хочешь говорить или стесняешься- отправь /skip',
        reply_markup=ReplyKeyboardRemove(),
    )

    # переходим к этапу `AGE`
    return AGE
    
##-=-=-=-=-=- BeLow New part about AGE -=-=-=-=-=-##
  
# Обрабатываем возраст пользователя
def age(update, _):
    # определяем возраст пользователя
    user = update.message.from_user
    # захватываем возраст пользователя
    user_age = update.message.text
    # Пишем в журнал сведения о возрасте
    logger.info(
        "Great, %s only %s years old ", user.first_name, user_age)
    # Отвечаем на сообщение о возрасте
    update.message.reply_text(
        'Класс! Желаю много раз по столько же!\n' 
        ' А фотку пришлешь, чтоб я знал как ты выглядишь?'
        ' Ну или отправь /skip, если стесняешься.'
    )
    # переходим к этапу `PHOTO`
    return PHOTO

# Обрабатываем команду /skip для возраста
def skip_age(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал сведения об отказе
    logger.info("User %s did not say own age.", user.first_name)
    # Отвечаем на сообщение с пропущенным возрастом
    update.message.reply_text(
        'Ну ладно, анонимность- тоже право!'
        'Пришли мне свою фотографию, чтоб я знал как ты '
        'выглядишь, или отправь /skip, если стесняешься.'
    )
    # переходим к этапу `PHOTO`
    return PHOTO                  
##-=-=-=-=-=- Upper New part about AGE -=-=-=-=-=-##


# Обрабатываем фотографию пользователя
def photo(update, _):
    # определяем пользователя
    user = update.message.from_user
    # захватываем фото 
    photo_file = update.message.photo[-1].get_file()
    # скачиваем фото 
    photo_file.download(f'{user.first_name}_photo.jpg')
    # Пишем в журнал сведения о фото
    logger.info("Фотография %s: %s", user.first_name, f'{user.first_name}_photo.jpg')
    # Отвечаем на сообщение с фото
    update.message.reply_text(
        'Великолепно! Делиться не буду- себе оставлю! А в каком городе ты живешь?'
        ' Напиши, или жми /skip если стесняешься.'
    )
    # переходим к этапу `LOCATION`
    return LOCATION

# Обрабатываем команду /skip для фото
def skip_photo(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал сведения о фото
    logger.info("Пользователь %s не отправил фото.", user.first_name)
    # Отвечаем на сообщение с пропущенной фотографией
    update.message.reply_text(
        ' Нет фото? Не беда. Держу пари, выглядишь ты великолепно!\n'
        'А в каком городе ты живешь? Напиши, или жми /skip если стесняешься.'
    )
    # переходим к этапу `LOCATION`
    return LOCATION

# Обрабатываем местоположение пользователя
def location(update, _):
    # определяем пользователя
    user = update.message.from_user
    # захватываем местоположение пользователя
    user_location = update.message.text
    # Пишем в журнал сведения о местоположении
    logger.info(
        " %s lives in %s ", user.first_name, user_location)
    # Отвечаем на сообщение с местоположением
    update.message.reply_text(
        'О, это круто! Может быть, я смогу как-нибудь навестить тебя!' 
        ' А расскажешь мне что-нибудь о себе?..'
    )
    # переходим к этапу `BIO`
    return BIO

# Обрабатываем команду /skip для местоположения
def skip_location(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал сведения о местоположении
    logger.info("User %s did not send a location.", user.first_name)
    # Отвечаем на сообщение с пропущенным местоположением
    update.message.reply_text(
        'Жаль! Ну ладно, а о себе то расскажешь что-нибудь? ...'
    )
    # переходим к этапу `BIO`
    return BIO

# Обрабатываем сообщение с рассказом/биографией пользователя
def bio(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал биографию или рассказ пользователя
    logger.info("Пользователь %s рассказал: %s", user.first_name, update.message.text)
    # Отвечаем на то что пользователь рассказал.
    update.message.reply_text('И на том спасибо! Надеюсь, когда-нибудь снова сможем поговорить.')
    # Заканчиваем разговор.
    return ConversationHandler.END

# Обрабатываем команду /cancel если пользователь отменил разговор
def cancel(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    # Отвечаем на отказ поговорить
    update.message.reply_text(
        ' Ну нет- так нет!'
        ' Будет скучно - пиши. Пока-пока!', 
        reply_markup=ReplyKeyboardRemove()
    )
    # Заканчиваем разговор.
    return ConversationHandler.END


if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(get_token())
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler` 
    # с состояниями GENDER, AGE, PHOTO, LOCATION и BIO
    conv_handler = ConversationHandler( # здесь строится логика разговора
        # точка входа в разговор
        
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            GENDER: [MessageHandler(Filters.regex('^(Boy|Girl)$'), gender)],
            AGE: [MessageHandler(Filters.text, age), CommandHandler('skip', skip_age)],
            PHOTO: [MessageHandler(Filters.photo, photo), CommandHandler('skip', skip_photo)],
            LOCATION: [MessageHandler(Filters.text, location), CommandHandler('skip', skip_location)],
            BIO: [MessageHandler(Filters.text & ~Filters.command, bio)]
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()