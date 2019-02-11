def maxSequence(arr):

    max_so_far =arr[0]
    curr_max = arr[0]

    for i in range(1,len(arr)):
        curr_max = max(arr[i], curr_max + arr[i])
        max_so_far = max(max_so_far,curr_max)

    return max_so_far
mylist = raw_input('Enter your list: ')
mylist = [int(x) for x in mylist.split(',')]
total = 0    
for number in mylist:    
    total += number   
print "Maximum synexomeno sum einai" , maxSequence(mylist)
