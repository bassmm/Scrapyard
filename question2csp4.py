arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

target = int(input("Input target number: "))

def linearSearch(list:list, target:int) -> bool:
    for num in list:
        if target == num:
            return True
    return False




if linearSearch(arrayData, target) == True:
    print(f"The number {target} has been found in the array!")
else:
    print(f"The number {target} was not found in the array.")

def bubbleSort(theArray:list):
    temp = 0
    for x in range(len(theArray)):
        for y in range(len(theArray)-1):
            if theArray[y] < theArray[y+1]:
                temp = theArray[y]
                theArray[y] = theArray[y+1]
                theArray[y+1] = temp
 
bubbleSort(arrayData)

print(f"arrayData in Descending order: {arrayData}")