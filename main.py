# Code designed and written by: Ramees Saiyid
# Andrew ID: rameezs
# File Created: November 11, 6:00pm
# Modification History:
# Start End
# 11/11 6:00pm 12/11 2:00am
# 14/11 8:30pm 14/11 11:15pm
# 18/11 7:00pm 18/11 10:15pm
# 21/11 4:00pm 21/11 7:00pm
# 25/11 5:00pm 26/11 10:00pm

import Tkinter
import speech_recognition as sr
from latex import build_pdf
import os
import subprocess
import time


#Main class that handles the main window via Tkinter
class Main:
    def __init__(self):
        self.window = Tkinter.Tk()
        self.window.title("ResuPy")
        self.window.geometry("800x400")
        self.menuFrame = Tkinter.Frame(self.window, bg = "#E1F5FE")
        self.pageFrame = Tkinter.Frame(self.window, bg = "#90A4AE")

        self.menuFrame.place(x = 0, y = 0, width = 200, height = 400)
        self.pageFrame.place(x = 200, y = 0, width = 600, height = 400)

        self.frames = {}
        self.pages = [Start, Profile, Education, Experience, Skills, Projects, Awards, Generate]
        self.stPages = []
        for F in self.pages:                                                    #for every class in list, create an instance of it, thus creating a page for each
            pName = F.__name__
            self.stPages.append(pName)
            f = F(frame = self.pageFrame, controller = self)
            f.pack(fill = Tkinter.BOTH)
            self.frames[pName] = f

        self.menuButs = []
        for i in self.stPages:                                                  #for every page create a button in the menu frame
            self.menuButs.append(Tkinter.Button(self.menuFrame, text = i, command = lambda x = i: self.showFrame(x), width = 15, height = 2, fg = "black", bg = "#B3E5FC"))
            self.menuButs[len(self.menuButs)-1].pack(fill = Tkinter.BOTH, side = Tkinter.TOP)
        self.showFrame("Start")
        self.window.resizable(width = False, height = False)
        self.window.mainloop()

    def showFrame(self, pageName):                                              #function for 'raising' certain frames when a menu button is pressed
        frame = self.frames[pageName]
        for i in self.frames.values():
            if not i == frame:
                i.pack_forget()
            else:
                frame.tkraise()
                frame.pack(fill = Tkinter.BOTH)

    def addMore(self, controller):                                              #function for adding more fields (education, experience, skills...)
        controller.Add.pack_forget()                                            #placed in main class so all instances of other pages can access
        controller.genFields()
        controller.Add.pack(side = Tkinter.TOP)

class Start(Tkinter.Frame):                                                     #simple page showing description of the program
    def __init__(self, frame, controller):
        Tkinter.Frame.__init__(self, frame)
        welcomeText = Tkinter.Label(self, text = "Welcome to ResuPy")
        welcomeText.pack(side = Tkinter.TOP)

        desc = Tkinter.Text(self, wrap = Tkinter.WORD, bg = "#90A4AE")
        desc.insert(Tkinter.INSERT, "A resume is a quick outline of an individual's experiences "+
        "and skills for employers to understand a candidate's abilities. Making a resume "+
        "these days is quite difficult, so with this program you should just be able to "+
        "input your information and allow the program to generate it into a LaTeX file. "+
        " - rameezs")
        desc.config(state = Tkinter.DISABLED)
        desc.pack()

class Profile(Tkinter.Frame):                                                   #page for setting profile data for resume
    def __init__(self, frame, controller):
        Tkinter.Frame.__init__(self, frame)
        headProfLab = Tkinter.Label(self, text = "Profile")
        headProfLab.pack(side = Tkinter.TOP)

        fields = ["Name", "Site", "Address", "Phone", "Email"]
        self.Fields = []

        for f in fields:                                                        #create a Field instance for every item in fields list
            self.Fields.append(Field(controller = self, label = f))             #this is repeated for every other page

class Education(Tkinter.Frame):
    def __init__(self, frame, controller):
        Tkinter.Frame.__init__(self, frame)
        headEdLab = Tkinter.Label(self, text = "Education")
        headEdLab.pack(side = Tkinter.TOP)
        self.Fields = []
        self.genFields()
        self.Add = Tkinter.Button(self, text = "Add More", bg = "#B3E5FC", fg = "white", command = lambda x = self: controller.addMore(x))
        self.Add.pack(side = Tkinter.TOP)

    def genFields(self):
        fields = ["University", "Location", "Degree", "Major", "GPA", "Graduation Date"]
        for f in fields:
            self.Fields.append(Field(controller = self, label = f))

