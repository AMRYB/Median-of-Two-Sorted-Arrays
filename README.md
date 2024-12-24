## 📌 About the Project

The objective of this project is to **find the median** of two **sorted arrays** without fully merging them. This is a common algorithmic problem, especially in interview settings, where **optimal performance** is expected.

The implemented solution uses a **non-recursive, linear-time approach** that tracks only the necessary elements to determine the median efficiently.

---

## ⚙️ System Workflow

### 🔁 Iterative Logic

1. Use two pointers `i` and `j` to iterate over `arr1` and `arr2`.
2. At each step, select the smaller element and update the variables `med1` and `med2`.
3. Repeat until reaching the middle index of the combined length.
4. Return:

   * `med1` if the total number of elements is odd.
   * `(med1 + med2) / 2` if the total number of elements is even.

---

## 🗃️ Project Files Overview

| File Name            | Description                                                           |
| -------------------- | --------------------------------------------------------------------- |
| `Main.py`            | Contains the main function `median_of_two()` and test arrays.         |
| `Pseudocode.md`      | Structured pseudocode version of the algorithm logic.                 |
| `Code analysis.md`   | Explains how the algorithm works with examples and key observations.  |
| `Time complexity.md` | Time complexity analysis and breakdown of each step in the algorithm. |

---

## 🧪 Sample Input & Output

### Example 1 (Odd total):

```python
arr1 = [1, 2, 6, 9, 13]
arr2 = [3, 5, 14, 17]

# Combined sorted: [1, 2, 3, 5, 6, 9, 13, 14, 17]
# Output: 6
```

### Example 2 (Even total):

```python
arr1 = [1, 2]
arr2 = [3, 5, 6, 9]

# Combined sorted: [1, 2, 3, 5, 6, 9]
# Output: (3 + 5) / 2 = 4.0
```

---

## 🧠 Key Features

* ✅ Supports **both even and odd** array lengths.
* 📉 **No full merge** of arrays required.
* ⏱️ Runs in **O(n)** time where n = total number of elements.
* 🧮 Simple, readable logic.
* 📄 Pseudocode and analysis files included for educational use.

---

## 🛠️ How to Run the Project

1. Ensure **Python 3.x** is installed.
2. Clone or download the repository files.
3. (Optional) Sort input arrays before calling the function, as the algorithm assumes sorted input.
4. Run the main script:

```bash
python Main.py
```

---

## 👨‍💻 Team Members

**Project Leader:** Amr Yasser Badr

**Team Members:**

* Youssef Mahmoud Younes
* Sama Saeed El-Fishawy
