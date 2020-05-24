from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import *
import time

root = Tk()
root.title("AutoBadoo")
root.geometry("400x200")
root.configure(background="purple")

heading = Label(text="Automate Badoo Right Swipes", bg='pink', fg="purple", width='380', height='1',
                font=("Courier", 16))
heading.pack()

email_text = Label(text="Email", )
email_text.place(x=50, y=70)
email_entry = Entry(width='30')
email_entry.place(x=130, y=70)

pass_text = Label(text="Password", )
pass_text.place(x=50, y=100)
pass_entry = Entry(root, width='30', show='*')
pass_entry.place(x=130, y=100)

swipecount_text = Label(text="Swipe Count", )
swipecount_text.place(x=50, y=130)
swipecount_entry = Entry(width='30')
swipecount_entry.place(x=130, y=130)

def autoit():
    email = email_entry.get()
    password = pass_entry.get()
    swipecount = int(swipecount_entry.get())

    driver = webdriver.Chrome()
    driver.get("https://www.badoo.com")
    time.sleep(2)
    driver.maximize_window()

    fbbutton = driver.find_element_by_xpath('''//*[@id="page"]/div[2]/div[3]/div/div[3]/div/div[1]/div[2]/div/div/a''')
    fbbutton.click()

    winhad = driver.window_handles
    driver.switch_to_window(winhad[1])

    emailbox = driver.find_element_by_id("email")
    emailbox.click()
    emailbox.send_keys(email)

    passbox = driver.find_element_by_id("pass")
    passbox.click()
    passbox.send_keys(password)

    loginbutton = driver.find_element_by_xpath('''//*[@id="u_0_0"]''')
    loginbutton.click()
    time.sleep(5)
    driver.switch_to_window(winhad[0])

    likeb = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '''//*[@id="mm_cc"]/div[1]/section/div/div[2]/div/div[2]/div[1]/div[1]''')))
    likeb.click()
    time.sleep(1)
    skipb = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '''/html/body/aside/section/div[1]/div/div/section/div/div/div/div[2]/div''')))
    skipb.click()
    time.sleep(1)
    
    x = 0
    while x <= swipecount:
        looplb = driver.find_element_by_xpath('''//*[@id="mm_cc"]/div[1]/section/div/div[2]/div/div[2]/div[1]/div[1]''')
        looplb.click()
        time.sleep(0.5)
        x+=1

    signout = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '''//*[@id="app_s"]/div/div/div/div[1]/div/div[2]/div/div[1]/div[2]''')))
    signout.click()

    signout_yes = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '''/html/body/aside/section/div[1]/div/div/section/div/div/div/div[1]/div''')))
    signout_yes.click()    

submit = Button(text="Submit", bg = "grey", fg = "black", command = autoit)
submit.pack()
root.mainloop()
