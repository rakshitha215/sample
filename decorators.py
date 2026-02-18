#Decorators 
def person_lister(func):
    def wrapper(people):
        people.sort(key=lambda x: int(x[2]))
        
        return [func(person) for person in people]
    
    return wrapper


@person_lister
def name_format(person):
    if person[3] == "M":
        title = "Mr. "
    else:
        title = "Ms. "
        
    return title + person[0] + " " + person[1]

n = int(input())
people = [input().split() for _ in range(n)]
print(people)

result = name_format(people)

# Printing output
for name in result:
    print(name)
