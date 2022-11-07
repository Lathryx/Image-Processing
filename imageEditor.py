import tkinter as tk 
from tkinter import filedialog as fd, ttk, Scale 
from tkinter.constants import CENTER, RAISED 
from PIL import Image, ImageTk 
from tkinter import messagebox 

from imageEditorLib.gaussBlur import gaussBlur  

ws = tk.Tk()
ws.title("Image Editor")
ws.geometry(f"{round(ws.winfo_screenwidth()*0.7)}x{round(ws.winfo_screenheight()*0.7)}")
style = ttk.Style()
style.theme_use('clam') 
rawImg = Image.open("./upload-icon.png") 
initImg = ImageTk.PhotoImage(Image.open("./upload-icon.png")) 


mainPane = tk.PanedWindow(ws, orient=tk.HORIZONTAL, opaqueresize=False, sashwidth=9, relief="flat", bg="#FFFFFF", bd=0)
mainPane.pack(fill=tk.BOTH, expand=1)

controlsPane = tk.PanedWindow(mainPane, orient=tk.VERTICAL) 
mainPane.add(controlsPane)

imgPane = tk.PanedWindow(mainPane, orient=tk.VERTICAL) 
mainPane.add(imgPane)

controlsPaneText = tk.Label(controlsPane, text="Controls Pane", font=("Arial", 20), bg="#FFFFFF", fg="#000000", anchor=CENTER) 
controlsPane.add(controlsPaneText) 

prevImgPreviewWidth = 1 
def handleResize(e): 
    global rawImg, prevImgPreviewWidth 
    w, h = rawImg.size 
    newImg = None 
    xBoundaryMet = imgPreview.winfo_width() <= imgPreview.image.width() 
    yBoundaryMet = imgPreview.image.height() >= imgPreview.winfo_height() 
    print(yBoundaryMet, imgPreview.image.height(), imgPreview.winfo_height(), xBoundaryMet, imgPreview.image.width(), imgPreview.winfo_width()) 
    if not yBoundaryMet: 
        if xBoundaryMet: 
            newImg = ImageTk.PhotoImage(rawImg.resize((imgFrame.winfo_width(), round(h*(imgFrame.winfo_width()/w))), resample=0))
        else: 
            newImg = imgPreview.image 
    else: 
        if xBoundaryMet: 
            if imgPreview.winfo_width() < prevImgPreviewWidth: 
                newImg = ImageTk.PhotoImage(rawImg.resize((imgFrame.winfo_width(), round(h*(imgFrame.winfo_width()/w))), resample=0))
            else: 
                newImg = imgPreview.image 
        else: 
            newImg = imgPreview.image 
        # if xBoundaryMet: 
        #     newImg = imgPreview.image 
        # else: 
        #     newImg = ImageTk.PhotoImage(rawImg.resize((imgFrame.winfo_width(), round(h*(imgFrame.winfo_width()/w))), resample=0)) 
    # newImg = ImageTk.PhotoImage(rawImg.resize((imgFrame.winfo_width(), round(h*(imgFrame.winfo_width()/w))), resample=0)) if not yBoundaryMet and xBoundaryMet else imgPreview.image 
    # .resize((round(w*imgFrame.winfo_height()/h), imgFrame.winfo_height()), resample=0) 
    

    imgPreview.configure(image=newImg) 
    imgPreview.image = newImg 
    prevImgPreviewWidth = imgPreview.winfo_width() 

def handleGaussBlur(x): 
    newImg = gaussBlur(rawImg, x) 
    imgPreview.configure(image=newImg) 
    imgPreview.image = newImg 

mainPane.bind("<Configure>", handleResize)
mainPane.bind("<ButtonRelease-1>", handleResize) 

imgFrame = tk.Frame(imgPane, width=imgPane.winfo_width(), height=imgPane.winfo_height(), padx=5, pady=5, bg="#202124") 
imgPane.add(imgFrame) 

gaussBlurSlider = Scale(controlsPane, from_=0, to=10, orient=tk.HORIZONTAL, length=200, label="Gaussian Blur", command=handleGaussBlur) 
controlsPane.add(gaussBlurSlider) 


# imgLabel = tk.Label(imgFrame, text="Image", image=initImg) 
# imgLabel.image = initImg 

# imgFrame.place(relx=0.5, rely=0.5, anchor=CENTER) 
# imgLabel.pack(fill="both", expand="yes") 

imgPreview = tk.Label(imgFrame, text="Image Preview Pane", image=initImg)
imgPreview.image = initImg 
imgPreview.place(relx=0.5, rely=0.5, relwidth=0.8, relheight=0.8, anchor=CENTER) 


def about():
    messagebox.showinfo('Image Editor', 'This program allows you to make simple edits to images on your PC. It uses a Python library also made by yours truly for all the functions that are available to make edits to your images. The desktop app itself was created using Python, the famous Tkinter module, PIL for loading images, and some others.')
def select_file(e=None): 
    global rawImg 
    filetypes = (
        ('Image files', '*.png *.jpg *.jpeg *.gif'),
        ('All files', '*.*')
    ) 

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='C:\Pictures',
        filetypes=filetypes)

    # showinfo(
    #     title='Selected File',
    #     message=filename
    # )

    rawImg = Image.open(filename) 
    w, h = rawImg.size 
    if h < imgFrame.winfo_height(): 
        newImg = ImageTk.PhotoImage(rawImg.resize((imgFrame.winfo_width(), round(h*(imgFrame.winfo_width()/w))), resample=0)) 
    else: 
        newImg = ImageTk.PhotoImage(rawImg) 

    imgPreview.configure(image=newImg) 
    imgPreview.image = newImg 
def save_file(e=None): 
    filetypes = (
        ('Image files', '*.png *.jpg *.jpeg *.gif'),
        ('All files', '*.*')
    ) 

    filename = fd.asksaveasfilename(
        title='Save a file',
        initialdir='C:\Pictures',
        filetypes=filetypes)

    # showinfo(
    #     title='Selected File',
    #     message=filename
    # )

    ImageTk.getimage(imgPreview.image).save(filename) 
def quit_program(e=None): 
    confirm = messagebox.askyesno(title="Quitting Program...", message="Are you sure you want to quit?")
    if confirm: ws.quit() 

menubar = tk.Menu(ws, background='#ff8000', foreground='black', activebackground='white', activeforeground='black') 
file = tk.Menu(menubar, tearoff=0) 
file.add_command(label="Open File...", command=select_file, accelerator="Ctrl+O")  
file.add_command(label="Save As...", accelerator="Ctrl+S")    
file.add_separator() 
file.add_command(label="Exit", command=quit_program, accelerator="Ctrl+Q") 
ws.bind("<Control-o>", select_file) 
ws.bind("<Control-s>", save_file) 
ws.bind("<Control-q>", quit_program) 
menubar.add_cascade(label="File", menu=file)  

# edit = tk.Menu(menubar, tearoff=0)  
# edit.add_command(label="Undo")  
# edit.add_separator()     
# edit.add_command(label="Cut")  
# edit.add_command(label="Copy")  
# edit.add_command(label="Paste")  
# menubar.add_cascade(label="Edit", menu=edit)  

help = tk.Menu(menubar, tearoff=0)  
help.add_command(label="About", command=about)  
menubar.add_cascade(label="Help", menu=help)  


mainPane.config(sashrelief=RAISED) 
ws.config(menu=menubar)
ws.protocol("WM_DELETE_WINDOW", quit_program) 
ws.mainloop() 