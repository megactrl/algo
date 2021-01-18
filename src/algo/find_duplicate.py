def return_dupli(a_list):

  #create an empty list to hold the duplicates
    dup = []
  #crate an empty set
    a_set = set()
  #use a for-loop to step hrough each item in the list
    for item in a_list:

        #get the length of the set
        length_one = len(a_set)
        #add an item from the list into set
        a_set.add(item)
        #check new length of the set
        length_two = len(a_set)

        if length_one == length_two:
            #append the duplicate item to the list of duplicate
            dup.append(item)

    return dup

a_list = ["john","Mark","steve","Tony","Mark"]
dup = return_dupli(a_list)
print(dup)
