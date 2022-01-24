class Polynomial:

    def __init__(self, coefs): #Class constructor

        self.coefficients = coefs #Attributes: Create an attribute just by assigning to it, and we can then read back the attribute using the same syntax

    def degree(self):

        return len(self.coefficients) - 1 #Methods return a value
    
    def __str__(self): #Produce a string of self

        coefs = self.coefficients
        terms = []

        if coefs[0]: #if coefs[0] == 0, 0 represents False, it will leave it out, so we don't need to check whetehr it's greater than 0
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x") #f-string: python string formatting form

        terms += [f"{'' if c == 1 else c}x^{d}"
                    for d, c in enumerate(coefs[2:], start = 2) if c]
        
        return ' + '.join(reversed(terms)) or '0'


''''
The role of 'self' parameter is helping to understand that f.degree() is just a short way of writing Polynomial.degree(f).
'''