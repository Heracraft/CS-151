from tkinter import *

window=Tk()

# title=Label(window, text="Some flipping window")
# title.pack()

window.title("Counter")
window.geometry("500x500")

countdown=10
countdownText=StringVar()
countdownText.set(countdown)

counter=Label(window, textvariable=countdownText, font=('Arial', 45))
counter.pack()

def decrementCount(countdown):
    # print(countdown)
    countdown-=1
    countdownText.set(countdown)

    if countdown>-10:
        window.after(1000, decrementCount, countdown)

decrementCount(countdown)

window.mainloop()