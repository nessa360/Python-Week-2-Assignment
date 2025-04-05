# Python function to manage a list as described

def manage_list():
    # Create an empty list
    my_list = []
    
    # Append elements to my_list
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    my_list.append(40)
    
    # Insert the value 15 at the second position
    my_list.insert(1, 15)
    
    # Extend my_list with another list: [50, 60, 70]
    my_list.extend([50, 60, 70])
    
    # Remove the last element from my_list
    my_list.pop()
    
    # Sort my_list in ascending order
    my_list.sort()
    
    # Find and print the index of the value 30 in my_list
    print("Index of 30:", my_list.index(30))
    
    # Return the final list after all operations
    return my_list

# Call the function and print the final list
final_list = manage_list()
print("Final list:", final_list)