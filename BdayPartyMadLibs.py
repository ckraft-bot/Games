#Players inputs
#s1 I'm... a...
v = input("verb-ing: ")
adv = input("adverb: ")
adj = input("adjective: ")
#s2 I'm... my best...
v2 = input("verb-ing: ")
n = input("proper noun (first name): ")
n2 = input("proper noun (first name): ")
n3 = input("proper noun (first name): ")
#s3 The party
place = input("place: ")
adj2 = input("adjective: ")
n4 = input("plural noun: ")
color = input("color: ")
n5 = input("plural noun: ")
#s4 First...
v3 = input("verb: ")
food = input("food: ")
food2 = input("food: ")
v4 = input("verb: ")
v5 = input("verb: ")
body_part = input("body part: ")
animal = input("animal: ")
v6 = input("verb: ")
n6 = input("plural noun: ")
#s5 Then comes
v7 = input("verb-ing: ")
v8 = input("verb-ing: ")
v9 = input("verb-ing: ")
adj3 = input("adjective: ")


#Story time
s1= f"I'm {v} a {adv} {adj} party for my birthday."
s2= f"I'm {v2} my friends, like {n}, {n2}, and {n3}."
s3= f"The party will be at the {place} with {adj2} {n4} and {color} {n5} for decorations."
s4= f"First, we will {v3} some snacks, like {food} and {food2}, and then we will {v4} some party games, like {v5} the {body_part} on the {animal} and {v6} the {n6}."
s5= f"Then comes my favorite part: {v7} Happy Birthday, {v8} presents, and {v9} some {adj3} cake."

story = s1 +s2 +s3 +s4 +s5
#Print the story
print(story)