from datetime import datetime, timedelta

tickets = [
    {"jenis": "VIP", "harga": 1000000, "stok": 1000},
    {"jenis": "VVIP", "harga": 2000000, "stok": 500},
    {"jenis": "Regular", "harga": 50000, "stok": 2000},
    {"jenis": "Student", "harga": 45000, "stok": 1500}
]
total_penjualan = 0
total_pembatalan = 0
keranjang  = {}

def data_customer():
    while True:
        try:
            name = input('enter your name:')
            while name == '':
                print('please enter your name')
                name = input('enter your name:')

            age = int(input('enter your age:'))
            if age <= 0:
                raise ValueError

            email = input('enter your email:')
            while email == '' or '@' not in email or '.' not in email:
                print('please enter your valid email')
                email = input('enter your email:')

            phone = int(input('enter your phone number:'))
            if phone <= 0:
                raise ValueError

            print(f"Name: {name}, Age: {age}, Email: {email}, Phone: {phone}")
            return
        except ValueError:
            print("Invalid input. Please enter the correct data types.")

def dashboard():
    print('welcome to the Surabaya Concert')
    print("Available Tickets:")
    for item, tiket in enumerate(tickets, start=1):
        print(f"{item}. {tiket['jenis']} - Harga: {tiket['harga']} - Stok: {tiket['stok']}")

