#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PySide import QtGui, QtCore

ver = 2.0
vername = "Pre-Alpha 1"

class CalculatorView(QtGui.QMainWindow):
    def __init__(self):
        super(CalculatorView, self).__init__()

        self.InitUI()

    def InitUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Anansi CalcPad")
        self.setWindowIcon(QtGui.QIcon("icon.ico"))

        # Set Status Bar
        self.statusBar().showMessage("Ready")

        # Create Main Menu
        menubar = self.menuBar()

        # Create File Menu
        newAction = QtGui.QAction("&New", self)
        newAction.setShortcut("Ctrl+N")
        newAction.setStatusTip("Open a New Window")
        #newAction.triggered.connect(self.newWindow)
        newAction.setEnabled(False)

        saveAction = QtGui.QAction("&Save", self)
        saveAction.setShortcut("Ctrl+S")
        saveAction.setStatusTip("Save the current file.")
        saveAction.setEnabled(False)

        saveAsAction = QtGui.QAction("&Save As...", self)
        saveAsAction.setShortcut("Ctrl+Shift+S")
        saveAsAction.setStatusTip("Save the current file as a new file.")
        saveAsAction.setEnabled(False)

        openAction = QtGui.QAction("&Open...", self)
        openAction.setShortcut("Ctrl+O")
        openAction.setStatusTip("Open a file that is already saved.")
        openAction.setEnabled(False)

        exitAction = QtGui.QAction("E&xit", self)
        exitAction.setShortcut("Alt+F4")
        exitAction.setStatusTip("Exit the program.")
        exitAction.setEnabled(False)

        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(newAction)
        QtGui.QMenu.addSeparator(fileMenu)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(saveAsAction)
        fileMenu.addAction(openAction)
        QtGui.QMenu.addSeparator(fileMenu)
        fileMenu.addAction(exitAction)

        # Edit Menu
        copyAction = QtGui.QAction("Copy", self)
        copyAction.setShortcut("Ctrl+C")
        copyAction.setStatusTip("Copy currently selected text.")
        copyAction.setEnabled(False)

        cutAction = QtGui.QAction("Cut", self)
        cutAction.setShortcut("Ctrl+X")
        cutAction.setStatusTip("Move text (i.e., copy and delete) into a new section.")
        cutAction.setEnabled(False)

        pasteAction = QtGui.QAction("Paste", self)
        pasteAction.setShortcut("Ctrl+V")
        pasteAction.setStatusTip("Paste text into new section.")
        pasteAction.setEnabled(False)

        selectAllAction = QtGui.QAction("Select All", self)
        selectAllAction.setShortcut("Ctrl+A")
        selectAllAction.setStatusTip("Select all text in current document.")
        selectAllAction.setEnabled(False)

        findAction = QtGui.QAction("Find...", self)
        findAction.setShortcut("Ctrl+F")
        findAction.setStatusTip("Find text in current document.")
        findAction.setEnabled(False)

        findAndReplaceAction = QtGui.QAction("Find and Replace...", self)
        findAndReplaceAction.setShortcut("Ctrl+Shift+F")
        findAndReplaceAction.setStatusTip("Find and replace text in current document.")
        findAndReplaceAction.setEnabled(False)

        preferencesAction = QtGui.QAction("Preferences", self)
        preferencesAction.setShortcut("Ctrl+P")
        preferencesAction.setStatusTip("Edit your preferences for our program.")
        preferencesAction.setEnabled(False)

        editMenu = menubar.addMenu("&Edit")
        editMenu.addAction(copyAction)
        editMenu.addAction(cutAction)
        editMenu.addAction(pasteAction)
        QtGui.QMenu.addSeparator(editMenu)
        editMenu.addAction(findAction)
        editMenu.addAction(findAndReplaceAction)
        QtGui.QMenu.addSeparator(editMenu)
        editMenu.addAction(preferencesAction)

        # View Menu
        viewMenu = menubar.addMenu("V&iew")

        calcView = QtGui.QAction("CalcPad(r)", self)
        calcView.setStatusTip("Change to the calculator")
        calcView.setEnabled(False)

        storyPadView = QtGui.QAction("StoryPad(r)", self)
        storyPadView.setStatusTip("Change to the StoryPad(r)/Journal view.")
        storyPadView.setEnabled(False)

        newsAggView = QtGui.QAction("News Aggregator", self)
        newsAggView.setStatusTip("Change to the News Aggregator View.")
        newsAggView.setEnabled(False)

        viewMenu.addAction(calcView)
        viewMenu.addAction(storyPadView)
        viewMenu.addAction(newsAggView)

        # Help Menu
        helpMenu = menubar.addMenu("&Help")
        
        helpAction = QtGui.QAction("Help", self)
        helpAction.setShortcut("F1")
        helpAction.setStatusTip("Get help with Anansi CalcPad")
        helpAction.setEnabled(False)
        helpMenu.addAction(helpAction)
        QtGui.QMenu.addSeparator(helpMenu)

        updateAction = QtGui.QAction("Check for Updates...", self)
        updateAction.setStatusTip("Check for updates to Anansi CalcPad.")
        updateAction.setEnabled(False)
        helpMenu.addAction(updateAction)

        reportAction = QtGui.QAction("Report an Issue...", self)
        reportAction.setStatusTip("Automatically open your default web browser to report an issue through Github.")
        reportAction.setEnabled(False)
        helpMenu.addAction(reportAction)
        QtGui.QMenu.addSeparator(helpMenu)

        aboutAction = QtGui.QAction("About Anansi CalcPad " + str(ver) + " " + vername, self)
        aboutAction.setStatusTip("View more information about Anansi CalcPad " + str(ver) + " " + vername)
        aboutAction.setEnabled(False)
        helpMenu.addAction(aboutAction)

        # End Menu Bar



        self.center()
        self.show()

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',
                                           "Are you sure you want to quit?", QtGui.QMessageBox.Yes |
                                           QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

def main():
    app = QtGui.QApplication(sys.argv)
    cv = CalculatorView()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()