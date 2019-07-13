# -*- coding: utf-8 -*-
class Telly(object):
    def __init__(self, channel=1, volume=10, non_volume=0):
        #podkluchit fail s nastroykami
        file_settings = open('settings.txt', 'r', encoding='utf-8')
        txt_channel = file_settings.readline()
        txt_volume = file_settings.readline()
        file_settings.close()
        self.channel = channel
        self.volume = volume
        self.non_volume = non_volume
        #esli file ne pustoy zamenit zhacheniya
        if txt_channel != "":
            self.channel = txt_channel
        if txt_volume != "":
            self.volume = txt_volume
    def __str__(self):
        settings = 'Настройки\n'
        settings += 'Канал ' +str(self.channel)+ '\n'
        settings += 'Громкость ' +str(self.volume)
        return settings
        
    def ans_channel(self):
        answer = int(input('Выбрать число от 1 до 100 '))
        self.channel = answer
    def level_vol(self):
        int_vol = self.volume
        int_vol = int(int_vol)
        self.volume = int_vol
        answer = int(input('выбрать число от 0 до 100 '))
        plus_minus = input('уменьшить(-) или прибавить(+) ')
        if plus_minus == '-':
            self.volume -= answer
        elif plus_minus == '+':
            self.volume += answer
        else:
            print('вы ввели нипонятно что')
        #proverka na ogranicheniya volume
        if self.volume < 0:
            self.volume = 0
        if self.volume > 100:
            self.volume = 100
    
    #menyam znacheniya mestami
    def on_off_volume(self):
        self.volume, self.non_volume = self.non_volume, self.volume
            
def main():
    my_telly = Telly()
    choice = None
    while choice != '0':
        print(
            """
            0 выход
            1 номер канала
            2 уровень громкости
            3 выбрать канал
            4 сменить уровень громкости
            5 звук (вкл/выкл)
            """
        )
        choice = input('выбрать пункт ')
        if choice == '0':
            print('пока')
            break
        elif choice == '1':
            print(my_telly.channel)
        elif choice == '2':
            print(my_telly.volume)
        elif choice == '3':
            my_telly.ans_channel()
        elif choice == '4':
            my_telly.level_vol()
        elif choice == '5':
            my_telly.on_off_volume()
    file_settings = open('settings.txt', 'w', encoding='utf-8')
    my_channel = str(my_telly.channel)
    my_volume = str(my_telly.volume)
    file_settings.write(my_channel+'\n')
    file_settings.write(my_volume+'\n')
    file_settings.close()
main()

input('\nEnter')