class Experience(Tkinter.Frame):
    def __init__(self, frame, controller):
        Tkinter.Frame.__init__(self, frame)
        headExLab = Tkinter.Label(self, text = "Experience")
        headExLab.pack(side = Tkinter.TOP)
        self.Fields = []
        self.genFields()
        self.Add = Tkinter.Button(self, text = "Add More", bg = "#B3E5FC", fg = "white", command = lambda x = self: controller.addMore(x))
        self.Add.pack(side = Tkinter.TOP)

    def genFields(self):                                                        #this is a function for every page except profile for adding another
        fields = ["Company", "Job Title", "Location", "Start Date", "End Date", "Job Responsibilities"] # instance of the instance of fields
        for f in fields:
            self.Fields.append(Field(controller = self, label = f))

class Skills(Tkinter.Frame):
    def __init__(self, frame, controller):
        Tkinter.Frame.__init__(self, frame)
        headSkLab = Tkinter.Label(self, text = "Skills")
        headSkLab.pack(side = Tkinter.TOP)
        self.Fields = []
        self.genFields()
        self.Add = Tkinter.Button(self, text = "Add More", bg = "#B3E5FC", fg = "white", command = lambda x = self: controller.addMore(x))
        self.Add.pack(side = Tkinter.TOP)

    def genFields(self):
        fields = ["Skill Name", "Skill Details"]
        for f in fields:
            self.Fields.append(Field(controller = self, label = f))

class Projects(Tkinter.Frame):
    def __init__(self, frame, controller):
        Tkinter.Frame.__init__(self, frame)
        headProjLab = Tkinter.Label(self, text = "Projects")
        headProjLab.pack(side = Tkinter.TOP)
        self.Fields = []
        self.genFields()
        self.Add = Tkinter.Button(self, text = "Add More", bg = "#B3E5FC", fg = "white", command = lambda x = self: controller.addMore(x))
        self.Add.pack(side = Tkinter.TOP)

    def genFields(self):
        fields = ["Project Name", "Description", "Technologies", "Link", "Start Date", "End Date"]
        for f in fields:
            self.Fields.append(Field(controller = self, label = f))

class Awards(Tkinter.Frame):
    def __init__(self, frame, controller):
        Tkinter.Frame.__init__(self, frame)
        headAwLab = Tkinter.Label(self, text = "Awards")
        headAwLab.pack(side = Tkinter.TOP)
        self.Fields = []
        self.genFields()
        self.Add = Tkinter.Button(self, text = "Add More", bg = "#B3E5FC", fg = "white", command = lambda x = self: controller.addMore(x))
        self.Add.pack(side = Tkinter.TOP)

    def genFields(self):
        fields = ["Award Name", "Description", "Award Date", "Award Location"]
        for f in fields:
            self.Fields.append(Field(controller = self, label = f))

class Generate(Tkinter.Frame):
    def __init__(self, frame, controller):
        Tkinter.Frame.__init__(self, frame)
        headLab = Tkinter.Label(self, text = "Generate")
        headLab.pack(side = Tkinter.TOP)

        self.controller = controller
        genBut = Tkinter.Button(self, text = "Generate", bg = "#B3E5FC", fg = "white", command = self.collect)
        genBut.pack(side = Tkinter.BOTTOM, pady = 100)

        self.defcon = Tkinter.Entry(self, width = 100)                          #because I wasn't able to call command line functions from Python on my machine
        self.defcon.pack(side=Tkinter.TOP)                                      # I resorted to giving the user a string of what to copy and paste into their
                                                                                #command line
    def collect(self):                                                          #This function creates a dictionary of lists of dictionaries with each label's
        self.dataList = {}                                                      #entry's text
        for N,F in self.controller.frames.items():
            if N != "Start" and N != "Generate":
                self.RAWINFO = [{}]
                curList = 0
                for e in F.Fields:
                    data = e.get()
                    if data[0] in self.RAWINFO[curList].keys():                 #this is if an entry's text is already repeated (this is for 'Add More' Case)
                        curList += 1
                        self.RAWINFO.append({})
                    self.RAWINFO[curList][data[0]] = data[1]
                self.dataList[N] = self.RAWINFO

        lastResort = 'pdflatex ' + os.getcwd() + '\\final.tex'
        self.defcon.insert(0, "enter in your command line:" + lastResort)
        createResume(self.dataList)

