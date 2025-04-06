# HashKey - Hash Tool

HashKey is a command-line tool written in Python that allows users to generate hash values using a variety of algorithms and crack hashes with a wordlist. It supports several hash algorithms like SHA-256, SHA-1, MD5, SHA-384, SHA-512, BLAKE2b, and BLAKE2s. The tool can also attempt to crack hashes using a wordlist.

## Features
- Generate hashes for various algorithms (SHA-256, SHA-1, MD5, SHA-384, SHA-512, BLAKE2b, BLAKE2s).
- Option to save generated hashes to a file (`hash.txt`).
- Crack hashes using a wordlist (`word.txt`).
- Interactive menu for easy navigation.

## Requirements

To run HashKey, you need the following:
- Python 3.x (tested on Python 3.6+)
- `colorama` module for colored output in the terminal

The tool should work on both Linux and Windows systems.

## Installation

Follow these steps to install and run HashKey:

### Step 1: Install Python

Ensure that Python 3.x is installed on your system. You can check if Python is installed by running the following command:

```bash
python --version
If it's not installed, you can download it from the official Python website: https://www.python.org/downloads/

Step 2: Clone the Repository
Clone the HashKey repository to your local machine:

bash
Kopyala
git clone https://github.com/yourusername/HashKey.git
Alternatively, you can download the ZIP file and extract it.

Step 3: Install Required Modules
In the terminal, navigate to the project directory and install the required modules:

bash
Kopyala
cd HashKey
python3 -m pip install -r requirements.txt
Or, if you don't have the requirements.txt file, you can manually install the required module:

bash
Kopyala
python3 -m pip install colorama
This will install the necessary dependencies to run the tool.

Step 4: Run the Tool
Once you've installed the required modules, you can run the tool by executing:

bash
Kopyala
python3 main.py
Step 5: Using HashKey
Upon running the tool, you will be presented with an interactive menu that allows you to:

Select a hash algorithm to generate a hash.

Generate a hash for a word you input.

Save the hash to a file (hash.txt).

Crack a hash using a wordlist (word.txt).

Exit the program.

Example Usage
Generate a Hash:

Select the algorithm (e.g., SHA-256).

Enter a word (e.g., "password").

The program will output the generated hash.

Crack a Hash:

Select the cracking option from the menu.

Enter the hash you want to crack (e.g., 5f4dcc3b5aa765d61d8327deb882cf99 for "password").

Select the algorithm used for generating the hash.

The program will attempt to crack the hash using the word.txt wordlist.

Cracking Hashes with Wordlist
To crack a hash, the program uses a wordlist file called word.txt. If you don't have a wordlist, you can either create your own or find a list online (e.g., from https://github.com/digininja/Wordlist-Collections).

The wordlist must be in plain text format, with one word per line.

Example of word.txt:
nginx
Kopyala
password
123456
letmein
qwerty
Linux Usage
To run HashKey on Linux, follow the same installation steps as above. However, you may need to use python3 instead of python in some commands:

Install dependencies:

bash
Kopyala
python3 -m pip install colorama
Run the tool:

bash
Kopyala
python3 main.py
License
This project is licensed under the MIT License - see the LICENSE file for details.

Disclaimer
Use this tool responsibly. HashKey is intended for educational purposes and ethical use only. Do not use it to crack passwords or hashes without explicit permission.

markdown
Kopyala

### Explanation of Sections:
- **Features**: Lists key features of the tool, including hash generation and cracking.
- **Requirements**: Details the requirements for the tool to run, including Python and necessary modules.
- **Installation**: Provides a step-by-step guide for installing and running the tool.
- **Example Usage**: Describes how the user can generate hashes and crack them using the tool.
- **Linux Usage**: Specific instructions for Linux users, noting the potential need for `python3` instead of `python`.
- **Cracking Hashes**: Details the process of cracking a hash using a wordlist and the file format expected for the wordlist.

This should give users a clear understanding of how to use the tool on both Linux and Windows platforms!


