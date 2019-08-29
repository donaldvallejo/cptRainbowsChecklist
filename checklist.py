
checklist = list()

# def my_fun_function(say_this):
#     print(say_this)

# checklist = list()
# checklist.append('Blue')
# print(checklist)
# checklist.append('Orange')
# print(checklist)

# #CREATE
# def create(item):
#     checklist.append(item)

# #READ
# def read(index):
#     item = checklist[index]
#     return item

# checklist = ['Blue', 'Orange']
# checklist[1] = 'Cats'
# print(checklist)

# #UPDATE
# def update(index, item):
#     checklist[index] = item

# checklist = ['Blue', 'Cats']
# checklist.pop(1)
# print(checklist)

# #DESTROY
# def destroy(index):
#     checklist.pop(index)



checklist = list()
checklist.append("purple socks")


def create(item):
    checklist.append(item)

def read(index):
    item = checklist[index]
    return item

def update(index, item):
    # checklist = ['purple socks']
    checklist[index] = item

def destroy(index):
    checklist.pop()

def list_all_items():
    index = 0
    for list_item in checklist:
        # print("{} {}".format(index, list_item))
        print(str(index) + " " + list_item)
        index += 1

def mark_completed(index):
    mark = "√"
    completed = mark + " " + checklist[index] 
    update(index, completed)
    
def user_input(prompt):
    user_input = input(prompt)
    return user_input

def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item: ")
        # print("C was clicked")
        create(input_item)
        return True
    elif function_code == "R":
        item_index = int(user_input("Index Number? "))
        # print("R was clicked")
        read(item_index)
        destroy(item_index)
        return True
    elif function_code == "P":
        # print("P was clicked")
        list_all_items()
        return True
    elif function_code == "complete":
        item_index = int(user_input("which items are complete? "))
        mark_completed(item_index)
        return True
    elif function_code == "Q":
        # print("Q was clicked")
        return False
    else:
        print("Unknown Option")


def test():
        create("purple sox")
        create("red cloak")

print(read(0))
# print(read(1))

update(0, "purple socks")

print(read(0))
# print(read(1))

list_all_items()

 # Call your new function with the appropriate value
select("C")
    # View the results
list_all_items()
    # Call function with new value
select("R")
    # View results
list_all_items()

# mark_completed()

test()
    
def loop():
    running = True
    while running:
      selection = user_input(
        "Press C to add to list, R to Read from list, P to display list, complete to display checked items and Q to quit ")
      running = select(selection)
      continue

loop()
print("end")
