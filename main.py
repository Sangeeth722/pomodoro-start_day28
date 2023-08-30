import tkinter as tk
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
def reset():
    global reps
    start_button.config(state="normal")


    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text = "00:00")
    timer_label.config(text="Timer")
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    start_button.config(state="disabled")
    reps +=1
    work_in_sec = WORK_MIN * 60
    short_brek_in_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN *60

    if reps %8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break",fg=RED)
    elif reps %2 == 0:
        count_down(short_brek_in_sec)
        timer_label.config(text="Break", fg=YELLOW)
    else:
        count_down(work_in_sec)
        timer_label.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(counts):

    #find minutes(via math library) and second(with reminder)
    count_minute = math.floor(counts/60)       #in this case cound_down = 300 sec.. connverrt to minute divide by 60
                                        #math.floor  is used to round down the number of minutes to the nearest whole number
    count_sec = counts %60                    #find the reminder and thats left seconds
    #if count_sec == 0:
    #    count_sec = "00"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    # configure canvas.create text methode to this time
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_sec}")
    if counts > 0:
        global timer
        timer = window.after(1000, count_down, counts-1)
    else:
        start_timer()

        #add check markss every two Reps
        marks = ""
        work_session = math.floor(reps/2)
        for i in range(work_session):
            marks += "✔"
        label_4_tick.config(text=marks)


#
# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.minsize(width=500,height=500)
window.title("pomodoro")
window.config(bg=PINK)
window.config(padx=100,pady=50)

#Label
timer_label = tk.Label(text="Timer",font=(FONT_NAME,45,"bold"),fg=RED,bg=PINK)
#timer_label.grid(row=0, column=0)

timer_label.grid(row=0,column=1)
#add canvas for image

canvas = tk.Canvas(width=220,height=223,bg=PINK,highlightthickness=0)
tomoto_image = tk.PhotoImage(file="tomato.png")
canvas.create_image(100,111,image = tomoto_image) #x and y axis x = total size of image x- axis
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,25,"bold"))
canvas.grid(row=1,column=1)

#image_label.grid(row=1,column=1)

#start_button

start_button = tk.Button(text="START",fg= "#e7305b",relief="sunken",cursor="hand2",highlightthickness=0,command=start_timer)
start_button.grid(row=2,column=0)

#reset_button

reset_button = tk.Button(text="RESET",fg="#e7305b",relief="sunken",cursor="hand2",highlightthickness=0,command=reset)
reset_button.grid(row=2,column=2)

#label_tick

label_4_tick = tk.Label(fg=GREEN,bg=PINK,font=("Helvetica", 20))
label_4_tick.grid(row=3,column=1)
window.mainloop()