from tkinter import *
from visionHandler import Vision

root = Tk()

# Functions

def runCamera():
    index = lb.curselection()[0] if lb.curselection() else 0
    vision = Vision(ImageName = "VipulSnapper")
    vision.VisonApplier(index)

# GUI Logic

root.title('VipulSnapper')
root.iconphoto(True,PhotoImage(file="imgs/logo.png"))
root.geometry('1280x720')
root.minsize(1280, 720)
root.maxsize(1919, 1080)
root.config(background="black") 

if __name__ == "__main__":
    CamImg = PhotoImage(file="imgs/camera.png")
    lb = Listbox(root,background="black",height=3,foreground="white",bd=10,relief=GROOVE,font=("Comic Sans", 30, "bold"),cursor="circle",highlightbackground="#70a1ff",highlightcolor="#ff6b81")
    lb.insert(0,"Tongue")
    lb.insert(1,"Beard")
    lb.insert(2,"Specs")
    lb.pack(anchor=NW,fill=X)
    button = Button(root,
                    text="Start Camera!",
                    font=("Comic Sans", 30, "bold"),
                    fg="#00FF00",
                    bg="black",
                    command=runCamera,
                    activeforeground="blue",
                    activebackground="black",
                    state=ACTIVE,
                    image=CamImg,
                    compound="left",
                    bd=10,
                    relief=RIDGE,
                    padx=20,
                    pady=20,
                    cursor="heart"
                    )
    button.pack(fill=X)

    root.mainloop()