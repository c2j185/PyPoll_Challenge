print("Hello World")

counties = ["Arapahoe", "Denver", "Jefferson"]

len(counties)

counties = ["Arapahoe", "Denver", "Jefferson"]

print(counties)

#index starts at 0
print(counties [0])


#length of list
print(len(counties))

#SLICING pulls specific information\

print(counties[0 : 2])

#Add item to list
#to end us .append
counties.append ("El Paso")
print(counties)

#insert into spot
counties.insert(2, "El Paso")
print(counties)


#remove
#end
counties.remove("El Paso")
print(counties)
#elsewhere
counties.pop(3)
print(counties)
#replace
counties[2] = "El Paso"
print(counties)

#tuples are lists that cannot be changes
counties_tuple = ("Arapahoe", "Denver", "Jefferson")
print(counties_tuple)

'dictionary stores data {key:value}'


counties_dict = {'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
print(counties_dict)

print(counties_dict.get("Denver"))

voting_data = []

voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

print(voting_data)

print(len(voting_data))


var = {"county": "El Paso", "registered_voters":461149}

voting_data.insert(1, {"county": "El Paso", "registered_voters":461149})

print(voting_data)

voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})


print(voting_data)


voting_data[1] = {"county":"Jefferson", "registered_voters": 432438}
voting_data[2] = {"county":"Denver", "registered_voters": 463353}
print(voting_data)

voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
print(voting_data)