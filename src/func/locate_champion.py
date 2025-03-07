import pyautogui

def locate_champ():
   image = pyautogui.locateOnScreen("src\img\Ahri.png", confidence=0.7)
   print(f"Champion found at: {image}")
   pyautogui.moveTo(image)