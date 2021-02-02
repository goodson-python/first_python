# What is this script for, what is the purpose

from switches import switch1
from switches import dev_login


def select_device():
    pass


def main():
    if select_device():
        dev_login()
    print('Error')


if __name__ == "__main__":
    main()