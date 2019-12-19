import random, module

class Question(object):
    """
    запрашивает вопрос
    и сохраняет результат
    передавая Алиске
    """
    def question(self):
        """вопрос пользователя"""
        ask = input("вопрос ").lower()
        return ask

class Answer(object):
    """ответ на вопрос"""
    def answer_options(self, options):
        """вариант ответа"""
        self.options = options
        len_options = len(options)
        choose_option = random.randint(0, len_options)
        return options[choose_option]

    def answer(self, user):
        """
        запрашивает вопрос пользователя и возвращает ответ
        если вопроса нет запрашивает снова
        выходит из цикла после слова пока
        """
        while True:
            request = user.question()
            if request in module.hello:
                index = self.answer_options(module.ans_hello)
                print(index)
            elif request in module.how_you:
                index = self.answer_options(module.ans_how_you)
                print(index)
            elif request in module.none_text:
                print("дружище ты забыл задать вопрос")
            elif request in module.bye:
                index = self.answer_options(module.ans_bye)
                print(index)
                break
            else:
                print("чё чё чё?")

user = Question()
aliska = Answer()

aliska.answer(user)