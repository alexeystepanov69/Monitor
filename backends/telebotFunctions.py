import backends.telebotMenu as d

def helpb(*args):
    print("Внутри функции helpb")
    return "Нажмите /start"

def setReasons(bot, message):
    print("Внутри функции helpc")
    bot.send_message(message.chat.id, "Укажите причину простоя оборудования:", reply_markup = d.keyboard)
    @bot.callback_query_handler(func=lambda call: True)
    def query_handler(call):
        bot.send_message(message.chat.id, "Вы выбрали причину: " + call.data)

def about(bot, *args):
    print("Внутри функции about")
    #bot.send_message(493603071, "Если вы читаете это сообщение, значит я понял, как рассылать сообщения от бота :)")
    return "Система мониторинга производственного оборудования"

def status(*args):
    print("Внутри функции status")
    return "Система выполняется"

def report(*args):
    print("Внутри функции report")
    return "Простои не обнаружены"
