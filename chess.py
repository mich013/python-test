
import getopt
import sys

"""
  Chess.py
"""


class Piece(object):
    """
        Piece
        this is the base class for chess peices
    """
    moves = None
    MAXSIZE = 8
    ASCII_OFFSET = 64

    # def __init__(self, moves):
    #     self.moves = moves

    def is_valid_xy_position(self, xy_position):
        """
            is_valid_yx_position
            this will take a array with x and y in it and insure it fits on the board
        """
        x, y = xy_position
        return (x>=1 and x<=self.MAXSIZE) and (y>=1 and y<=self.MAXSIZE)
    
    def position_to_xy(self,position):
        """
            position to xy
            this method will take a positioni.e. a1, b5, g1 and return its xy position 1,1 2,5 ...
        """
        return [ord(position[0])-self.ASCII_OFFSET, int(position[1:])]
    
    def xy_to_position(self, xy):
        """
            xy_to_position
            this will take a xy and return a positionie [1,1] -> a1
        """
        return chr(self.ASCII_OFFSET + xy[0]) + str(xy[1]).strip()
    
    def possible_positions(self, position):
        """
            possible_positions
            this method will take a position and return the possible position
            this is driven bye the move data that is used by the clss that inherents this base class
        """
        for move in self.moves:
            xy_position = self.position_to_xy(position)
            new_xy_position = [x + y for x, y in zip(xy_position, move)]
            while self.is_valid_xy_position(new_xy_position):
                new_position = self.xy_to_position(new_xy_position)
                new_xy_position = [x + y for x, y in zip(new_xy_position, move)]
                yield new_position
                
class Rook(Piece):
    """
        Rook class
        
    """
    moves = [
        [1,0],
        [0,1],
        [-1,0],
        [0,-1]
        ]
    
                  
class Bishop(Piece):
    """
        bishop class
    """
    moves = [
        [1, 1],
        [1, -1],
        [-1, 1],
        [-1, -1],
    ]

class Knight(Piece):
    """
        Knight class
        this class overides the posible_positions method due to the nature of Knights movement
    """
    moves = [
        [-1, -2],
        [2, -1],
        [2, 1],
        [1, 2],
        [-1, 2],
        [-2, 1],
        [-2, -1],
        [-1, -2],
        ]
    
    def posible_positions(self, position):
        for move in self.moves:
            xy_position = self.position_to_xy(position)
            new_xy_position = [x + y for x, y in zip(xy_position, move)]
            if self.is_valid_xy_position(new_xy_position):
                new_position = self.xy_to_position(new_xy_position)
                yield new_position

class Queen(Piece):
    """
        Queen class
    """
    moves = [
        [1, 0],
        [0, 1],
        [1, 1],
        [-1, 0],
        [0, -1],
        [-1, -1],
        [1, -1],
        [-1, 1],
    ]
     
def main(argv):
    """
        main program
    """
    
    # PEICES is used as a vector for the parsing of input 
    PIECES = {"KNIGHT":Knight(),
              "ROOK":Rook(),
              "BISHOP":Bishop(),
              "QUEEN":Queen(),
    }
    opts, args = getopt.getopt(argv,"", ["piece=", "position="])
    try:
        opts, args = getopt.getopt(argv,"", ["piece=", "position="])
    except getopt.GetoptError:
         print ('chess.py -piece [Knight, Rook, Queen] -position position')
         sys.exit(2)
    
    position = None
    piece = None
    
    for opt, arg in opts:
        if opt in ['--help']:
            print ('chess.py -piece [Knight, Rook, Queen] -position position')
            sys.exit() 
        elif opt in ["--position"]:
            position = arg.upper()
        elif opt in ["--piece"]:
            piece = arg.upper()
            
            if piece not in ["KNIGHT", "ROOK", "BISHOP", "QUEEN"]:
                print("piece argument must be 'Knight, Rook, Bishop or Queen exiting")
                sys.exit(2)
    if position is None or piece is None:
        print("chess.py must have both the piece and position parameters exiting")
        print ('chess.py -piece [Knight, Rook, Queen] -position position')
        sys.exit(2)
    l = [found_position for found_position in PIECES[piece].possible_positions(position)]
    print('"', end="")
    print(*l, sep=",", end='"\n')  
       

if __name__ == "__main__":
    main(sys.argv[1:])


    