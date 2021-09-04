# Youtube Video downloader with python and Tkinter

# pip install tk
# pip install pytube

import tkinter as tk
from pytube import YouTube


def Download_Video():
    url = YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download()
    tk.Label(window, text = 'Your video is Downloaded!',font = 'arial 15',bg = '#EC7063').place(x = 10, y = 140)

window = tk.Tk()
window.geometry("700x400")
window.config(bg = "blue")
window.resizable(width = False, height = False)
window.title("Youtube Video Downloader")

link = tk.StringVar()

tk.Label(window, text = '          Youtube Video Downloader           ',font= 'arial 20 bold',fg='White',bg = 'Black').pack()
tk.Label(window, text = '  Paste You Youtube Video Link Below  ',font = 'arial 20 bold',fg = 'Black').place(x = 100, y = 60)

link_enter = tk.Entry(window, width = 53, textvariable=link, font = 'arial 15 bold', bg = 'lightblue').place(x = 45, y = 100)

tk.Button(window, text = 'Download Video', font = 'arial 15 bold', fg = 'white', bg = 'black', padx = 2, command=Download_Video).place(x = 285, y = 135)

window.mainloop()


