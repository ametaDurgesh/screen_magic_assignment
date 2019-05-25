def devisible_by_seven(bin_list):
    result = []
    for bin_num in bin_list:
    	int_num = int(bin_num, 2)
    	if not int_num%7:
        	result.append(bin_num)
    return result

bin_list=[bin_num for bin_num in raw_input().split(',')]
result = devisible_by_seven(bin_list)
print(','.join(result))

