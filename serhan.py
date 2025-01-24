import speech_recognition

def kontr():
    mikrofon=speech_recognition.Microphone()
    kayit=speech_recognition.Recognizer()

    with mikrofon as ses:
        kayit.adjust_for_ambient_noise(ses)

        serhan=kayit.listen(ses)
        try:

            return kayit.recognize_google(serhan, language="tr-TR")
        except:
            return "Anlamadım, Tekrarla"

def konen():
    mikrofon=speech_recognition.Microphone()
    kayit=speech_recognition.Recognizer()

    with mikrofon as ses:
        kayit.adjust_for_ambient_noise(ses)

        serhan=kayit.listen(ses)
        try:

            return kayit.recognize_google(serhan, language="en-US")
        except:
            return "i dont get it, please repeat it"



if __name__ == "__main__":

    print("Sesiniz şimdi kaydediliyor")

    gosling=kontr()

    print(gosling)










