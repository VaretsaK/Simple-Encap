class Account:
    """
    Represents a bank account.

    Attributes:
    - account_holder (str): The name of the account holder.
    - __balance (int): The balance of the account (private attribute).
    """
    def __init__(self, account_holder: str, balance: int = 0) -> None:
        """
        Initializes a new Account object with the specified account holder and balance.

        Args:
        - account_holder (str): The name of the account holder.
        - balance (int, optional): The initial balance of the account (default is 0).
        """
        self.__balance = balance
        self._account_holder = account_holder

    def get_balance(self) -> int:
        """
        Retrieves the balance of the account.

        Returns:
        - int: The balance of the account.
        """
        return self.__balance


def main() -> None:
    """
    Main function to demonstrate the usage of the Account class.
    """
    ...


if __name__ == "__main__":
    main()
