from tkinter import Tk, Frame, Label, Entry, Button, messagebox
import webbrowser 
from PIL import Image,ImageTk


font_type = ('Courier New',17,'bold')
font_type2 = ('Courier New',10,'bold')
font_type3 = ('Courier New',18,'bold')
font_type4 = ('Courier New',14,'bold')
master = Tk()

class Tic:
    def __init__(self,master):
        self.master = master
        self.full = Frame(self.master, width=700, height=550)
        self.full.place(x=0,y=0)

        self.background = Image.open('../assets/imag1.png')
        self.background = self.background.resize((700, 550))
        self.background = ImageTk.PhotoImage(self.background)
        self.background_label = Label(self.full, image= self.background)
        # self.background_label.image = self.background
        self.background_label.place(x=0,y=0)

        self.button_on_campus = Button(self.full,text='On Campus',font = font_type,bg='silver',width = 12,command=self.On_Btn1)
        self.button_on_campus.place(x=258,y=120)
        self.description1 = Label(self.full, text='Staff and Locations inside the academic blocks',bg='lavender',fg='black',font=font_type2)
        self.description1.place(x=170,y=190)

        self.button_off_campus = Button(self.full,text='Off Campus',font = font_type,bg='silver',width=12,command=self.On_Btn2)
        self.button_off_campus.place(x=258,y=270)
        self.description1 = Label(self.full, text='Locations outside the academic blocks',bg='lavender',fg='black',font=font_type2)
        self.description1.place(x=195,y=330)
        
    #defining functions for buttons

    def On_Btn1(self):
        self.full.destroy()
        obj_classbut1 = Btn1(master)



    def On_Btn2(self):
        self.full.destroy()
        obj_classbut2 = Btn2(master)

class Btn1:
    def __init__(self,master):
        self.master = master
        self.master.title('On Campus')
        self.full_1= Frame(self.master, width=700, height=550,bg='beige')
        self.full_1.place(x=0,y=0)

        self.background_1 = Image.open('../assets/imag5.png')
        self.background_1= self.background_1.resize((700, 550))
        self.background_1= ImageTk.PhotoImage(self.background_1)
        self.background_1_label = Label(self.full_1, image= self.background_1)
        self.background_1_label.image = self.background_1
        self.background_1_label.place(x=0,y=0)

        self.Title_1 = Label(self.full_1, text='Staff :',bg='pink',font=font_type)
        self.Title_1.place(x=50,y=40)

        self.button_on_campus_s = Button(self.full_1,text='Mrs L.V.A Priya ',font = font_type2,bg='silver',width = 18,command=self.On_Priya)
        self.button_on_campus_s.place(x=50,y=80)
        self.button_on_campus_s = Button(self.full_1,text='Mr N.Praveen Kumar',font = font_type2,bg='silver',width = 18)
        self.button_on_campus_s.place(x=50,y=130)

        self.Title_1 = Label(self.full_1, text='Places :' , bg='pink',font=font_type)
        self.Title_1.place(x=50,y=280)

        self.button_on_campus_p = Button(self.full_1,text='C Block Labs',font = font_type2,bg='silver',width = 18,command=self.On_Cbl)
        self.button_on_campus_p.place(x=50,y=325)
        self.button_on_campus_p = Button(self.full_1,text='Restrooms',font = font_type2,bg='silver',width = 18)
        self.button_on_campus_p.place(x=50,y=376)

        self.tool_imag = Image.open('../assets/imag_staff.png')
        self.tool_imag = self.tool_imag.resize((170, 150))
        self.tool_imag = ImageTk.PhotoImage(self.tool_imag)
        self.tool_imag_label= Label(self.full_1, image= self.tool_imag)
        self.tool_imag_label.image = self.tool_imag
        self.tool_imag_label.place(x=420,y=30)

        self.tool_imag = Image.open('../assets/places.png')
        self.tool_imag = self.tool_imag.resize((170, 150))
        self.tool_imag = ImageTk.PhotoImage(self.tool_imag)
        self.tool_imag_label= Label(self.full_1, image= self.tool_imag)
        self.tool_imag_label.image = self.tool_imag
        self.tool_imag_label.place(x=420,y=270)

    def On_Priya(self):
        self.full_1.destroy()
        obj_classPriya = Priya(master)
    
    def On_Cbl(self):
        self.full_1.destroy()
        obj_classC_Block_Labs = C_Block_Labs(master)

