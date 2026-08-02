# Coffee Shop Ordering System (Python) 

This is a simple command-line coffee shop ordering system I built in Python to practice working with **dictionaries, loops, and functions**. You can browse a menu, add items to your cart, view your cart, and check out with a final receipt.

I made this project as a beginner to practice handling user input and building a simple shopping cart flow.

## What it does?

- Shows a menu of coffee items with prices
- Lets you pick an item and enter how many you want
- Adds items to a cart and keeps a running total
- Lets you view your cart at any time before checking out
- Prints a final receipt with all items and the total price when you're done

## What I learned / used :

- Python basics (functions, loops, if-else, input/output)
- Dictionaries to store menu items and prices
- Lists to build and manage a shopping cart
- Input validation (making sure quantity entered is a valid positive number)
- Formatted string output (`f-strings`) for clean menu and receipt printing

## How to run it :

1. Make sure Python 3 is installed
2. Download/clone this project
3. Run this command in your terminal:

```bash
python pjt2.py
```

4. Pick an item number from the menu, enter a quantity, and repeat as needed
5. Choose option `6` anytime to view your cart, or `0` to checkout and see your receipt

## Example


*** COFFEE SHOP MENU ***
1. Cortadito - ₹250.00
2. Greek Frappé - ₹300.00
3. Latte - ₹350.00
4. Cappuccino - ₹350.00
5. Frappé - ₹400.00
6. View Cart
0. Checkout & Exit
********************
Enter your choice: 3
How many Latte(s)? 2
Added 2 x Latte to your cart. (₹700.00)


## Things I want to improve later

- Save orders to a file so past orders aren't lost when the program closes
- Let users remove items from their cart before checkout
- Add discounts or offers
- Turn this into a small GUI app instead of a command-line one

## Made by

Abhishek Seishiro — this was one of my early Python practice projects 
[GitHub](https://github.com/Abhishek-Seishiro)
