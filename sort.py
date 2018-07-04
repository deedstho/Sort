def insertion_sort(sortable):
    for unsorted_item_index in range(1,len(sortable)):
        for possible_destination in range(unsorted_item_index-1, -1, -1):
            if(sortable[possible_destination+1] < sortable[possible_destination]):
                sortable[possible_destination], sortable[possible_destination+1] = sortable[possible_destination+1], sortable[possible_destination]
            else:
                break

def shell_sort(sortable):
    gaps = [4095,2047,1023,511,255,127,63,31,15,7,5,3,1]
    for gap in gaps:
        gapped_insertion_sort(sortable, gap)


def gapped_insertion_sort(sortable, gap):
        for unsorted_item_index in range(gap,len(sortable)):
            for possible_destination in range(unsorted_item_index-gap, gap-1, -gap):
                if(sortable[possible_destination+gap] < sortable[possible_destination]):
                    sortable[possible_destination], sortable[possible_destination+gap] = sortable[possible_destination+gap], sortable[possible_destination]
                else:
                    break