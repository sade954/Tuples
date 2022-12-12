#Creating a tuple
point = (2.0, 3.0)
point_3d = point + (4.0,)
point_3d
(2.0, 3.0, 4.0)

#Unpacking a tuple
x, y, z = point_3d
x
2.0
y
3.0
z
4.0

#Format string
print("My name is: %s %s" % ("Candace", "Hollinger"))
My name is: Candace Hollinger

