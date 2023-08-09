import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def get_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak("The current time is " + current_time)

def get_date():
    current_date = datetime.datetime.now().strftime("%d %B %Y")
    speak("The current date is " + current_date)

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Sorry, I didn't catch that. Could you repeat?")
        return "None"
    return query

# Function to provide a language translation
def translate_language():
    """Function to translate text from one language to another."""
    speak("Sure, please provide the text you want to translate.")
    text_to_translate = take_command()
    speak("Which language should I translate it to?")
    target_language = take_command()
    # Use a translation API to translate the text to the specified language

def find_nearby_places():
    """Function to search for nearby places based on user's location."""
    speak("Sure, what type of places are you looking for?")
    place_type = take_command()
    speak("Please provide your current location.")
    user_location = take_command()
    # Use a location-based service or API to find nearby places


    # >>>>>>>>>>>>>>

    
def send_email(to, content):
    """Function to send an email."""
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_email@gmail.com', 'your_password')
    server.sendmail('your_email@gmail.com', to, content)
    server.close()

def search_web(query):
    """Function to search the web using the default browser."""
    speak("Sure, I'll search that for you.")
    wb.open_new_tab('https://www.google.com/search?q=' + query)

def get_system_info():
    """Function to get CPU usage and battery information."""
    cpu_usage = psutil.cpu_percent()
    battery = psutil.sensors_battery()
    speak(f"CPU usage is {cpu_usage}%")
    speak(f"Battery is at {battery.percent}%")

# Function to set an alarm
def set_alarm():
    """Function to set an alarm for a specific time."""
    speak("Sure, when should I set the alarm?")
    alarm_time = take_command()
    # Parse alarm_time and set an actual alarm using a library like 'time' or 'schedule'

# Function to tell the weather
def tell_weather():
    """Function to fetch and speak the current weather."""
    # Use a weather API to get the weather information for the user's location
    weather_info = "The weather today is sunny with a high of 25°C."
    speak(weather_info)
# ... (import statements and previous code)

# Function to open a specific application
def open_application(app_name):
    """Function to open a specific application on the computer."""
    app_paths = {
        'notepad': 'C:\\Windows\\system32\\notepad.exe',
        'calculator': 'C:\\Windows\\system32\\calc.exe',
        # Add more application paths here
    }
    if app_name in app_paths:
        os.startfile(app_paths[app_name])
    else:
        speak("Sorry, I don't have information for that application.")

# Function to get driving directions
def get_directions():
    """Function to provide driving directions using a location API."""
    speak("Sure, please provide the starting and ending locations.")
    start_location = take_command()
    end_location = take_command()
    # Use a location API to fetch and provide driving directions

def tell_fact():
    """Function to provide a random interesting fact."""
    # Fetch facts from an API or a predefined list
    random_fact = "Did you know that honey never spoils?"
    speak(random_fact)

# Function to create and manage a to-do list
def manage_todo_list():
    """Function to create, view, and manage a to-do list."""
    speak("Welcome to your to-do list. Would you like to view your current tasks or add a new one?")
    choice = take_command()
    if 'view' in choice:
        # Display the existing to-do list
        speak("Here are your current tasks:")
        # Fetch and read tasks from a to-do list file
    elif 'add' in choice:
        speak("What task would you like to add?")
        new_task = take_command()
        # Append the new task to the to-do list file

    # <<<<<<<<<<<<<<

if __name__ == "__main__":
    speak("Initializing JARVIS...")

    while True:
        query = take_command().lower()

        if "what's the time" in query:
            get_time()

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>

        elif 'to-do list' in query:
            manage_todo_list()

        elif 'nearby places' in query:
            find_nearby_places()

        elif 'translate language' in query:
            translate_language()

        elif 'fact' in query:
            tell_fact()

        elif 'set alarm' in query:
            set_alarm()
        elif 'open app' in query:
            app_name = query.replace("open app", "").strip()
            open_application(app_name)

        elif 'directions' in query:
            get_directions()

        elif 'weather' in query:
            tell_weather()

        elif 'system info' in query:
            get_system_info()
        elif 'email' in query:
            try:
                speak("What should I say in the email?")
                content = take_command()
                to = 'recipient_email@gmail.com'
                send_email(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I couldn't send the email.")
                # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        elif "today's date" in query:
            get_date()
        elif 'search' in query:
            speak("What should I search for?")
            search_query = take_command()
            wb.open_new_tab("https://www.google.com/search?q=" + search_query)
        elif 'wikipedia' in query:
            speak("What should I search on Wikipedia?")
            wiki_query = take_command()
            result = wikipedia.summary(wiki_query, sentences=2)
            print(result)
            speak(result)
        elif 'open website' in query:
            speak("Which website should I open?")
            website = take_command()
            wb.open_new_tab("https://" + website + ".com")
        elif 'tell me a joke' in query:
            speak(pyjokes.get_joke())
        elif 'play music' in query:
            music_dir = 'C:\\Music'  # Change to your music directory
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'exit' in query:
            speak("Goodbye!")
            exit()
        else:
            speak("I'm sorry, I don't understand that command.")
