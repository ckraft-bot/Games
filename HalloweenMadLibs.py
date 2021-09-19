#Players inputs
#s1 I can't...
holiday = input("holiday: ")
n = input("noun: ")
place = input("place: ")
#s2 This year...
person = input("person: ")
adj = input("adjective: ")
body_part = input("body part (plural): ")
#s3 Before I...
v = input("verb: ")
adj2 = input("adjective: ")
n2 = input("noun: ")
food = input("food: ")
#s4 Finally, ...
n3 = input("plural noun: ")
#s5 When____...
famous_person = input("famous person: ")
n4 = input("noun: ")
#s6 Yum! I got...
food2 = input("food: ")
food3 = input("food: ")
#s7 Wee visit...
number = input("number: ")
v2 = input("verb: ")
#s8 My___...
family = input("family member: ")
food4 = input("food: ")
body_part2 = input("body part: ")
number2 = input("number: ")
#s9 I hope I'll...
adj3 = input("adjective: ")
n5 = input("plural noun: ")
#s10
holiday2 = input("holiday: ")


#Story time

s1= f"I can't believe it's already {holiday}! I can't wait to put on my {n} and visit every {place} in my neighborhood."
s2= f"This year, I am going to dress up as (a) {person} with {adj} {body_part}."
s3= f"Before I {v}, I make sure to grab my {adj2} {n2} to hold all of my {food}."
s4= f"Finally, all of my {n3} are ready to go!"
s5= f"When {famous_person} answers the door, I say, '{n4} or Tread!'"
s6= f"Yum! I got a {food2} and a {food3}."
s7= f"We visit {number} houses and decide it's time to {v2} home."
s8= f"My {family} says if I eat too much {food4}, my {body_part2} will hurt, so I'll eat just {number2} pieces and go straight to bed."
s9= f"I hope I'll have {adj3} dreams of {n5} tonight!"
s10= f"Happy {holiday2}!"

story = s1+ s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10
#Print the story
print(story)