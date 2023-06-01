import re
import pyperclip
import pyautogui
from time import sleep

def start_string(tag: str) -> str:
    """returns the entered tag without the number part"""
    
    # find the last non int tag
    return re.sub(r' \d+$', '', tag).strip()

pyperclip.copy("")
sleep(1)

def copy():
    # swap to chrome
    pyautogui.keyDown("command")
    pyautogui.keyDown("tab")
    sleep(0.05)
    pyautogui.keyUp("command")
    pyautogui.keyUp("tab")

    sleep(0.1)

    # paste 
    pyautogui.keyDown("command")
    pyautogui.keyDown("v")
    sleep(0.05)
    pyautogui.keyUp("v")
    pyautogui.keyUp("command")

    sleep(0.1)
    # enter the tag
    pyautogui.press("Enter")

    # swap to vs code
    pyautogui.keyDown("command")
    pyautogui.keyDown("tab")
    sleep(0.05)
    pyautogui.keyUp("command")
    pyautogui.keyUp("tab")

    # go onto the next item
    #pyautogui.press("Enter")
    #sleep(0.1)
tags = []
with open("tag.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    if not line.startswith("?"):
        continue
    current = line.split("? ")[1]
    tag = (start_string(current))
    if tag not in tags:
        tags.append(tag)

pyperclip.copy("")
for i, tag in enumerate(tags):
    print(f"{i+1}/{len(tags)}): {tag}")
    pyperclip.copy(tag)
    sleep(0.15)
    copy()
    #sleep(0.15)
    #input()