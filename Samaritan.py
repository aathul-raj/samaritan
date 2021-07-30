# imports speech recognition library
# import speech_recognition as sr

import speech_recognition as sr

from text_Finder import Finder

import pyautogui as gui

# import pyttsx3 for text to speech, random library for random numbers and webbrowser module

import pyttsx3, random, webbrowser, datetime, os, sys, socket, requests, time

from bs4 import BeautifulSoup
        
# This makes it talk


def speak(audio):
    print('Samaritan:', audio)
    engine.setProperty('voice', voices[len(voices) - 1].id)
    engine.say(audio)
    engine.runAndWait()


def dateTime(section):
    currentDT = datetime.datetime.now()
    if section == 'date':
        date = currentDT.strftime("%b %d, %Y")
        return date

    if section == 'time':
        time = currentDT.strftime("%H:%M %p")
        return time


# Def for ending sequence


def end():
    greeting = random.randint(1, 5)
    if 'shut down' in task:
        speak('Shutting down...')
    elif greeting == 1:
        speak('Okay')
        speak('Have a good day!')
    elif greeting == 2:
        speak('All right then.')
        speak('Good bye!')
    elif greeting == 3:
        speak('So long, see you later.')
    elif greeting == 4:
        speak('Farewell, and take care.')
    elif greeting == 5:
        speak('Bye!')


# Takes in voice input from user

r = sr.Recognizer()

mic = sr.Microphone()

engine = pyttsx3.init()
voices = engine.getProperty('voices')


def myCommand():
    with mic as source:
        print('Listening...')
        r.adjust_for_ambient_noise(source)
        engine.runAndWait()
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')

    except sr.UnknownValueError:
        print('Waiting...')
        query = 'void'

    return query

# Checks for internet

def internet(host="8.8.8.8", port=53, timeout=3):
  try:
    socket.setdefaulttimeout(timeout)
    socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
    print('Connected...')
    return True
  except socket.error as ex:
    speak('Connection failed...')
    speak('You do not have internet. Check your connection.')
    time.sleep(6)
    sys.exit()
    return False
internet()

# Saves user's name and greets them print(statement)

name = 'Athul'

statement = str(dateTime('time'))

print(statement)

print('System is running and operational...')

statementLen = len(statement)

if statement[statementLen - 2] == 'A':
    hourTick = statement[0 : 2]
    hourTick = int(hourTick)
    if hourTick < 4:
        speak('Wow, you are up late!')
    else:
        speak('Good morning!')

elif statement[statementLen - 2] == 'P':
    hourTick = statement[0 : 2]
    hourTick = int(hourTick)
    if hourTick < 16:
        speak('Good afternoon!')
    elif hourTick < 19:
        speak('Good evening!')
    elif hourTick < 25:
        speak('Hope you have had a good day.')

hiDecider = random.randint(1, 3)

if hiDecider == 1:
    speak('What do you have for me?')
elif hiDecider == 2:
    speak('How may I assist you?')
elif hiDecider == 3:
    speak('What is it that you require, sir?')

# Primary loop for running system

