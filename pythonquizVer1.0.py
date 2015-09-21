__author__ = 'grael_000'
"""
The following program can be used as a template for creating a python GUI for an application


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

If text can be read from Ctrl Box then create another Ctrl Box else create a widget that will read text
    input by computer user.
Add code to display the users score and average / grade


Work on code that will allow you answer ctrl box to recognize when the enter key is pressed.

Following 2 lines below represent code that has been tried to eliminate text dissapearance on cursor
questionText = wx.StaticText(panel, -1, str(q), (455,115), style=wx.TE_READONLY)
questionText = wx.TextCtrl(panel, -1, str(q), (455,115), style=wx.TE_READONLY)

self.answer = wx.TextCtrl(panel, pos=(450,250), size=(350,100))

"""

import wx

class windowClass(wx.Frame):

    def __init__(self, parent):
        super(windowClass, self).__init__(parent, size=(1400,800))

        self.basicGUI()

    def basicGUI(self):
        panel = wx.Panel(self)
#        panel1 = wx.Panel(self)
        menuBar = wx.MenuBar()
        fileButton = wx.Menu()
#        editButton = wx.Menu()

        exitItem = fileButton.Append(wx.ID_EXIT, 'Exit', 'status_msg.....')

        menuBar.Append(fileButton, 'File')
#        menuBar.Append(editButton, 'Edit')

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)

        nameBox = wx.TextEntryDialog(None, 'What is your name?', 'Welcome','name')

# Gets userName response

        if nameBox.ShowModal()==wx.ID_OK:
            userName = nameBox.GetValue()

# Gets answer to yes / no question

        yesNoBox = wx.MessageDialog(None, 'Start Python Quiz?', 'Question',wx.YES_NO)
        yesNoAnswer = yesNoBox.ShowModal()
        yesNoBox.Destroy()

#        if yesNoAnswer == wx.ID_YES:
#            print("What a wonderful day it is (userName)")

        if yesNoAnswer == wx.ID_NO:
            userName = "Loser!"

# Display python image on the GUI

        png = wx.Image('python2.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, -1, png, (1065, 1), (png.GetWidth(), png.GetHeight()))

#        png = wx.Image('python3.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
#        wx.StaticBitmap(self, -1, png, (400,500), (png.GetWidth(), png.GetHeight()))



# Sets the positioning for the text ctrl panels

#        wx.TextCtrl(panel, pos=(450,100), size=(350,100))
        wx.TextCtrl(panel, pos=(450,250), size=(350,100))

# Creates Question text and sets foreground and background colors

        questionText = wx.StaticText(panel, -1, "Question:", (400,75))
        questionText.SetForegroundColour('Blue')
        questionText.SetBackgroundColour('White')

# Displays question text in the question text control box

        question = {"What information does a dictionary contain?": "Key value pairs."}
        qText = question.keys()
        for q in qText:
            questionText = wx.StaticText(panel, -1,(q), (455,115), style=wx.TE_READONLY)
            questionText.SetForegroundColour('Blue')
            questionText.SetBackgroundColour('White')



# Creates Answer text and sets foreground and background colors

        answerText = wx.StaticText(panel, -1, "Type Your Answer In The Text Box Below:", (400,225))
        answerText.SetForegroundColour('Blue')
        answerText.SetBackgroundColour('White')

# Sets the positioning for the text ctrl panels


#        wx.TextCtrl(panel, pos=(450,100), size=(350,100))
#        wx.TextCtrl(panel, pos=(450,250), size=(350,100))

        def GetAnswer(self):
            self.answer = wx.TextEntryDialog(panel, "Enter Your Answer", pos=(450,250))
            userAnswer = self.answer.GetValue()
            print(userAnswer)
        GetAnswer(self)


# Creates the motivation text displayed below the answer text ctrl box

        motivationText = wx.StaticText(panel, -1, "Correct....Great Job!", (450,375))
        motivationText.SetForegroundColour('Green')
        motivationText.SetBackgroundColour('White')


# Creates the title diplayed on the GUI

        self.SetTitle("Welcome To Python Quiz " + (userName) + "!")
        self.Show(True)

    def Quit(self, e):
        self.Close()

def main():
    app = wx.App()
    windowClass(None)

    app.MainLoop()

main()