# Swapping of 2 nos


def main():
    print ('Enter the 1st number :')
    num1 = int(input())
    print('Enter the 2nd number :')
    num2 = int(input())
    print('-'*30)
    print('Before swap   a= %s  b=%s ' %(num1,num2))
    #Swapping starts here
    temp = num1
    num1 = num2
    num2 = temp
    print('-' * 30)
    print('After swap   a= %s  b=%s ' % (num1, num2))
    print('-' * 30)
if __name__ == "__main__":
    main()

