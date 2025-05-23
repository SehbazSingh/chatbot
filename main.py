# importing modules
import ollama
import pyttsx3
import speech_recognition as sr
import webbrowser
import time
import requests	
from plyer import notification






# timer
def set_timer(minutes):
    seconds = minutes * 60
    time.sleep(seconds)
    print("Timer finished!")







# enabled voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Changing index changes voices but only 0 and 1 are working here
engine.setProperty('rate', 140)  # Speed percent (can go over 100)
engine.setProperty('volume', 0.9) 



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
# use speak("text") to hear the audio.



# getting news from bbc

def NewsFromBBC():
	
	# BBC news api
	# following query parameters are used
	# source, sortBy and apiKey
	query_params = {
	"source": "bbc-news",
	"sortBy": "top",
	"apiKey": "your api key"
	}
	main_url = " https://newsapi.org/v1/articles"

	# fetching data in json format
	res = requests.get(main_url, params=query_params)
	open_bbc_page = res.json()

	# getting all articles in a string article
	article = open_bbc_page["articles"]

	# empty list which willwhat is 
	# contain all trending news
	results = []
	
	for ar in article:
		results.append(ar["title"])
		
	for i in range(len(results)):
		
		# printing all trending news
		print(i + 1, results[i])

	#to read the news out loud for us
	from win32com.client import Dispatch
	speak = Dispatch("SAPI.Spvoice")
	speak.Speak(results)	

# getting audio input from user
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:  
        print("Unable to recognise ,Switching to keyboard mode.")
        speak("Unable to recognise  ,Switching to keyboard mode")  
        user=input("User :")
        return "None"
    return query

speak("HI , How can i help you?")
print("HI , How can i help you?")
while True:
    user=takeCommand()
    # user = input("User :")
    
    if "view satellite images" in user:
        speak("Opening satellite images")
        print("Opening satellite images")
        webbrowser.open("https://worldview.earthdata.nasa.gov/")
    
        time.sleep(10)
         
        
    elif "open spotify" in user:
        speak("Opening spotify")
        print("Opening Spotify")
        webbrowser.open("https://spotify.com")
        break
    
    
    elif "news" in user:
        NewsFromBBC()


    elif "search in Spotify for" in user:
        song = user.replace("search in Spotify for ", "")
        print("searching on Spotify for ", song)
        speak("searching on Spotify for "+ song)
        webbrowser.open("https://open.spotify.com/search/" + song)
        break
    
    elif "search in Google for" in user:
        query = user.replace("search in Google for ", "")
        print("searching on Google for ", query)
        speak("searching in Google for "+query)
        webbrowser.open("https://www.google.com/search?q=" + query)
        break
    
    
    elif "search in YouTube for" in user:
        video = user.replace("search in YouTube for ", "")
        print("searching on youtube for ", video)
        speak("searching in YouTube for "+video)
        webbrowser.open("https://www.youtube.com/results?search_query=" + video)
        break
    
    elif "open Quora" in user:
        print("opening Quora")
        speak ("opening Quora")
        webbrowser.open("https://www.quora.com/")
        break
    
    elif "search in Quora for" in user:
        query=user.replace("search in Quora for","")
        print("Searching in Quora for ",query)
        speak("Searching in Quora for"+query)
        webbrowser.open("https://www.quora.com/search?q="+query)
        break
 
        
    elif "do some shopping" in user:
        print("opening Amazon.in")
        speak("opening Amazon.in")
        webbrowser.open("https://www.amazon.in/")
        break
        
        
    elif "search in Amazon for " in user:
        query=user.replace("search in Amazon for","")
        webbrowser.open("https://www.amazon.in/s?k="+query)
        print("Searching in Amazon for ",query)
        speak("Searching in Amazon for"+query)
        break
    
    elif "create an image of " in user:
        query=user.replace("create an image of ","")
        webbrowser.open("https://picsart.com/create/editor?category=photos&app=t2i&prompt="+query)
        print("Creating an image of ",query)
        speak("Creating an image of "+query)
        break
    
    elif "weather" in user:
        print("opening weather report.")
        speak("opening weather report.")
        webbrowser.open("https://www.accuweather.com/")
        break
    
    elif "switch to focus mode" in user:
        print ("switching to focus mode, a timer have been set of 15 minutes.")
        speak("switching to focus mode , a timer have been set of 15 minutes..")
        set_timer(1)
        speak("Alert  time over.")
        notification.notify(
		title = "TIME OUT",
		message="Focus mode is over now.." ,
		
		# displaying time
		timeout=10
        )


    elif "what is in my to do list" in user:
        print("your to do list of today is:")
        todolist=open("todolist.txt","r")
        a=todolist.read()
        print(a)
        speak("your to do list of today include")
        speak(a)


    elif "add to my to do list" in user:
        todo =user.replace("add to to do list  ","")
        f = open("todolist.txt", "a")
        f.write(todo)
        f.write("\n")
        f.close()
        speak("your to do list is updated!")
        print("your to do list is updated")
        
        
    elif "shutdown the PC" in user:
        print("Are you sure you want to shutdown the pc ,yes or no ")
        speak("Are you sure you want to shutdown the pc ,yes or no ")

        if user == "yes":
            print("The pc is going to shutdown in 10s")
            speak("The pc is going to shutdown in 10s")
            import os
            os.system("shutdown /s /t 10")
        
        else:
            print("command denied")
            speak("command denied")
            
            
    
    elif " in Wikipedia" in user:
        import wikipedia
        a = user.replace("search in Wikipedia for", "")
        result = wikipedia.summary(a, sentences=2)
        print(result)
        speak(result)
        
    elif "exit the program" in user:
        time.sleep(2)
        print("Bye")
        speak("good Byee")
        
        break
    
    else:
        import ollama
        print("Gearing up mind............")
        speak("Gearing up mind")



        model_name = 'orca-mini'  # Ensure the model name is a string

        # Function to generate a response
        def generate_response(prompt):
            response = ollama.chat(model=model_name, messages=[{'role': 'user', 'content': prompt}])
            return response['message']['content']

        if __name__ == "__main__":
            user_prompt = user
            response = generate_response(user_prompt)
            print("Ollama: ", response)

        

        print(response)
        speak(response)
        