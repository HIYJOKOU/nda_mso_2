import argparse

from app.calculator import add, divide, multiply, subtract


def main() -> None:
    parser = argparse.ArgumentParser(description="Prosty kalkulator CLI")
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"])
    parser.add_argument("a", type=float)
    parser.add_argument("b", type=float)

    args = parser.parse_args()

    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    result = operations[args.operation](args.a, args.b)
    print(result)


if __name__ == "__main__":
    main()
