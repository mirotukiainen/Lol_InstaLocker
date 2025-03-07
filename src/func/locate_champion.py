import pyautogui
import time

def search(champion):
   search_location = pyautogui.locateOnScreen(f"src\img\search.png", confidence=0.6)
   print(f"Searchbar found at: {search_location}")
   pyautogui.moveTo(search_location)
   pyautogui.leftClick()
   time.sleep(1)
   pyautogui.write(champion)