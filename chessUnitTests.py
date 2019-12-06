import unittest
from chess import Piece, Rook, Knight, Bishop, Queen

class TestChessClasses(unittest.TestCase):
    
    def testPeiceClassVars(self):
        # Test Pieces Base Constants and internal vriables
        self.assertEqual(Piece.moves, None)
        self.assertEqual(Piece.MAXSIZE, 8)
        self.assertEqual(Piece.ASCII_OFFSET, 64)
        
    def testPeiceClassMethods(self):
        
        # test is_valid_xy_position
        p = Piece()
        # Positive Test
        self.assertTrue(p.is_valid_xy_position([1,1]))
        self.assertTrue(p.is_valid_xy_position([8,8]))
        # Negative Test             
        self.assertFalse(p.is_valid_xy_position([0,0]))
        self.assertFalse(p.is_valid_xy_position([9,9]))
        
        # position_to_xy
        self.assertEqual(p.position_to_xy("A1"), [1,1])
   
        # xy_to_position(self, xy)
        self.assertEqual(p.xy_to_position([1,1]), "A1")
    
    def testRookClass(self):
        # test moves array
        self.assertEqual(Rook.moves, [
                                        [1,0],
                                        [0,1],
                                        [-1,0],
                                        [0,-1]
                                        ])
        r = Rook()
        l = [found_position for found_position in r.possible_positions("D4")]
        self.assertEqual(l, ['E4', 'F4', 'G4', 'H4', 'D5', 'D6',
                             'D7', 'D8', 'C4', 'B4', 'A4', 'D3',
                             'D2', 'D1'])
    def testBishopClass(self):
        # test moves array
        self.assertEqual(Bishop.moves, [
                                        [1, 1],
                                        [1, -1],
                                        [-1, 1],
                                        [-1, -1]
                                        ])
        b = Bishop()
        l = [found_position for found_position in b.possible_positions("D4")]
        self.assertEqual(l, ['E5', 'F6', 'G7', 'H8', 'E3', 'F2', 'G1', 'C5',
                             'B6', 'A7', 'C3', 'B2', 'A1'])    
    def testKnightClass(self):
        # test moves array
        self.assertEqual(Knight.moves, [
                                        [-1, -2],
                                        [2, -1],
                                        [2, 1],
                                        [1, 2],
                                        [-1, 2],
                                        [-2, 1],
                                        [-2, -1],
                                        [-1, -2],
                                        ])
        k = Knight()
        l = [found_position for found_position in k.possible_positions("D4")]
        self.assertEqual(l, ['C2', 'F3', 'H2', 'F5', 'H6', 'E6', 'F8', 'C6',
                             'B8', 'B5', 'B3', 'C2'])
        
    def testQueenClass(self):
        # test moves array
        self.assertEqual(Queen.moves, [
                                        [1, 0],
                                        [0, 1],
                                        [1, 1],
                                        [-1, 0],
                                        [0, -1],
                                        [-1, -1],
                                        [1, -1],
                                        [-1, 1]
                                        ])
        q = Queen()
        l = [found_position for found_position in q.possible_positions("D4")]
        self.assertEqual(l,['E4', 'F4', 'G4', 'H4', 'D5', 'D6', 'D7', 'D8',
                            'E5', 'F6', 'G7', 'H8', 'C4', 'B4', 'A4', 'D3',
                            'D2', 'D1', 'C3', 'B2', 'A1', 'E3', 'F2', 'G1',
                            'C5', 'B6', 'A7'])
    
if __name__ == '__main__':
    unittest.main()