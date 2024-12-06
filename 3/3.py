import re
import time


def parte1():
    pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
    digits = re.compile(r"\d+")
    with open(r"dia3\3.txt", mode="r") as file:
        lines = file.readlines()
    total = 0
    for line in lines:
        matches: list[str] = pattern.findall(line)
        for mul in matches:
            nums = [int(i) for i in digits.findall(mul)]
            total += nums[0] * nums[1]
    print(total)


def parte2():
    # regex
    pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
    digits = re.compile(r"\d+")
    pattern_do = re.compile(r"do\(\)")
    pattern_dont = re.compile(r"don't\(\)")

    with open(r"3\3.txt", mode="r") as file:
        lines = file.readlines()

    total = 0
    dont_index = float("inf")
    for line in lines:
        matches = pattern.finditer(line)
        matches_do = pattern_do.finditer(line)
        matches_dont = pattern_dont.finditer(line)
        mul = next(matches)
        do = next(matches_do, None)

        # Caso tenha um valor anterior tem que achar a proxima multiplicacao que possa ser usada
        if dont_index != float("inf"):
            while mul is not None and mul.span()[0] < do.span()[0]:
                mul = next(matches, None)

        dont_index = next(matches_dont).span()[0]

        while mul is not None and do is not None:
            while mul is not None and mul.span()[0] < dont_index:
                if mul.span()[0] > dont_index:
                    break
                nums = list(map(int, digits.findall(mul.group())))
                total += nums[0] * nums[1]
                mul = next(matches, None)

            while do is not None and mul is not None:
                if do.span()[0] > dont_index:
                    dont_index = next(matches_dont, None)
                    if dont_index is None:
                        dont_index = float("inf")
                    else:
                        dont_index = dont_index.span()[0]
                    while mul is not None and mul.span()[0] < do.span()[0]:
                        mul = next(matches, None)
                    break
                else:
                    do = next(matches_do, None)

    print(total)


if __name__ == "__main__":
    start_time = time.perf_counter()
    parte2()
    end_time = time.perf_counter()
    print(f"Execution time: {end_time - start_time} seconds")
