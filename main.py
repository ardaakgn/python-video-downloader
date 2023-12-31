from cgitb import text
from pytube import YouTube
import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.font import BOLD
from tkinter import ttk
from pytube import Playlist

#------------------------------------------------------------------------------#

screen = tk.Tk()
screen.iconbitmap(default="youtube.ico")
title = screen.title("Arda Youtube MP3 MP4 Downloader")
screen.geometry("800x700")

yt_logo = PhotoImage(file="youtube.png")
yt_label = Label(screen,image=yt_logo)
yt_label.pack()

 # Künye Alanı





label14 = Label(screen,text="Arda",font=("Helvetica",13,BOLD),fg="black")
label14.place(x=30, y=640)

label15 = Label(screen,text="Akgün",font=("Helvetica",13,BOLD),fg="black")
label15.place(x=30, y=660)

label16 = Label(screen,text="sametardaakgun999@gmail.com",font=("Helvetica",10,BOLD),fg="#780b0b")
label16.place(x=570, y=640)

label17 = Label(screen,text="İletişim:",font=("Helvetica",10,BOLD),fg="black")
label17.place(x=570, y=620)

label19 = Label(screen,text="www.sametarda.site",font=("Helvetica",11,BOLD),fg="black")
label19.place(x=570, y=660)

#------------------------------------------------------------------------------#

class Window:
    def __init__(self, master):
        self.master = master
 
        self.notebook = ttk.Notebook(self.master)

        # Video Bilgilerini Getiren Fonksiyon
        def video_info():
            link = link_field.get()
            yt = YouTube(link)
            title_label_2.config(text=yt.title)
            author_label_2.config(text=yt.author)
            view_label_2.config(text=yt.views)
            len_label_2.config(text=yt.length)
            download_label.config(text="")
        
        # İndirilecek Konumu Seçtiren Fonksiyon
        def select_directory():
            path_select = filedialog.askdirectory()
            path_label.config(text=path_select)
            if select_directory == "":
                download_button.config(state=tk.DISABLED)
        # İndirme İşlemini Yapan Fonksiyon
        def download_mp3():
            link = link_field.get()
            
            try:
                yt = YouTube(link)
            except:
                download_label.config(text="Geçersiz Link")

            folder =path_label.cget("text")

            uzanti = cmb.get()
            if uzanti == "":
                download_label.config(text="Uzantı Seçiniz!")
                download_button.config(state=tk.DISABLED)
            elif uzanti == ".mp3":
                download_button.config(state=tk.NORMAL)
                mp3 = yt.streams.filter(only_audio=True).first() 
                output = mp3.download(folder)
                base ,ext  = os.path.splitext(output)
                to_mp3 = base + uzanti
                os.rename(output, to_mp3)
                download_label.config(text="Başarıyla İndirildi!")
            elif uzanti ==".mp4":
                download_button.config(state=tk.NORMAL)
                mp4 = YouTube(link).streams.get_highest_resolution().download(folder)
                download_label.config(text="Başarıyla İndirildi!")
    
 #------------------------------------------------------------------------------#
        # Frame 1, 2 and 3
        frame1 = ttk.Frame(self.notebook)
        frame2 = ttk.Frame(self.notebook)
        canvas1 = Canvas(frame1,width=700,height=400)
        canvas1.pack() 
        canvas2 = Canvas(frame2,width=700,height=400)
        canvas2.pack() 

#------------------------------------------------------------------------------#
        # Uzantı Seçimi

        ayarlar = [
            ".mp3",
            ".mp4"
        ]

        cmb = ttk.Combobox(canvas1,value = ayarlar,width=10)

        canvas1.create_window(260,300,window=cmb)


        ext_label = Label(canvas1,text="Uzantı Seçiniz",font=("Helvetica",12,BOLD),fg="black")

        canvas1.create_window(150,300,window=ext_label)

        # Link Girilen Alan

        link_field = Entry(canvas1,width=30)
        link_label = Label(canvas1,text="Linki Giriniz",font=("Helvetica",12,BOLD),fg="#780b0b")


        canvas1.create_window(150,80,window=link_label)
        canvas1.create_window(150,125,window=link_field)

        # İndirilecek Konumun Çekildiği Alan

        path_label_text = Label(canvas1,text="İndirilecek Konumu Seçiniz",font=("Helvetica",12,BOLD),fg="#780b0b")
        canvas1.create_window(150,155,window=path_label_text)

        path_label = Label(canvas1,text="",font=("Helvetica",10,BOLD),fg="#3e7804")
        path_button = Button(canvas1,text="Konum Seçiniz",command=select_directory,fg="white",bg="#780b0b",font=("Helvetica",10))

        canvas1.create_window(150,195,window=path_label)
        canvas1.create_window(150,245,window=path_button)

        # İndirme Butonu

        download_button = Button(canvas1,text="İndir",command=download_mp3,fg="white",bg="#780b0b",font=("Helvetica",15))
        canvas1.create_window(150,360,window=download_button)

        # İndiriliyor Bilgisi 

        download_label = Label(canvas1,text="",font=("Helvetica",13,BOLD),fg="black")
        canvas1.create_window(360,360,window=download_label)

        # Video Bilgileri

        title_label_1 = Label(canvas1,text="Video Başlığı",font=("Helvetica",12,BOLD),fg="#780b0b")
        title_label_2 = Label(canvas1,text="",font=("Helvetica",10,BOLD),fg="#3e7804")

        canvas1.create_window(500,50,window=title_label_1)
        canvas1.create_window(500,80,window=title_label_2)

        author_label_1 = Label(canvas1,text="Video Sahibi",font=("Helvetica",12,BOLD),fg="#780b0b")
        author_label_2 = Label(canvas1,text="",font=("Helvetica",10,BOLD),fg="#3e7804")

        canvas1.create_window(500,110,window=author_label_1)
        canvas1.create_window(500,140,window=author_label_2)

        view_label_1 = Label(canvas1,text="Görüntülenme Sayısı",font=("Helvetica",12,BOLD),fg="#780b0b")
        view_label_2 = Label(canvas1,text="",font=("Helvetica",10,BOLD),fg="#3e7804")

        canvas1.create_window(500,170,window=view_label_1)
        canvas1.create_window(500,200,window=view_label_2)

        len_label_1 = Label(canvas1,text="Video Uzunluğu",font=("Helvetica",12,BOLD),fg="#780b0b")
        len_label_2 = Label(canvas1,text="",font=("Helvetica",10,BOLD),fg="#3e7804")

        canvas1.create_window(500,230,window=len_label_1)
        canvas1.create_window(500,260,window=len_label_2)

        # Video Bilgilerini Getiren Buton

        info_button = Button(canvas1,text="Kontrol Et",command=video_info,fg="white",bg="#780b0b",font=("Helvetica",10))
        canvas1.create_window(300,125,window=info_button)
