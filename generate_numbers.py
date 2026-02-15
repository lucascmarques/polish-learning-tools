ONES = ["zero", "jeden", "dwa", "trzy", "cztery", "pięć", "sześć", "siedem", "osiem", "dziewięć"]
TEENS = ["dziesięć", "jedenaście", "dwanaście", "trzynaście", "czternaście", "piętnaście", "szesnaście", "siedemnaście", "osiemnaście", "dziewiętnaście"]
TENS = ["", "", "dwadzieścia", "trzydzieści", "czterdzieści", "pięćdziesiąt", "sześćdziesiąt", "siedemdziesiąt", "osiemdziesiąt", "dziewięćdziesiąt"]
FILE_PATH = "files/numbers.txt"


def to_polish(n: int) -> str:
    if n < 0 or n > 100:
        raise ValueError("Supported range is 0..100")
    if n < 10:
        return ONES[n]
    if n < 20:
        return TEENS[n - 10]
    if n == 100:
        return "sto"
    tens = n // 10
    ones = n % 10
    if ones == 0:
        return TENS[tens]
    return f"{TENS[tens]} {ONES[ones]}"


def main():
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        for n in range(0, 101):
            file.write(f"{n}; {to_polish(n)}\n")


if __name__ == "__main__":
    main()