class Field:                                                                    #class of fields with respective entries, speech buttons, and labels
    def __init__(self, controller, label):
        self.controller = controller
        self.lab = label

        self.Frame = Tkinter.Frame(self.controller)
        self.Frame.pack(side = Tkinter.TOP)

        self.Label = Tkinter.Label(self.Frame, text = self.lab)
        self.Label.pack(fill = Tkinter.BOTH, side = Tkinter.LEFT)

        self.speechBut = Tkinter.Button(self.Frame, text = "Speech", command = lambda: Speech(controller = self))
        self.speechBut.pack(side = Tkinter.RIGHT)

        self.Entry = Tkinter.Entry(self.Frame)
        self.Entry.pack(fill = Tkinter.BOTH, side = Tkinter.RIGHT)
        self.Entry.insert(0, "Test")

    def get(self):
        return [self.lab, self.Entry.get()]

class Speech:                                                                   #class for dealing with speech. By opening a new window and offering its buttons
    def __init__(self, controller):
        self.controller = controller
        self.window = Tkinter.Tk()
        self.window.title("ResuPy - Speech")
        self.window.geometry("300x200")

        self.Entry = Tkinter.Entry(self.window)
        self.Entry.pack(fill = Tkinter.X, side = Tkinter.TOP)

        self.CapButton = Tkinter.Button(self.window, text = "Capture", command = self.getSpeech)
        self.CapButton.pack(side = Tkinter.LEFT)

        self.SuccButton = Tkinter.Button(self.window, text = "Success", command = self.success)
        self.SuccButton.pack(side = Tkinter.LEFT)

    def getSpeech(self):                                                        #get speech thru google
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=5)
            audio = r.listen(source)

        try:
            self.Entry.delete(0, Tkinter.END)
            self.Entry.insert(0, r.recognize_google(audio))
        except sr.UnknownValueError:
            self.Entry.delete(0, Tkinter.END)
            self.Entry.insert(0, "Try Again.")
        except sr.RequestError as e:
            self.Entry.delete(0, Tkinter.END)
            self.Entry.insert(0, "Try Again.")

    def success(self):                                                          #if success then put text in respective entry in main page
        self.controller.Entry.delete(0, Tkinter.END)
        self.controller.Entry.insert(0, self.Entry.get())
        self.window.destroy()

class createResume:                                                             #create latex and pdf file
    def __init__(self, data):
        file = open("resume2.tex", 'r+')
        contents = file.read()
        initcontent = contents[:contents.find("\\begin{document}")]
        contents = contents[contents.find("\\begin{document}"):]

        profile = data["Profile"]
        education = data["Education"]
        experience = data["Experience"]
        skill = data["Skills"]
        project = data["Projects"]
        award = data["Awards"]

        data = [profile, education, experience, project, award, skill]

        templates = [("""\\textbf{\Large %(Name)s}  & %(Phone)s\\""" + "\\\n"   #strings for replacing text with users data
        """%(Address)s &  %(Email)s \\""" + "\\\n"
        """%(Site)s\\""" + "\\\n"),("""\\item\n\\ressubheading{%(University)s}{%(Location)s}{%(Degree)s, %(Major)s (GPA: %(GPA)s)}{%(Graduation Date)s}\n"""),("""\\item\n
        \\ressubheading{%(Company)s}{%(Location)s}{%(Job Title)s}{%(Start Date)s - %(End Date)s}\n
        	\\begin{itemize}\n
        		\\resitem{%(Job Responsibilities)s}\n
        	\end{itemize}\n"""), ("""\item
        	\\ressubheading{%(Project Name)s}{%(Technologies)s}{%(Link)s}{%(Start Date)s - %(End Date)s}
        	\\begin{itemize}
        		\\resitem{%(Description)s}
        	\end{itemize}\n"""), ("""%(Award Name)s | (%(Award Location)s) | %(Award Date)s | %(Description)s\\""" + "\\\n"), ("""\item[%(Skill Name)s] | %(Skill Details)s\n""")]

        def breakUp(raw):                                                       #breakup latex template
            heads = []
            for h in range(6):
                # print raw, "RARARA"
                if raw[11:].find("\\resheading") < 0:
                    heads.append(raw[:])
                else:
                    heads.append(raw[:raw[11:].find("\\resheading")+11])
                    raw = raw[raw[11:].find("\\resheading") + 11:]
            return heads

        contents = breakUp(contents)

        for c in range(len(contents)):                                          #replace text in respective template
            end = contents[c][contents[c].find("%INSERT")+7:]
            contents[c] = contents[c][:contents[c].find("%INSERT")]
            for e in data[c]:
                contents[c] += templates[c]%e
            contents[c] += end

        final = open("final.tex", "w")                                          #generate latex file
        page = initcontent
        for c in contents:
            page += c
        final.write(page)
        final.close()

        os.system('pdflatex final.tex')                                         #convert latex to pdf

main = Main()
