# creating an empty list

my_list = []

# introducing a second list
second_list = ["50", "60", "70"]

# adding values to the first list using the append command

my_list.append("10")
my_list.append("20")
my_list.append("30")
my_list.append("40")

# inserting an item into my_list using the insert command

my_list.insert(1, "15")

# adding the second_list to my_list using the extend command
my_list.extend(second_list)

# removing last item and sorting in ascending order
my_list.pop()
my_list.sort

# finding and printing '30' 
print(my_list[3])