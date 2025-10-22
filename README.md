# 🧩 LZ77 Data Compression Algorithm

## 📌 Introduction
The **LZ77 Data Compression Algorithm** is a Python program that demonstrates **lossless data compression** using the **Lempel–Ziv 1977** technique.  
It compresses text by finding repeated patterns and replacing them with short references, allowing the original data to be restored perfectly.  

This project was made as part of a **Information Theory and Data compression** course to apply theoretical concepts in a practical way.

---

## ✨ Key Features
- Performs both **compression** and **decompression**.  
- Uses **tags** in the form `<distance, length, next>` to represent data.  
- Applies a **sliding window** to find repeated sequences.  
- Handles **repetitive text patterns** efficiently.  
- Simple and clear implementation for learning purposes.

---

## 📈 Benefits
- **Lossless compression** – no data is lost.  
- **Handles repetitive data** effectively.  
- **Easy to understand** and good for studying how compression works.  

---

## 🧮 Time Complexity
- **Compression:** O(n²)  
- **Decompression:** O(n)

---

## 🎯 Learning Objectives
- Understand how **lossless compression** works.  
- Learn how to detect and reuse **repeated patterns**.  
