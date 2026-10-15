
# Surabaya Concert Ticket System

A console-based concert ticket management system built with Python.

## Features

- Display concert ticket categories, prices, and stock
- Collect customer information
- Purchase multiple ticket types
- Calculate purchase totals
- Select a payment method (simulation only)
- Cancel purchased tickets
- Restore ticket stock after cancellation
- View vendor dashboard
- Calculate revenue, operational costs, net profit, and profit margin

## Ticket Categories

| Ticket Type | Price | Initial Stock |
|---|---:|---:|
| VIP | Rp1,000,000 | 1,000 |
| VVIP | Rp2,000,000 | 500 |
| Regular | Rp50,000 | 2,000 |
| Student | Rp45,000 | 1,500 |

## Requirements

- Python 3
- No third-party packages required

## How to Run

1. Install Python 3.
2. Open the project folder in VS Code.
3. Open the integrated terminal.
4. Run the Python file:

   `python nama_file_python_kamu.py`

   Replace the filename with your actual Python filename.

## How to Use

1. Open the Customer Dashboard to enter customer details and purchase tickets.
2. Choose a ticket category and quantity.
3. Select a payment method.
4. Use Cancel Order to cancel tickets previously purchased in the current session.
5. Open Vendor Dashboard to view sales and financial summaries.
6. Select Exit to close the program.

## Notes

- This project is an educational console simulation.
- Payments are not processed by a real payment provider.
- Ticket stock, cart data, and sales totals are stored in memory and reset when the program exits.
- Do not enter real payment-card details or sensitive personal information.
- The vendor dashboard asks for operational costs when opened.

## Project Structure

- Python source file: main program
- `README.md`: project documentation
- `.gitignore`: excludes selected files from Git
- `requirements.txt`: dependency information

## License

No license has been specified yet.
