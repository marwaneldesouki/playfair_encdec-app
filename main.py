
import os
import tkinter
import tkinter.messagebox
import customtkinter
from PIL import ImageGrab,ImageOps,Image
from tkinter import ttk, filedialog,StringVar
from tkinter.filedialog import askopenfile
from threading import *
import random
import time
import concurrent.futures
import encryption as enc
import decryption as dec
import Ai.key_classifier as kc
import functions as fn
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("PlayFair Cipher")
        self.geometry(f"{970}x{680}")
        self.resizable(0,0)
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=1)
        self.grid_rowconfigure((0, 1, 2,4), weight=2)
        
        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Pages", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton( self.sidebar_frame,text="Text Cipher", command=lambda : self.sidebar_button_event(page=self.page_0))
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame,text="Image Cipher", command=lambda : self.sidebar_button_event(page=self.page_1))
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame,text="Audio Cipher", command=lambda : self.sidebar_button_event(page=self.page_2))
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
          #########
        # create slider and progressbar frame
        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=3, column=1,  padx=0, pady=0, sticky="nwe")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
       
        self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.progressbar_1.set(100)
        #########
    def page_0(self):
        try:
            self.main_frame_3.grid_forget()
            self.main_frame_4.grid_forget()
            self.main_frame_5.grid_forget()
            self.main_frame_6.grid_forget()
        except:
            pass
        self.encryption_text_var = StringVar()
        self.decryption_text_var = StringVar()
        self.prediction_var = StringVar()
        self.prediction_var.set("Predict:")
        self.title_frame = customtkinter.CTkFrame(self)
        self.title_frame.grid(row=0, column=1, padx=(20, 20),sticky="nwe")
        self.title_lable = customtkinter.CTkLabel(self.title_frame,anchor='center',text="Text Cipher Page",font=("Comic Sans MS", 40, "bold"),)
        self.title_lable.grid(row=0, column=0,padx=(200,0) ,pady=(10, 0))
        #########
        self.main_frame = customtkinter.CTkFrame(self)
        self.main_frame.grid(row=0,column=1,sticky="wne",pady=100,padx=50,)

        self.plain_label = customtkinter.CTkLabel(self.main_frame,text="Plain Text:")
        self.plain_label.grid(column=0,row=0,pady=20,padx=10,sticky="w")
        self.plain_textbox = customtkinter.CTkEntry(self.main_frame,placeholder_text="Put your text here",width=250)
        self.plain_textbox.grid(column=0,row=0,sticky="w",padx=75)

        self.key_label = customtkinter.CTkLabel(self.main_frame,text="Key:")
        self.key_label.grid(column=0,row=1,pady=20,padx=40,sticky="w")
        self.entry_var = customtkinter.StringVar()
        self.entry_var.trace('w', self.on_text_changed)  # 'w' means trace on write (i.e., when the variable changes)
        self.key_textbox = customtkinter.CTkEntry(self.main_frame,placeholder_text="Put your key here",width=250,textvariable=self.entry_var)
        self.key_textbox.grid(column=0,row=1,sticky="w",padx=70)
        self.key_predict_label = customtkinter.CTkLabel(self.main_frame,textvariable=self.prediction_var)
        self.key_predict_label.grid(column=0,row=1,padx=330,sticky="w")

        self.cypher_label = customtkinter.CTkLabel(self.main_frame,text="Cypher Text:")
        self.cypher_label.grid(column=0,row=3,pady=20,padx=150,sticky="w")

        self.cypher_textbox = customtkinter.CTkEntry(self.main_frame,width=250)
        self.cypher_textbox.grid(column=0,row=3,sticky="W",padx=230)

        self.enc_button = customtkinter.CTkButton(self.main_frame,text="Encrypt Text",command= lambda:self.encryption_text())
        self.enc_button.grid(column=0,row=4,sticky="w",padx=250,rowspan=2)

        #########
        self.main_frame_2 = customtkinter.CTkFrame(self)
        self.main_frame_2.grid(row=0,column=1,sticky="n",pady=(370,0),padx=50,)

        self.plain_label_2 = customtkinter.CTkLabel(self.main_frame_2,text="Cypher Text:")
        self.plain_label_2.grid(column=0,row=0,pady=20,padx=10,sticky="w")
        self.plain_textbox_2 = customtkinter.CTkEntry(self.main_frame_2,placeholder_text="Put your Cypher Text here",width=250)
        self.plain_textbox_2.grid(column=0,row=0,sticky="w",padx=90)

        self.key_label_2 = customtkinter.CTkLabel(self.main_frame_2,text="Key:")
        self.key_label_2.grid(column=0,row=1,pady=20,padx=60,sticky="w")
        self.key_textbox_2 = customtkinter.CTkEntry(self.main_frame_2,placeholder_text="Put your key here",width=250)
        self.key_textbox_2.grid(column=0,row=1,sticky="w",padx=90)

        self.cypher_label_2 = customtkinter.CTkLabel(self.main_frame_2,text="Plain Text:")
        self.cypher_label_2.grid(column=0,row=3,pady=20,padx=170,sticky="w")
        self.cypher_textbox_2 = customtkinter.CTkEntry(self.main_frame_2,width=250)
        self.cypher_textbox_2.grid(column=0,row=3,sticky="W",padx=230)
        self.dec_button_2 = customtkinter.CTkButton(self.main_frame_2,text="Decrypt Text")
        self.dec_button_2.grid(column=0,row=4,sticky="w",padx=250,rowspan=2)
        self.dec_button = customtkinter.CTkButton(self.main_frame_2,text="Decrypt Text",command= lambda:self.decryption_text())
        self.dec_button.grid(column=0,row=4,sticky="w",padx=250,rowspan=2)
      
      
    def page_1(self):
        try:
            self.main_frame.grid_forget()
            self.main_frame_2.grid_forget()
            self.main_frame_5.grid_forget()
            self.main_frame_6.grid_forget()
        except:
            pass
     
        self.encryption_image_var = StringVar()
        self.decryption_image_var = StringVar()
        self.prediction_var = StringVar()
        self.image_input_path_enc = StringVar()
        self.image_outputpath_enc = StringVar()
        self.prediction_var.set("Predict:")
        self.title_frame = customtkinter.CTkFrame(self)
        self.title_frame.grid(row=0, column=1, padx=(20, 20),sticky="nwe")
        self.title_lable = customtkinter.CTkLabel(self.title_frame,anchor='center',text="Image Cipher Page",font=("Comic Sans MS", 40, "bold"),)
        self.title_lable.grid(row=0, column=0,padx=(200,0) ,pady=(10, 0))
        #########
        self.main_frame_3 = customtkinter.CTkFrame(self)
        self.main_frame_3.grid(row=0,column=1,sticky="wne",pady=100,padx=50,)

        self.plain_label = customtkinter.CTkLabel(self.main_frame_3,text="Image Path:")
        self.plain_label.grid(column=0,row=0,pady=20,padx=10,sticky="w")
        self.plain_textbox = customtkinter.CTkEntry(self.main_frame_3,textvariable=self.image_input_path_enc,placeholder_text="Put Image Path Here",width=250)
        self.plain_textbox.grid(column=0,row=0,sticky="w",padx=85)
        self.choose_plain_image_button = customtkinter.CTkButton(self.main_frame_3,text="ChooseImage",command= lambda:self.open_image_encoded(),width=20)
        self.choose_plain_image_button.grid(column=0,row=0,sticky="w",padx=340,rowspan=1)

        self.key_label = customtkinter.CTkLabel(self.main_frame_3,text="Key:")
        self.key_label.grid(column=0,row=1,pady=20,padx=50,sticky="w")
        self.entry_var = customtkinter.StringVar()
        self.entry_var.trace('w', self.on_text_changed)  # 'w' means trace on write (i.e., when the variable changes)
        self.key_textbox = customtkinter.CTkEntry(self.main_frame_3,placeholder_text="Put your key here",width=250,textvariable=self.entry_var)
        self.key_textbox.grid(column=0,row=1,sticky="w",padx=80)
        self.key_predict_label = customtkinter.CTkLabel(self.main_frame_3,textvariable=self.prediction_var)
        self.key_predict_label.grid(column=0,row=1,padx=350,sticky="w")

        self.cypher_label = customtkinter.CTkLabel(self.main_frame_3,text="OutPut Path:")
        self.cypher_label.grid(column=0,row=3,pady=20,padx=10,sticky="w")

        self.cypher_textbox = customtkinter.CTkEntry(self.main_frame_3,width=250,textvariable=self.image_outputpath_enc)
        self.cypher_textbox.grid(column=0,row=3,sticky="W",padx=85)
        self.choose_save_image_button = customtkinter.CTkButton(self.main_frame_3,text="OutPut Path",command= lambda:self.save_image_encoded(),width=20)
        self.choose_save_image_button.grid(column=0,row=3,sticky="w",padx=340,rowspan=1)

        self.enc_button = customtkinter.CTkButton(self.main_frame_3,text="Encrypt Image",command= lambda:self.encryption_image())
        self.enc_button.grid(column=0,row=4,sticky="w",padx=250,rowspan=2)

        #########
        self.image_path_dec = StringVar()
        self.image_outputpath_dec = StringVar()
        self.main_frame_4 = customtkinter.CTkFrame(self)
        self.main_frame_4.grid(row=0,column=1,sticky="n",pady=(370,0),padx=50,)


        self.plain_label = customtkinter.CTkLabel(self.main_frame_4,text="Image Path:")
        self.plain_label.grid(column=0,row=0,pady=20,padx=10,sticky="w")
        self.plain_textbox = customtkinter.CTkEntry(self.main_frame_4,textvariable=self.image_path_dec,placeholder_text="Put Image Path Here",width=250)
        self.plain_textbox.grid(column=0,row=0,sticky="w",padx=85)
        self.choose_enc_image_button = customtkinter.CTkButton(self.main_frame_4,text="ChooseImage",command= lambda:self.open_image_decoded(),width=20)
        self.choose_enc_image_button.grid(column=0,row=0,sticky="w",padx=340,rowspan=1)

        self.key_label = customtkinter.CTkLabel(self.main_frame_4,text="Key:")
        self.key_label.grid(column=0,row=1,pady=20,padx=50,sticky="w")
        self.key_textbox = customtkinter.CTkEntry(self.main_frame_4,placeholder_text="Put your key here",width=250,textvariable=self.entry_var)
        self.key_textbox.grid(column=0,row=1,sticky="w",padx=80)
      
        self.cypher_label = customtkinter.CTkLabel(self.main_frame_4,text="OutPut Path:")
        self.cypher_label.grid(column=0,row=3,pady=20,padx=10,sticky="w")

        self.cypher_textbox = customtkinter.CTkEntry(self.main_frame_4,width=250,textvariable=self.image_outputpath_dec)
        self.cypher_textbox.grid(column=0,row=3,sticky="W",padx=85)
        self.choose_save_image_button = customtkinter.CTkButton(self.main_frame_4,text="OutPut Path",command= lambda:self.save_image_decoded(),width=20)
        self.choose_save_image_button.grid(column=0,row=3,sticky="w",padx=340,rowspan=1)

        self.dec_button = customtkinter.CTkButton(self.main_frame_4,text="Decrypt Image",command= lambda:self.decryption_image())
        self.dec_button.grid(column=0,row=4,sticky="w",padx=250,rowspan=2)
      
       
       

    def page_2(self):
        try:
            self.main_frame.grid_forget()
            self.main_frame_2.grid_forget()
            self.main_frame_3.grid_forget()
            self.main_frame_4.grid_forget()
        except:
            pass
        # self.main_frame.grid_forget()
        # self.main_frame_2.grid_forget()
        self.encryption_audio_var = StringVar()
        self.decryption_audio_var = StringVar()
        self.prediction_var = StringVar()
        self.audio_input_path_enc = StringVar()
        self.audio_outputpath_enc = StringVar()
        self.prediction_var.set("Predict:")
        self.title_frame = customtkinter.CTkFrame(self)
        self.title_frame.grid(row=0, column=1, padx=(20, 20),sticky="nwe")
        self.title_lable = customtkinter.CTkLabel(self.title_frame,anchor='center',text="Audio Cipher Page",font=("Comic Sans MS", 40, "bold"),)
        self.title_lable.grid(row=0, column=0,padx=(200,0) ,pady=(10, 0))
        #########
        self.main_frame_5 = customtkinter.CTkFrame(self)
        self.main_frame_5.grid(row=0,column=1,sticky="wne",pady=100,padx=50,)

        self.plain_label = customtkinter.CTkLabel(self.main_frame_5,text="Audi Path:")
        self.plain_label.grid(column=0,row=0,pady=20,padx=10,sticky="w")
        self.plain_textbox = customtkinter.CTkEntry(self.main_frame_5,textvariable=self.audio_input_path_enc,placeholder_text="Put Image Path Here",width=250)
        self.plain_textbox.grid(column=0,row=0,sticky="w",padx=85)
        self.choose_plain_Audio_button = customtkinter.CTkButton(self.main_frame_5,text="ChooseAudio",command= lambda:self.open_audio_encoded(),width=20)
        self.choose_plain_Audio_button.grid(column=0,row=0,sticky="w",padx=340,rowspan=1)

        self.key_label = customtkinter.CTkLabel(self.main_frame_5,text="Key:")
        self.key_label.grid(column=0,row=1,pady=20,padx=50,sticky="w")
        self.entry_var = customtkinter.StringVar()
        self.entry_var.trace('w', self.on_text_changed)  # 'w' means trace on write (i.e., when the variable changes)
        self.key_textbox = customtkinter.CTkEntry(self.main_frame_5,placeholder_text="Put your key here",width=250,textvariable=self.entry_var)
        self.key_textbox.grid(column=0,row=1,sticky="w",padx=80)
        self.key_predict_label = customtkinter.CTkLabel(self.main_frame_5,textvariable=self.prediction_var)
        self.key_predict_label.grid(column=0,row=1,padx=350,sticky="w")

        self.cypher_label = customtkinter.CTkLabel(self.main_frame_5,text="OutPut Path:")
        self.cypher_label.grid(column=0,row=3,pady=20,padx=10,sticky="w")

        self.cypher_textbox = customtkinter.CTkEntry(self.main_frame_5,width=250,textvariable=self.audio_outputpath_enc)
        self.cypher_textbox.grid(column=0,row=3,sticky="W",padx=85)
        self.choose_save_audio_button = customtkinter.CTkButton(self.main_frame_5,text="OutPut Path",command= lambda:self.save_audio_encoded(),width=20)
        self.choose_save_audio_button.grid(column=0,row=3,sticky="w",padx=340,rowspan=1)

        self.enc_button = customtkinter.CTkButton(self.main_frame_5,text="Encrypt Audio",command= lambda:self.encryption_audio())
        self.enc_button.grid(column=0,row=4,sticky="w",padx=250,rowspan=2)

        #########
        self.audio_path_dec = StringVar()
        self.audio_outputpath_dec = StringVar()
        self.main_frame_6 = customtkinter.CTkFrame(self)
        self.main_frame_6.grid(row=0,column=1,sticky="n",pady=(370,0),padx=50,)


        self.plain_label = customtkinter.CTkLabel(self.main_frame_6,text="Audio Path:")
        self.plain_label.grid(column=0,row=0,pady=20,padx=10,sticky="w")
        self.plain_textbox = customtkinter.CTkEntry(self.main_frame_6,textvariable=self.audio_path_dec,placeholder_text="Put Audio Path Here",width=250)
        self.plain_textbox.grid(column=0,row=0,sticky="w",padx=85)
        self.choose_enc_image_button = customtkinter.CTkButton(self.main_frame_6,text="ChooseAuido",command= lambda:self.open_audio_decoded(),width=20)
        self.choose_enc_image_button.grid(column=0,row=0,sticky="w",padx=340,rowspan=1)

        self.key_label = customtkinter.CTkLabel(self.main_frame_6,text="Key:")
        self.key_label.grid(column=0,row=1,pady=20,padx=50,sticky="w")
        self.key_textbox = customtkinter.CTkEntry(self.main_frame_6,placeholder_text="Put your key here",width=250,textvariable=self.entry_var)
        self.key_textbox.grid(column=0,row=1,sticky="w",padx=80)
      
        self.cypher_label = customtkinter.CTkLabel(self.main_frame_6,text="OutPut Path:")
        self.cypher_label.grid(column=0,row=3,pady=20,padx=10,sticky="w")

        self.cypher_textbox = customtkinter.CTkEntry(self.main_frame_6,width=250,textvariable=self.audio_outputpath_dec)
        self.cypher_textbox.grid(column=0,row=3,sticky="W",padx=85)
        self.choose_save_image_button = customtkinter.CTkButton(self.main_frame_6,text="OutPut Path",command= lambda:self.save_audio_decoded(),width=20)
        self.choose_save_image_button.grid(column=0,row=3,sticky="w",padx=340,rowspan=1)

        self.dec_button = customtkinter.CTkButton(self.main_frame_6,text="Decrypt Audio",command= lambda:self.decryption_audio())
        self.dec_button.grid(column=0,row=4,sticky="w",padx=250,rowspan=2)
      
       

      

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self,page):
        page()
    def encryption_text(self):
       self.encryption_text_var.set("")
       self.encryption_text_var.set(enc.encode_text_function(self.plain_textbox.get(),self.key_textbox.get()))
       self.cypher_textbox.delete(0,customtkinter.END)
       self.cypher_textbox.insert(0,self.encryption_text_var.get())
    def decryption_text(self):
       self.decryption_text_var.set("")
       self.decryption_text_var.set(dec.decode_text_function(self.plain_textbox_2.get(),self.key_textbox_2.get()))
       self.cypher_textbox_2.delete(0,customtkinter.END)
       self.cypher_textbox_2.insert(0,self.decryption_text_var.get())
    def encryption_image(self):
       print(self.image_outputpath_enc.get(),self.key_textbox.get())
       enc.encode_image_to_base64(self.image_input_path_enc.get(),self.key_textbox.get(),self.image_outputpath_enc.get())
    def decryption_image(self):
       print(self.image_outputpath_dec.get(),self.key_textbox.get())
       dec.decode_base64_to_image(self.image_path_dec.get(),self.key_textbox.get(),self.image_outputpath_dec.get())
    
    def encryption_audio(self):
       print(self.audio_outputpath_enc.get(),self.key_textbox.get())
       enc.encode_wav_to_base64(self.audio_input_path_enc.get(),self.key_textbox.get(),self.audio_outputpath_enc.get())
    def decryption_audio(self):
       print(self.audio_outputpath_dec.get(),self.key_textbox.get())
       dec.decode_base64_to_wav(self.audio_path_dec.get(),self.key_textbox.get(),self.audio_outputpath_dec.get())
      
    def on_text_changed(self,*args):
    # This function will be called whenever the text in the Entry widget changes
        predicted_power_status = "Predict:"+kc.predict_key_power(len(self.entry_var.get()),fn.has_numbers(self.entry_var.get()))[0]
        self.prediction_var.set(predicted_power_status)
    def open_image_encoded(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;")])
        if file_path:
            self.image_input_path_enc.set(file_path)
    def open_image_decoded(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;")])
        if file_path:
            self.image_path_dec.set(file_path)
    def save_image_encoded(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ])
        if file_path:
            self.image_outputpath_enc.set(file_path)
    def save_image_decoded(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ])
        if file_path:
            self.image_outputpath_dec.set(file_path)
    
    
    def open_audio_encoded(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio file", "*.wav;")])
        if file_path:
            self.audio_input_path_enc.set(file_path)
    def open_audio_decoded(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio file", "*.wav;")])
        if file_path:
            self.audio_path_dec.set(file_path)
    def save_audio_encoded(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".WAV", filetypes=[("Wav", "*.wav;"),])
        if file_path:
            self.audio_outputpath_enc.set(file_path)
    def save_audio_decoded(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".WAV", filetypes=[("Wav", "*.wav;"),])
        if file_path:
            self.audio_outputpath_dec.set(file_path)
 
if __name__ == "__main__":
    app = App()
    app.page_0()
    app.mainloop()