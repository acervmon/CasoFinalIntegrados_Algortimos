import os
import platform
import re

def clear_screen():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')

def read_text(min_length=0, max_length=100, message=None):
    print(message) if message else None
    while True:
      text = input("> ")
      if len(text) >= min_length and len(text) <= max_length:
         return text

def valid_dni(dni, customer_list):
    if not re.match('[0-9]{2}[A-Z]$', dni):
      print("Invalid DNI, it must follow the specified format.")
      return False
    for customer in customer_list:
      if customer.dni == dni:
         print("DNI already used by another customer.")
         return False
    return True
