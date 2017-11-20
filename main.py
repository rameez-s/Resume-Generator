import Tkinter

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
        self.pages = [Start, Template, Profile, Education, Experience, Skills, Projects, Awards, Generate]
        self.stPages = []
        for F in self.pages:
            pName = F.__name__
            self.stPages.append(pName)
            f = F(frame = self.pageFrame, controller = self)
            f.pack(fill = Tkinter.BOTH)
            self.frames[pName] = f

        self.menuButs = []
        for i in self.stPages:
            self.menuButs.append(Tkinter.Button(self.menuFrame, text = i, command = lambda x = i: self.showFrame(x), width = 15, height = 2, fg = "black", bg = "#B3E5FC"))
            self.menuButs[len(self.menuButs)-1].pack(fill = Tkinter.BOTH, side = Tkinter.TOP)
        self.showFrame("Start")
        self.window.resizable(width = False, height = False)
        self.window.mainloop()

    def showFrame(self, pageName):
        frame = self.frames[pageName]
        for i in self.frames.values():
            if not i == frame:
                i.pack_forget()
            else:
                frame.tkraise()
                frame.pack(fill = Tkinter.BOTH)

    def addMore(self, controller):
        controller.Add.pack_forget()
        controller.genFields()
        controller.Add.pack(side = Tkinter.TOP)

class Start(Tkinter.Frame):
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

class Template(Tkinter.Frame):
    def __init__(self, frame, controller):
        Tkinter.Frame.__init__(self, frame)
        chooseTemp = Tkinter.Label(self, text = "Choose a Template")
        chooseTemp.pack()

        self.resumeTemp = ""
        temp1 = Tkinter.Button(self, text = "Resume 1", padx = 10, pady = 10, bg = "black", fg = "white", command = lambda: self.setResumeTemplate("resume1"))
        temp1.pack(side = Tkinter.LEFT)
        # temp1.grid(row = 2, column = 1)

    def setResumeTemplate(self, type):
        self.resumeTemp = type

class Profile(Tkinter.Frame):
    def __init__(self, frame, controller):
        Tkinter.Frame.__init__(self, frame)
        headProfLab = Tkinter.Label(self, text = "Profile")
        headProfLab.pack(side = Tkinter.TOP)

        fields = ["Full Name", "Site", "Address", "Phone Number", "Email"]
        self.Fields = []

        for f in fields:
            self.Fields.append(Field(controller = self, label = f))

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
        fields = ["University", "Degree", "Major", "GPA", "Graduation Date"]
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

    def genFields(self):
        fields = ["Company", "Job Title", "Location", "Start Date", "End Date", "Job Responsibilities"]
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
        fields = ["Project Name", "Description", "Technologies", "Link"]
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
        fields = ["Award Name", "Description", "Award Date"]
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

    def collect(self):
        self.RAWINFO = []
        print self.controller.frames.keys()
        for N,F in self.controller.frames.items():
            if N != "Start" and N != "Template" and N != "Generate":
                for e in F.Fields:
                    print e.get()
                    self.RAWINFO.append(e.get())
        file = open("resumeRaw.txt", "w")
        for w in self.RAWINFO:
            file.write(str(w[0]) + "~|~" + str(w[1]) + "\n")

class Field:
    def __init__(self, controller, label):
        self.controller = controller
        self.lab = label

        self.Frame = Tkinter.Frame(self.controller)
        self.Frame.pack(side = Tkinter.TOP)

        self.Label = Tkinter.Label(self.Frame, text = self.lab)
        self.Label.pack(fill = Tkinter.BOTH, side = Tkinter.LEFT)

        self.Entry = Tkinter.Entry(self.Frame)
        self.Entry.pack(fill = Tkinter.BOTH, side = Tkinter.RIGHT)

    def get(self):
        return [self.lab, self.Entry.get()]

main = Main()
