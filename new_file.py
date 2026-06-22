import datetime

def main():
    now = datetime.datetime.now()
    print("GitHub test commit")
    print(f"Run at: {now.strftime('%Y-%m-%d %H:%M:%S')}")

    numbers = [1, 2, 3, 4, 5]
    total = sum(numbers)
    print(f"Numbers: {numbers}")
    print(f"Sum: {total}")
    print(f"Average: {total / len(numbers)}")

if __name__ == "__main__":
    main()
