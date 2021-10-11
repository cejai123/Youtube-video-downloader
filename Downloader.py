import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog

root = Tk()
root.geometry("520x280")
root.resizable(False, False)
root.title("Youtube video downloader")

video_Link = StringVar()
download_Path = StringVar()

def widgets():
    headlabel = Label(root, text="YouTube Video Downloader by Cejai",padx=15,pady=15,)
    headlabel.grid(row=1,column=1,pady=10,padx=5,columnspan=3)
    linklabel = Label(root,text="YouTube link :",pady=5,padx=5)
    linklabel.grid(row=2,column=0,pady=5,padx=5)
    root.linkText = Entry(root,width=35,textvariable=video_Link)
    root.linkText.grid(row=2,column=1,pady=5,padx=5,columnspan=2)
    destlabel = Label(root,text="Destination :",pady=5,padx=9)
    destlabel.grid(row=3,column=0,pady=5,padx=5)
    root.destinationText = Entry(root,width=27,textvariable=download_Path)
    root.destinationText.grid(row=3,column=1,pady=5,padx=5)
    browsebutton = Button(root,text="Browse",command=browse,width=10,relief=GROOVE)
    browsebutton.grid(row=3,column=2,pady=1,padx=1)
    downloadbutton = Button(root,text="Download Video",command=download,width=20,pady=10,padx=15,relief=GROOVE)
    downloadbutton.grid(row=4,column=1,pady=20,padx=20)

def browse():
    director = filedialog.askdirectory(initialdir="Your File Path",title="Save video")
    download_Path.set(director)

def download():
    if len(root.linkText.get()) == 0:
        tk.messagebox.showerror("Error","No link found")
    elif len(root.destinationText.get()) == 0:
        tk.messagebox.showerror("Error","No destination found")
    else:
        messagebox = tk.messagebox.askquestion("Checking","Are you sure your want to download")
        if messagebox == "yes":
            getvideo = video_Link.get()
            downloadfolder = download_Path.get()
            video = YouTube(getvideo)
            stream = video.streams.first()
            stream.download(downloadfolder)
            messagebox.showinfo("Successful","Downloaded Video successfully\n"+ downloadfolder)
        else:
            root.destroy()
widgets()
root.mainloop()