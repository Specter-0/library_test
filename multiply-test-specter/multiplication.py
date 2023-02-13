class Multiplication:   
    """
    Instantiate a multiplication operation.
    numbers will be multiplied by the given multiplier

    :param: multiplier
    :type: int
    """
    def __init__(self, multiplier):
        self.multiplier = multiplier
    
    def multiply(self, number):
        """
        multiply a number by the multiplier

        :param number: number to multiply
        :type: int

        :return: number multiplied by the given multiplier
        :return type: int
        """
        
        return number * self.multiplier

