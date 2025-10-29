class MultiPoly():
    def __init__(self, coefs: list):
        self.coefs = coefs
        
    def _f(self, x, coefs):
        sum = 0
        for exponent, coef in enumerate(coefs):
            sum += coef * (x ** exponent)
        
        return sum

    
    def f(self, x):
        return self._f(x, self.coefs)

    
    def _derive(self, coefs):
        
        new_coefs = []
        for i in range(1, len(coefs)):
            new_coefs.append(coefs[i] * i)
        
        return new_coefs

    def derive(self):
        return self._derive(self.coefs)


    def get_tangent_line_points(self, x1, z):

        # y = mx + c

        derivative_ceofs = self.derive()
        
        m = self._f(x1, derivative_ceofs)
        c = self.f(x1) - ( self._f(x1, derivative_ceofs) * x1 )

        return m * z + c