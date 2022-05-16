from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading
import datetime
import time
import winsound
import webbrowser
import numpy as np
import cv2
import pyautogui
import sys

import Gesture_Controller

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:", date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            winsound.PlaySound("sound.mp3", winsound.SND_ASYNC)
            break


def actual_time():
    #set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    #alarm(set_alarm_timer)
    print(1)


def gui():
    engine = pp.init()

    voices = engine.getProperty('voices')
    print(voices)

    engine.setProperty('voice', voices[0].id)


    def speak(words):
        engine.say(words)
        engine.runAndWait()


# pyttsx3
    bot = ChatBot("ICHIGO Bot")

    convo = open('chat.txt', 'r').readlines()

    trainer = ListTrainer(bot)

# now training the bot with the help of trainer

    trainer.train(convo)



    main = Tk()

    main.geometry("500x550")

    main.title("ICHIGO")

    img = PhotoImage(file="bot.png")

    #photoL = Label(main, image=img)

    #photoL.pack(pady=5)


# takey query : it takes audio as input from user and convert it to string..

    def takeQuery():
        sr = s.Recognizer()
        sr.pause_threshold = 1
        print("your bot is listening try to speak")
        with s.Microphone() as m:
            print('1')
            try:
                print('2')
                sr.adjust_for_ambient_noise(m, duration=1)
                audio = sr.listen(m)
                print('3')
                query = sr.recognize_google(audio, language='eng-in')
                print(query)
                if query=='stop':
                    return
                    print('yes')



                #speak(query)
                textF.delete(0, END)
                textF.insert(0, query)
                ask_from_bot()
            except Exception as e:
                print(e)
                print("not recognized")


    def ask_from_bot():
        query = textF.get()
        if query=='Google':
            webbrowser.get(chrome_path).open('https://www.google.com/')
        if query=='launch gesture recognition' :
            gc = Gesture_Controller.GestureController()
            t = threading.Thread(target=gc.start)
            t.start()
        if query=='YouTube':
            webbrowser.get(chrome_path).open('https://www.youtube.com/')
        if query=='set reminder':
            webbrowser.get(chrome_path).open('https://keep.google.com/u/0/#reminders')
        if query=='take notes':
            webbrowser.get(chrome_path).open('https://keep.google.com/u/0/')
        if query=='take screenshot':
            image = pyautogui.screenshot()
            image = cv2.cvtColor(np.array(image),
                                 cv2.COLOR_RGB2BGR)
            cv2.imwrite("image1.png", image)
        answer_from_bot = bot.get_response(query)
        msgs.insert(END, "you : " + query)
        print(type(answer_from_bot))
        msgs.insert(END, "ICHIGO : " + str(answer_from_bot))
        speak(answer_from_bot)
        #if query=='stop':
            #sys.exit()
        textF.delete(0, END)
        msgs.yview(END)


    frame = Frame(main)

    sc = Scrollbar(frame)
    msgs = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)

    sc.pack(side=RIGHT, fill=Y)

    msgs.pack(side=LEFT, fill=BOTH, pady=10)

    frame.pack()

# creating text field

    textF = Entry(main, font=("Courier", 10))
    textF.pack(fill=X, pady=10)

    btn = Button(main, text="Ask Ichigo", font=(
        "Courier", 10),bg='red', command=ask_from_bot)
    btn.pack()


# creating a function
    def enter_function(event):
        btn.invoke()


# going to bind main window with enter key...

    main.bind('<Return>', enter_function)


    def repeatL():
        while True:
            takeQuery()


    t = threading.Thread(target=repeatL)

    t.start()

    main.mainloop()


