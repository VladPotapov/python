# -*- coding: utf-8 -*-

class Player(object):
    """ Игрок """
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score 
    
    def __str__(self):
        rep = self.name + ":\t" + self.score 
        return rep

    def ask_yes_no(que):
        """ задаёт вопрос и принимает (да/нет)"""
        response = None
        while response not in ("y", "n"):
            response = input(que).lower()
        return response

    def ask_number(que, low, high):
        """ ввод числа из диапазона low, high """
        response = None
        while response not in range(low, high):
            response = int(input(que))
        return response

if __name__ == "__main__":
    print("вы не подключили модуль")
    input("\nEnter")