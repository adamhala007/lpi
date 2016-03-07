import sys
import os
sys.path[0:0] = [os.path.join(sys.path[0], '../examples/sat')]
import sat

class SudokuSolver:
    def solve(self, pole):
        def s(x, y, n):
            return 9 * 9 * x + 9 * y + n

        def des(x):
            return [x // 81, x % 81 // 9, x % 9]
    
        def check(x, y, n):
            
            for i1 in range(x, x + 3):
                for j1 in range(y, y + 3):
                    for i2 in range(x, x + 3):
                        for j2 in range(y, y + 3):
                            if i1 != i2 or j1 != j2:
                                f.write('{} {} 0\n'.format(-(s(i1, j1, n)), -(s(i2, j2, n))))
                            
        with open('output.txt', 'w') as f:
            for i in range(9):
                for j in range(9):
                    if pole[i][j] != 0:
                        
                        f.write('{} 0\n'.format(s(i, j, pole[i][j])))

            for i in range(9):
                for j in range(9):
                    for n in range(1, 10):
                        
                        f.write('{} '.format(s(i, j, n)))

                    f.write('0\n')

            for n in range(1, 10):
                for i in range(9):
                    for j1 in range(9):
                        for j2 in range(9):
                            if j1 != j2:
                                
                                f.write('{} {} 0\n'.format(-(s(i, j1, n)), -(s(i, j2, n))))

                for i in range(9):
                    for j1 in range(9):
                        for j2 in range(9):
                            if j1 != j2:
                                
                                f.write('{} {} 0\n'.format(-(s(j1, i, n)), -(s(j2, i, n))))

                for i in range(0, 7, 3):
                    for j in range(0, 7, 3):
                        check(i, j, n)

        solver = sat.SatSolver()
        splnene, riesenie = solver.solve("output.txt", "output2.txt")

        if not splnene:
            return [[0] * 9] * 9
        
        for x in riesenie:
            if x > 0:
                i, j, n = des(x - 1)
                n += 1
                pole[i][j] = n

        return pole
