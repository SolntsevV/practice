import pyautogui as pag
import os, time
import pyperclip, keyboard

class Notepad:

    def __init__(self):
        os.startfile('notepad.exe')
        self.poem = """
Варкалось. Хливкие шорьки
Пырялись по наве,
И хрюкотали зелюки,
Как мюмзики в мове.

О, бойся Бармаглота, сын!
Он так свирлеп и дик!
А в глу́ше ры́мит исполин —
Злопастный Брандашмыг!

Но взял он меч, и взял он щит,
Высоких полон дум.
В глущобу путь его лежит
Под дерево Тумтум.

Он стал под дерево и ждёт.
И вдруг граахнул гром —
Летит ужасный Бармаглот
И пылкает огнём!

Раз-два, раз-два! Горит трава,
Взы-взы — стрижает меч,
Ува! Ува! И голова
Барабардает с плеч!

О светозарный мальчик мой!
Ты победил в бою!
О храброславленный герой,
Хвалу тебе пою!

Варкалось. Хливкие шорьки
Пырялись по наве.
И хрюкотали зелюки,
Как мюмзики в мове.
        """

    def paste(self, text: str):
        pyperclip.copy(text)
        keyboard.press_and_release('ctrl + v')
    
    def save(self):
        keyboard.press_and_release('ctrl + s')


    def barmaglot(self):
        self.paste(self.poem)

        self.save()

        time.sleep(0.1)
        self.paste('barmaglot.txt')
        
        time.sleep(1)
        keyboard.press_and_release('ctrl + l')
        
        time.sleep(1)
        # self.paste('Desktop')
        keyboard.press_and_release('enter')

        time.sleep(1)
        keyboard.press_and_release('enter')
        
        keyboard.press_and_release('enter')
        keyboard.press_and_release('enter')
        time.sleep(0.1)
        self.paste('Редактируем файл')

        time.sleep(0.1)
        self.save()
        keyboard.press_and_release('tab')
        keyboard.press_and_release('enter')

        time.sleep(0.1)
        self.paste('new_barmaglot.txt')

        keyboard.press_and_release('enter')
        keyboard.press_and_release('enter')

        keyboard.press_and_release('alt + f4')

        return True

