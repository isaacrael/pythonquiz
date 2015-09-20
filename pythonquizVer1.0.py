__author__ = 'grael_000'
"""
The following program can be used as a template for creating a python GUI for an application


X Change Set Title text Welcome userName to Python Quiz
X Make panel size the right size
X Make Ctrl Text box the right size
X Move answer text above the second panel
Research adding an image to top right corner of panel
Research Use of Ctrl Text Box and how to display into it


"""

import wx

class windowClass(wx.Frame):

    def __init__(self, parent):
        super(windowClass, self).__init__(parent, size=(1200,700))

        self.basicGUI()

    def basicGUI(self):
        panel = wx.Panel(self)
        menuBar = wx.MenuBar()
        fileButton = wx.Menu()
        editButton = wx.Menu()

        exitItem = fileButton.Append(wx.ID_EXIT, 'Exit', 'status_msg.....')

        menuBar.Append(fileButton, 'File')
        menuBar.Append(editButton, 'Edit')

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



        if yesNoAnswer == wx.ID_NO:
            userName = "Loser!"


# Sets up the positioning of the text ctrl panel

        wx.TextCtrl(panel, pos=(450,100), size=(350,100))


# Creates Question text and sets foreground and background colors

        questionText = wx.StaticText(panel, -1, "Question:", (400,75))
        questionText.SetForegroundColour('Blue')
        questionText.SetBackgroundColour('White')

# Creates Answer text and sets foreground and background colors

        answerText = wx.StaticText(panel, -1, "Type Your Answer In The Text Box Below:", (400,275))
        answerText.SetForegroundColour('Blue')
        answerText.SetBackgroundColour('White')


        self.SetTitle("Welcome To Python Quiz " + (userName) + "!")
        self.Show(True)

    def Quit(self, e):
        self.Close()

def main():
    app = wx.App()
    windowClass(None)

    app.MainLoop()

main()