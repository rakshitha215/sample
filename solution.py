#Find the largest number numbers = [45, 99, 3, 20, 60]
list1=[45, 99, 3, 20, 60]
print(max(list1))
#Duplicate_numbers=[1,1,2,3,4,4,5,5,6,6,6]
Duplicate_numbers=[1,1,2,3,4,4,5,5,6,6,6]
repeated=[]
for i in Duplicate_numbers:
    if Duplicate_numbers.count(i)>1:
        if i not in repeated:
            repeated.append(i) 
print("Duplicate numbers in list are",repeated)
# Zero in last nums = [0, 1, 0, 3, 0, 12]
temperature_in_fah= int(input("Enter the Temperature value in Fahrenite"))
celcius=(temperature_in_fah-32)*(5/9)
print("Temperature in celcius is ",round(celcius))
Duplicate_numbers = [1,1,2,3,4,4,5,5,6,6,6]

seen = set()
print(seen)
repeated = set()
print(repeated)

for i in Duplicate_numbers:
    if i in seen:
        repeated.add(i)
    else:
        seen.add(i)

print("Duplicate numbers in list are", list(repeated))
