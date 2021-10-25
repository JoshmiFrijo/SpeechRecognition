# Driver code
def main() :
  
    # Training Samples ( m, n ) with their class vector
    X =  dataset
  
    Y = [ 1 ,  1 , 1  , 1 , 0 , 0 , 0 , 0 , 0]
    m, n = len( X ), len( X[0] )
      
    # weight initialization ( n, c )
    weights = []
    weights.append( X.pop( 0 ) )
    weights.append( X.pop( 1 ) )
  
    # Samples used in weight initialization will
    # not use in training
    m = m - 2
      
    # training
    ob = LVQ()
    epochs = 3
    alpha = 0.1
      
    for i in range( epochs ) :
        for j in range( m ) :
              
            # Sample selection
            T = X[j]
              
            # Compute winner
            J = ob.winner( weights, T )
           
            # Update weights
            ob.update( weights, T, J, alpha )
              
    # classify new input sample
    T = testfeature[0]
    J = ob.winner( weights, T )
    output=word(J)
    print( "Recognized word : ", output )
    print( "Trained weights : ", weights )
      
if __name__ == "__main__":
    main()
