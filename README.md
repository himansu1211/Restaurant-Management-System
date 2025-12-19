# Restaurant Management System

A comprehensive Python-based GUI application for managing restaurant billing and orders. Built using Tkinter, this system allows users to select food and drink items, calculate totals, generate receipts, and perform basic calculations.


**Note:** This is a desktop GUI application designed to run locally on Windows, macOS, or Linux systems. It is not a web application and cannot be deployed to web platforms like Heroku, GitHub Pages, or web servers. Attempting to deploy it as a web app will result in errors such as "404 page not found" because Tkinter requires a local desktop environment to display the GUI.

## Features

- **Menu Management**: Select from a variety of drinks (Cocktail, Iced Tea, Hot Chocolate, etc.) and Filipino dishes (Fried Chicken, Kare Kare, Crispy Pata, etc.)
- **Quantity Input**: Enter quantities for selected items
- **Automatic Calculations**: Compute subtotals, taxes, service charges, and total costs
- **Receipt Generation**: Generate detailed receipts with order reference numbers
- **Built-in Calculator**: Perform basic arithmetic operations
- **Reset Functionality**: Clear all selections and start fresh
- **User-Friendly GUI**: Intuitive interface with checkboxes, entry fields, and buttons

## Requirements

- Python 3.x
- Tkinter (usually included with Python installations)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/restaurant-management-system.git
   cd restaurant-management-system
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies (if any additional packages are needed in the future):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python restaurant_billing.py
   ```

2. Select desired drinks and food items by checking the boxes
3. Enter quantities in the corresponding entry fields
4. Click "Total" to calculate costs
5. Click "Receipt" to generate a receipt
6. Use the built-in calculator for any additional calculations
7. Click "Reset" to clear all selections
8. Click "Exit" to close the application

## Menu Items and Prices

### Drinks
- Cocktail: ₱50
- Iced Tea: ₱45
- Hot Chocolate: ₱60
- Orange Juice: ₱35
- Milk Shake: ₱70
- Mountain Dew: ₱40
- Sting: ₱55
- Cobra: ₱75

### Foods
- Fried Chicken: ₱490
- Kare Kare: ₱450
- Crispy Pata: ₱350
- Sinigang Baboy: ₱400
- Sinigang Hipon: ₱500
- Bicol Express: ₱250
- Asparagus Tofu: ₱650
- Chicken Sisig: ₱370

## Tax and Charges

### Service Charge
- **Amount**: ₱1.59 (fixed per order)
- **Description**: A standard service charge applied to every bill regardless of order size or total amount.
- **Purpose**: Covers operational costs and staff service fees.

### Tax
- **Rate**: 15% (VAT - Value Added Tax)
- **Calculation**: Applied to the subtotal, which includes the total cost of food, drinks, and service charge.
- **Formula**: Tax = (Subtotal) × 0.15
- **Subtotal Calculation**: Subtotal = (Total Drinks + Total Foods) + Service Charge

### Total Cost Breakdown
The final total cost is calculated as follows:
1. Calculate individual item totals based on quantity and unit price
2. Sum all drink costs and food costs separately
3. Add the fixed service charge (₱1.59)
4. Calculate tax as 15% of the subtotal (drinks + foods + service charge)
5. Final Total = Subtotal + Tax

**Example Calculation**:
- Drinks: 2 Cocktails (₱50 each) = ₱100
- Foods: 1 Fried Chicken (₱490) = ₱490
- Subtotal: ₱100 + ₱490 + ₱1.59 = ₱591.59
- Tax (15%): ₱591.59 × 0.15 = ₱88.74
- Total Cost: ₱591.59 + ₱88.74 = ₱680.33

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with Python and Tkinter
- Inspired by restaurant management needs
