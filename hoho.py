max_row_count , print_count = 1,1
pointer = ord("A") - 1 
while max_row_count < 7  :
    while print_count < max_row_count :
        pointer += 1 
        print(chr(pointer),end="")
        print_count+=1
    print()
    print_count = 1
    max_row_count +=1 
