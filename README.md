# palindromic-multiples-of-7-sum

# Palindromic Multiples of 7 🔢✨

This Python program calculates the **sum of all numbers from 1 to 50,000** that are:

* divisible by 7
* palindromes (read the same forwards and backwards)

---

## 🚀 What the program does

* Checks if a number is a palindrome
* Checks if a number is divisible by 7
* Filters numbers from 1 to 50,000
* Computes the sum of all valid numbers

---

## 🧠 Concept

A number is included if:

* `n % 7 == 0`
* `str(n) == str(n)[::-1]`

Both conditions must be true.

---

## ▶️ How to run

```bash id="p07"
python main.py
```

---

## 📌 Output

The program prints the sum of all numbers that satisfy both conditions:

```text id="p08"
<result number>
```

---

## 🧩 What I learned

This project helped me practice:

* String manipulation (palindrome checking)
* Modulo operations
* Loop filtering
* Combining multiple conditions
* Writing reusable functions

---

## 🔮 Possible improvements

* Optimize performance using list comprehensions
* Avoid redefining built-in functions like `sum`
* Print the list of valid numbers instead of only the sum
* Allow user-defined range and divisor
