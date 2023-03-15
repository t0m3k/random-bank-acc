import csv
from random_uk_bank_account import GenerateUkBankAccount
from sort_code_from_csv import random_sort_code
from params import get_params

def random_bank_accounts(code, total):
    """Return random bank account number."""
    sort_codes = {}
    for _ in range(0, code):
        while True:
            sort_code, bank_acc = random_bank_acc(total)
            if sort_code not in sort_codes:
                break
        
        sort_codes[sort_code] = bank_acc

    return sort_codes

def random_bank_acc(total):
    """Return random bank account number."""
    sort_code = random_sort_code()
    try:
        return (sort_code, GenerateUkBankAccount().generate_for_sort_code(sort_code, total=total).account_numbers)
    except:
        return random_bank_acc(total)
    
def save_to_csv(data, file):
    """Save data to csv file."""
    with open(file, "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Sort Code", "Account Number"])
        for sort_code, bank_acc in data.items():
            for acc in bank_acc:
                writer.writerow([sort_code, acc])

if __name__ == "__main__":
    codes, accounts, file = get_params()
    accounts = random_bank_accounts(100, 50)
    save_to_csv(accounts, file)
