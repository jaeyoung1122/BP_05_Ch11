import pickle
from tkinter import *

phone_book = { }
current = 0
name = ""
phone = ""

window = Tk()

frame1 = Frame(window)
frame1.pack()
Label(frame1, text = "이름 ").grid(row = 1, column = 1, sticky = W)
nameEntry = Entry(frame1, textvariable = name, width = 30)
nameEntry.grid(row = 1, column = 2)

frame2 = Frame(window)
frame2.pack()
Label(frame2, text = "전화번호").grid(row = 1, column = 1, sticky = W)
phoneEntry = Entry(frame2, textvariable = phone, width = 30)
phoneEntry.grid(row = 1, column = 2)

frame3 = Frame(window)
frame3.pack()


def save():
  outfile = open("phonebook.dat", "wb")
  pickle.dump(phone_book, outfile)
  print("주소들이 파일에 저장되었습니다")
  outfile.close()
  
def load():
