from tkinter import *
from random import randint, choice


positive = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
    'Конечно же, да!', 'Ни в коем случае!', 'Абсолютно!', 'Не ожидал такого вопроса, но да!', 'А ты что думаешь?', 'Скорее всего да!', 
    'Однозначно да!', 'На пятьдесят процентов да!', 'Я бы сказал - да!']
positive_indesive = ['Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да',
    'Если понадобится - то да!', 'Ну, почему бы и нет?', 'Возможно, но это не точно!', 'Не очень уверен, но скажу - да!', 'Мой ответ - возможно да!', 
    'Да, но не спеши радоваться!', 'Да, но не более!', 'Если повезет - то да!', 'Может быть, но нужно подумать!', 'Может и да, может и нет!']
neutral = ['Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять'
    'Не могу раскрыть все секреты...', 'Лучше не рассказывать!', 'Пока ответа нет...', 'Очень интересный вопрос!', 'Даже не знаю, что сказать!', 
    'Да, но не спеши с выводами!', 'Не стоит расстраиваться!', 'Нужно еще подумать!', 'Это не мое дело!', 'Никаких комментариев!']
negative = ['Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно',
    'Ой, нет, это не для тебя!', 'Ты уверен, что хочешь это знать?', 'Лучше тебе этого не знать!', 'Нет, и еще раз - нет!', 'Вряд ли!', 
    'Серьезно? Нет!', 'Нет, и я тебе скажу почему - потому что нет!', 'Не стоит даже задумываться!', 'Даже не думай!', 'Ты никогда не узнаешь ответа!']

def predictor():
    text = (question_tf.get())
    num = randint(1, 4)
    if num == 1:
        message.set('Предсказатель думает!!!')
        window.after(5000, lambda: mess.set(choice(positive)))
    elif num == 2:
        message.set('Связываюсь с космосом!!!')
        window.after(5000, lambda: mess.set(choice(positive_indesive)))
    elif num == 3:
        message.set('Сейчас гляну в магический шар!!!')
        window.after(5000, lambda: mess.set(choice(neutral)))
    elif num == 4:
        message.set('Сейчас раскину карты!!!')
        window.after(5000, lambda: mess.set(choice(negative)))
        
def clearTextInput():
    question_tf.delete("0", END)
    answer_tf.delete("0", END)
    magic_tf.delete("0", END)
    
def exit_programm():
    window.destroy()  
    
window = Tk()
window.title('Программа "Предказатель"')
window.geometry('600x400')
window["bg"] = "snow3"

description_lb = Label(window, text='Я Великий Предсказатель,\nзадай свой вопрос и получи ответ.', borderwidth=1, relief='ridge', bg='Silver', fg='blue', font=("Arial", 15))
description_lb.place(x=130, y=10, width=340, height=60)

question_lb = Label(window, text='Введите свой вопрос:', borderwidth=1, relief='ridge', bg='PeachPuff1', fg='DarkGreen', font=("Arial", 12))
question_lb.place(x=20, y=80, width=180, height=35)

answer_lb = Label(window, text='Мой ответ:', borderwidth=1, relief='ridge', bg='PeachPuff1', fg='DarkGreen', font=("Arial", 13))
answer_lb.place(x=20, y=170, width=180, height=35)

question_tf = Entry(window, borderwidth=1, relief='ridge', bg='LightCyan', fg='DarkGreen' ,font=("Arial", 16))
question_tf.place(x=230, y=80, width=350, height=35)

mess = StringVar()
answer_tf = Entry(window, textvariable=mess, borderwidth=1, relief='ridge', bg='LightCyan', width=20, fg='DarkGreen', font=("Arial", 16))
answer_tf.place(x=230, y=170, width=350, height=35)

message = StringVar()
magic_tf = Entry(window, textvariable=message, justify=CENTER, borderwidth=1, relief='ridge', bg='LightCyan', width=20, fg='red', font=("Arial", 20))
magic_tf.place(x=90, y=270, width=420, height=60)

question_btn = Button(window, text='Предсказать', borderwidth=1, relief='ridge', bg='burlywood2', fg='red', font=("Arial", 12), command=predictor)
question_btn.place(x=230, y=120, width=110, height=40)

answer_btn = Button(window, text='Очистить', borderwidth=1, relief='ridge', bg='burlywood2', fg='red', font=("Arial", 12), command=clearTextInput)
answer_btn.place(x=230, y=220, width=110, height=40)

exit_btn = Button(window, text='Выход', borderwidth=1, relief='ridge', bg='Silver', fg='blue', font=("Arial", 12), command=exit_programm)
exit_btn.place(x=500, y=350, width=80, height=40)

window.mainloop()