__author__ = '184766'
"""

The following program can be used as a template for creating a python GUI for an application

X Add image to GUI
X Create Yes / No Answer Box
X Set title displayed on GUI
X Change Set Title text Welcome userName to Python Quiz
X Make panel size the right size
X Make Ctrl Text box the right size
X Move answer text above the second panel
X Research adding an image to top right corner of panel
X Comment out the edit button code
In Progress Research Use of Ctrl Text Box and how to display text into it
In Progress Research Git workflow when developing on two different systems.
X Move answer instruction text up in the panel
X Create text crtl for answer panel
X Add motivation text
X Change "Your Question" to read "Question:

Add icons to the motivational text line like those found on cell phones
Add code to display the users score and average / grade
in Text Ctrl Boxes on the top left of the screen
calculate average score and letter grade
add ***** 5 stars being and A, 4 stars B etc.....

Following 2 lines below represent code that has been tried to eliminate text dissapearance on cursor
questionText = wx.StaticText(panel, -1, str(q), (455,115), style=wx.TE_READONLY)
questionText = wx.TextCtrl(panel, -1, str(q), (455,115), style=wx.TE_READONLY)
self.answer = wx.TextCtrl(panel, pos=(450,250), size=(350,100))

"""

import wx
import random


class PythonQuiz(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)
        self.panel = wx.Panel(self)
#        self.quote = wx.StaticText(self.panel, label="Question:")
        self.result = wx.StaticText(self.panel, label="")
        self.questionText = wx.StaticText(self.panel, -1, "Question:", (500, 250))
        self.questionText.SetForegroundColour('Blue')
        self.questionText.SetBackgroundColour('White')
        self.result.SetForegroundColour(wx.RED)
        self.button = wx.Button(self.panel, label="Submit")
        self.lblname = wx.StaticText(self.panel, label="Type Your Answer \nThen Click Submit:")
        self.lblname.SetForegroundColour('Blue')
        self.lblname.SetBackgroundColour('White')
        self.editname = wx.TextCtrl(self.panel, size=(200, -1))
# Creates the motivation text displayed below the answer text ctrl box
        self.motivationText = wx.StaticText(self.panel, -1, "Correct....Great Job!")
        self.motivationText.SetForegroundColour('Green')
        self.motivationText.SetBackgroundColour('Grey')

# Setup your menu bar
        self.menuBar = wx.MenuBar()
        self.fileButton = wx.Menu()
        self.exitItem = self.fileButton.Append(wx.ID_EXIT, 'Exit', 'status_msg.....')
        self.menuBar.Append(self.fileButton, 'File')
        self.SetMenuBar(self.menuBar)
        self.Bind(wx.EVT_MENU, self.Quit, self.exitItem)

# Setup namebox and get userName response
        self.nameBox = wx.TextEntryDialog(None, 'What is your name?', 'Welcome','name')
        if self.nameBox.ShowModal()==wx.ID_OK:
            self.userName = self.nameBox.GetValue()

# Gets answer to yes / no question
        self.yesNoBox = wx.MessageDialog(None, 'Start Python Quiz?', 'Question',wx.YES_NO)
        self.yesNoAnswer = self.yesNoBox.ShowModal()
        self.yesNoBox.Destroy()

        if self.yesNoAnswer == wx.ID_NO:
            self.userName = "Loser!"

# Display python logo image on the GUI
        self.png = wx.Image('python2.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, -1, self.png, (1625, 0), (self.png.GetWidth(), self.png.GetHeight()))


# Set sizer for the frame, so we can change frame size to match widgets
        self.windowSizer = wx.BoxSizer()
        self.windowSizer.Add(self.panel, 1, wx.ALL | wx.EXPAND)

# Set sizer for the panel content
        self.sizer = wx.GridBagSizer(20, 20)
#        self.sizer.Add(self.quote, (0, 0))
        self.sizer.Add(self.result, (0, 1))
        self.sizer.Add(self.questionText, (7,15))
        self.sizer.Add(self.lblname, (10, 15))
        self.sizer.Add(self.editname, (10, 16))
#        self.sizer.Add(self.png, (1650, 0))
        self.sizer.Add(self.button, (10, 17), (1, 2), flag=wx.EXPAND)
        self.sizer.Add(self.motivationText, (11,15))

# Displays question text in the question text control box

#            questions = list(question_answer.keys())
#            question = random.choice(questions)
#            question = random.choice(questions)
#            answer = question_answer[question]
#            user_answer = raw_input(question)
        self.question_answer = {"What information does a dictionary contain?": "key value pairs"}
        self.questions = list(self.question_answer.keys())
        self.question = random.choice(self.questions)
        self.answer = self.question_answer[self.question]

        for self.question in self.questions:
            self.question = wx.StaticText(self.panel, -1,(self.question), (510,282), style=wx.TE_READONLY)
            self.question.SetForegroundColour('Blue')
            self.question.SetBackgroundColour('White')
            self.userResponse = self.editname.GetValue()
            print(self.answer)
            print(self.userResponse)
            if self.answer == self.userResponse:
                print("True")
            else:
                print("False")




# Set simple sizer for a nice border
        self.border = wx.BoxSizer()
        self.border.Add(self.sizer, 1, wx.ALL | wx.EXPAND, 5)

# Use the sizers
        self.panel.SetSizerAndFit(self.border)
        self.SetSizerAndFit(self.windowSizer)

# Set event handlers
        self.button.Bind(wx.EVT_BUTTON, self.OnButton)

# Creates the title diplayed on the GUI
        self.SetTitle("Welcome To Python Quiz " + (self.userName) + "!")
        self.Show(True)

# Function gets the input from the computer user
    def OnButton(self, e):
        self.result.SetLabel(self.editname.GetValue())
        answer2 = self.editname.GetValue()
        print(answer2)


    def Quit(self, e):
        self.Close()

app = wx.App(False)
frame = PythonQuiz(None)
frame.Show()
app.MainLoop()