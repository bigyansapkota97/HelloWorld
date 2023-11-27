name = ["name1", "name2", "name3", "name4", "name5"]
print(name)
# accessing items from the list
print(name[0])
print(name[1])
print(name[-1])
print(name[-2])

# Using Individual Values from a List
# capitalises the first letter
print(f"The first name is {name[0].title()}")

print(name[2:5])
print(name[:5])
print(name[2:5:2])
print(name[0:-1])
print(name[0:4])
print(name[0:])

for n in name:
    print(n)

if "name2" in name:
    print("name 2 is present in the name list")
else:
    print("name2 isnt in the list")

# append/Inset/pop/DEL
print(len(name))
name.append("name6")
print(name)
name.insert(2, "added_name")
print(name)
name.remove("added_name")
print(name)

name.pop()
print(name)

del (name[1])
print(name)

name.clear()
print(name)

name_new = name.copy()
print(name_new)

name_new = ["name0"]
name_new.extend(name)
print(name_new)

name.reverse()
print(name)

name.extend(["hello"])  # adds hello to the list
name.extend("hi")  # adds h and i to the list as separate entities
print(name)

# SORT
name.sort(reverse=True)  # Descending
name.sort(reverse=False) #ascending
print(name)

new_name2 = ["1", "2", "3"]
name.extend(new_name2)
name.sort(reverse=True)
print(name)

# TRY IT YOURSELF
# 3.1/3.2/3.3

names = ["Leo", "Neymar", "Ronaldo"]
for n in names:
    print(n)
    print(f"Good Morning {n}")

transport = ["bike", "car", "airlines"]
print(f"I like to drive Harley Davidson {transport[0]}.")
print(f"I like to sit on mercedes {transport[1]}.")
print(f"I prefer to travel on Qatar {transport[2]}.")

# 3.4/3.5/3.6/3.7

guest = ["lewandowski", "raphinha", "torres"]
for n in guest:
    print(f"{n}, You are invited to our dinner today at 8 pm")

# 3.5
print(f"\n{guest[2]} is not coming")

guest[2] = "yemel"

for n in guest:
    print(f"\n {n}, You are invited to our dinner today at 8 pm")

# 3.6
print("\n Hello guys, I just found a bigger dinner table, so I am inviting more people")

guest.insert(0, "Halland")
guest.insert(2, "DeBruyne")
print(guest)

for n in guest:
    print(f"\n {n}, You are invited to our dinner today at 8 pm")

# 3.7
guest.pop()
guest.pop()
guest.pop()
print(guest)

for n in guest:
    print(f"\n {n}, You are invited to our dinner today at 8 pm")

# 3.8/3.9/3.10/3.11
places = ["paris", "London", "Barcelona", "Manchester", "Madrid"]

print(places)

alp_places = sorted(places)
print(alp_places)

rev_places = list(reversed(places))
print(rev_places)

places.reverse()
print(places)
places.reverse()
print(places)

print("\nsort\n")

places.sort(reverse=False)
print(places)

places.sort(reverse=True)
print(places)

print(f"total of {len(guest)} guests are invited")









