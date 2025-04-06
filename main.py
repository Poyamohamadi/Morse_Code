from customtkinter import *
from pygame import mixer
from PIL import Image
import os 

class MyApp(CTk):
    def __init__(self):
        super(MyApp,self).__init__()
        self.run()

    def run(self):
        # Define window 
        self.title('Morse Code')
        self.geometry('430x310')
        self.resizable(0,0)

        # Create morse code dictionaries
        self.english_to_morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
                            'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
                            'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
                            'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
                            'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
                            'u': '..--', 'v': '...-', 'w': '.--', 'x': '-..-',
                            'y': '-.--', 'z': '--..', '1': '.----',
                            '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                            '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                            '0': '-----', ' ':' ', '|':'|', "":"" }

        self.morse_to_english = dict([(value, key) for key, value in self.english_to_morse.items()])

        # Define layout:
            # Create frame
        input_frame = CTkFrame(master=self,fg_color="gray")
        input_frame.pack(padx=16, pady=(16,8))
        output_frame = CTkFrame(master=self,fg_color="gray")
        output_frame.pack(padx=16, pady=(8,16))

        #Layout for self.input_frame:
        self.input_text = CTkTextbox(input_frame,height=120,activate_scrollbars=0,font=('bold',18))
        self.input_text.grid(row=0, column=1, rowspan=3, padx=10, pady=5)

            # Variable 
        self.language = IntVar()
        self.language.set(1)

            # RadioButton
        morse_button = CTkRadioButton(input_frame, text="English --> Morse Code",
        variable=self.language, value=1)
        morse_button.grid(row=0, column=0, pady=(15,0))

        english_button = CTkRadioButton(input_frame, text="Morse Code --> English",
        variable=self.language, value=2)
        english_button.grid(row=1, column=0)
            # Button
        guide_button = CTkButton(input_frame, text="Guide",command=self.show_guide)
        guide_button.grid(row=2, column=0, sticky="WE", padx=10,ipadx=10,pady=10)

        # Layout for self.output_frame:
        self.output_text = CTkTextbox(output_frame, height=120,activate_scrollbars=0,font=('bold',23))
        self.output_text.grid(row=0, column=1, rowspan=4, padx=10, pady=5)

            # Button 
        convert_button = CTkButton(output_frame, text="Convert",height=25,command=self.convert)
        convert_button.grid(row=0, column=0,  padx=5,ipadx=15)

        play_button = CTkButton(output_frame, text="Play Morse",height=25,command=self.play)
        play_button.grid(row=1, column=0, padx=5, sticky="WE")

        clear_button = CTkButton(output_frame, text="Clear",height=25,command=self.clear)
        clear_button.grid(row=2, column=0, padx=5, sticky="WE")

        quit_button = CTkButton(output_frame, text="Quit",height=25,command=self.destroy)
        quit_button.grid(row=3, column=0, padx=5, sticky="WE")

        # Run window's main loop
        self.mainloop()
    
    def show_guide(self):
        guide = CTkToplevel()
        guide.title("Morse Guide")
        guide.geometry(f'430x310+{self.winfo_x()+535}+{self.winfo_y()}')
        
        morse = CTkImage(light_image=Image.open(os.path.join('morse.png')),size=(300,300))
        CTkLabel(master=guide,image=morse,text='').pack(fill='both',expand=1)

    def get_morse(self):
        morse_code = ""
        text = str(self.input_text.get("1.0", 'end')).lower()

        for letter in text:
            if letter not in self.english_to_morse.keys():
                text = text.replace(letter, '')

        word_list = text.split(" ")

        for word in word_list:
            letters = list(word)
            for letter in letters:
                morse_char = self.english_to_morse[letter]
                morse_code += morse_char
                morse_code += " "
            morse_code += "|"
        self.output_text.delete("1.0", 'end')
        self.output_text.insert("1.0", morse_code)

    def get_english(self):
        english = ""
        text = str(self.input_text.get("1.0", 'end'))

        for letter in text:
            if letter not in self.morse_to_english.keys():
                text = text.replace(letter, '')

        word_list = text.split("|")

        for word in word_list:
            letters = word.split(" ")
            for letter in letters:
                english_char = self.morse_to_english[letter]
                english += english_char
            english += " "
        self.output_text.delete("1.0", 'end')
        self.output_text.insert("1.0", english)

    def convert(self):
        if self.language.get() == 1: # English to morse code:
            self.get_morse()
        elif self.language.get() == 2: # morse code to English:
            self.get_english()
    
    def play(self):
        if self.language.get() == 1:
            text = self.output_text.get("1.0", END)
        elif self.language.get() == 2:
            text = self.input_text.get("1.0", END)

        mixer.init()
        for value in text:
            if value == ".":
                mixer.music.load(os.path.join("dot.mp3"))
                mixer.music.play()
                self.after(100)
            elif value == "-":
                mixer.music.load(os.path.join("dash.mp3"))
                mixer.music.play()
                self.after(200)
            elif value == " ":
                self.after(300)
            elif value == "|":
                self.after(700)

    def clear(self):
        self.input_text.delete('1.0','end')
        self.output_text.delete('1.0','end')

if __name__ == "__main__":
    MyApp()