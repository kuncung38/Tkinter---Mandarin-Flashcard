from tkinter import *
from tkinter import messagebox
from pandas import read_csv
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

#-----------------------------------Data Extraction----------------------------------------#
df= read_csv('data/mandarin_words.csv')
df = df.to_dict(orient="records")

score = -1
iteration = 0
def next_card(text):
    global score, iteration
    if iteration == 907:
        messagebox.showinfo(title= "Thats all for beginner level", 
                            message=f"Your score is {score}, you have finished all 907 words")
    iteration +=1
    if text == "Known":
        score +=1
    else:
        score = score

    if score == 907:
        on_closing()

    for key in option.keys():
        button_dict[key]['state'] = DISABLED
    score_label.config(text=f"Score: {score}")

    current_card = choice(df)
    current_question = current_card['Simplified']
    current_pinyin = current_card['Pinyin']
    current_answer = current_card['English']
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(card_title, text="Chinese", fill= "black")
    canvas.itemconfig(card_text, text=current_question, fill= "black")
    canvas.itemconfig(mandarin_pinyin, text=current_pinyin, fill= "black")

    def flip_card():
        canvas.itemconfig(canvas_image, image=card_back_img)
        canvas.itemconfig(card_title, text="English", fill= "white")
        canvas.itemconfig(card_text, text=current_answer, fill= "white")
        canvas.itemconfig(mandarin_pinyin, text="")
        for key in option.keys():
            button_dict[key]['state'] = NORMAL
    wd.after(3000, flip_card)

#--------------------------------------UI------------------------------------------#
wd = Tk()
wd.title("Flash Card for noob")
wd.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

score_label = Label(text="Score: 0", bg=BACKGROUND_COLOR, 
                    highlightthickness=0, font=("Tahoma", 40,))
score_label.grid(row=0, column=0, columnspan=2)

canvas = Canvas(width=800, height=526)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

canvas_image = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 150, font=("Tahoma", 40, "italic"))
card_text = canvas.create_text(400, 263, font=("Tahoma", 60, "bold"))
mandarin_pinyin = canvas.create_text(400, 350, font=("Tahoma", 30, "bold"))
canvas.config(bg = BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=1, column=0, columnspan=2)

#Create Multiple Buttons with different commands
cross_image = PhotoImage(file="images/wrong.png")
check_image = PhotoImage(file="images/right.png")

button_dict={}
option= {"Known":[1, check_image], "Unknown":[0, cross_image]}

for i in option.keys():
    def func(x=i):
      return next_card(x)

    button_dict[i]=Button(image=option[i][1], highlightthickness=0 ,command= func)
    button_dict[i].grid(row = 2, column=option[i][0])

canvas.itemconfig(card_title, text="Ready")
canvas.itemconfig(card_text, text="Press green button to start!", font=("Tahoma", 30, "bold"))


#--------------------------------------On windows closing------------------------------------------#
def on_closing():
    if score <10:
        messagebox.showinfo(title= "Damn noob", message=f"Your score is {score}, Cant even get 10 correct and give up pfftt")
    elif score >= 10:
        messagebox.showinfo(title= "Noob", message=f"Your score is {score}, At least you got 10 correct, still noob tho pfftt")
    elif score == 907:
        messagebox.showinfo(title= "Impossible", 
                            message=f"Your score is {score}, you are cheating for sure")
    wd.destroy()

wd.protocol("WM_DELETE_WINDOW", on_closing)

wd.mainloop()