import array


print("input player 1's name")
player1 = input()
print("input player 2's name")
player2 = input()
print("input player 3's name")
player3 = input()
print("input player 4's name")
player4 = input()
print("input player 5's name")
player5 = input()
print("input player 6's name")
player6 = input()
print("input player 7's name")
player7 = input()
print("input player 8's name")
player8 = input()
print("input player 9's name")
player9 = input()

array1 = [player1, player2, player3, player4, player5, player6, player7, player8, player9]
#print(array1)


print("input player 1's batting average")
ba1 = input(int())
print("input player 2's batting average")
ba2 = input(int())
print("input player 3's batting average")
ba3 = input(int())
print("input player 4's batting average")
ba4 = input(int())
print("input player 5's batting average")
ba5 = input(int())
print("input player 6's batting average")
ba6 = input(int())
print("input player 7's batting average")
ba7 = input(int())
print("input player 8's batting average")
ba8 = input(int())
print("input player 9's batting average")
ba9 = input(int())

print("input player 1's position")
po1 = input()
print("input player 2's position")
po2 = input()
print("input player 3's position")
po3 = input()
print("input player 4's position")
po4 = input()
print("input player 5's position")
po5 = input()
print("input player 6's position")
po6 = input()
print("input player 7's position")
po7 = input()
print("input player 8's position")
po8 = input()
print("input player 9's position")
po9 = input()


array2 = [ba1 + ": " + player1 + ", " + po1, ba2 + ": " + player2 + ", " + po2, ba3 + ": " + player3 + ", " + po3, ba4 + ": " + player4 + ", " + po4, ba5 + ": " + player5 + ", " + po5, ba6 + ": " + player6 + ", " + po6, ba7 + ": " + player7 + ", " + po7, ba8 + ": " + player8 + ", " + po8, ba9 + ": " + player9 + ", " + po9]

array2.sort(reverse = True)
#print(array2)

l1 = array2[0]
l2 = array2[1]
l3 = array2[2]
l4 = array2[3]
l5 = array2[4]
l6 = array2[5]
l7 = array2[6]
l8 = array2[7]
l9 = array2[8]

array3 = [l1, l2, l3, l4, l5, l6, l7, l8, l9]
#print(array3)

class Person:
    array1 = [player1, player2, player3, player4, player5, player6, player7, player8, player9]
    def __init__(self, name_average):
        self.name_average = name_average


print("Lineup:")
p1 = Person(l1)
p2 = Person(l2)
p3 = Person(l3)
p4 = Person(l4)
p5 = Person(l5)
p6 = Person(l6)
p7 = Person(l7)
p8 = Person(l8)
p9 = Person(l9)


print(p1.name_average)
print(p2.name_average)
print(p3.name_average)
print(p4.name_average)
print(p5.name_average)
print(p6.name_average)
print(p7.name_average)
print(p8.name_average)
print(p9.name_average)
