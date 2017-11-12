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

        siteFrame = Tkinter.Frame(self)
        siteFrame.pack(side = Tkinter.BOTTOM)
        siteLab = Tkinter.Label(siteFrame, text = "Site")
        siteEntry = Tkinter.Entry(siteFrame)
        siteLab.pack(fill = Tkinter.X, side = Tkinter.LEFT)
        siteEntry.pack(fill = Tkinter.X, side = Tkinter.LEFT)

        addressFrame = Tkinter.Frame(self)
        addressFrame.pack(side = Tkinter.BOTTOM)
        addressLab = Tkinter.Label(addressFrame, text = "Address")
        addressEntry = Tkinter.Entry(addressFrame)
        addressLab.pack(fill = Tkinter.X, side = Tkinter.LEFT)
        addressEntry.pack(fill = Tkinter.X, side = Tkinter.LEFT)

        phoneFrame = Tkinter.Frame(self)
        phoneFrame.pack(side = Tkinter.BOTTOM)
        phoneLab = Tkinter.Label(phoneFrame, text = "Phone Number")
        phoneEntry = Tkinter.Entry(phoneFrame)
        phoneLab.pack(fill = Tkinter.X, side = Tkinter.LEFT)
        phoneEntry.pack(fill = Tkinter.X, side = Tkinter.LEFT)

        emailFrame = Tkinter.Frame(self)
        emailFrame.pack(side = Tkinter.BOTTOM)
        emailLab = Tkinter.Label(emailFrame, text = "Email Address")
        emailEntry = Tkinter.Entry(emailFrame)
        emailLab.pack(fill = Tkinter.X, side = Tkinter.LEFT)
        emailEntry.pack(fill = Tkinter.X, side = Tkinter.LEFT)

        nameFrame = Tkinter.Frame(self)
        nameFrame.pack(side = Tkinter.BOTTOM)
        fullNameLab = Tkinter.Label(nameFrame, text = "Full Name")
        fullName = Tkinter.Entry(nameFrame)
        fullNameLab.pack(fill = Tkinter.X, side = Tkinter.LEFT)
        fullName.pack(fill = Tkinter.X, side = Tkinter.LEFT)

        self.text = [fullName, emailEntry, phoneEntry, addressEntry, siteEntry]

    def getText(self):
        return self.text

class Education(Tkinter.Frame):
    def __init__(self, frame, controller):
        Tkinter.Frame.__init__(self, frame)
        headEdLab = Tkinter.Label(self, text = "Education")
        headEdLab.pack(side = Tkinter.TOP)

        gradFrame = Tkinter.Frame(self)
        gradFrame.pack(side = Tkinter.BOTTOM)
        gradLab = Tkinter.Label(gradFrame, text = "Graduation Date")
        gradEntry = Tkinter.Entry(gradFrame)
        gradLab.pack(fill = Tkinter.X, side = Tkinter.LEFT)
        gradEntry.pack(fill = Tkinter.X, side = Tkinter.LEFT)

        gpaFrame = Tkinter.Frame(self)
        gpaFrame.pack(side = Tkinter.BOTTOM)
        gpaLab = Tkinter.Label(gpaFrame, text = "GPA")
        gpaEntry = Tkinter.Entry(gpaFrame)
        gpaLab.pack(fill = Tkinter.X, side = Tkinter.LEFT)
        gpaEntry.pack(fill = Tkinter.X, side = Tkinter.LEFT)

        majorFrame = Tkinter.Frame(self)
        majorFrame.pack(side = Tkinter.BOTTOM)
        majorLab = Tkinter.Label(majorFrame, text = "Major")
        majorEntry = Tkinter.Entry(majorFrame)
        majorLab.pack(fill = Tkinter.X, side = Tkinter.LEFT)
        majorEntry.pack(fill = Tkinter.X, side = Tkinter.LEFT)

        degFrame = Tkinter.Frame(self)
        degFrame.pack(side = Tkinter.BOTTOM)
        degLab = Tkinter.Label(degFrame, text = "Degree")
        degEntry = Tkinter.Entry(degFrame)
        degLab.pack(fill = Tkinter.X, side = Tkinter.LEFT)
        degEntry.pack(fill = Tkinter.X, side = Tkinter.LEFT)

        uniFrame = Tkinter.Frame(self)
        uniFrame.pack(side = Tkinter.BOTTOM)
        uniLab = Tkinter.Label(uniFrame, text = "University")
        uniEntry = Tkinter.Entry(uniFrame)
        uniLab.pack(fill = Tkinter.X, side = Tkinter.LEFT)
        uniEntry.pack(fill = Tkinter.X, side = Tkinter.LEFT)

        self.text = [uniEntry, degEntry, majorEntry, gpaEntry]

    def getText(self):
        return self.text

