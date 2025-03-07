import pyautogui
import time

def search(champion):
   search_location = pyautogui.locateOnScreen(f"src\img\search.png", confidence=0.6)
   print(f"Searchbar found at: {search_location}")
   pyautogui.moveTo(search_location)
   
   pyautogui.leftClick()
   pyautogui.write(champion)
   
   pyautogui.moveTo(search_location.left - 400, search_location.top + 70)
   time.sleep(0.2)
   pyautogui.leftClick()
   
   lock_in = pyautogui.locateOnScreen("src\img\lock_in.png", confidence=0.6)
   pyautogui.moveTo(lock_in)
   pyautogui.leftClick()