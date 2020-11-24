from selenium.webdriver import Chrome
from tkinter import *

root=Tk()
root.title("Google Search")
root.geometry('400x400')

def get():
    return input_query.get()
def query():
    query=get()
    if (len(query) == 0):
        print("Please Enter something to input First.")
    else:
        browser = Chrome(r"C:\\Users\faraz\PycharmProjects\Automation\Selenium Model\chromedriver.exe")
        browser.get("https://google.com")
        query_box = browser.find_element_by_name("q")
        query_box.send_keys(query)
        query_box.submit()

input_query=Entry(root,width=20,font=("Helvetica",20))
input_query.pack(pady=10)
submit=Button(root,text="SUBMIT",font=(10),command=query)
submit.pack(pady=10)

root.mainloop()