def proses_pembelian():
    global total_penjualan
    orders = []
    total_pembelian = 0
    while True:
        try:
            ticket_choice = int(input("Select ticket type (1-4) or 0 to finish: "))
            if ticket_choice == 0:
                break
            if ticket_choice < 1 or ticket_choice > 4:
                print("Invalid choice. Please select a valid ticket type.")
                continue
            selected_ticket = tickets[ticket_choice - 1]
            print(f"You selected {selected_ticket['jenis']} ticket.")

            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue
            if quantity > int(selected_ticket['stok']):
                print(f"Insufficient stock. Only {selected_ticket['stok']} tickets available.")
                continue

            orders.append((ticket_choice, quantity))
            keranjang[ticket_choice] = keranjang.get(ticket_choice, 0) + quantity
            selected_ticket['stok'] -= quantity
            total_pembelian += selected_ticket['harga'] * quantity
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        print('1. transfer via virtual account')
        print('2 . transfer via e-wallet')
        print('3. debit card')
        print('4. credit card')
        try:
            method = int(input("Select payment method (1-4): "))
            if method == 1:
                print("You selected transfer via virtual account.")
                no_va = int(input("Enter your virtual account number: "))
                print(f"Your virtual account number is: {no_va}")
            elif method == 2:
                print("You selected transfer via e-wallet.")
                no_rek = int(input("Enter your e-wallet number: "))
                print(f"Your e-wallet number is: {no_rek}")
            elif method == 3:
                print("You selected debit card.")
                number_card = int(input("Enter your debit card number: "))
                print(f"Your debit card number is: {number_card}")
            elif method == 4:
                print("You selected credit card.")
                card_number = int(input("Enter your credit card number: "))
                print(f"Your credit card number is: {card_number}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    print("Selected Tickets:")
    for ticket_choice, quantity in orders:
        selected_ticket = tickets[ticket_choice - 1]
        print(f"- {selected_ticket['jenis']}: {quantity} pcs")
        print(f"Total Price: {selected_ticket['harga'] * quantity}")
        print(datetime.now().strftime("Date: %Y-%m-%d Time: %H:%M:%S"))
        print("Payment successful")
        print("Your ticket has been sent to your email.")
        print("Thank you for your purchase! Enjoy the concert.")

    total_penjualan += total_pembelian
    print("\nSisa stok setelah pembelian/penjualan:")
    for tiket in tickets:
        print(f"- {tiket['jenis']}: {tiket['stok']} tiket")

def cancel_order():
    global total_penjualan, total_pembatalan
    while True:
        try:
            cancel_choice = int(input("Enter the ticket type to cancel (1-4) or 0 to finish: "))
            if cancel_choice == 0:
                break
            if cancel_choice < 1 or cancel_choice > 4:
                print("Invalid choice. Please select a valid ticket type.")
                continue
            purchased_quantity = keranjang.get(cancel_choice, 0)
            if purchased_quantity == 0:
                print("Cancellation rejected: this ticket is not in the buyer's cart.")
                continue
            elif cancel_choice == 1:
                print("You selected VIP ticket for cancellation.")
            elif cancel_choice == 2:
                print("You selected VVIP ticket for cancellation.")
            elif cancel_choice == 3:
                print("You selected Regular ticket for cancellation.")
            elif cancel_choice == 4:
                print("You selected Student ticket for cancellation.")
            cancel_quantity = int(input("Enter quantity to cancel: "))
            if cancel_quantity <= 0:
                print("Quantity must be greater than zero.")
                continue
            if cancel_quantity > purchased_quantity:
                print(f"Cancellation rejected: you only bought {purchased_quantity} ticket(s) of this type.")
                continue
            else:
                selected_ticket = tickets[cancel_choice - 1]
                refund = selected_ticket['harga'] * cancel_quantity
                selected_ticket['stok'] += cancel_quantity
                keranjang[cancel_choice] -= cancel_quantity
                total_pembatalan += refund
                print(f"Cancelled {cancel_quantity} pcs of ticket type {cancel_choice}.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")


def vendor_dashboard():
    global total_pembatalan
    total_sisa_stok = sum(tiket['stok'] for tiket in tickets)
    biaya_operational = int(input("Enter operational costs: "))
    total_pendapatan = total_penjualan - total_pembatalan
    net_profit = total_pendapatan - biaya_operational
    margin = (net_profit / total_pendapatan) * 100 if total_pendapatan > 0 else 0

    print(f"Total Penjualan: {total_penjualan}")
    print(f"Total Sisa Stok: {total_sisa_stok} tiket")
    print("Sisa stok per jenis tiket:")
    for tiket in tickets:
        print(f"- {tiket['jenis']}: {tiket['stok']} tiket")
    print(f"Total Pendapatan: {total_pendapatan}")
    print(f"Net Profit: {net_profit}")
    print(f"Biaya Operational: {biaya_operational}")
    print(f"Cancel Revenue: {total_pembatalan}")
    print(f"Margin: {margin}%")

def route():
    while True:
        print("Welcome to the Concert Ticket System")
        print("1. Customer Dashboard")
        print("2. Cancel Order")
        print("3. Vendor Dashboard")
        print("4. Exit")
        try:
            choice = int(input("Select an option (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            data_customer()
            dashboard()
            proses_pembelian()
            while True:
                print('1. order ticket lagi')
                print('2. Back to menu')
                try:
                    sub_choice = int(input("Select an option (1-2): "))
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 2.")
                    continue
                if sub_choice == 1:
                    proses_pembelian()
                    continue
                elif sub_choice == 2:
                    break
                else:
                    print("Invalid choice. Please select a valid option.")
        elif choice == 2:
            cancel_order()
            while True:
                print('1. cancel ticket lagi')
                print('2. Back to menu')
                try:
                    sub_choice = int(input("Select an option (1-2): "))
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 2.")
                    continue
                if sub_choice == 1:
                    cancel_order()
                    continue
                elif sub_choice == 2:
                    break
                else:
                    print("Invalid choice. Please select a valid option.")
        elif choice == 3:
            vendor_dashboard()
            while True:
                print('1. Back to menu')
                try:
                    sub_choice = int(input("Select an option (1): "))
                except ValueError:
                    print("Invalid input. Please enter 1 to go back to the menu.")
                    continue
                if sub_choice == 1:
                    break
                else:
                    print("Invalid choice. Please select a valid option.")
        elif choice == 4:
            print("Exiting the system. Goodbye!")
            return
        else:
            print("Invalid choice. Please select a valid option.")

route()
