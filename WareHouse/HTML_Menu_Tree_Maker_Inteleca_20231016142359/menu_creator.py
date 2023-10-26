'''
This module creates a nested menu based on the categorized data.
'''
import tkinter as tk
from tkinter import ttk
def create_menu(categorized_data):
    # Create the root window
    root = tk.Tk()
    
    # Create the menu
    menu = tk.Menu(root)
    root.config(menu=menu)
    
    # Create the submenus
    for category, items in categorized_data.items():
        submenu = tk.Menu(menu)
        menu.add_cascade(label=category, menu=submenu)

        added_items = set()  # Set to keep track of items already added

        for item in items:
            series_name = item['Series']
            
            if series_name not in added_items:  # If item is not already added, add it
                submenu.add_command(label=series_name)
                added_items.add(series_name)  # Add the item to the set

    # Start the main loop
    root.mainloop()