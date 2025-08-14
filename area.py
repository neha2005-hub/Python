name = input("Enter the name of shape : ")

if name == "rectangle":
    l = int(input("Enter rectangle's length : "))
    b = int(input("Enter rectangle's breadth : "))
        
    rect_area = l * b
    rect_peri = 2 * (l + b)

    print("The area of rectangle is ", rect_area)
    print("The perimeter of rectangle is ", rect_peri)

  
elif name == "square":
    s = int(input("Enter square's side length : "))

    sqt_area = s * s
    sqt_peri = 4 * s

    print("The area of square is ", sqt_area)
    print("The perimeter of square is ", sqt_peri)


elif name == "triangle":
    h = int(input("Enter triangle's height length : "))
    b = int(input("Enter triangle's breadth length : "))
    side1 = int(input("Enter triangle's first side : "))
    side2 = int(input("Enter triangle's second side : "))
    side3 = int(input("Enter triangle's third side : "))
        
    tri_area = 0.5 * b * h
    tri_peri = side1 + side2 + side3

    print("The area of triangle is ", tri_area)
    print("The perimeter of triangle is ", tri_peri)


elif name == "circle":
    r = int(input("Enter circle's radius length : "))
    pi = 3.14

    circ_area = pi * r * r
    circ_peri = 2 * pi * r

    print("The area of circle is ", circ_area)
    print("The perimeter of circle is ", circ_peri)


else:
    print("Sorry! This shape is not available")