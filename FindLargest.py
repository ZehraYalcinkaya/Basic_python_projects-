def find_largest(numbers):
    largest = numbers[0]

    for x in numbers:
        if x >largest:
           largest = x
        
    return largest 


integers =[10, 48, 45, 9, 12, 13, 4 ,150, 74 ,26]  
print('The largest number of this list is ', find_largest(integers))        