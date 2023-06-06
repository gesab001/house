import subprocess
import json
import webbrowser
import os

# MacOS
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows

chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

# Linux
# chrome_path = '/usr/bin/google-chrome %s'


def viewItems(jsondata):
  for h in jsondata["items"]:
   command = "python -m webbrowser -t " + h["url"]
   subprocess.call(command, shell=False)
   url = h["url"]
   #webbrowser.get(chrome_path).open(url)
while True:
 fopen = open("houses.json", "r")
 jsondata = json.loads(fopen.read())
 fopen.close()


 title = input("title: ")
 if title=="view":
   viewItems(jsondata)
   break
 if title!="":
  url = input("url: " )
  itemToAdd = {"title": title, "url": url}
  jsondata["items"].append(itemToAdd)
  with open("houses.json", "w") as outfile:
   json.dump(jsondata, outfile, indent=4, sort_keys=True)
  command = "python3 pushtogit.py"
  subprocess.call(command, shell=True)  

 else:
  for h in jsondata["items"]:
   url = h["url"]
   #command = "python -m webbrowser -t " + h["url"]
   #subprocess.call(command, shell=False)
   webbrowser.get(chrome_path).open(url)
