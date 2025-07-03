from tkinter import *
from tkinter import font
from tkinter.ttk import Progressbar,Style
from PIL import ImageTk,Image
from main import *
from time import sleep
import os, sys
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # folder created by PyInstaller
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

#setup
root=Tk()
root.withdraw()
root.iconbitmap(resource_path("icons/safepass.ico")) 
root.resizable(0,0)
root.title("Safepass")
window_w=400
window_h=400
screen_w=root.winfo_screenwidth()
screen_h=root.winfo_screenheight()
x_cord=int((screen_w/2)-(window_w/2))
y_cord=int((screen_h/2)-(window_h/2))
root.geometry(f"{window_w}x{window_h}+{x_cord}+{y_cord}")
root["bg"]="black"
#icons
safepass_icon=ImageTk.PhotoImage(Image.open("icons/safepass.png").resize((40,40)))
day_icon=ImageTk.PhotoImage(Image.open("icons/day_icon.png").resize((30,30)))
dark_icon=ImageTk.PhotoImage(Image.open("icons/dark_icon.png").resize((30,30)))
generate_icon=ImageTk.PhotoImage(Image.open("icons/generate_icon.png").resize((30,30)))
check_icon=ImageTk.PhotoImage(Image.open("icons/check_icon3.png").resize((30,30)))
copy_icon=ImageTk.PhotoImage(Image.open("icons/copy_icon.png").resize((30,30)))
copy_success_icon=ImageTk.PhotoImage(Image.open("icons/check_icon1.png").resize((30,30)))
eye_close_icon=ImageTk.PhotoImage(Image.open("icons/eye_close.png").resize((20,21)))
eye_open_icon=ImageTk.PhotoImage(Image.open("icons/eye_open.png").resize((20,21)))
safe_icon=ImageTk.PhotoImage(Image.open("icons/safe_icon.png").resize((40,40)))
key_icon=ImageTk.PhotoImage(Image.open("icons/key_icon.png").resize((20,20)))
feedback_icon=ImageTk.PhotoImage(Image.open("icons/feedback_icon.png").resize((20,20)))
suggestion_icon=ImageTk.PhotoImage(Image.open("icons/suggestion_dark_icon.png").resize((20,20)))
suggestion_day_icon=ImageTk.PhotoImage(Image.open("icons/suggestion_day_icon.png").resize((20,20)))
warning_dark_icon=ImageTk.PhotoImage(Image.open("icons/warning_dark.png").resize((20,20)))
warning_day_icon=ImageTk.PhotoImage(Image.open("icons/warning_day.png").resize((20,20)))
#clipboard frame
clipboard_frame=Frame(root,width=14,bd=0,bg=root["bg"],height=1);
generated_password_label=Text(clipboard_frame,bd=0,bg="#8f3cfb",fg="white",font=("Opensans",16,"bold"),width=14,height=1);
generated_password_label.grid(row=0,column=0)
copy_btn=Button(clipboard_frame,image=copy_icon,bd=0,bg=root["bg"],command=lambda:copy_to_clipboard(generated_password_label));copy_btn.grid(row=0,column=1)
#styles
style=Style()
style.theme_use("clam")
#check results frame
results_frame=Frame(root,width=400,bd=0,bg=root["bg"]);
#check results frame children
score_label=Label(results_frame,fg="white",font="Roboto 10 bold",image=key_icon,compound="left",text="Password Score  :",bg=root["bg"]);
score_label.grid(row=0,column=0,padx=5,pady=(5,0),sticky="w")
score_value=Label(results_frame,text="",fg="white",bg="black",font="Roboto 10 bold",anchor="w",width=3);
score_value.grid(row=0,column=2,padx=5,pady=(5,0),sticky="w")
score_bar=Progressbar(results_frame,length=150,mode="determinate",style="TProgressbar")
score_bar.grid(row=0,column=1,padx=5,pady=(5,0),sticky="we")

feedback_label=Label(results_frame,fg="white",font="Roboto 10 bold",image=feedback_icon,compound="left",text="Feedback\t:",bg=root["bg"]);
feedback_label.grid(row=1,column=0,padx=5,pady=(5,0),sticky="nw")
feedback_value=Label(results_frame,text="Test Feedback",fg="white",bg="black",font="Roboto 10 bold");
feedback_value.grid(row=1,column=1,columnspan=2,padx=5,pady=(5,0),sticky="w")

