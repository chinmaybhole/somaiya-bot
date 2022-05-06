from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer
# google speech to txt
import gtts  
from playsound import playsound  
# Offline speech to txt engine
import pyttsx3  
from txt import clean,ans_list

engine = pyttsx3.init()  
voices = engine.getProperty('voices')

chatbot=ChatBot('trial bot')


# trainer = ListTrainer(chatbot)
trainer = ChatterBotCorpusTrainer(chatbot,read_only=True) # Change this to True if you do not want to train the model while running 

conversation = [
    'What is your name?',
    'I am Alexa',

    'What is your name?',
    'Hello, I am Alexa',

    'What is your name?',
    'Hey there I am Alexa',

    'What is your name?',
    'You can call me Alexa',

    'What is your name?',
    'People call me Alexa',

    'What is your name?',
    'call me Alexa',
]

# trainer.train(conversation)
# trainer.train("chatterbot.corpus.custom")
while True:
    inp = input('You: ')
    if inp != '0':
        response = chatbot.get_response(inp)
        ### google speech to txt online ###
        # t1 = gtts.gTTS(str(response))
        # t1.save("bot-audio.mp3")   
        # playsound("bot-audio.mp3") 
        print('Bot: ',response)
        engine.setProperty("rate", 140)
        engine.setProperty('voice', voices[1].id)   
        engine.say(response)   
        engine.runAndWait()
        # rate = engine.getProperty("rate")  
        # print(rate)        
    else:
        break

