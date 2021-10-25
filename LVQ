import math
  
  
class LVQ :
    
     
    # Function here computes the winning vector
    # by Euclidean distance
    def winner( self, weights, sample ) :
          
        D0 = 0
        D1 = 0
          
        for i  in range( len( sample ) ) :
            D0 = D0 + math.pow( ( sample[i] - weights[0][i] ), 2 )
            D1 = D1 + math.pow( ( sample[i] - weights[1][i] ), 2 )
              
            if D0 > D1 :
                return 0
            else : 
                return 1
  
    # Function here updates the winning vector     
    def update( self, weights, sample, J, alpha ) :
        for i in range(len(weights)) :
            weights[J][i] = weights[J][i] + alpha * ( sample[i] - weights[J][i] ) 
  
