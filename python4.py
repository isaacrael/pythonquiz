__author__ = '184766'
"""
The following program can be used as a template for creating a python GUI for an application


Add image to GUI
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

# Setup your menu bar

        menuBar = wx.MenuBar()
        fileButton = wx.Menu()
        exitItem = fileButton.Append(wx.ID_EXIT, 'Exit', 'status_msg.....')
        menuBar.Append(fileButton, 'File')
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)

# Setup namebox and get userName response

        nameBox = wx.TextEntryDialog(None, 'What is your name?', 'Welcome','name')
        if nameBox.ShowModal()==wx.ID_OK:
            userName = nameBox.GetValue()

# Gets answer to yes / no question

        yesNoBox = wx.MessageDialog(None, 'Start Python Quiz?', 'Question',wx.YES_NO)
        yesNoAnswer = yesNoBox.ShowModal()
        yesNoBox.Destroy()

        if yesNoAnswer == wx.ID_NO:
            userName = "Loser!"

        # Display python image on the GUI

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

        # Set simple sizer for a nice border
        self.border = wx.BoxSizer()
        self.border.Add(self.sizer, 1, wx.ALL | wx.EXPAND, 5)

        # Use the sizers
        self.panel.SetSizerAndFit(self.border)
        self.SetSizerAndFit(self.windowSizer)

        # Set event handlers
        self.button.Bind(wx.EVT_BUTTON, self.OnButton)

        # Creates the title diplayed on the GUI

        self.SetTitle("Welcome To Python Quiz " + (userName) + "!")
        self.Show(True)


    def OnButton(self, e):
        self.result.SetLabel(self.editname.GetValue())

    def Quit(self, e):
        self.Close()

app = wx.App(False)
frame = PythonQuiz(None)
frame.Show()
app.MainLoop()