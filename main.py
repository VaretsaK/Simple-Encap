class Account:
    """
    Represents a bank account.

    Attributes:
    - account_holder (str): The name of the account holder.
    - __balance (int): The balance of the account (private attribute).
    """
    def __init__(self, account_holder: str) -> None:
        """
        Initializes a new Account object with the specified account holder and balance.

        Args:
        - account_holder (str): The name of the account holder.
        - balance (int, optional): The initial balance of the account (default is 0).
        """
        self.__balance: int = 0
        self._account_holder = account_holder

    @property  # getter
    def balance(self) -> int:
        """
        Retrieves the balance of the account.

        Returns:
        - int: The balance of the account.
        """
        return self.__balance

    @balance.setter  # setter
    def balance(self, value: int) -> None:
        """
        Sets the account balance to a new value, ensuring that it cannot be set to a negative number.

        Args:
            value (int): The new balance of the account.

        Raises:
            ValueError: If the new balance is below 0.
        """
        if value <= 0:
            raise ValueError("Balance should be above 0.")
        self.__balance = value


def main() -> None:
    """
    Main function to demonstrate the usage of the Account class.
    """
    acc1 = Account("Dave")
    print(acc1.balance)
    acc1.balance = 50
    print(acc1.balance)


if __name__ == "__main__":
    main()
