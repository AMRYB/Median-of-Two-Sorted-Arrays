# MEDIAN OF TWO SORTED ARRAYS

## Non-Recursive Algorithm: MedianOfTwo

```python
MedianOfTwo(arr1, arr2):
1. Initialize:
   med1 ← 0, med2 ← 0
   len1 ← length(arr1), len2 ← length(arr2)
   i ← 0, j ← 0

2. For count ← 0 to (len1 + len2) // 2:
   3. Update med2 ← med1
   4. If i != len1 and j != len2:
        5. If arr1[i] < arr2[j]:
            6. Update med1 ← arr1[i]
            7. Increment i ← i + 1
        8. Else:
            9. Update med1 ← arr2[j]
            10. Increment j ← j + 1
   11. Else If i < len1:
        12. Update med1 ← arr1[i]
        13. Increment i ← i + 1
   14. Else:
        15. Update med1 ← arr2[j]
        16. Increment j ← j + 1

17. If (len1 + len2) % 2 == 0:
    18. Return (med1 + med2) / 2

19. Else:
    20. Return med1
```
