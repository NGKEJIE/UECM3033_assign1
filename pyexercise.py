import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(your_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate( (x**1/2)*sy.sin((x**3/2)+1), (x,0, sy.oo))
    return ans

    
def my_solution():
    A = np.array( [[0,3,5,9,2,4,7,2,0,8], [0,3,7,0,2,6,8,0,2,9],
                   [3,4,1,8,3,0,0,4,1,8], [4,0,2,5,0,2,6,0,2,2], 
                   [0,0,0,4,1,8,2,0,4,9], [3,6,8,1,0,0,0,1,6,9], 
                   [2,3,6,8,0,1,7,0,0,0], [0,4,7,9,1,5,3,8,2,0], 
                   [0,3,1,0,0,1,4,0,5,0], [3,0,5,0,1,4,0,0,1,0]] )
    b = np.array([5,9,0,1,6,9,1,2,6,3])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1405676
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())
