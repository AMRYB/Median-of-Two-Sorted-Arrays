def median_of_two(arr1, arr2):
    med1 = 0
    med2 = 0

    len1 = len(arr1)
    len2 = len(arr2)

    i = 0
    j = 0

    for count in range((len1 + len2) // 2 + 1):
        med2 = med1
        if i != len1 and j != len2:
            if arr1[i] < arr2[j]:
                med1 = arr1[i]
                i += 1
            else:
                med1 = arr2[j]
                j += 1
        elif i != len1:
            med1 = arr1[i]
            i += 1

        else:
            med1 = arr2[j]
            j += 1

    if (len1 + len2) % 2 == 0:
        return (med1 + med2) / 2
    else:
        return med1


arr1 = [7,6,2,9,1]
arr2 = [3,5]

print(median_of_two(arr1,arr2))