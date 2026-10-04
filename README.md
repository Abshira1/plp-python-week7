# Week 7 Assignment: Shopping List Manager

- list_warmup.py – practises list indexing, append, remove and len.
- shopping_list.py – menu-driven shopping list (add/remove/show/done).
- list_report.py – numbers items, counts long names, finds the longest.
- screenshots/ – screenshots of each program running.

## Why check `in` before `.remove()`?
`.remove()` raises a ValueError if the item isn't in the list, which
crashes the program. Checking with `in` first lets us print a friendly
message instead, so the program keeps running.