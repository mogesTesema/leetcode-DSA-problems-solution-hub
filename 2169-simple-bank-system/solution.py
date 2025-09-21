class Bank:
    def __init__(self, balance: List[int]):
        self.users = balance  # use list directly

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        account1 -= 1
        account2 -= 1
        # validate accounts
        if 0 <= account1 < len(self.users) and 0 <= account2 < len(self.users):
            if self.users[account1] >= money:
                self.users[account1] -= money
                self.users[account2] += money
                return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        account -= 1
        if 0 <= account < len(self.users):
            self.users[account] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        account -= 1
        if 0 <= account < len(self.users) and self.users[account] >= money:
            self.users[account] -= money
            return True
        return False

