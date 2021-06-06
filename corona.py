import requests
from bs4 import BeautifulSoup
from tkinter import messagebox, Tk, Entry, Button, END, Label, LEFT

url = "https://www.worldometers.info/coronavirus/"

r = requests.get(url)
s = BeautifulSoup(r.text, "html.parser")
data = s.find_all("div",class_ = "maincounter-number")

root =Tk()
root.title("Covid static")
t = Label(bg='black', fg='white')
c = Label()
d = Label()
r = Label()

t['text'] = "Coronavirus Static:"
c['text'] = "Coronavirus Cases: "+data[0].text.strip()
d['text'] = "Deaths: "+data[1].text.strip()
r['text'] = "Recovered: "+data[2].text.strip()
t.pack()
c.pack()
d.pack()
r.pack()
root.resizable(0, 0)
root.mainloop()