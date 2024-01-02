class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = capacity
        self._cookies = 0

    def __str__(self):
        return "🍪" * self._cookies

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Number of cookies to deposit must be a non-negative integer.")
        if self._cookies + n > self._capacity:
            raise ValueError("Cookie jar capacity exceeded.")
        self._cookies += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Number of cookies to withdraw must be a non-negative integer.")
        if n > self._cookies:
            raise ValueError("Not enough cookies in the jar.")
        self._cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies


def main():
    cookie_jar = Jar(capacity=10)
    print(cookie_jar)  # Output: ""

    cookie_jar.deposit(3)
    print(cookie_jar)  # Output: "🍪🍪🍪"

    cookie_jar.withdraw(2)
    print(cookie_jar)  # Output: "🍪"

    print(cookie_jar.capacity)  # Output: 10
    print(cookie_jar.size)  # Output: 1

if __name__ == "__main__":
    main()
