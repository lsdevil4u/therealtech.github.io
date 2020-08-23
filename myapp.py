import pyttsx3
import os

pyttsx3.speak("most welcome to my world")

print('plz tell me what can i do for you: ' , end=' ')
p=input()


if (('run' in p)or('open' in p)or('start' in p)or('execute' in p)or('use' in p)) and (('chrome' in p)or('browser' in p)or('web browser' in p)):
  os.system('chrome')

elif (('run' in p)or('open' in p)or('start' in p)or('execute' in p)or('use' in p)) and (('notepad' in p)or('text editor' in p)or('coding editor' in p)or('keep notes' in p)):
  os.system('notepad')

elif (('run' in p)or('open' in p)or('start' in p)or('use' in p)or('execute' in p)) and (('player' in p)or('media' in p)or('video player' in p)or('audio player' in p)):
  os.system('wmplayer')
else:
  print('dont support')