suggestion_label=Label(results_frame,fg="white",font="Roboto 10 bold",image=suggestion_icon,compound="left",text="Suggestion\t:",bg=root["bg"]);
suggestion_value=Label(results_frame,wraplength=240,justify="left",anchor="w",text="",fg="yellow",bg="black",font="Roboto 10 bold");

warning_label=Label(results_frame,fg="white",font="Roboto 10 bold",image=warning_day_icon,compound="left",text="Warning\t\t:",bg=root["bg"]);
warning_value=Label(results_frame,wraplength=240,justify="left",text="",fg="red",bg="black",font="Roboto 10 bold");



#functions
def splash_screen():
    splash=Toplevel()
    splash.overrideredirect(1)
    splash.geometry("400x200+500+300")
    splash.configure(bg="black")
    Label(splash,image=safepass_icon,compound="left",text=" SafePass", font=("Terminal", 28, "bold"), fg="cyan", bg="black").pack(pady=70)
    splash.attributes("-alpha",0.0)
    for i in range(0,11):
        splash.attributes("-alpha",i/10)
        splash.update()
        sleep(0.05)
    splash.after(2200,lambda:[splash.destroy(),root.deiconify()])
def theme():
    if root["bg"]=="black":
        root["bg"]="white"
        label1.configure(bg="white",fg="purple")
        theme_btn["image"]=dark_icon
        password_entry.configure(fg="white",bg="#1e1e1e",insertbackground="white",highlightthickness=2,highlightbackground="#00ffff",highlightcolor="#00ffcc")
        check_btn.configure(bg="black",fg="white")
        generate_btn.configure(bg="black",fg="white")
        copy_btn.configure(bg="white")
        score_label.configure(bg="white",fg="black")
        score_value.configure(bg="white")
        feedback_label.configure(bg="white",fg="black")
        feedback_value.configure(bg="white")
        suggestion_label.configure(bg="white",fg="black")
        suggestion_value.configure(fg="blue",bg="white")
        warning_label.configure(bg="white",fg="black")
        warning_value.configure(bg="white")
        results_frame.configure(bg="white")
    else:
        root["bg"]="black"
        label1.configure(bg="black",fg="yellow")
        theme_btn["image"]=day_icon
        password_entry.configure(fg="black",bg="#f0f0f0",insertbackground="black",highlightthickness=2,highlightbackground="#0066cc",highlightcolor="#3399ff")
        check_btn.configure(bg="white",fg="darkgreen")
        generate_btn.configure(bg="white",fg="#8f3cfb")
        score_label.configure(bg="black",fg="white")
        score_value.configure(bg="black")
        feedback_label.configure(bg="black",fg="white")
        feedback_value.configure(bg="black")
        suggestion_label.configure(bg="black",fg="white")
        suggestion_value.configure(fg="yellow",bg="black")
        warning_label.configure(bg="black",fg="white")
        warning_value.configure(bg="black")
        results_frame.configure(bg="black")
def password_display():
    if password_entry["show"]=="*":
        password_entry.configure(show="")
        password_display_btn.configure(image=eye_open_icon)
    else:
        password_entry.configure(show="*")
        password_display_btn.configure(image=eye_close_icon)
def strip_ansi(text):
    ansi_escape = re.compile(r'\x1b\[[0-9;]*m')
    return ansi_escape.sub('', text)

def Check_password():
    score,feedback,warning=check_password(password_entry.get())[1]
    if score<20:
          enter_password_msg=Label(image=key_icon,text="Please Enter Your Password!",fg="blue",bg=root["bg"],font="Lato 16 bold",compound="left");enter_password_msg.place(x=30,y=250)
          enter_password_msg.after(3000,enter_password_msg.place_forget)
          return
    if clipboard_frame.winfo_ismapped():
        clipboard_frame.place_forget()
    
    
    try:
        feedback,suggestion=feedback.split("\n")
        suggestion=suggestion.split(":")[1]
        if len(suggestion)>64:
            suggestion=suggestion[:32]+"\n"+suggestion[32:60]+"\n"+suggestion[60:]
        elif len(suggestion)>32:
            suggestion=suggestion[:32]+"\n"+suggestion[32:]
        suggestion_value.configure(text=suggestion)
