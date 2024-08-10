
# Local File Inclusion (LFI) Vulnerability Demonstration

This project demonstrates the concept and exploitation of Local File Inclusion (LFI) vulnerabilities in web applications. The repository contains a simple web application vulnerable to LFI, which can be used for educational and testing purposes.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Security Warning](#security-warning)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Local File Inclusion (LFI) is a type of security vulnerability in web applications that allows an attacker to include files from the server in the application. This project provides a controlled environment to understand and experiment with LFI vulnerabilities, enabling developers and security enthusiasts to learn how to detect and mitigate such issues.

## Features

- Demonstrates LFI vulnerability exploitation.
- Provides a simple vulnerable web application for testing.
- Educational resource for learning about web security.

## Requirements

- Python 3.x
- Flask
- Git

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/arifbinekram/Local-File-Inclusion.git
   cd Local-File-Inclusion
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your web browser and navigate to `http://localhost:5000` to access the application.

## Usage

Once the application is running, you can explore the LFI vulnerability by manipulating URL parameters to include files from the server. Use this environment to test various LFI scenarios and understand the risks associated with file inclusion vulnerabilities.

### Examples

To demonstrate an LFI attack, try accessing different files using the `page` parameter in the URL, such as:

- `http://localhost:5000/?page=../../../../etc/passwd`
- `http://localhost:5000/?page=../../../../var/log/apache2/access.log`

**Note**: These examples are for educational purposes only and should not be used to attack any real-world systems.

## Security Warning

This project is intended for educational and testing purposes only. It is highly recommended not to deploy this application on any production server or expose it to the internet. Use it in a controlled, local environment to avoid potential security risks.

## Contributing

Contributions are welcome! If you have suggestions, bug fixes, or improvements, feel free to submit a pull request or open an issue in the repository.

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add new feature or fix'
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request and describe your changes.

### Notes:

- Ensure that the URLs and examples match the actual implementation in the project.
- Include any additional instructions or notes that might be specific to the project setup or usage.
- Make sure to update the contributing section if there are specific guidelines for contributing to the project.
