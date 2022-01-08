#Author: Mylan Nguyen
##This program takes shape(s) (cylinder, rectangular prism, sphere) as input, sorts them by volume from smallest to largest, and prints the volume of the shapes

#Import the function volumes
import volumes

#Create the list of volumes of the inputted shapes
my_list = []

quit = False
error = False
while quit == False:
    if error == False:
        #Prompt the user to input shape
        shape = input("Please enter shape (quit/q, cylinder/c, prism/p, sphere/s): ")
    else:
        #Prompt the user for shape if an invalid input was entered
        shape = input("Please enter shape: ")
        error = False

    if shape.lower() == "quit" or shape.lower() == "q":
        #When the user enters quit or q, exit the while loop
        quit = True
    elif shape.lower() == "cylinder" or shape.lower() == "c":
        #Prompt for the height and radius of the cylinder and print the volume of the cylinder
        height = int(input("Enter height of side for the cylinder: "))
        radius = int(input("Enter radius of side for the cylinder: "))
        print("The volume of a cylinder with height %.1f and radius %.1f is: \t %.2f." % (height, radius, volumes.volume_of_cylinder(radius, height)))
        print()
        #Append the cylinder and the volume of the shape to the list of volumes
        my_list.append(("cylinder", volumes.volume_of_cylinder(radius, height)))
    elif shape.lower() == "prism" or shape.lower() == "p":
        #Prompt for the length, width and height of the prism and print the volume of the prism
        length = int(input("Enter the length of the rectangular prism: "))
        width = int(input("Enter the width of the rectangular prism: "))
        height = int(input("Enter the height of my rectangular: "))
        print("The volume of a rectangular prism with length %.1f, width %.1f and height %.1f is: \t %.2f." % (length, width, height, volumes.volume_of_prism(length, width, height)))
        print()
        #Append the pyramid and the volume of the shape to the list of volumes
        my_list.append(("prism", volumes.volume_of_prism(length, width, height)))
    elif shape.lower() == "sphere" or shape.lower() == "s":
        #Prompt for the radius of the sphere and print the volume of the sphere
        radius_sphere = int(input("Enter the sphere's radius: "))
        print("The volume of a sphere with radius %.1f is: \t %.2f." % (radius_sphere, volumes.volume_of_sphere(radius_sphere)))
        print()
        #Append the sphere and the volume of the shape to the list of volumes
        my_list.append(("sphere", volumes.volume_of_sphere(radius_sphere)))
    else:
        #For invalid inputs, print an error message and prompt for another shape
        print("\t-- invalid input: enter (quit/q, cylinder/c, prism/p, sphere/s): ")
        print()
        error = True

#Sort the shapes in my_list from lowest volume to highest volume
my_list.sort(key=lambda my_list: my_list[1])

#For when no shape is inputed, print message
if my_list == []:
    print("Output: No shapes entered")
#Print an output statement and the list of tuples in order if shape is entered
else:
    print("Output: Volume of shapes entered in sorted order:")
    for i in range(len(my_list)):
        print("%s %.2f" % (my_list[i][0], my_list[i][1]))
