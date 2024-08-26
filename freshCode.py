# import tkinter as tk
# from tkinter import messagebox
# # print("hello world")

# # list = [2,45,6,4,32,45,6,7,755,1]

# # list.sort()

# # for i in list:
# #     print(i)

# # Create the main application window
# # root = tk.Tk()
# # root.title("Simple Tkinter App")
# # root.geometry("300x200")

# # # Create a label widget
# # label = tk.Label(root, text="Hello, Tkinter!")
# # label.pack(pady=20)

# # # Create a button widget
# # button = tk.Button(root, text="Click Me", command=lambda: label.config(text="Button Clicked!"))
# # button.pack(pady=10)

# # # Run the Tkinter event loop
# # root.mainloop()


# def show_message():
#     messagebox.showinfo("Message", "You clicked the button!")

# # Create the main application window
# root = tk.Tk()
# root.title("Advanced Tkinter App")
# root.geometry("400x300")

# # Create a frame to hold widgets
# frame = tk.Frame(root)
# frame.pack(padx=20, pady=20)

# # Create a label widget
# label = tk.Label(frame, text="Enter your name:")
# label.grid(row=0, column=0, padx=5, pady=5)

# # Create an entry widget
# entry = tk.Entry(frame)
# entry.grid(row=0, column=1, padx=5, pady=5)

# # Create a button widget
# button = tk.Button(frame, text="Submit", command=show_message)
# button.grid(row=1, columnspan=2, pady=10)

# # Run the Tkinter event loop
# root.mainloop()

import tkinter as tk
from tkinter import filedialog
from pygame import mixer

# Initialize the mixer
mixer.init()

class MusicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("300x150")
        
        # Initialize music file path
        self.music_file = None

        # Create and place widgets
        self.label = tk.Label(root, text="No file selected")
        self.label.pack(pady=10)

        self.play_button = tk.Button(root, text="Play", command=self.play_music)
        self.play_button.pack(pady=5)

        self.pause_button = tk.Button(root, text="Pause", command=self.pause_music)
        self.pause_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=5)

        self.open_button = tk.Button(root, text="Open", command=self.open_file)
        self.open_button.pack(pady=5)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
        if file_path:
            self.music_file = file_path
            self.label.config(text=f"Playing: {file_path}")

    def play_music(self):
        if self.music_file:
            mixer.music.load(self.music_file)
            mixer.music.play()
        else:
            self.label.config(text="No file selected")

    def pause_music(self):
        if mixer.music.get_busy():
            mixer.music.pause()
        else:
            self.label.config(text="No music playing")

    def stop_music(self):
        if mixer.music.get_busy():
            mixer.music.stop()
        else:
            self.label.config(text="No music playing")

# Create the main application window
root = tk.Tk()
app = MusicApp(root)
root.mainloop()
