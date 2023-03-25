import speech_recognition as sr
import pyttsx3
import openai
import webbrowser
openai.api_key = "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"

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

r = sr.Recognizer()
mic = sr.Microphone(device_index=0)
conversation = ""
user_name = "Anant"
bot_name = "Boss"

while True:
    with mic as source:
        print("\n Listening...")
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
        print("no longer listening")

    try:
        user_input = r.recognize_google(audio)
    except:
        continue

    prompt = user_name+":"+user_input + "\n"+bot_name+":"
    conversation += prompt

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=conversation,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    response_str = response["choices"][0]["text"].replace("\n", "")
    response_str =response_str.split(
        user_name + ":" ,1)[0].split(bot_name+ ":",1)[0]

    conversation+= response_str +"\n"
    print(response_str)

    if "open youtube" in response_str.lower():
        webbrowser.open("https://www.youtube.com/")
    elif 'open google' in response_str.lower():
        webbrowser.open("https://www.google.com/")
        
    elif 'open spotify' in response_str.lower():
        webbrowser.open("https://open.spotify.com/")

    elif 'open latest news' in response_str.lower():
        webbrowser.open("https://www.hindustantimes.com/")

    elif 'open cricbuzz ' in response_str.lower():
        webbrowser.open("https://www.cricbuzz.com/")

    elif 'open career point university website' in  response_str.lower():
        webbrowser.open("https://cpukota.mastersofterp.in/iitmsv4eGq0RuNHb0G5WbhLmTKLmTO7YBcJ4RHuXxCNPvuIw=?enc=EGbCGWnlHNJ/WdgJnKH8DA==")

    elif 'exit' in response_str.lower():
        exit()
    
    engine.say(response_str)
    engine.runAndWait()
