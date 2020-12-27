import speech_recognition as sr 
import time 

r = sr.Recognizer()
mic = sr.Microphone()


def transcript(transcript=''):
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        transcript = r.recognize_google(audio,language='tr-TR')
    except sr.UnknownValueError:
        time.sleep(1)
    except sr.RequestError:
        time.sleep(1)

    return transcript
    
'''
#speech to text


hey = transcript()

@app.route('/')
def hello_world():
   while 1:
        transcript()

if __name__ == '__main__':
   app.run()
'''