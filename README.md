# VulnScan

VulnScan is a simple command-line application for user registration and login. It uses MongoDB for storing user data and pyfiglet for displaying a welcome message.

## Features

- User Registration
- User Login
- Welcome Message

## Requirements

- Python 3.x
- MongoDB
- Required Python packages (listed in `requirement.txt`)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/VulnScan.git
    cd VulnScan
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirement.txt
    ```

3. Ensure MongoDB is running on `localhost:27017`.

## Usage

Run the application:
```sh
python main.py
```

## Project Structure

```markdown
main.py
modules/
    __init__.py
    __pycache__/
    db.py
    register.py
    welcome.py
README.md
requirement.txt
```

Feel free to modify the content as needed.