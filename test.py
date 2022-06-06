
import speech_recognition as s

sr = s.Recognizer()
sr.pause_threshold = 1
print("your bot is listening try to speak")
with s.Microphone() as m:
    print('1')
    print('2')
    sr.adjust_for_ambient_noise(m, duration=1)
    audio = sr.listen(m)
    print('3')
    query = sr.recognize_google(audio, language='eng-in')
    print(query)
