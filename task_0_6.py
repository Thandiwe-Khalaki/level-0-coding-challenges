def maximum_number(*args):
    biggest_number = args[0]
    for i in args:
        if i > biggest_number:
            biggest_number = i
    print(biggest_number)



def main():
    maximum_number(102.03, 11115555, 108 ** 2, 1000000)

if __name__ == "__main__":
    main()