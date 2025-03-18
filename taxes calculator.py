class TaxCalculator:
    def __init__(self, income, tax_rate):
        self.income = income
        self.tax_rate = tax_rate

    def calculate_tax(self):
        return self.income * self.tax_rate / 100

def main():
    print("Welcome to the Taxes Calculator App!")
    try:
        income = float(input("Please enter your income: "))
        tax_rate = float(input("Please enter the tax rate (in percentage): "))
        
        if income < 0 or tax_rate < 0:
            print("Income and tax rate should be non-negative numbers.")
            return
        
        calculator = TaxCalculator(income, tax_rate)
        tax = calculator.calculate_tax()

        print(f"\nYour calculated tax is: {tax:.2f}")
        print(f"Your income after tax is: {income - tax:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values for income and tax rate.")

if __name__ == "__main__":
    main()
