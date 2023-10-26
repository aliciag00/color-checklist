checklist = list()
checklist.append('Blue')
print(checklist)
checklist.append('Orange')
print(checklist)

# CREATE
def create(item):
    # Create item code here
    checklist.append(item)
    
def read(index):
    # Read code here
    return checklist[index]

# UPDATE
def update(index, item):
    # Update code here
    checklist[index] = item

# DESTROY
def destroy(index):
    # Destroy code here
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

# def mark_completed(index):

def select(function_code):

    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    elif function_code == "R": 
        item_index = int(input("Index Number?"))

        read(item_index)

    elif function_code == "P":
        list_all_items()

    elif function_code == "P":
        list_all_items()

    else: 
        print("Unknown Option")
        return True

def user_input(prompt):

    user_input = input(prompt)
    return user_input

def test():
    create("purple sox")
    create("red cloak")

test()
running = True
while running:
    selection = user_input(
        "Press C to add to list , R to Read, P to display list, and Q to quit")
    select(selection)



