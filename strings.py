mytring = 'abcdefg Lock'  #offset = [0][1][2][3][4][5][6]

#slicing
print (mytring[3]) #print the letter at offset 3 in string
print (mytring[3:]) #print the string from offset 3 
print (mytring[:3]) #print the string before offset 3
print (mytring[2:5]) #print string from offset 2 to offset 4, [2][3][4]
print (mytring[::2]) #aceg 
print (mytring.capitalize())
print (mytring.upper())
print (mytring.split())
print(mytring.split("d"))

x= "I like {} as well as {}".format("Sushi","Game")
print(x)