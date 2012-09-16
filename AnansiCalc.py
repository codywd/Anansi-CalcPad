## Standard Libraries ##
import math
import os
import sys
import urllib
import webbrowser
import tempfile

## Third-Party Libraries ##
from PySide import QtCore, QtGui, QtWebKit

ver = 1.5

class CalcPad(QtGui.QMainWindow):
    def __init__(self):
        super(CalcPad, self).__init__()
        self.InitUI()
            
    def InitUI(self):
        self.setWindowTitle("Anansi CalcPad")
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
            
        self.statusBar().showMessage('Ready')
            
        menubar = self.menuBar()
            
        ## File Menu ##
        fileMenu = menubar.addMenu("&File")
            
        newWin = QtGui.QAction("&New Window", self)
        newWin.setShortcut("Ctrl+N")
        newWin.setStatusTip("Open a brand new window!")
        newWin.setEnabled(False)
            
        clearAllAction = QtGui.QAction("C&lear All", self)
        clearAllAction.setShortcut("Ctrl+l")
        clearAllAction.setStatusTip("Clear all text.")
        clearAllAction.setEnabled(False)
            
        exitAction = QtGui.QAction("E&xit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit the application")
        exitAction.triggered.connect(self.close)
            
        fileMenu.addAction(newWin)
        fileMenu.addAction(clearAllAction)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAction)
            
        ## View Menu ##
        viewMenu = menubar.addMenu("V&iew")
        
        calcViewAction = QtGui.QAction("CalcPad View", self)
        calcViewAction.setStatusTip("View the Calculator")
        calcViewAction.setEnabled(False)
            
        storypadViewAction = QtGui.QAction("Storypad View", self)
        storypadViewAction.setStatusTip("View StoryPad")
        storypadViewAction.setEnabled(False)
        
        newsAggViewAction = QtGui.QAction("NewsPad View", self)
        newsAggViewAction.setStatusTip("Open the News Aggregator")
        newsAggViewAction.triggered.connect(self.opennewsagg)
        newsAggViewAction.setEnabled(False)
        
        viewMenu.addAction(calcViewAction)
        viewMenu.addAction(storypadViewAction)
        viewMenu.addAction(newsAggViewAction)
        
        ## Help Menu ##
        helpMenu = menubar.addMenu("&Help")
        
        helpAnansiAction = QtGui.QAction("Help with Anansi CalcPad", self)
        helpAnansiAction.setStatusTip("Get Help with Anansi CalcPad")
        helpAnansiAction.setEnabled(False)
        
        checkUpdatesAction = QtGui.QAction("Check for Updates...", self)
        checkUpdatesAction.setStatusTip("Check for Updates!")
        checkUpdatesAction.setEnabled(False)
        
        reportIssueAction = QtGui.QAction("Report an Issue...", self)
        reportIssueAction.setStatusTip("Report a bug, or give a suggestion")
        reportIssueAction.setEnabled(False)
        
        specCreditAction = QtGui.QAction("Special Credits...", self)
        specCreditAction.setStatusTip("Special Credits for Special People")
        specCreditAction.setEnabled(False)
            
        aboutAnansiAction = QtGui.QAction("About Anansi CalcPad", self)
        aboutAnansiAction.setStatusTip("About Anansi CalcPad Version " + str(ver))
        aboutAnansiAction.setEnabled(False)
            
        helpMenu.addAction(helpAnansiAction)
        helpMenu.addAction(checkUpdatesAction)
        helpMenu.addAction(reportIssueAction)
        helpMenu.addSeparator()
        helpMenu.addAction(specCreditAction)
        helpMenu.addAction(aboutAnansiAction)
            
        ## Main GUI ##
        btntxt = ['Cls', 'Bck', 'x'u"\u00B2", u"\u221A", 
                  '7', '8', '9', '/',
                  '4', '5', '6', '*', 
                  '1', '2', '3', '-',
                  '0', '.', '=', '+']
        centralwidget = QtGui.QWidget(self)
        grid = QtGui.QGridLayout(centralwidget)
        j=4
        
        lineEdit = QtGui.QLineEdit()
        
        pos = [(0, 0), (0, 1), (0, 2), (0, 3),
                (1, 0), (1, 1), (1, 2), (1, 3),
                (2, 0), (2, 1), (2, 2), (2, 3),
                (3, 0), (3, 1), (3, 2), (3, 3 ),
                (4, 0), (4, 1), (4, 2), (4, 3),
                (5, 0), (5, 1), (5, 2), (5, 3)]
        
        grid.addWidget(lineEdit, 0, 0, 1, 4)
        
        for i in btntxt:
            button = QtGui.QPushButton(i)
            grid.addWidget(button, pos[j][0], pos[j][1])
            j = j + 1
    
        self.setLayout(grid)
        self.setCentralWidget(centralwidget)
        self.center()
        self.show()
        
    
            
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
            
    def opennewsagg(self):
        nav = NewsAggQT()
        nav.show() 
        
