from tkinter import *
import pygame
from tkinter import PhotoImage
import tkinter.messagebox
from PIL import ImageTk, Image 
import time
pygame.mixer.init()

def moye_moye():
    global s4
    s4 = pygame.mixer.Sound("moye.mp3")
    s4.play()

w=Tk()


#splash window
width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
#w.configure(bg='#ED1B76')
w.overrideredirect(1) #for hiding titlebar
#new window to open





Frame(w, width=427, height=250, bg='#272727').place(x=0,y=0)
label1=Label(w, text='   WORD GUESS', fg='white', bg='#272727') #decorate it 
label1.configure(font=("Game Of Squids", 24, "bold"))   #You need to install this font in your PC or try another one
label1.place(x=80,y=90)

label2=Label(w, text='Loading...', fg='white', bg='#272727') #decorate it 
label2.configure(font=("Calibri", 11))
label2.place(x=10,y=215)

#making animation

image_a=ImageTk.PhotoImage(Image.open('c2.png'))
image_b=ImageTk.PhotoImage(Image.open('c1.png'))




for i in range(4): #5loops
    l1=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)
moye_moye()

w.destroy()
w.mainloop()



def play_sound_effect():
   global s1
   s1 = pygame.mixer.Sound("bgmusic.mp3")
   s1.play()

def beep_sound():
    global s2
    s2 = pygame.mixer.Sound("beep.mp3")
    s2.play()

def reveal():
    s1.stop()
    s3 = pygame.mixer.Sound("show_word.mp3")
    s3.play()









def switch_to_window1():
    s1.stop()
    moye_moye()
    root2.withdraw()  # Hide the second window
    gui.deiconify()  # Show the first window

selected_number = []
def store_button_number(number):
    beep_sound()
    selected_number.append(number)

# Function to store the value of the slider 
value = None
def get_len_words():
    s1.stop()
    s1.play()
    global value
    value = slider.get()
    
# function to generate the word from given hints   
def show_word():
    reveal()

    alpha = [] 
    for i in range(5):
        start=65+(i*5)
        list=[chr(x) for x in range(start,start+5)]
        if i==4:
            list.append('Z')
        else:
            list.append(' ')
        alpha.append(list)
    name=[alpha[selected_number[i+value]-1][selected_number[i]-1] for i in range(value)]
    
    w=Tk()
    w.title("Hurrah!! GUESSED IT...")


    #Using piece of code from old splash screen
    width_of_window = 427
    height_of_window = 250
    screen_width = w.winfo_screenwidth()
    screen_height = w.winfo_screenheight()
    x_coordinate = (screen_width/2)-(width_of_window/2)
    y_coordinate = (screen_height/2)-(height_of_window/2)
    w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
    #w.configure(bg='#ED1B76')
    w.overrideredirect(0) #for hiding titlebar

    Frame(w, width=427, height=250, bg='#272727').place(x=0,y=0)
    label1=Label(w, text=f"{''.join(name).title()}", fg='white', bg='#272727',anchor="center",justify="center") #decorate it 
    label1.configure(font=("Game Of Squids", 48, "bold"))   #You need to install this font in your PC or try another one
    label1.place(x=200,y=100,anchor="center")
    name.clear()
    selected_number.clear()
    w.mainloop()

#Function to reset the value of label
# def reset_label():
#     word_label.config(text="") 
def switch_to_second_window(event):
    s4.stop()
    gui.withdraw()  # Hide the first window
    play_sound_effect()
    root2.deiconify()  # Show the second window  



# Function to pop up the help box
def onClick(event):
    tkinter.messagebox.showinfo("Instructions",  '''1. Think of any Word. 
2. Slide the slider to number of letters in word.
3. Click SUBMIT button.                                
4. Tell number column of each Character in first and second grid respectively.
5. Click SHOW WORD to reveal the word.
''')
    
# Function to quit from the game
def quit(event):
   ans = tkinter.messagebox.askquestion("Confirm","Are you sure you want to exit?")
   if ans=="yes":
      gui.destroy()
   else :
      pass

# Create the main application window
gui = Tk()
gui.title("Full Screen Image")

# Get the screen width and height
screen_width = gui.winfo_screenwidth()
screen_height = gui.winfo_screenheight()
gui.attributes("-fullscreen", True)

