#Game of guessing a random number
#The computer will set and guess the number by itself

import numpy as np
number = np.random.randint(1,101) #define random number

def random_predict(number:int=1)->int:

    """Randomly guessing the number
    Args:
         number (int, optional): Defined number. Defaults to 1.
    
    Returns:
        int: Number of tries
    """

    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
    return(count)
print(f'Number of tries: {random_predict()}')