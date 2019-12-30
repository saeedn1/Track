import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I[i][i] = 1.0
        return I


class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # 
        if self.w<1:
            return self
        else:
            return (self[0][0]*self[1][1]-self[0][1]*self[1][0])
                

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # 
        digsum=0
        for i in range(self.h):
            for x in range(self.w):
                if x == i:
                    digsum = digsum + self[i][x]
        return digsum
        

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        inverse =[]
        # 
        if self.h == 1:
                inverse.append([1 / self[0][0]])
        elif self.h == 2:
                # If the matrix is 2x2, check that the matrix is invertible
                if self[0][0] * self[1][1] == self[0][1] * self[1][0]:
                    raise ValueError('The matrix is not invertible.')
                else:
                    # Calculate the inverse of the square 1x1 or 2x2 matrix.
                    a = self[0][0]
                    b = self[0][1]
                    c = self[1][0]
                    d = self[1][1]

                    factor = self.determinant()

                    inverse = [[d, -b],[-c, a]]

                    for i in range(self.h):
                        for j in range(self.w):
                            inverse[i][j] =  inverse[i][j]/factor
    
        return Matrix(inverse)
    
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # 
        trans = []
        for i in range(self.h):
            raw = []
            for j in range(self.w):
                raw.append(self[j][i])
            trans.append(raw)
        return Matrix(trans)          

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # 
        #
        matrixSum=[]
        raw = [];
        for i in range(self.h):
            raw=[]
            for x in range(self.w):
                raw.append( self[i][x] + other[i][x])
            matrixSum.append(raw)
        return Matrix(matrixSum)
    
    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # 
        #
        netagive=[]
        raw=[]
        for i in range (self.h):
            raw=[]
            for x in range(self.w):
                raw.append(-self[i][x])
            netagive.append(raw)
        return Matrix(netagive)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # 
        #
        matrixSub=[]
        raw = [];
        for i in range(self.h):
            raw=[]
            for x in range(self.w):
                raw.append( self[i][x] - other[i][x])
            matrixSub.append(raw)
        return Matrix(matrixSub)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # 
        #
        colsum =0
        matrixMul=[]
        for i in range (self.h):
            raw=[]
            for x in range(self.h):
                msum = 0
                for j in range(other.h):
                    msum = msum + self[i][j] * other[j][x]
                raw.append(msum)
            matrixMul.append(raw)
        return Matrix(matrixMul)
    
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
#         print("this is other: ", other)
#         print("this is self: ",self)
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            matrixMul=[]
            for i in range(self.h):
                raw=[]
                for j in range(self.w):
                    raw.append(other * self[i][j])
                matrixMul.append(raw)
                
            return Matrix(matrixMul)
            
            
            
            
            
            
            
            