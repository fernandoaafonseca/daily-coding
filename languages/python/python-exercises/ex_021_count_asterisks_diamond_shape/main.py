def main() -> None:
    with open("diamond.txt", "r") as file:
        diamond_lines = file.readlines()
        lines = [line.rstrip("\n") for line in diamond_lines]

    asterisks_count = count_asterisks(lines)
    print(asterisks_count)


def count_asterisks(lines: list[str]) -> list[int]:
    asterisks_count = []

    for line in lines:
        char_amount = 0
        for char in line:
            if char == '*':
                char_amount += 1
        if char_amount > 0:
            asterisks_count.append(char_amount)

    return asterisks_count


if __name__ == '__main__':
    main()