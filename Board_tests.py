import unittest
from unittest.mock import Mock
from Board import *

class BoardTests(unittest.TestCase):

        boardPoints = []
        for i in range(24):
                boardPoints.append(0)
        
        Board.__init__(Board)
        Board.initBoard(Board)
        Board.boardPoints[1] = 6
        
        def testCountMan(self):
                firstTest = Board.countMan(self, 1)
                self.assertEqual(firstTest, 0, "Should return 1")

        def testPlacingMan(self):
                boardPoints = Mock()
                Board.placingMan(self, 0)
                Board.placingMan(self, 2)

        def testMoveMan(self):
                boardPoints = Mock()
                # Validate move from one pos to another
                Board.moveMan(self, 0, 1)
                Board.moveMan(self, 1, 2)

        def testFlyMan(self):
                boardPoints = Mock()
                # Validate fly from one pos to another (0 to 1, 1 to 3, etc.)
                Board.flyMan(self, 0, 1)
                Board.flyMan(self, 1, 3)
        
        def testIsMill(self):
                firstTest = Board.isMill(1, 1, 5)
                self.assertFalse(firstTest, "Should return false") # Verify that mill is invalid
                
        def testRemoveMan(self):
                boardPoints = Mock()
                # Place piece to remove
                Board.placingMan(self, 0)

                # Validate removal
                Board.removeMan(self, 0, 1)
                Board.removeMan(self, 25, 1) # 25 is out of range, so this removal should not be possible

        def testIndexTransfer(self):
                firstTest = Board.indexTransfer(self, 35, 30)
                secondTest = Board.indexTransfer(self, 231, 226)
                thirdTest = Board.indexTransfer(self, 427, 128)
        
                self.assertEqual(firstTest, 0, "Should return 0")
                self.assertEqual(secondTest, 16, "Should return 16")
                self.assertEqual(thirdTest, 10, "Should dreturn 10")

        def testAdjacentPos(self):
                firstTest = Board.adjacentPos(self, 1)
                secondTest = Board.adjacentPos(self, 4)
                thirdTest = Board.adjacentPos(self, 7)

                self.assertEqual(firstTest, [0, 2, 9], "Should return list containing 0, 2, and 9")
                self.assertEqual(secondTest, [2, 7, 12], "Should return list containing 2, 7, and 12")
                self.assertEqual(thirdTest, [4, 6], "Should return list containing 4 and 6")

unittest.main()
