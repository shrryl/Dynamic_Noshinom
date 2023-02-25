# iNTUition_Noshinom
iNTUition Hackathon v9.0 Open Track

# Objective 
Our idea is a dynamic pricing system that will **incentivise consumers to purchase perishable good with shorter shelf-life**.
This contributes to the food waste efforts on a consumer and retail level.

## Consumer Behaviour
Consumers tend to take the goods with the longest expiration date, just so they have a longer time on the shelf, even if it's just a few days.
They are also incredibly price-sensitive, looking out for discounts with reasonable quality.

However, when it comes to perishables, even with enticing discounts slapped on top, no one really wants that 2-day-old chicken thigh, or that loaf of bread with only 3 days of shelf life left.
We intend to alter that behaviour. 

## Our Goal
We motivate consumers with dynamic discounts, changing every few hours in the day, instead of at the end of day. 
We want consumers to choose those items, and start thinking and planning what they buy and eat.

# Product
These price tags are to be used in supermarkets or anywhere that sells perishable goods, with **algorithms** that automatically update prices on each tag.

## Breakdown
- (Cloud) Database for real-time changes
- Price tags with Wi-Fi / BlueTooth connection

This is a diagram of how dynamic price tags will work ![pricetag_diagram](pricetag_diagram.jpg)

## Our Code
This repository contains 
1. [pricetag_display.ino](pricetag_display.ino/pricetag_display.ino.ino) - mock Arduino code that programs an LCD display
- Watch this [video demo](https://youtu.be/EqCVVbBfOiI)

2. [main.py](main.py) - runs our mock database in Google Firebase

![diagram](firebase_example.jpg)

It has 2 main functions
- `uploadPrice()` - to allow the user to add new prices based on import date for new product batches
- `changePrice()` - to allow the user to edit said prices
To be included: algorithm with parameters to adjust prices automatically 


