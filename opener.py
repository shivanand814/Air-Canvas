import tkinter as tk
from PIL import ImageTk, Image
import subprocess

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Set window title
        self.title("AIR CANVA")

        # Set window size
        self.geometry("800x600")

        # Create a container to hold multiple frames
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Dictionary to store frames
        self.frames = {}

        # Create and add frames to the dictionary
        for F in (StartPage, PageOne, PageTwo):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the initial frame
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Load the background image
        image = Image.open("8.png")
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the background image
        background_label = tk.Label(self, image=photo)
        background_label.image = photo  # Keep a reference to prevent garbage collection

        # Place the background label
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Next button to navigate to the next frame
        next_button = tk.Button(self, text="Next", command=lambda: controller.show_frame(PageOne), bg="#40E0D0", fg="white", font=("Arial", 12), padx=5, pady=2, bd=0)
        next_button.pack(side="bottom", padx=20, pady=20, anchor="se")

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Load the background image
        image = Image.open("6.png")
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the background image
        background_label = tk.Label(self, image=photo)
        background_label.image = photo  # Keep a reference to prevent garbage collection

        # Place the background label
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

       

        # Next button to navigate to the next frame
        next_button = tk.Button(self, text="Next", command=lambda: controller.show_frame(PageTwo), bg="#40E0D0", fg="white", font=("Arial", 12), padx=5, pady=2, bd=0)
        next_button.pack(side="bottom", padx=20, pady=20, anchor="se")

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Load the background image
        image = Image.open("7.png")
        photo = ImageTk.PhotoImage(image)

        # Create a label to hold the background image
        background_label = tk.Label(self, image=photo)
        background_label.image = photo  # Keep a reference to prevent garbage collection

        # Place the background label
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        

        # Open Canvas button to open canvas.py file
        open_canvas_button = tk.Button(self, text="Open Air Canvas", command=self.open_canvas, bg="#40E0D0", fg="white", font=("Arial", 12), padx=5, pady=2, bd=0)
        open_canvas_button.pack(side="bottom", padx=20, pady=20, anchor="se")
        drag_button = tk.Button(self, text="Open DnD", command=self.d_n_d, bg="#40E0D0", fg="white", font=("Arial", 12), padx=7, pady=4, bd=0)
        drag_button.pack(side="bottom", padx=20, pady=20, anchor="se")

    def open_canvas(self):
        subprocess.Popen(['python', 'canvas.py'])
    def d_n_d(self):
        subprocess.Popen(['python', 'draganddrop.py'])

app = SampleApp()
app.mainloop()