class Experience(Tkinter.Frame):
    def __init__(self, frame, controller):
        Tkinter.Frame.__init__(self, frame)
        headExLab = Tkinter.Label(self, text = "Experience")
        headExLab.pack(side = Tkinter.TOP)

        compFrame = Tkinter.Frame(self)
        compFrame.pack(side = Tkinter.TOP)
        compLab = Tkinter.Label(compFrame, text = "Company")
        compEntry = Tkinter.Entry(compFrame)
        compLab.pack(fill = Tkinter.X, side = Tkinter.LEFT)
        compEntry.pack(fill = Tkinter.X, side = Tkinter.LEFT)

        jobFrame = Tkinter.Frame(self)
        jobFrame.pack(side = Tkinter.TOP)
        jobLab = Tkinter.Label(jobFrame, text = "Job Title")
        jobEntry = Tkinter.Entry(jobFrame)
        jobLab.pack(fill = Tkinter.X, side = Tkinter.LEFT)
        jobEntry.pack(fill = Tkinter.X, side = Tkinter.LEFT)

        respFrame = Tkinter.Frame(self)
        respFrame.pack(side = Tkinter.TOP)
        respLab = Tkinter.Label(respFrame, text = "University")
        respEntry = Tkinter.Entry(respFrame)
        respLab.pack(fill = Tkinter.X, side = Tkinter.LEFT)
        respEntry.pack(fill = Tkinter.X, side = Tkinter.LEFT)

        self.text = [compEntry, jobEntry, respEntry]

    def getText(self):
        return self.text

class Skills(Tkinter.Frame):
    def __init__(self, frame, controller):
        Tkinter.Frame.__init__(self, frame)
        headSkLab = Tkinter.Label(self, text = "Skills")
        headSkLab.pack(side = Tkinter.TOP)

        skillFrame = Tkinter.Frame(self)
        skillFrame.pack(side = Tkinter.TOP)
        skillLab = Tkinter.Label(skillFrame, text = "Skills")
        skillEntry = Tkinter.Entry(skillFrame)
        skillLab.pack(fill = Tkinter.X, side = Tkinter.LEFT)
        skillEntry.pack(fill = Tkinter.X, side = Tkinter.LEFT)

        self.text = [skillEntry]

    def getText(self):
        return self.text

class Projects(Tkinter.Frame):
    def __init__(self, frame, controller):
        Tkinter.Frame.__init__(self, frame)
        headProjLab = Tkinter.Label(self, text = "Projects")
        headProjLab.pack(side = Tkinter.TOP)

        nameFrame = Tkinter.Frame(self)
        nameFrame.pack(side = Tkinter.TOP)
        nameLab = Tkinter.Label(nameFrame, text = "Project Name")
        nameEntry = Tkinter.Entry(nameFrame)
        nameLab.pack(fill = Tkinter.X, side = Tkinter.LEFT)
        nameEntry.pack(fill = Tkinter.X, side = Tkinter.LEFT)

        descFrame = Tkinter.Frame(self)
        descFrame.pack(side = Tkinter.TOP)
        descLab = Tkinter.Label(descFrame, text = "Description")
        descEntry = Tkinter.Entry(descFrame)
        descLab.pack(fill = Tkinter.X, side = Tkinter.LEFT)
        descEntry.pack(fill = Tkinter.X, side = Tkinter.LEFT)

        linkFrame = Tkinter.Frame(self)
        linkFrame.pack(side = Tkinter.TOP)
        linkLab = Tkinter.Label(linkFrame, text = "Link")
        linkEntry = Tkinter.Entry(linkFrame)
        linkLab.pack(fill = Tkinter.X, side = Tkinter.LEFT)
        linkEntry.pack(fill = Tkinter.X, side = Tkinter.LEFT)

        self.text = [nameEntry, descEntry, linkEntry]

    def getText(self):
        return self.text

class Awards(Tkinter.Frame):
    def __init__(self, frame, controller):
        Tkinter.Frame.__init__(self, frame)
        headAwLab = Tkinter.Label(self, text = "Awards")
        headAwLab.pack(side = Tkinter.TOP)

        nameFrame = Tkinter.Frame(self)
        nameFrame.pack(side = Tkinter.TOP)
        nameLab = Tkinter.Label(nameFrame, text = "Award Name")
        nameEntry = Tkinter.Entry(nameFrame)
        nameLab.pack(fill = Tkinter.X, side = Tkinter.LEFT)
        nameEntry.pack(fill = Tkinter.X, side = Tkinter.LEFT)

        descFrame = Tkinter.Frame(self)
        descFrame.pack(side = Tkinter.TOP)
        descLab = Tkinter.Label(descFrame, text = "Description")
        descEntry = Tkinter.Entry(descFrame)
        descLab.pack(fill = Tkinter.X, side = Tkinter.LEFT)
        descEntry.pack(fill = Tkinter.X, side = Tkinter.LEFT)

        self.text = [nameEntry, descEntry]

    def getText(self):
        return self.text

class Generate(Tkinter.Frame):
    def __init__(self, frame, controller):
        Tkinter.Frame.__init__(self, frame)
        headLab = Tkinter.Label(self, text = "Generate")
        headLab.pack(side = Tkinter.TOP)

        self.controller = controller
        genBut = Tkinter.Button(self, text = "Generate", bg = "#B3E5FC", fg = "white", command = self.collect)
        genBut.pack(fill = Tkinter.X, side = Tkinter.BOTTOM)

    def collect(self):
        self.RAWINFO = []
        print self.controller.frames.keys()
        for N,F in self.controller.frames.items():
            if N != "Start" and N != "Template" and N != "Generate":
                for e in F.text:
                    self.RAWINFO.append(e.get())
        file = open("resumeRaw.txt", "w")
        file.writelines(self.RAWINFO)

main = Main()
