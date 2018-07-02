def insertion_sort(sortable):
    for unsorted_item_index in range(1,len(sortable)):
        for possible_destination in range(unsorted_item_index-1, -1, -1):
            if(sortable[possible_destination+1] < sortable[possible_destination]):
                sortable[possible_destination], sortable[possible_destination+1] = sortable[possible_destination+1], sortable[possible_destination]
            else:
                break
