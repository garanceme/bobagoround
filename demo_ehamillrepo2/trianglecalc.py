pi = 3.141592653589793
import math
r = 'angle' , 'side'
r = input('angle or side with theta?')
if r== 'angle':
    x = 'cos', 'sin' , 'tan'
    x = input('cos, sin or tan?')
    if x == 'cos':
        a = 'yes' , 'no'
        a = input('do you need to find the hypotenuse?')
        if a == 'yes':
            b = float(input('what is the length of side one')) 
            c = float(input('what is teh lenght of side two'))
            z = (math.sqrt((b * b) + (c * c)))
            print('hypotenuse' , math.sqrt((b * b) + (c * c)))
            d = float(input('what is the length of the adjacent side'))
            print('theta in degrees:')
            print(math.acos(d/z) * (180/pi))
        elif a == 'no':
            k = float(input('what is the length of the hypotenuse'))
            e = float(input('what is the length of the adjacent side'))
            print('theta in degrees:')
            print(math.acos(e/k) * (180/pi))
    elif x == 'sin':
        a = 'yes' , 'no'
        a = input('do you need to find the hypotenuse?')
        if a == 'yes':
            b = float(input('what is the length of side one')) 
            c = float(input('what is teh lenght of side two'))
            z = math.sqrt((b * b) + (c * c))
            print('hypotenuse' , math.sqrt((b * b) + (c * c)))
            d = float(input('what is the length of the opposite side'))
            print('theta in degrees:')
            print(math.asin(d/z) * (180/pi)) 
        elif a == 'no':
            k = float(input('what is the length of the hypotenuse'))
            e = float(input('what is the length of the oppostie side'))
            print('theta in degrees:')
            print(math.asin(e/k) * (180/pi))
    elif x == 'tan':
        a = float(input('what is the length of the adjacent side?'))
        b = float(input('what is the length of the opposite side?'))
        print('theta in degrees')
        print(math.atan(b/a) * (180/pi))
elif r == 'side with theta':
    k = 'adjacent' , 'hypotenuse'
    m = 'opposite' , 'adjacent' , 'hypotenuse'
    x = input('cos, sin or tan?')
    if x == 'tan':
        m = input('do you need to find the opposite, adjacent, or hypotenuse side?')
        if m == 'opposite':
            k = input('which side do you already know? (adjacent , hypotenuse)')
            if k == 'adjacent':
                a = float(input('whats the length of the adjacent side'))
                b = float(input('whats theta?'))
                print('side length:')
                print((math.tan(math.degrees(b)) * a))
            elif k == 'hypotenuse':
                a = float(input('whats the length of the hypotenuse')
                b = float(input('whats theta)
                print('side length')
                print((math.sin(math.degrees(b)) * a))
        
            
            
                          
        
            
            

