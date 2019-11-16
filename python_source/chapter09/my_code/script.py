class Question(object):
    def que(self):
        question = input("You question ")
        return question

class Answer(object):
    def ans(self, zapros):
        while True:
            user_que = zapros.que().lower()
            if user_que == "привет":
                print("и тебе привет")
            elif user_que == "как дела?":
                print("хорошо")
            elif user_que == "что делаешь?":
                print("фигнёй страдаю")
            elif user_que == "пока":
                break
            else:
                print("чё чё чё?")

user = Question()
alisa = Answer()

alisa.ans(user)