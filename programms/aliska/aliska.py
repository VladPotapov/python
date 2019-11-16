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
    def answer(self, user):
        """
        запрашивает вопрос пользователя
        и возвращает ответ
        если вопроса нет запрашивает снова
        выходит из цикла после слова пока
        """
        while True:
            request = user.question()
            if request == "привет":
                print("И тебе привет")
            elif request == "":
                print("дружище ты забыл задать вопрос")
            elif request == "пока":
                print("до встречи")
                break
            else:
                print("чё чё чё?")
    

user = Question()
aliska = Answer()

aliska.answer(user)