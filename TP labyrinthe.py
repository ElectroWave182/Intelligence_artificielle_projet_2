from random import randint

"""
labyrinth = [
    ['_', 'P', '.', '_'],
    ['.', '.', '.', 'P'],
    ['.', 'P', '.', '_'],
    ['E', '_', '.', 'S']
]
"""
labyrinth = [
    ['E', '.', '_', '.', 'P'],
    ['.', '.', '.', '.', 'S'],
    ['.', 'P', '.', '_', 'P'],
    ['.', '_', '.', '.', '.'],
    ['.', '.', '.', 'P', '.'],
    ['_', '.', 'P', '_', '.'],
    ['P', 'S', '.', '.', '_']
]


def main ():

    # Parameters

    nbLines = len (labyrinth)
    nbColumns = len (labyrinth[0])
    
    
    # Entry searching
    
    def entrance ():
    
        for line in range (nbLines):
            for column in range (nbColumns):
                if labyrinth[line][column] == 'E':
                    return (line, column)
                    
    start = entrance ()
    
    
    # Bellman application
    
    valuation = [[0] * nbColumns for _ in range (nbLines)]
    for _ in range (1000):
        
        # Route of the labyrinth
        
        line, column = start
        while True:
        
            up = (line - 1, column)
            down = (line + 1, column)
            left = (line, column - 1)
            right = (line, column + 1)
            
            tile = labyrinth[line][column]
            match tile:
            
            
                # Valuation modification
            
                case 'S':
                    valuation[line][column] = 1000
                    break
                    
                case 'P' | '_':
                    valuation[line][column] = -1000
                    break
                
                case 'E' | '.':
                
                    # Calculation of the average value
                    
                    values = []
                    def lookup (direction):
                    
                        nearbyLine, nearbyColumn = direction
                        
                        if 0 <= nearbyLine < nbLines and 0 <= nearbyColumn < nbColumns:
                            values.append (valuation[nearbyLine][nearbyColumn])
                        
                    lookup (up)
                    lookup (down)
                    lookup (left)
                    lookup (right)
                        
                    valuation[line][column] = sum (values) / len (values)
                
                case other:
                    print ("An unrecognized tile has been put in the labyrinth.")
                    return
                
                
            # Next tile
            
            near = []
            def directionCheck (direction):
            
                nextLine, nextColumn = direction
                
                if 0 <= nextLine < nbLines and 0 <= nextColumn < nbColumns:
                    near.append (valuation[nextLine][nextColumn])
                else:
                    near.append (float ('-inf'))
            
            directionCheck (up)
            directionCheck (down)
            directionCheck (left)
            directionCheck (right)
            
            best = max (near)
            possibilities = [
                direction
                for direction in range (4)
                if near[direction] == best
            ]
            
            
            # Randomnizing directions with the same values
            
            choice = randint (0, len (possibilities) - 1)
            path = possibilities[choice]

            
            # Updating line and column
            
            match path:
            
                case 0: line -= 1
                case 1: line += 1
                case 2: column -= 1
                case 3: column += 1
                
                
    # Displaying
    
    for line in valuation:
        for nb in line:
        
            print (round (nb), end = "      ")
        print ('\n')


main ()
