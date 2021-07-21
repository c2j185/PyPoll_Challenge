#if statements
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

temperature = int(input("What is the temperature outside? "))


#if-else
if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")


#Nested If-Else
    #What is the score?
score = int(input("What is your test score? "))

    # Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')


#if-elif-elseed
    # What is the score?
score = int(input("What is your test score? "))

    # Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')


#membership operators
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")    


#logical operators
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")


#For Loops
for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])

    #Keys and Values
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county, voters in counties_dict.items():
    print(county, voters)


print((county) "has" (voters) "registered voters")








#While Loops (condition controlled operation)
x = 0
while x <= 5:
    print(x)
    x = x + 1

#For Loops
numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)
    #Same outcome as above
for num in range(5):
    print(num)



counties = ["Arapahoe", "Denver", "Jefferson"]
voters = ["422829", "463353", "432438"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

# logical operators
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

# For Loops
for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])

    # Keys and Values

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

voters: int
for county, voters in counties_dict.items():
    print(county, voters)

#concatenation
for county, voters in counties_dict.items():
    print(county , ' county has ' , voters , 'registered voters.')

    #f-string (same output as above)
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")



voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)


for county_dict in voting_data:
    for value in county_dict.values():
        print(value)


for county_dict in voting_data:
    print(county_dict['county'])


#f-strings
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")


#multiline f-strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)


#SKILL DRILL 2

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")