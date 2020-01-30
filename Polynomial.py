#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Checkpoint 1
# Date: 23/01/2020
# Name: Yizhe Fan
# Std Number: s2017502

# creeate class polynomial
class Polynomial(object):
    def __init__(self, coeff=[]):
        self.coeff = coeff[:]
    
    # change values of poly
    def change_value(self, new=[]):
        self.coeff = new[:]

    # get order for list
    def get_order(self):
        return len(self.coeff)-1
    
    # to represent a polynomial 
    def show_poly(self):
        poly_term = ''
        for n in range(len(self.coeff)):
            power = n
            if self.coeff[n] > 0:
                # if coefficient is 1 print only sign eg. + 1x -> +x
                if self.coeff[n] == 1 and power > 0:
                    coeff = ' + '
                # if the const is positive number
                elif power == 0:
                    coeff = ' ' + str(self.coeff[n])
                elif power == 1 and self.coeff[0] == 0:
                    coeff = ' ' + str(self.coeff[n])
                else:
                    coeff = ' + ' + str(self.coeff[n])
            # negative coeffs
            elif self.coeff[n] == 0:
                continue
            else:
                # if coefficient is -1 print only sign eg. -1x -> -x
                if self.coeff[n] == -1 and power > 0:
                    coeff = ' - '
                elif power == 0:
                    coeff = ' ' + str(self.coeff[n])
                else:
                    coeff = ' - ' + str(abs(self.coeff[n]))

            if power == 0:
                # dsiplay only constant
                poly_term = poly_term + str(coeff)
            elif power == 1:
                # display only coeff and X
                poly_term = poly_term + str(coeff) + 'x'
            else:
                # display full polynomial term AX^b
                poly_term = poly_term + str(coeff) + 'x^' + str(power)
        return poly_term

    # get list of coefficients
    def get_coeff(self):
        return self.coeff

    # adding polynomial
    def __add__(self, poly2):
        # get the length of 2 polynomials and set an empty list of result
        a = len(self.coeff)
        b = len(poly2.coeff)
        result = []
        
        # case that 2 polynomials are in different length
        if a >= b:
            max = a
            for i in range(a-b):
                # add extra zeros to the shorter one
                poly2.coeff.append(0)   
        else:
            max = b
            for i in range(b-a):
                self.coeff.append(0)
        
        # adding numbers
        for n in range(max):
            result.append(self.coeff[n] + poly2.coeff[n])
        return Polynomial(result[:])

    # differentiating polynomial
    def diff_poly(self):
        c =[]
        for n in range(len(self.coeff)):
            c1 = self.coeff[n] * n
            c.append(c1)
        del c[0]
        result = Polynomial(c)
        return result

    # intergrating polynomial
    def intg_poly(self, const):
        # get the const from input parameter
        c = [const]
        
        # deal with each coefficient and add to the matrix c
        for n in range(len(self.coeff)):
            c1 = self.coeff[n]/(n+1)
            c.append(round(c1,2))
        
        result = Polynomial(c)
        return result
   


# main demonstration
def main():
    # create 2 polynomials
    Pa = Polynomial([2,0,4,-1,0,6])
    Pb = Polynomial([-1,-3,0,4.5])
    print('Pa =' + Pa.show_poly())
    print('Pb =' + Pb.show_poly())
    
    # show the order of Pa
    print('The order of Pa is: ', end='')
    print(Pa.get_order())

    # add 2 polys
    P = Pa + Pb
    print('The sum of two polynomials is: ', end='')
    print(P.show_poly())

    # calculate the first derivative of Pa
    Pa_diff_1 = Pa.diff_poly()
    print('The first derivative of Pa is: ', end='')
    print(Pa_diff_1.show_poly())

    # calculates the antiderivative of the result
    print('With the constant of integration equals to 2.\nThe antiderivative of the result is: ', end='')
    print(Pa_diff_1.intg_poly(2).show_poly())

main()