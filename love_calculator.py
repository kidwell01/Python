print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
name1_lowercase = name1.lower()
name2_lowercase = name2.lower()

#checking for TRUE
count_T = name1_lowercase.count('t') + name2_lowercase.count('t')
count_R = name1_lowercase.count('r') +  name2_lowercase.count('r')
count_U = name1_lowercase.count('u') +  name2_lowercase.count('u')
count_E = name1_lowercase.count('e') +  name2_lowercase.count('e')
total_count1 = count_T + count_R + count_U + count_E

print(f"T occurs {count_T} times")
print(f"R occurs {count_R} times")
print(f"U occurs {count_U} times")
print(f"E occurs {count_E} times")
print(f"Total = {total_count1}")

#checking for LOVE
count_L = name1_lowercase.count('l') +  name2_lowercase.count('l')
count_O = name1_lowercase.count('o') +  name2_lowercase.count('o')
count_V = name1_lowercase.count('v') +  name2_lowercase.count('v')
count_E = name1_lowercase.count('e') +  name2_lowercase.count('e')
total_count2 = count_L + count_O + count_V + count_E

print(f"L occurs {count_L} times")
print(f"O occurs {count_O} times")
print(f"V occurs {count_V} times")
print(f"E occurs {count_E} times")
print(f"Total = {total_count2}")

count1 = str(total_count1)
count2 = str(total_count2)


score = count1 + count2
love_score = int(score)
if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your love score is {love_score}.")


