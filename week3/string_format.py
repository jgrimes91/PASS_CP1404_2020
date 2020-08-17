names = ["Bob", "Bill", "Barbara", "Jane", "Joe", "Jill"]
degree = ["IT", "Law", "Engineering", "IT", "Education", "Arts"]
age = [35, 18, 45, 27, 29, 21]

info_string = "Name = {:15} Degree = {:20} Age = {:5}"
for i in range(0, len(names)):
    print(info_string.format(names[i], degree[i], age[i]))


name = "Bill"
age = 10

print("Hello my name is {} and I am {} years old.".format(name, age))