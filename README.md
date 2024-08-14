# Random Password Generator

## Overview

The **Random Password Generator** is a Python-based tool that generates secure, random passwords. This tool allows users to create passwords of varying lengths and complexity, ensuring the security of accounts and sensitive data.

## Features

- Generate random passwords with a specified length.
- Include or exclude letters, numbers, and special characters.
- Easily customizable to meet different security requirements.
- User-friendly command-line interface.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/random-password-generator.git

   
2.Navigate to the project directory:
  

      cd random-password-generator '/'


###Usage
1.Run the script:

python password_generator.py

2.Follow the on-screen prompts:

Enter the desired password length.
Specify whether to include letters, numbers, and special characters.

3.The generated password will be displayed on the screen.

Example

python password_generator.py
Enter desired password length: 12
Include letters? (y/n): y
Include numbers? (y/n): y
Include special characters? (y/n): y

Generated Password: a8#sG@k2V9hJ


Customization
You can customize the script by modifying the options for character sets in the password_generator.py file:
```bash

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
special_chars = '!@#$%^&*()-_=+[]{}|;:,.<>?'