#------------------------------------------------------------------------------#
        # Playlist Fonksiyonları

        # İndirme İşlemini Yapan Fonksiyon
        def download_playlist_mp3():

            link = link_field2.get()
            folder =path_label2.cget("text")

            yt_playlist = Playlist(link)

            uzanti = cmb2.get()
            if uzanti == ".mp3":
                for video in yt_playlist.videos:
                    mp3 = video.streams.filter(only_audio=True).first() 
                    output = mp3.download(folder)
                    base ,ext  = os.path.splitext(output)
                    to_mp3 = base + uzanti
                    os.rename(output, to_mp3)
                download_label2.config(text="Başarıyla İndirildi!")
            elif uzanti ==".mp4":
                for video in yt_playlist.videos:
                    video.streams.get_highest_resolution().download(folder)
                download_label2.config(text="Başarıyla İndirildi!")       
            elif uzanti == "":
                download_label2.config(text="Uzantı Seçiniz!")
                download_button.config(state=tk.DISABLED)

        # İndirilecek Konumu Seçtiren Fonksiyon
        def select_directory2():
            path_select2 = filedialog.askdirectory()
            path_label2.config(text=path_select2)
#------------------------------------------------------------------------------#
        #Playlist GUI

        ayarlar2 = [
            ".mp3",
            ".mp4"
        ]

        cmb2 = ttk.Combobox(canvas2,value = ayarlar2,width=10)

        canvas2.create_window(400,200,window=cmb2)

        ext_label = Label(canvas2,text="Uzantı Seçiniz",font=("Helvetica",12,BOLD),fg="black")

        canvas2.create_window(300,200,window=ext_label)

        # Link Girilen Alan (Playlist)

        link_field2 = Entry(canvas2,width=30)
        link_label2 = Label(canvas2,text="Linki Giriniz",font=("Helvetica",12,BOLD),fg="#780b0b")


        canvas2.create_window(350,60,window=link_label2)
        canvas2.create_window(350,95,window=link_field2)

        # İndirilecek Konumun Çekildiği Alan (Playlist)

        path_label_text2 = Label(canvas2,text="İndirilecek Konumu Seçiniz",font=("Helvetica",12,BOLD),fg="#780b0b")
        canvas2.create_window(350,130,window=path_label_text2)

        path_label2 = Label(canvas2,text="",font=("Helvetica",10,BOLD),fg="#3e7804")
        path_button2 = Button(canvas2,text="Konum Seçiniz",command=select_directory2,fg="white",bg="#780b0b",font=("Helvetica",10))

        canvas2.create_window(350,155,window=path_label2)
        canvas2.create_window(350,245,window=path_button2)

        # İndirme Butonu (Playlist)

        download_button2 = Button(canvas2,text="İndir",command=download_playlist_mp3,fg="white",bg="#780b0b",font=("Helvetica",15))
        canvas2.create_window(350,310,window=download_button2)

        # İndiriliyor Bilgisi  (Playlist)

        download_label2 = Label(canvas2,text="",font=("Helvetica",13,BOLD),fg="black")
        canvas2.create_window(350,350,window=download_label2)
#------------------------------------------------------------------------------#
        #Final
         
        frame1.pack()
        frame2.pack()
        self.notebook.add(frame1, text = "Video İndir")
        self.notebook.add(frame2, text = "Playlist İndir")
 
        self.notebook.select(frame1)
         
        self.notebook.pack()
         
 

window = Window(screen)
screen.mainloop()