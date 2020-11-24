import unittest
from Board import *

class BoardTests(unittest.TestCase):

    # Should place piece
    def testPlacingMan():
        str firstTest = placingMan(self, 10) # Test invalid input (10) to validate except block
        str excepText = "Couldn't get the input value")

        str secondTest = placingMan(self, 1)
        str invalText

        self.assertEqual(firstTest, excepText, "Should output " + excepText)
        self.

    def testMoveMan():
        moveMan(self, 1, 3)
        moveMan(self, 2, 5)

    def testFlyMan():
        flyMan(self, 0, 1)
        flyMan(self, 1, 1) # Should bypass try block, print "You cannot fly this man")

   def testIsWin():
        bool firstTest = isWin(2)
        bool secondTest = isWin(1)
        bool thirdTest = isWin(4)
        
        self.assertTrue(firstTest, "Should return true")
        self.assertFalse(secondTest, "Should return true")
        self.assertFalse(thirdTest, "Should return false")
        
    def testIsMill():
        ''' Player == 0, so this statement should return false '''
        bool firstTest = isMill(self, 1, 0)
        self.assertFalse(firstTest, "Should return false")
        
    def testRemoveMan():
        str firstTest = removeMan(self, 10, 1) # Test invalid input (10) to validate except block
        str excepText = "Input was either out of bounds or wasn't an integer"

        str secondTest = removeMan(self, 1, -1)
        str invalText = "Invalid position at: "
        
        self.assertEqual(firstTest, excepText, "Should output " + excepText)
        self.assertEqual(secondTest, invalText, "Should output " + invalText)

    def testIndexTransfer():
        int firstTest = IndexTransfer(self, 35, 30)
        int secondTest = IndexTransfer(self, 231, 226)
        int thirdTest = IndexTransfer(self, 427, 128)
        
        self.assertEqual(firstTest, 0, "Should return 0")
        self.assertEqual(secondTest, 16, "Should return 16")
        self.assertEqual(thirdTest, 10, "Should dreturn 10")

    def testAdjacentPos():
        int firstTest = adjacentPos(self, 1)
        int secondTest = adjacentPos(self, 4)
        int thirdTest = adjacentPos(self, 7)

        self.assertEqual(firstTest, [0, 2, 9], "Should return list containing 0, 2, and 9")
        self.assertEqual(secondTest, [2, 7, 12], "Should return list containing 2, 7, and 12")
        self.assertEqual(thirdTest, [4, 6], "Should return list containing 4 and 6")
