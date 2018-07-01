def insertion_sort(sortable):
    for unsorted_location in range(1,len(sortable)):
        for possible_destination in range(unsorted_location-1, -1, -1):
            if(sortable[unsorted_location] >= sortable[possible_destination]):
                # insert after this location
                insert(sortable, possible_destination + 1, unsorted_location)
                break

def insert(in_list, destination_index, source_index):
    in_list.insert(destination_index, in_list[source_index])
    in_list.pop(source_index + 1)


