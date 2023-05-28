
class checkSum:
    def checkIfSumIsAqcuired(arr, k):
        for i in arr:
            for j in arr:
                if i + j == k:
                    return [i, j]

class Main:
    k = input("Welcome user! Please enter a random digit to begin: ");
    print("You entered: " + k);
    print("............");
    arr = [int(i) for i in input("Please enter an array of 6 digits separated by commas:").split(',')];

    while len(arr) != 6:
        print("Invalid array input, Try again!");
        arr = [int(i) for i in input("Please enter an array of 6 digits separated by commas:").split(',')];
        if len(arr) == 6:
            break;
   
    print(f'Lets see if the array numbers {arr} you gave me can sum to the given {k} value you entered.');

    result = checkSum.checkIfSumIsAqcuired(arr, int(k));

    if result:
        print(f'True: {result[0]} + {result[1]} is equal to {k}.')
    else:
        print(f'False: none of the array numbers match {k}.')




   
    
    
