from kontekst import Logger, FileWriter, SafeDivision


def main():
    # 1. Logger
    with Logger():
        print("Jesteśmy w środku bloku with")

    # 2. FileWriter - zwykły zapis
    with FileWriter("output.txt") as f:
        f.write("Hello, context manager!\n")

    # 3. FileWriter - wyjątek nie jest tłumiony
    try:
        with FileWriter("output2.txt") as f:
            f.write("Zapis przed błędem\n")
            raise ValueError("coś poszło nie tak")
    except ValueError as e:
        print(f"Złapany wyjątek poza blokiem with: {e}")

    # 4. SafeDivision
    with SafeDivision() as sd:
        print(sd.divide(10, 2))
        print(sd.divide(5, 0))


if __name__ == "__main__":
    main()
