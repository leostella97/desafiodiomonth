def main():
    month_number = int(input())
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    print(months[month_number - 1])

if __name__ == '__main__':
    main()
