#question2
str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False
print(str1[-1]=='!')
print(str2[-1]=='!')

#question3
famous_words = "seven years ago..."
string_prepend = "Four score and "
str3 = string_prepend + famous_words
str4 = ''.join([string_prepend, famous_words])
print(str3)
print(str4)

#question4
munsters_description = "the Munsters are CREEPY and Spooky."
# => 'The munsters are creepy and spooky.'
print(munsters_description.capitalize())

#question5
munsters_description = "The Munsters are creepy and spooky."
print(munsters_description.swapcase())

#question6
str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."
print("Dino" in str1)
print("Dino" in str2)

#question7
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.append("Dino")
print(flintstones)

#question8
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.extend(["Dino","Hoppy"])
print(flintstones)

#question9
advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as
print(advice[:advice.find("house")])

#question10
advice = "Few things in life are as important as house training your pet dinosaur."
print(advice.replace("important","urgent"))