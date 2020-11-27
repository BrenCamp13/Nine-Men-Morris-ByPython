import unittest
from GUI import *
from Board import *

class BoardTests:

    def testBoardOutput(event):
        boardOutput();

    def testGUIplacing():
        

    def testGUIremove(event):
        test = GUIremove(event)
        str output = "remove index "

        self.assertEqual(test, output, "Should output " + output)

    def testGUImovefrom(event):

    def testGUImoveto(event):
        test = GUImoveto(event)
        firstOutput = "move index to: "
        secondOutput = "move finished"
        
        self.assertEqual(test, firstOutput, "Should output " + firstOutput)
        if index in adjacent:
            self.assertEqual(test, secondOutput, "Should output " + secondOutput)

    # def testGUIremove2(event):

    def testGUIflyfrom(event):

    def testGUIflyto(event):

    # def testGUIremove3(event):
