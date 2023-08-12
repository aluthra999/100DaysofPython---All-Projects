from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def time_reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_lable.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it's 8th rep
    if reps % 8 == 0:
        countdown(long_break_sec)
        title_lable.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        # if it's 2nd/4th/6th rep
        countdown(short_break_sec)
        title_lable.config(text="BREAK", fg=PINK)
    else:
        # If it's 1st/3rd/5th/7th rep:
        countdown(work_sec)
        title_lable.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_minute = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    if count_minute < 10:
        count_minute = f"0{count_minute}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
            check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_lable = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
title_lable.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(110, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, bg=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, bg=YELLOW, command=time_reset)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))
check_marks.grid(column=1, row=3)

window.mainloop()