class StoryPad(QtGui.QMainWindow):
    def __init__(self):
        super(StoryPadQT, self).__init__()
        
        self.InitUI()
        
    def InitUI(self):
        
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle("Anansi CalcPad")
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        
        self.statusBar().showMessage('Ready')
        
        menubar = self.menuBar()
        
        ## File Menu ##
        fileMenu = menubar.addMenu("&File")
            
        newWin = QtGui.QAction("&New Window", self)
        newWin.setShortcut("Ctrl+N")
        newWin.setStatusTip("Open a brand new window!")
        newWin.setEnabled(False)
            
        clearAllAction = QtGui.QAction("C&lear All", self)
        clearAllAction.setShortcut("Ctrl+l")
        clearAllAction.setStatusTip("Clear all text.")
        clearAllAction.setEnabled(False)
            
        exitAction = QtGui.QAction("E&xit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit the application")
        exitAction.triggered.connect(self.close)
            
        fileMenu.addAction(newWin)
        fileMenu.addAction(clearAllAction)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAction)
            
        ## View Menu ##
        viewMenu = menubar.addMenu("V&iew")
        
        calcViewAction = QtGui.QAction("CalcPad View", self)
        calcViewAction.setStatusTip("View the Calculator")
        calcViewAction.setEnabled(False)
            
        storypadViewAction = QtGui.QAction("Storypad View", self)
        storypadViewAction.setStatusTip("View StoryPad")
        storypadViewAction.setEnabled(False)
        
        newsAggViewAction = QtGui.QAction("NewsPad View", self)
        newsAggViewAction.setStatusTip("Open the News Aggregator")
        newsAggViewAction.triggered.connect(self.opennewsagg)
        newsAggViewAction.setEnabled(False)
        
        viewMenu.addAction(calcViewAction)
        viewMenu.addAction(storypadViewAction)
        viewMenu.addAction(newsAggViewAction)
        
        ## Help Menu ##
        helpMenu = menubar.addMenu("&Help")
        
        helpAnansiAction = QtGui.QAction("Help with Anansi CalcPad", self)
        helpAnansiAction.setStatusTip("Get Help with Anansi CalcPad")
        helpAnansiAction.setEnabled(False)
        
        checkUpdatesAction = QtGui.QAction("Check for Updates...", self)
        checkUpdatesAction.setStatusTip("Check for Updates!")
        checkUpdatesAction.setEnabled(False)
        
        reportIssueAction = QtGui.QAction("Report an Issue...", self)
        reportIssueAction.setStatusTip("Report a bug, or give a suggestion")
        reportIssueAction.setEnabled(False)
        
        specCreditAction = QtGui.QAction("Special Credits...", self)
        specCreditAction.setStatusTip("Special Credits for Special People")
        specCreditAction.setEnabled(False)
            
        aboutAnansiAction = QtGui.QAction("About Anansi CalcPad", self)
        aboutAnansiAction.setStatusTip("About Anansi CalcPad Version " + str(ver))
        aboutAnansiAction.setEnabled(False)
            
        helpMenu.addAction(helpAnansiAction)
        helpMenu.addAction(checkUpdatesAction)
        helpMenu.addAction(reportIssueAction)
        helpMenu.addSeparator()
        helpMenu.addAction(specCreditAction)
        helpMenu.addAction(aboutAnansiAction)
        
        ## Toolbar ##
        self.toolbar = self.addToolBar("main")
        
        saveAction = QtGui.QAction("Save", self)
        saveAction.setShortcut("Ctrl+S")
        
        loadAction = QtGui.QAction("Open", self)
        loadAction.setShortcut("Ctrl+O")
        
        boldAction = QtGui.QAction("B", self)
        boldAction.setShortcut("Ctrl+B")
        
        italicAction = QtGui.QAction("I", self)
        italicAction.setShortcut("Ctrl+I")
        
        underlineAction = QtGui.QAction("U", self)
        underlineAction.setShortcut("Ctrl+U")
        
        self.toolbar.addAction(saveAction)
        self.toolbar.addAction(loadAction)
        self.toolbar.addSeparator()
        self.toolbar.addAction(boldAction)
        self.toolbar.addAction(italicAction)
        self.toolbar.addAction(underlineAction)
        
        ## Main GUI ##
        self.qte = QtGui.QTextEdit(self)
        
        self.setCentralWidget(self.qte)
        self.center()
        self.show()
    

        
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def opennewsagg(self):
        nav = NewsAggQT()
        nav.show()
        