while True:

    task = myCommand()
    task = task.lower()

    # Function for if user is silent
    runCount = 0
    
    if 'void' in task:
        task = myCommand()
        task = task.lower()

    # Says whatever you want it to say

    if 'talk' in task:
        speak('What would you like me to say? ')
        n = myCommand()
        speak('Ok! ' + n)

    elif 'pause' in task:
        print('Pausing...')
        speak('Simply say okay or wake up to start me again.')
        runCount = 0
        while runCount == 0:
            userStart = myCommand()
            userStart = userStart.lower()
            if 'wake up' in userStart:
                break
            elif 'ok' in userStart:
                break
            elif 'okay' in userStart:
                break
        speak('Welcome back sir.')

    elif 'wait' in task:
        print('Pausing...')
        speak('Simply say okay or wake up to start me again.')
        runCount = 0
        while runCount == 0:
            userStart = myCommand()
            userStart = userStart.lower()
            if 'wake up' in userStart:
                break
            elif 'ok' in userStart:
                break
            elif 'okay' in userStart:
                break
        speak('Welcome back sir.')

    elif 'sleep' in task:
        print('Pausing...')
        speak('Simply say okay or wake up to start me again.')
        runCount = 0
        while runCount == 0:
            userStart = myCommand()
            userStart = userStart.lower()
            if 'wake up' in userStart:
                break
            elif 'ok' in userStart:
                break
            elif 'okay' in userStart:
                break
        speak('Welcome back sir.')

    # Morning brief

    elif 'news' in task:

        try:
            soup = BeautifulSoup
            news_url = "https://news.google.com/news/rss"
            Client = urlopen(news_url)
            xml_page = Client.read()
            Client.close()
            soup_page = soup(xml_page,"xml")
            news_list = soup_page.findAll("item")
            for news in news_list[:15]:
                speak(news.title.text.encode('utf-8'))
        except Exception as e:
                speak(e)


    # Music

    elif 'music' in task:
        try:
            print('Opening Spotify...')
            os.startfile('C:Users\sures\AppData\Roaming\Spotify\Spotify.exe')

        except FileNotFoundError:
            print('Opening Youtube Music...')
            webbrowser.open('https://music.youtube.com/')

    elif 'spotify' in task:
        try:
            print('Opening Spotify...')
            os.startfile('C:Users\sures\AppData\Roaming\Spotify\Spotify.exe')

        except FileNotFoundError:
            print('Spotify can not be found.')
            print('Opening Youtube Music...')
            webbrowser.open('https://music.youtube.com/')

    elif 'songs' in task:
        try:
            print('Opening Spotify...')
            os.startfile('C:Users\sures\AppData\Roaming\Spotify\Spotify.exe')

        except FileNotFoundError:
            print('Opening Youtube Music...')
            webbrowser.open('https://music.youtube.com/')

    # Browser functions

    elif 'la liga' in task:
        print('Opening La Liga table...')
        webbrowser.open(
            'https://www.google.com/search?client=firefox-b-1-d&q=la+liga#sie=lg;/g/11ff1xzn64;2;/m/09gqx;st;fp;1;;')
        
    elif 'dashboard' in task:
        print('Pulling up your Google dashboard...')
        webbrowser.open('https://news.google.com/?hl=en-US&gl=US&ceid=US%3Aen')

    elif 'images' in task:
        
        question = Finder.noEnd(task, 'of')

        print('Opening Google Images...')
        webbrowser.open('https://www.google.com/search?tbm=isch&q=' + question)

    elif 'pictures' in task:
        
        question = Finder.noEnd(task, 'of')

        print('Opening Google Images...')
        webbrowser.open('https://www.google.com/search?tbm=isch&q=' + question)

    elif 'amazon' in task:
        loopKill = True
        speak('Got anything specific in mind?')
        specific = myCommand()

        if 'yes' in specific:

            product = Finder.noEnd(specific, 'a ')
            if product == None:
                product = Finder.noEnd(specific, 'an')
                if product == None:
                    product = Finder.noEnd(specific, 'some')
                    if product == None:
                        product = Finder.noEnd(specific, 'the')
                        if product == None:
                            loopKill = False

            if loopKill == False:
                speak('Tell me exactly what it is, please.')
                product = myCommand()
            if product[len(product) - 1] == 's':
                print('Opening ' + product + ' on Amazon...')
            else:
                print('Opening ' + product + 's on Amazon...')
            webbrowser.open('https://www.amazon.com/s?k=' + product)

        elif 'yeah' in specific:

            product = Finder.noEnd(specific, 'a ')
            if product == None:
                product = Finder.noEnd(specific, 'an')
                if product == None:
                    product = Finder.noEnd(specific, 'some')
                    if product == None:
                        product = Finder.noEnd(specific, 'the')
                        if product == None:
                            loopKill = False

            if loopKill == False:
                speak('Tell me exactly what it is, please.')
                product = myCommand()
            if product[len(product) - 1] == 's':
                print('Opening ' + product + ' on Amazon...')
            else:
                print('Opening ' + product + 's on Amazon...')
            webbrowser.open('https://www.amazon.com/s?k=' + product)
            
        else:            
            print('Opening Amazon...')
            webbrowser.open('https://www.amazon.com/')

    elif 'calendar' in task:
        print('Opening Google Calendar...')
        webbrowser.open('https://calendar.google.com/calendar/r?pli=1')

    elif 'maps' in task:
        speak('Do you have a specific address in mind?')
        loc = myCommand()
        loc = loc.lower()
        if 'no' in loc:
            print('Opening Google Maps...')
            webbrowser.open('https://www.google.com/maps/')
        elif 'nah' in loc:
            print('Opening Google Maps...')
            webbrowser.open('https://www.google.com/maps/')

        elif 'nope' in loc:
            print('Opening Google Maps...')
            webbrowser.open('https://www.google.com/maps/')

        elif 'not' in loc:
            print('Opening Google Maps...')
            webbrowser.open('https://www.google.com/maps/')

        elif 'yeah' or 'yes' in loc:
            speak('Do you want to speak the name?')
            ansLoc = myCommand()
            ansLoc = ansLoc.lower()
            if 'void' in ansLoc:
                speak('You have timed out.')

            elif ansLoc[0] == 'y':
                speak('Say just the name, nothing more.')
                location = myCommand()
                print('Opening the location in Google Maps...')
                webbrowser.open('https://www.google.com/maps/place/' + location)

            elif ansLoc[0] == 's':
                speak('Say just the name, nothing more.')
                location = myCommand()
                print('Opening the location in Google Maps...')
                webbrowser.open('https://www.google.com/maps/place/' + location)

            elif ansLoc[0] == 'n':
                speak('Enter just the address.')
                location = input(name + ': ')
                print('Opening the location in Google Maps...')
                webbrowser.open('https://www.google.com/maps/place/' + location)

        elif 'void' in loc:
            speak('You have timed out.')


    elif 'youtube' in task:
        print('Opening Youtube...')
        webbrowser.open('https://www.youtube.com/')

    elif 'barca' in task:
        print('Opening Barca Blaugranes...')
        webbrowser.open('https://www.barcablaugranes.com/')

    elif 'premier league' in task:
        print('Opening Premier League table...')
        webbrowser.open(
            'https://www.google.com/search?client=firefox-b-1-d&ei=gSeZXYXsM8rQsAWQoKTQAw&q=premier+league&oq=premier+league&gs_l=psy-ab.3..0i131i67l6j0i67j0i131i67j0i67j0i131i67.2771.3681..3920...0.2..0.109.777.8j1......0....1..gws-wiz.......0i71j0.fwxyiMYFtJk&ved=0ahUKEwjFsNSYo4blAhVKKKwKHRAQCToQ4dUDCAo&uact=5')

    elif 'games' in task:
        print('Opening 6969 Unblocked Games...')
        webbrowser.open('https://sites.google.com/site/unblockedgamessms6969/')

    elif 'code' in task:
        print('Opening Repl...')
        webbrowser.open('https://repl.it/repls')

    elif 'weather' in task:
        print('Opening the weather on Google...')
        webbrowser.open('https://www.google.com/search?client=firefox-b-1-d&q=weather')

    elif 'classroom' in task:
        print('Opening your Google Classroom...')
        webbrowser.open('https://classroom.google.com/u/0/h')
        
    elif 'search' in task:

        question = Finder.noEnd(task, 'search')
        
        print('Opening Google...')
        webbrowser.open('https://www.google.com/search?-b-1-d&q=' + question)

    elif 'get to' in task:

        target = Finder.noEnd(task, 'to ')
        if 'from' in target:
            home = Finder.noEnd(target, 'from ')
            target = Finder.searcher(target, target[0], ' from')
            target = target[0 : len(target) - 5]
            speak("I'm pulling up the directions right now.")
            print('Opening Google Maps...')
            webbrowser.open('https://www.google.com/maps/dir/' + home + '/' + target)
        else:
            speak('Where are you starting from?')
            home = myCommand()
            speak("I'm pulling up the directions right now.")
            print('Opening Google Maps...')
            webbrowser.open('https://www.google.com/maps/dir/' + home + '/' + target)

    elif 'get from' in task:

        home = Finder.noEnd(task, 'from ')
        if 'to' in home:
            target = Finder.noEnd(home, 'to ')
            home = Finder.searcher(home, home[0], ' to ')
            home = home[0 : len(home) - 3]
            speak("I'm pulling up the directions right now.")
            print('Opening Google Maps...')
            webbrowser.open('https://www.google.com/maps/dir/' + home + '/' + target)
        else:
            speak('Where are you going to?')
            target = myCommand()
            speak("I'm pulling up the directions right now.")
            print('Opening Google Maps...')
            webbrowser.open('https://www.google.com/maps/dir/' + home + '/' + target)

    elif 'school' in task:
        print('Opening your school homepage...')
        webbrowser.open('https://stonypoint.roundrockisd.org/')

    
    elif 'drive' in task:
        print('Opening your Google Drive...')
        webbrowser.open('https://drive.google.com/drive/u/0/my-drive')

    # TEMPORARY: REMOVE LATER
    # Music

    elif 'play' in task:

        song = Finder.noEnd(task, 'play')
        speak('Opening Youtube Music...')
        webbrowser.open('https://music.youtube.com/search?q=' + song)
        time.sleep(7.5)
        gui.moveTo(282, 456)
        gui.click()

    elif 'up' in task:

        question = Finder.noEnd(task, 'up')

        print('Opening Google...')
        webbrowser.open('https://www.google.com/search?-b-1-d&q=' + question)

    elif 'tell me a joke' in task:
        n = random.randrange(4)
        if n == 0:
            speak("What is the best thing about Switzerland? I do not know either, but the flag is a big plus!")
        elif n == 1:
            speak('I invented a new word! Plagiarism!')
        elif n == 2:
            speak('Hear about the new restaurant called karma? There is no menu, because you get what you deserve.')
        elif n == 3:
            speak('Did you hear about the actor who fell through the floorboards? He was just going through a stage.')

    # Prints out any value of the Fibonacci sequence

    elif 'fibonacci' in task:

        speak('What value of the sequence do you want to know? ')
        value = myCommand()

        value = int(value)

        run = 2

        if value == 1:
            speak('0')

        elif value == 2:
            speak('1')
            run = value
        x = 0
        y = 1

        while run != value:
            q = x + y

            if run == 0:
                x = q

            elif run == 1:
                y = q

            elif run % 2 == 0:
                x = q

            elif run % 2 == 1:
                y = q
            run = run + 1

        if value == run:
            speak('Do you want me to read out the number?')
            order = myCommand()
            order = order.lower
            if order[0] == 'y':
                speak(q)
            elif order[0] == 's':
                speak(q)
            elif order[0] == 'n':
                print(q)

    # Gives information about school schedule. Currently only two works - could easily add others.

    elif 'schedule' in task:

        if name == 'Athul':
            speak('What period do you want information on? ')
            period = input(name + ': ')

            if period == '1':
                speak('First period is Pre-IB chemistry with Mr. Calvin at room B208. This is the start of your A day.')

            elif period == '2':
                speak('Second period is Pre-IB English 2 with Mr. Powell at room C117.')

            elif period == '3':
                speak(
                    'Third period is Intro to Engineering Design with Mr. Claypool at room D142. You have C lunch halfway through this period.')

            elif period == '4':
                speak(
                    'Fourth period is Pre-IB Algebra 2 with Mr. Sullivan at room C267. This is the end of your A day.')

            elif period == '5':
                speak('Fifth period is AP World History with Mr. Thomas at room C209. This is the start of your B day.')

            elif period == '6':
                speak('Sixth period is Art 1 with Ms. Underwood at room F113.')

            elif period == '7':
                speak(
                    'Seventh period is Pre-IB French 3 with Ms. Tarplay at P3A. You have C lunch halfway thorough this period.')

            elif period == '8':
                speak(
                    'Eigth period is AP Computer Science with Mr. Holder at room A211. This is the end of your B day.')

        else:
            print('Unfortunately, ' + name + ', I do not have any information about your schedule.')

    # Motivation

    elif 'motivate' in task:
        speak('This should cheer you up.')
        webbrowser.open('https://repl.it/@PETAfam227/Samaritan')

    # Prints out values of pi up to 500

    elif 'pi' in task:
        speak('Please say only the exact number of digits of Pi you want. I can do up to 500 digits. ')
        place = myCommand()
        x = 0

        if place == 0:
            speak('Well that is easy! Zero!')
        place = int(place)

        if place >= 501:
            speak('I can not do that. Sorry.')
            x = place

        pi = '3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364367892590360011330530548820466521384146951941511609433057270365759591953092186117381932611793105118548074462379962749567351885752724891227938183011949129833673362440656643086021394946395224737190702179860943702770539217176293176752384674818467669405132000568127145263560827785771342757789609173637178721468440901224953430146549585371050792279689258923542019956112129021960864034418159813629774771309960518707211349999998372978049951059731732816096318595024459455346908302642522308253344685035261931188171010003137838752886587533208381420617177669147303598253490428755468731159562863882353787593751957781857780532171226806613001927876611195909216420198 '

        speak('Do you want me to read it out?')
        userRead = myCommand()

        if 'yes' in userRead:
            speak(pi[0: place + 1])

        elif 'yeah' in userRead:
            speak(pi[0: place + 1])

        elif 'go' in userRead:
            speak(pi[0: place + 1])

        elif 'free' in userRead:
            speak(pi[0: place + 1])

        elif 'no' in userRead:
            print(pi[0: place + 1])

        elif 'nope' in userRead:
            print(pi[0: place + 1])

        elif 'nah' in userRead:
            print(pi[0: place + 1])

        elif 'not' in userRead:
            print(pi[0: place + 1])

    # date

    elif 'date' in task:
        speak('It is ' + dateTime('date') + '.')

    elif 'day' in task:
        speak('The date is ' + dateTime('date') + '.')

    # System help command

    elif 'help' in task:
        speak(
            'Do you need to know about my Browser, Math, or Other functions? Or do you just want a general list of them all? If you want to exit, just tell me to shut down.')
        helpWith = myCommand()
        if 'general' in helpWith:
            print(
                'I have several basic keywords I '
                'can respond to. I respond to the commands Binary, Admin, Browser, Random Number, Hexidecimal, Schedule, Pi, Length, Number Game, Temp, Joke, Convo, '
                'Vowel, Add, Admin, Fibonacci, Talk, Pause, Sub, Divide, Spotify, Multiply, and quite clearly, Help.')
        elif 'browser' in helpWith:
            print(
                'I have several browser functions I can open. These include Dashboard, Spotify, Search or Look Up, Images, Youtube, Barca, Code, Maps, Amazon, Calendar, Weather, La Liga, Premier League, Games, School, Classroom, and Drive.')
        elif 'math' in helpWith:
            print(
                'I respond to the math keywords: Random Number, Pi, and Fibonacci.')
        elif 'other' in helpWith:
            print('I respond to the keywords: Schedule, News, Date, Motivate, Pause, and obviously help.')

    # Exit functions

    elif 'exit' in task:
        end()
        break

    elif 'shut down' in task:
        end()
        break

    elif 'nope' in task:
        end()
        break

    elif 'no' in task:
        end()
        break

    elif 'nah' in task:
        end()
        break

    # Basic fallback

    else:
        try:
            print(
                'You either spelled that wrong, forgot a capital letter, or I do not have the ability to assist you with that right now. To see the acceptable inputs, type "Help". If you want to exit the program, simply type "Exit".')
            pass

        except task == 'void':
            pass

    # Loop text function

    if task == 'void':
        pass
    else:
        turn = random.randint(1, 3)
        if turn == 1:
            speak('Do you require anything else? ')
        elif turn == 2:
            speak('Got any other things for me? ')
        elif turn == 3:
            speak('Is there anything else I could do for you?')
