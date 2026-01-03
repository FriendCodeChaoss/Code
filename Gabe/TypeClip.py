import pyautogui
import time
import pyperclip

time.sleep(2)

IncludeTabs = True
def type_clipboard(interval=0.01):
    text = pyperclip.paste()
    if IncludeTabs == False:
        text = text.replace('\t', '')
        text = text.replace('    ', '')
    # Write all characters with a small interval
    pyautogui.write(text, interval=interval)

if __name__ == "__main__":
    type_clipboard(interval=0.004)  # Adjust interval for speed
