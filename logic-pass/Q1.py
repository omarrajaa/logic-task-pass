
# the question : Q1/Write a method that will remove any given character from a String?

# solution :

# the method to remove character from string :
class TextEdit:
    def remover(self,c,s):    # c = given character  s = string  r = final result
        r = ''
        for i in s:
            if i != c:
                r = r + i
        return r

# _________________________________________________________________________________________________________

# test the method assuming : string = hi my name is omar   ,   character = a

string = "hi my name is omar"
character = "a"

result = TextEdit().remover(character,string)  # call the method
print("the original string : " + string + " | the character :" + character)
print(result)


# _____________________________________________________________________________________________

# program from method

string = input("put string : ")
character = input("put character without space : ")
print(TextEdit().remover(character,string))
