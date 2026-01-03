from pyperclip import paste, copy
from time import sleep

import keyboard,pyautogui

IncludeTabs = False

def type_clipboard(interval=0.01):
    text = paste()
    if not IncludeTabs:
        text = text.replace('\t', '')
        text = text.replace('    ', '')
    pyautogui.write(text, interval=interval)

def on_hotkey():
    type_clipboard(interval=0.01)

#Bind Ctrl + ` (tilde) to run your function
keyboard.add_hotkey('`', on_hotkey)

print("Hotkey active: Press Ctrl + ` to type clipboard content.")
keyboard.wait()   # Keeps the script running


#text
def strip_formatting(text: str) -> str:
    return text

def main():
    last_text = ""
    while True:
        try:
            text = paste()
            if text != last_text:
                plain_text = strip_formatting(text)
                copy(plain_text)
                last_text = plain_text
            sleep(1)
        except KeyboardInterrupt:
            break
        except Exception as e:
            sleep(1)

if __name__ == "__main__":
    main()
