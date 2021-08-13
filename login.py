import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime
from PIL import ImageGrab
from functools import partial

def sign_in(meetingid, name, pswd):
    #opens the zoom app
    subprocess.call(r"C:\Users\nehac\AppData\Roaming\Zoom\bin\Zoom.exe")
    
    time.sleep(10)
    
    #clicks the join button
    join_btn = pyautogui.locateCenterOnScreen('join_button.png',grayscale=True, confidence=.8)
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    
    time.sleep(5)
    
    #type the meeting ID
    meeting_id_btn = pyautogui.locateCenterOnScreen('meeting_id_button.png')
    if meeting_id_btn != None:
        pyautogui.moveTo(meeting_id_btn)
    else:
        meeting_id_btn = pyautogui.locateCenterOnScreen('meeting_id_button_2.png')
        pyautogui.moveTo(meeting_id_btn)
    pyautogui.click()
    pyautogui.write(meetingid)
    
    #type the name
    name_btn = pyautogui.locateCenterOnScreen('name_button.png', grayscale=True, confidence = .5)
    pyautogui.moveTo(name_btn)
    pyautogui.tripleClick()
    pyautogui.write(name)
    
    #disables camera
    media_btn = pyautogui.locateAllOnScreen('media_button.png')
    i = 0
    for btn in media_btn:
        if i==1:
            pyautogui.moveTo(btn)
            pyautogui.click()
        i = i+1
    
    time.sleep(2)
    
    #hits the join button
    join_btn = pyautogui.locateCenterOnScreen('final_join.png',grayscale=True)
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    
    time.sleep(2)
    
    #types the password and hits enter
    meeting_pswd_btn = pyautogui.locateCenterOnScreen('meeting_password.png', grayscale=True, confidence=.5)
    pyautogui.moveTo(meeting_pswd_btn)
    pyautogui.click()
    pyautogui.write(pswd)
    pyautogui.press('enter')
    
    #presses got it if appears
    got_it_btn = pyautogui.locateCenterOnScreen('got_it_button.png', grayscale=True, confidence=.5)
    if got_it_btn != None:
        pyautogui.moveTo(got_it_btn)
        pyautogui.click()
    
#reading the CSV file
df = pd.read_csv('timings.csv')
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

while True:
        now = datetime.now().strftime("%H:%M")
        if now in str(df['timings']):
        
            row = df.loc[df['timings'] == now]
            m_id = str(row.iloc[0,1])
            m_name = str(row.iloc[0,2])
            m_pswd = str(row.iloc[0,3])
            
            sign_in(m_id, m_name, m_pswd)
            time.sleep(40)
            print('signed in')