# Public Data Collector

A Python application that collects publicly available user data from a REST API and saves it to a CSV file.

## Features

- Connects to a REST API
- Collects user information
- Saves data to CSV
- Searches collected data
- Handles API connection errors
- Uses a simple command-line menu

## How to Run

Install the required package:

    python -m pip install requests

Run the program:

    python data_collector.py

## Menu

    1. Collect users
    2. Search users
    3. Exit

## Technologies Used

- Python
- Requests
- REST API
- CSV
- File handling

## Project Structure

- `data_collector.py` — Main application
- `users.csv` — Collected data
- `README.md` — Project documentation

## Future Improvements

- Add more API sources
- Add advanced filtering
- Export to Excel
- Add a graphical interface
- Add data visualization