class Priya:
    def __init__(self,master):
        self.master = master
        self.master.title('Mrs.L.V.A Priya')
        self.full_2 = Frame(self.master, width=700, height=550)
        self.full_2.place(x=0,y=0)

        self.background_2 = Image.open('../assets/pb.png')
        self.background_2= self.background_2.resize((700, 550))
        self.background_2= ImageTk.PhotoImage(self.background_2)
        self.background_2_label = Label(self.full_2, image= self.background_2)
        self.background_2_label.image = self.background_2
        self.background_2_label.place(x=0,y=0)

        self.P_Title = Label(self.full_2, text='Mrs.L.V.A Priya' , bg='Dark green',fg='white',font=font_type3)
        self.P_Title.place(x=240,y=240)
        self.P_Title = Label(self.full_2, text = 'Position = Assistant Lecturer\nDepartment = Artificial Intelligence\nBlock = C\nRoom = 211',justify = ['left'], bg='Dark green',fg='white',font=font_type4)
        self.P_Title.place(x=150,y=310)

        self.tool_imag_1 = Image.open('../assets/imag.png')
        self.tool_imag_1 = self.tool_imag_1.resize((150, 130))
        self.tool_imag_1 = ImageTk.PhotoImage(self.tool_imag_1)
        self.tool_imag_label_1= Label(self.full_2, image= self.tool_imag_1)
        self.tool_imag_label_1.image = self.tool_imag_1
        self.tool_imag_label_1.place(x=270,y=80)
    

class C_Block_Labs:
    def __init__(self,master):
        self.master = master
        self.master.title('C Block Labs')
        self.full_3 = Frame(self.master, width=700, height=550)
        self.full_3.place(x=0,y=0)

        self.background_3 = Image.open('../assets/imag4.png')
        self.background_3= self.background_3.resize((700, 550))
        self.background_3= ImageTk.PhotoImage(self.background_3)
        self.background_3_label = Label(self.full_3, image= self.background_3)
        self.background_3_label.image = self.background_3
        self.background_3_label.place(x=0,y=0)

        self.tool_imag_2 = Image.open('../assets/lab1.png')
        self.tool_imag_2 = self.tool_imag_2.resize((140, 200))
        self.tool_imag_2 = ImageTk.PhotoImage(self.tool_imag_2)
        self.tool_imag_label_2= Label(self.full_3, image= self.tool_imag_2)
        self.tool_imag_label_2.image = self.tool_imag_2
        self.tool_imag_label_2.place(x=140,y=40)

        self.tool_imag_3 = Image.open('../assets/lab2.png')
        self.tool_imag_3 = self.tool_imag_3.resize((240, 130))
        self.tool_imag_3 = ImageTk.PhotoImage(self.tool_imag_3)
        self.tool_imag_label_3= Label(self.full_3, image= self.tool_imag_3)
        self.tool_imag_label_3.image = self.tool_imag_3
        self.tool_imag_label_3.place(x=330,y=60)
     

class Btn2:
    def __init__(self,master):
        self.master=master
        self.master.title('Off Campus')
        self.full_4 = Frame(self.master, width=700, height=550)
        self.full_4.place(x=0,y=0)

        self.background_4 = Image.open('../assets/imag7.png')
        self.background_4= self.background_4.resize((700, 550))
        self.background_4= ImageTk.PhotoImage(self.background_4)
        self.background_4_label = Label(self.full_4, image= self.background_4)
        self.background_4_label.image = self.background_4
        self.background_4_label.place(x=0,y=0)

        self.button_off_campus_p = Button(self.full_4,text='Miniplex',font = font_type3,bg='brown',width = 18,command=self.open_link)
        self.button_off_campus_p.place(x=200,y=200)
'''
    def open_link(self):
        self.url =        
        webbrowser.open(url)'''





        

master.title('College-Compass')
master.geometry('700x550+300+65')
Tic = Tic(master)
master.mainloop()