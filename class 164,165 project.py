from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
root=Tk()
root.geometry("650x650")
root.config(bg="yellow")

label_image=Label(root,bg="light yellow",highlightthickness=3)
label_image.place(relx=0.5,rely=0.3,anchor=CENTER)

img_path=""

def open_img():
    global img_path
    img_path=filedialog.askopenfilename(title="Open Text File",filetypes=(("Text Files","*.jpg;*.gif;*.png;*.jpg;;*.txt"),))
    print(img_path)
    img=ImageTk.PhotoImage(Image.open(img_path))
    label_image['image']=img
    img.close()
def rotate_img():
    global img_path
    image=open(img_path)
    rotate_img=image.rotate(90)
    img=ImageTk.PhotoImage(Image.open(rotate_img))
    img.close()


btn=Button(root,text="open Image",bg="royalblue",fg="white",font=("arial",25,"bold"),padx=10,pady=10,command=open_img)
btn.place(relx=0.7,rely=0.7,anchor=CENTER)
btn2=Button(root,text="rotate Image",bg="royalblue",fg="white",font=("arial",25,"bold"),padx=10,pady=10)
btn2.place(relx=0.2,rely=0.7,anchor=CENTER)
label=Label(root,text="Created By:Poshika Tumula",bg="grey",fg="black",font=("comic sans",15,"bold","italic"))
label.place(relx=0.2,rely=0.9,anchor=W)

root.mainloop()