##        print(score,feedback,suggestion,warning,sep="\n")
        if not suggestion_label.winfo_ismapped():
            suggestion_label.grid(row=2,column=0,padx=5,pady=(5,0),sticky="nw")
            suggestion_value.grid(row=2,column=1,pady=(5,0),columnspan=2,padx=5,sticky="w")
    except:
        if suggestion_label.winfo_ismapped():
            suggestion_label.grid_remove()
            suggestion_value.grid_remove()
    if warning:
        warning=strip_ansi("".join(warning))
        warning_value.configure(text=warning)
        if not warning_label.winfo_ismapped():
            warning_label.grid(row=3,column=0,padx=5,pady=(5,0),sticky="nw")
            warning_value.grid(row=3,column=1,columnspan=2,padx=5,pady=(5,0),sticky="w")
    else:
        if warning_label.winfo_ismapped():
            warning_label.grid_remove()
            warning_value.grid_remove()
    show_score(score)
    score_value.configure(text=str(score))
    feedback_value.configure(text=feedback)
    if not results_frame.winfo_ismapped():
        results_frame.place(x=0,y=215)

def copy_to_clipboard(text_widget):
    root.clipboard_clear()
    root.clipboard_append(text_widget.get("1.0","end-1c"))
    copied_success_msg=Label(image=copy_success_icon,text="Password Copied Successfully!",fg="blue",bg=root["bg"],font="Lato 16 bold",compound="left");copied_success_msg.place(x=15,y=250)
    copied_success_msg.after(3000,copied_success_msg.place_forget)
def Generate_password():
    generated_password=generate_password()
    if results_frame.winfo_ismapped():
        results_frame.place_forget()
    generated_password_label.delete("1.0",END)
    generated_password_label.insert(END,generated_password)
    if not clipboard_frame.winfo_ismapped():
        clipboard_frame.place(relx=0.5,y=210,anchor="n")
def show_score(score:int):
    global score_bar
    if score<40:
        bar_color="red"
    elif score<60:
        bar_color="orange"
    elif score<80:
        bar_color="pink"
    else:
        bar_color="green"
    style.configure("TProgressbar",thickness=20,troughcolor="white",bordercolor="gray",background=bar_color)
    score_bar["value"]=score
    score_value.configure(fg=bar_color)
    feedback_value.configure(fg=bar_color)

#App Bar
appbar=Frame(root,width=400,height=60,bg="cyan")
appbar.pack()
#title
title=Label(appbar,image=safe_icon,compound="left",text="SafePass",fg="red",bg=appbar["bg"],font="Terminal 24 bold")
title.place(x=70,y=10)
#theme button
theme_btn=Button(appbar,image=day_icon,bg=appbar["bg"],bd=0,command=theme);theme_btn.place(x=10,y=15)
                                #root 
label1=Label(root,text="\U0001F512 Enter Your Password",fg="yellow",bg=root["bg"],font=("Segoe UI Emoji",14,"bold"))
label1.place(x=80,y=70)
#password entry
password_entry=Entry(root,fg="white",show="*",highlightbackground="#00ffff",highlightcolor="#00ffcc",highlightthickness=2,bg="#1e1e1e",width=35,justify="center")
password_entry.place(x=105,y=110)
password_entry.focus_set()
password_display_btn=Button(root,image=eye_close_icon,bg="#00ffff",bd=0,command=password_display)
password_display_btn.place(x=85,y=110)
#check button
check_btn=Button(root,image=check_icon,bg="white",fg="darkgreen",text="Check",highlightthickness=1,highlightbackground="#00cc66",highlightcolor="#00ff99",compound="right",bd=0,font=("Roboto",10,"bold"),command=Check_password)
check_btn.place(x=85,y=160)
generate_btn=Button(root,image=generate_icon,bg="white",fg="#8f3cfb",text="Generate",highlightthickness=1,highlightbackground="#8f3cfb",highlightcolor="#c084fc",compound="right",bd=0,font=("Opensans",10,"bold"),command=Generate_password)
generate_btn.place(x=220,y=160)
#splash screen
splash_screen()
#button bindings
root.bind("<Return>",lambda event:Check_password())
root.mainloop()
