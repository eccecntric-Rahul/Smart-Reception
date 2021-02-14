import datetime
import pyttsx3 as pyt
import speech_recognition as sp
import pushbullet as p
import re
import time

#setting up pyttsx3
core=pyt.init('sapi5')
voices =core.getProperty('voices')
core.setProperty('voices',voices[1].id)
core.setProperty('rate',150)

#setting up details of creoators
def access(acc):
    if acc=='code 0001':
        speak('welcome master ')
        speak('please say the name of technology')
        tech=takeresp().lower()
        speak('please say the name of faculty')
        fac=takeresp().lower()
        speak('please say the number of the faculty')
        no_=takeresp().lower()
        #ky.__setitem__(tech, fac)
        #phn.__setitem__(fac, no_)
    elif acc=='code 0002':
        speak('My master is Rahul Kumar ')
        speak('My name is hinata and i am a smart receptionist')


#setting up speak function
def speak(audio):
    core.say(audio)
    core.runAndWait()
    print(audio)

#quit function
def quity(a):
    if 'quit'  in a:
        exit()
    elif 'exit' in a:
        exit()
    elif 'terminate' in a:
        exit()
    elif 'stop' in a:
        exit()
    elif  'creat' in a:
        speak('Rahul Kumar and Deepanshu Tyagi created me ')
    elif 'your name' in a:
        speak("My name is Hinata")
    elif 'date' in a:
        hour= datetime.date.today()
        speak(hour)

#setting up listening feature
def takeresp():

    resp = sp.Recognizer()
    with sp.Microphone() as source :
        print('listening.....')
        resp.pause_threshold=1
        audio = resp.listen(source)
    try:
        print("Recognizing...")
        query = resp.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "1"
    quity(query)
    access(query)
    return query

# setting up phone no. taking feature
def phnno(query):
    if type(query)==str:
        speak("please tell me your mobile number ")
        phno = takeresp().lower()
        return phno

def cont():
    speak('Do you want to continue then say Yes or No to exit if you dont reply the program will restsart in 3 seconds ')
    a=takeresp().lower()
    quity(a)
    if 'yes' in a:
        return 1
    elif 'no' in a:
        return 0
    else:
        time.sleep(5)
        return 1
def main():
    ky = {"cloud": "rahul", "iot": "deepanshu"}
    phn = {"deepanshu": "9868434198", "rahul": "9015709221"}
    f = p.Pushbullet("o.3W0inOrP9mAMSTJ4OwD9jegih4rG2PmF")
    a=1
    while a==1:
                query='1'
                speak('hello sir, how may i help you')
                while query=='1':
                    query=takeresp().lower()
                    respo=query
                phno=phnno(query)
                phno = re.sub(r"\s+","", phno, flags=re.UNICODE)
                pho=phno
                if len(pho)==10 :
                    speak('PLease wait on the couch you will recieve a message for what to do next ')
                f.push_sms(f.devices[0],pho,"open this link and fill the google form " + "https://docs.google.com/forms/d/e/1FAIpQLSfLc9AJJ9Hjb4F4vjZy96BT7zgw40HwV7j00UXmUylzzGcTDA/viewform?usp=sf_link" + "go in room no.")
                for key in ky:
                    if key in respo:
                        f.push_sms(f.devices[0], phn[ky[key]], "you have a client waiting in room ")
                        print(phno,phn[ky[key]])

                a=cont()

if __name__=='__main__':
    main()