# Load and resize the image
image = Image.open("banner.png")  # Replace with the path to your image
image = image.resize((screen_width, screen_height))
photo = ImageTk.PhotoImage(image)

# Create a full-screen canvas
canvas = Canvas(gui, width=screen_width, height=screen_height)
canvas.pack()

# Display the image on the canvas
canvas.create_image(0, 0, anchor=NW, image=photo)

# Function to handle window resizing
def on_resize(event):
    # Update the canvas size to match the window size
    canvas.config(width=gui.winfo_width(), height=gui.winfo_height())

# Bind the resize function to window resizing
gui.bind("<Configure>", on_resize)
play_imag = ImageTk.PhotoImage(Image.open("pr2.png"))

button1 = canvas.create_image(1160,250,image = play_imag)

canvas.tag_bind(button1,'<Button-1>',switch_to_second_window)
help_imag = ImageTk.PhotoImage(Image.open("h1.png"))
button2 = canvas.create_image(1000,550,image = help_imag)
canvas.tag_bind(button2,'<Button-1>',onClick)
exit_imag = ImageTk.PhotoImage(Image.open("e.png"))
button3 = canvas.create_image(1300,550,image = exit_imag)
canvas.tag_bind(button3,'<Button-1>',quit)


#236b2d
root2 = Toplevel(gui)
root2.title("Two Frames Example")
root2.withdraw()
root2.geometry(f"{screen_width}x{screen_height}")  # Set the window size
root2.configure(bg="#236b2d")
root2.attributes("-fullscreen", True)
# Create the left frame
left_frame = Frame(root2, width=582, height=528,bg="grey",borderwidth=6,relief="sunken")
left_frame.pack(side=LEFT,expand=False,padx=30,pady=100,ipadx=20,ipady=10)
# Create the right frame
right_frame = Frame(root2, width=582, height=528, bg="grey",borderwidth=6,relief="sunken")
right_frame.pack(side=RIGHT,expand=False,padx=30,pady=100,ipadx=20,ipady=10)


# Create a slider between the frames
slider = Scale(root2, from_=1, to=15, orient=HORIZONTAL,
                activebackground="blue",bg="grey",bd=5,cursor="hand2",label="Length of word",sliderlength=20,length=250,relief="groove",
                font=('Times', '12', 'bold italic'))
slider.pack(fill=BOTH,pady=20)

# Create a submit button
submit_img = PhotoImage(file='submit.png')
submit_button = Button(root2, image = submit_img,bg = "#236b2d",activebackground="#236b2d",borderwidth=0, command=get_len_words)
submit_button.pack(pady=10)
back_img = PhotoImage(file='back.png')
#img_label= Label(image=back_img,bg="#236b2d",borderwidth=0)
back_button = Button(root2,image = back_img,command=switch_to_window1,bg = "#236b2d",activebackground="#236b2d",borderwidth=0)
back_button.pack(pady=10)
next_img = PhotoImage(file='next.png')
show_button = Button(root2, image = next_img,bg = "#236b2d",activebackground="#236b2d",borderwidth=0, command=show_word)
show_button.pack(pady=10)
# reset_button = Button(root2, text="Reset", command=reset_label)
# reset_button.pack()

# Create buttons and image in the left frame
left_buttons_frame = Frame(left_frame,bg="grey")
left_buttons_frame.pack(side=TOP,pady=10,padx=2)

for i in range(1,7):
    button = Button(left_buttons_frame, text=f"Column {i}",command=lambda i=i: store_button_number(i),background="#bab529",activeforeground="#80db2a")
    button.pack(side=LEFT, padx=11)

# Load and display an image in the left frame
left_image = PhotoImage(file="table1.png")
left_image_label = Label(left_frame, image=left_image)
left_image_label.pack(pady=5)

# Create buttons and image in the right frame
right_buttons_frame = Frame(right_frame,bg="grey")
right_buttons_frame.pack(side=TOP,pady=10)

for i in range(1,6):
    button = Button(right_buttons_frame, text=f"Column {i}",command=lambda i=i: store_button_number(i),background="#bab529",activeforeground="#80db2a")
    button.pack(side=LEFT, padx=16)

# Load and display an image in the right frame
right_image = PhotoImage(file="table2.png")
right_image_label = Label(right_frame, image=right_image)
right_image_label.pack(pady=5)
gui.mainloop()
root2.mainloop()
