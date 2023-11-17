def print_array(n):
    array = ''
    for i in range(1, n+1):
        array = array + str(i)
    print(array)
		
if __name__ == '__main__':
    n = int(input())
    print_array(n)