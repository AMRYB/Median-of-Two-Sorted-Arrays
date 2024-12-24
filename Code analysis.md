# 🟦 **Problem Statement**

You are given **two sorted arrays**, `arr1` and `arr2`. Your task is to **find the median** when both arrays are **combined** into a single **sorted array**.

---

## 🌟 **Two Cases for Finding the Median**

### 🔹 **Case 1: Odd Total Number of Elements**

If the total number of elements in the combined array is **odd**, the **median** is simply the **middle element**.

**🟢 Input:**
`arr1 = [1, 2, 6, 9, 13]`
`arr2 = [3, 5, 14, 17]`

**🟢 Output:**
`6`

---

### 🔍 **Why 6?**

* Combined array: `[1, 2, 3, 5, 6, 9, 13, 14, 17]`
* Total elements: **9** (odd)
* Middle element: **5th element = 6**

✅ **Median = 6**

---

### 🔹 **Case 2: Even Total Number of Elements**

If the total number of elements is **even**, the **median** is the **average of the two middle elements**.

**🟢 Input:**
`arr1 = [1, 2]`
`arr2 = [3, 5, 6, 9]`

**🟢 Output:**
`4`

---

### 🔍 **Why 4?**

* Combined array: `[1, 2, 3, 5, 6, 9]`
* Total elements: **6** (even)
* Two middle elements: **3rd = 3**, **4th = 5**
* Median = (3 + 5) ÷ 2 = **4**

✅ **Median = 4**

---

### 💡 Note

* The arrays are already sorted — **no need to sort them manually** if you're merging them carefully.
* Efficient solution (without full merge) can be achieved in **O(log(min(n, m)))** time using binary search (advanced version).