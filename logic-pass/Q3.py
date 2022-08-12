
# Q3/write a function that count how many the given character repeated in a given string?

# solution :

# the function :
def CountCharacter(c,s): # c = character  and s = string
    counter = 0 # count the repeated of given character
    for i in s:
        if i == c:
            counter += 1
    return counter

# _________________________________________________________________________________________

# test the function assuming : string = hi my name is omar   ,   character = a

string = "hi my name is omar"
character = "a"
print("the original string : " + string + " | the character :" + character)
print(CountCharacter(character,string))  # call the function and print

# __________________________________________________________________________________________

# program from function

string = input("put string : ")
character = input("put character without space : ")
print(CountCharacter(character,string))

