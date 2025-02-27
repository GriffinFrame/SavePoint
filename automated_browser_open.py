### bash: 
####pip install selenium  # instal for web browser access
####pip install pyautogui # instal for curor move   
####


###Actual Program 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
	
import pyautogui
import time
    
# Set up the browser driver (replace with your actual path)
driver = webdriver.Chrome()
    
# Navigate to Google
driver.get("https://www.google.com")
    
# Find the search box and enter the search query
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("your search query") # this is where we will put the Local IP for the pi 
    
# Submit the search
search_box.send_keys(Keys.RETURN)
    
# Wait for the results to load (optional)
time.sleep(2)



# Get the current cursor position
current_position = pyautogui.position()
print(f"Current cursor position: {current_position}")

# Move the cursor to a specific position (x, y)
pyautogui.moveTo(100, 150, duration=1)  # this will need to be calibrated 


# Move the cursor relative to its current position
pyautogui.move(0, 50, duration=0.5)  # will also need to be calibrated 

# Click at the current cursor position
pyautogui.click()






#these next few arnt needed just though they were cool
# Double click
#pyautogui.doubleClick()

# Right click
#pyautogui.rightClick()

# Drag the mouse
#pyautogui.moveTo(100, 150, duration=1)
#pyautogui.dragTo(200, 250, duration=1)
	
	
	
# Close the browser
driver.quit() # this needs to be here or it will shit out 

	






