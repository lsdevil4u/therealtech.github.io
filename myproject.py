import pyttsx3
import os

pyttsx3.speak("welcome to my world")

print('tell me what can i do for you: ' , end=' ')
p=input()
#print(p)

#os.system(p)

if ('run' in p) or ('open' in p) and ('chrome' in p):
  os.system('chrome')

elif ('run' in p) or ('open' in p) or ('execute' in p) or ('use' in p) and ('notepad' in p) or ('text editor' in p):
  os.system('notepad')

elif ('run' in p) or ('open' in p) or ('start' in p) or ('use' in p) and ('player' in p) and ('media' in p):
  os.system('wmplayer')
else:
  print('dont support')
