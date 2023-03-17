import csv
from random_uk_bank_account import GenerateUkBankAccount
from sort_code_from_csv import random_sort_code
from params import get_params


class RandomSortCodes:
    def __init__(self, sort_code_qty, bank_account_qty):
        self.sort_code_qty = sort_code_qty
        self.bank_account_qty = bank_account_qty
        self.sort_codes = {}

    def generate(self):
        sort_code_list = {}
        for _ in range(0, self.sort_code_qty):
            while True:
                sort_code, bank_acc = self.__random_sort_code_with_bank_accounts()
                if sort_code not in sort_code_list:
                    break
            sort_code_list[sort_code] = bank_acc
        self.sort_codes = sort_code_list
        return sort_code_list

    def __random_sort_code_with_bank_accounts(self):
        sort_code = random_sort_code()
        try:
            return (sort_code, GenerateUkBankAccount().generate_for_sort_code(sort_code, total=self.bank_account_qty).account_numbers)
        except:
            return self.__random_sort_code_with_bank_accounts()

    def save_to_csv(self, file):
        with open(file, "w") as f:
            writer = csv.writer(f)
            writer.writerow(["Sort Code", "Account Number"])
            for sort_code, bank_acc in self.sort_codes.items():
                for acc in bank_acc:
                    writer.writerow([sort_code, acc])

if __name__ == "__main__":
    codes, accounts, file = get_params()

    random_sort_codes = RandomSortCodes(codes, accounts)
    random_sort_codes.generate()
    random_sort_codes.save_to_csv(file)
