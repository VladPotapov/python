import random
hello = ["привет", "прив", "хай", "здравствуйте", "здравствуй", "здрасти", "здорово", "здоровенько"]
how_you = ["как дела?", "как ты?", "чё как?", "как оно?" "как настроение?", "как настрой?"]
bye = ["пока", "до встречи", "удачи", "до скорого", "прощай", "гудбай", "чао" "чао бомбино", "покеда", "покедова"]
none_text = ["", " "]

ans_hello = ["и тебе привет", "о привет давно не виделись", "ну привет коль не шутишь", "привет дружище", "слава богу ты пришёл"]
ans_how_you = ["отлично", "хорошо", "нормально", "плохо", "неплохо", "отвратительно", "ок", "всё окей", "лучше всех", "всё супер", "супер"]
ans_bye = ["и тебе пока", "ну давай бывай", "удачи тебе", "бывай дружище"]

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
            if request in hello:
                index = self.answer_options(ans_hello)
                print(index)
            elif request in how_you:
                index = self.answer_options(ans_how_you)
                print(index)
            elif request in none_text:
                print("дружище ты забыл задать вопрос")
            elif request in bye:
                index = self.answer_options(ans_bye)
                print(index)
                break
            else:
                print("чё чё чё?")

if __name__ == "__main__":
    print("Подключите модуль к файлу")