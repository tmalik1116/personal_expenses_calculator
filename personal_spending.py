import datetime

expenses = {
    
}

# Returns the anticipated total amount I am making this co-op term based on my hourly rate
# Some values are hardcoded (tax amount) because I do not know how to calculate it
def calc_total_earnings(wage_1, wage_2):
    total = (wage_1 * 40 * 16 * 0.82)
    total += (wage_2 * 40 * 16 * 0.85)
    return float(total)

def total_remaining(total, spending):
    return float(total - spending)

def total_expenses(expenses: dict):
    total = 0
    for expense in expenses.values():
        total += expense
    return float(total)

def add_expense(name: str, cost, expenses: dict):
    expenses[name] = cost

def relative_spending(percentage, week: int, weeks: int):
    return float(((week / weeks) * 100.0) / percentage)

def expenses_percentage(total, spending):
    return (spending / total) * 100.0

def date_difference():
    date = datetime.date.day

total_expenses(expenses)