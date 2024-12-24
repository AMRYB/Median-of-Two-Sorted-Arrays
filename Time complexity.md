# MEDIAN OF TWO SORTED ARRAYS

## Non-Recursive Algorithm: MedianOfTwo

```
MedianOfTwo(arr1, arr2):
1. Initialize:
   med1 ← 0, med2 ← 0                            -----> O(1)
   len1 ← length(arr1), len2 ← length(arr2)
   i ← 0, j ← 0

2. For count ← 0 to (len1 + len2) // 2:         -----> O(n/2) ≈ O(n)
   3. Update med2 ← med1                        -----> O(1)
   4. If i != len1 and j != len2:
        5. If arr1[i] < arr2[j]:
            6. Update med1 ← arr1[i]
            7. Increment i ← i + 1              -----> O(1)
        8. Else:
            9. Update med1 ← arr2[j]
            10. Increment j ← j + 1             -----> O(1)
   11. Else If i < len1:
        12. Update med1 ← arr1[i]
        13. Increment i ← i + 1                 -----> O(1)
   14. Else:
        15. Update med1 ← arr2[j]
        16. Increment j ← j + 1                 -----> O(1)

17. If (len1 + len2) % 2 == 0:
    18. Return (med1 + med2) / 2                -----> O(1)
19. Else:
    20. Return med1                             -----> O(1)
```

---

### **Analysis of the `MedianOfTwo` Algorithm**

#### **1. Initialization (Step 1):**

* Variables `med1`, `med2`, `len1`, `len2`, `i`, `j` are initialized.
* **Time Complexity:** O(1)

---

#### **2. For Loop (Steps 2–16):**

* Loop runs from `count = 0` to `(len1 + len2) // 2`
  Let `n = len1 + len2`
* Loop executes about **n/2 iterations**

##### Inside Each Iteration:

* **Step 3:** Assigning `med2 ← med1` → O(1)
* **Step 4–10:**

  * Compare `arr1[i]` and `arr2[j]`
  * Assign new value to `med1`
  * Increment appropriate pointer → O(1)
* **Step 11–16:**

  * If one array is exhausted, take value from the other → O(1)

**Total Loop Time Complexity:**
→ O(n/2) = **O(n)**

---

#### **3. Final Check (Steps 17–20):**

* Check if `(len1 + len2)` is even or odd
* Return average or single value accordingly
* Both operations take **O(1)** time

---

### **Overall Time Complexity**

Let `n = len1 + len2`

| Step                    | Time Complexity |
| ----------------------- | --------------- |
| Initialization          | O(1)            |
| For Loop                | O(n)            |
| Final Conditional Check | O(1)            |
| **Total**               | **O(n)**        |