class NewsPad(QtGui.QMainWindow):
    def __init__(self):
        super(NewsAggQT, self).__init__()
        
        self.InitUI()
        
    def InitUI(self):
        
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle("News Aggregator View")
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        
        self.statusBar().showMessage('Ready')
        
        menubar = self.menuBar()
        
        ## File Menu ##
        fileMenu = menubar.addMenu("&File")
            
        newWin = QtGui.QAction("&New Window", self)
        newWin.setShortcut("Ctrl+N")
        newWin.setStatusTip("Open a brand new window!")
        newWin.setEnabled(False)
            
        clearAllAction = QtGui.QAction("C&lear All", self)
        clearAllAction.setShortcut("Ctrl+l")
        clearAllAction.setStatusTip("Clear all text.")
        clearAllAction.setEnabled(False)
            
        exitAction = QtGui.QAction("E&xit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit the application")
        exitAction.triggered.connect(self.close)
            
        fileMenu.addAction(newWin)
        fileMenu.addAction(clearAllAction)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAction)
            
        ## View Menu ##
        viewMenu = menubar.addMenu("V&iew")
        
        calcViewAction = QtGui.QAction("CalcPad View", self)
        calcViewAction.setStatusTip("View the Calculator")
        calcViewAction.setEnabled(False)
            
        storypadViewAction = QtGui.QAction("Storypad View", self)
        storypadViewAction.setStatusTip("View StoryPad")
        storypadViewAction.setEnabled(False)
        
        newsAggViewAction = QtGui.QAction("NewsPad View", self)
        newsAggViewAction.setStatusTip("Open the News Aggregator")
        newsAggViewAction.triggered.connect(self.opennewsagg)
        newsAggViewAction.setEnabled(False)
        
        viewMenu.addAction(calcViewAction)
        viewMenu.addAction(storypadViewAction)
        viewMenu.addAction(newsAggViewAction)
        
        ## Help Menu ##
        helpMenu = menubar.addMenu("&Help")
        
        helpAnansiAction = QtGui.QAction("Help with Anansi CalcPad", self)
        helpAnansiAction.setStatusTip("Get Help with Anansi CalcPad")
        helpAnansiAction.setEnabled(False)
        
        checkUpdatesAction = QtGui.QAction("Check for Updates...", self)
        checkUpdatesAction.setStatusTip("Check for Updates!")
        checkUpdatesAction.setEnabled(False)
        
        reportIssueAction = QtGui.QAction("Report an Issue...", self)
        reportIssueAction.setStatusTip("Report a bug, or give a suggestion")
        reportIssueAction.setEnabled(False)
        
        specCreditAction = QtGui.QAction("Special Credits...", self)
        specCreditAction.setStatusTip("Special Credits for Special People")
        specCreditAction.setEnabled(False)
            
        aboutAnansiAction = QtGui.QAction("About Anansi CalcPad", self)
        aboutAnansiAction.setStatusTip("About Anansi CalcPad Version " + str(ver))
        aboutAnansiAction.setEnabled(False)
            
        helpMenu.addAction(helpAnansiAction)
        helpMenu.addAction(checkUpdatesAction)
        helpMenu.addAction(reportIssueAction)
        helpMenu.addSeparator()
        helpMenu.addAction(specCreditAction)
        helpMenu.addAction(aboutAnansiAction)
        
        web = QtWebKit.QWebView(self)
        web.load(QtCore.QUrl("http://www.google.com/reader"))
        web.show()
        
        self.setCentralWidget(web)
        self.center()
        self.show()        
        
        
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())    

def main():
    app = QtGui.QApplication(sys.argv)
    sp = CalcPad()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()