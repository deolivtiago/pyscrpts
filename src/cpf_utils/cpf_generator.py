from random import randint


def generate_first_numbers(starts_with = ""):
    first_numbers = [randint(0, 9) for _n in range(9)]
    starts_with = [int(n) for n in starts_with]
    # print(f"starts_with: {starts_with}")

    if starts_with:
        first_numbers = starts_with + first_numbers[len(starts_with):]
    
    return first_numbers


def calculate_total(first_numbers, digit_position):
    multipliers = list(range(digit_position, 0, -1))
    multipliers = multipliers[:len(first_numbers)]
    multipliers = { m: v for m, v in zip(multipliers, first_numbers) }
    # print(f"multipliers = {multipliers}")
    
    results = [ m * v for m, v in multipliers.items() ]
    # print(f"results = {results}")

    return sum(results)


def calculate_digit(first_numbers, digit_position):
    total = calculate_total(first_numbers, digit_position)
    # print(f"total = {total}")

    remainder = (total * 10) % 11
    # print(f"remainder = {remainder}")

    return remainder if remainder < 10 else 0


def generate_cpf(starts_with = ""):
    first_numbers = generate_first_numbers(starts_with)
    # print(f"first_numbers = {first_numbers}")

    digit_10 = calculate_digit(first_numbers, 10)
    # print(f"digit_10 = {digit_10}")
    
    first_numbers.append(digit_10)
    # print(f"first_numbers = {first_numbers}")

    digit_11 = calculate_digit(first_numbers, 11)
    # print(f"digit_11 = {digit_11}")

    first_numbers.append(digit_11)
    # print(f"first_numbers = {first_numbers}")

    cpf = [str(n) for n in first_numbers]

    return "".join(cpf)


def is_cpf_valid(cpf):
    cpf = [ int(n) for n in cpf ]
    # print(f"cpf = {cpf}")

    first_numbers = cpf[:9]
    # print(f"first_numbers = {first_numbers}")

    digit_10 = calculate_digit(first_numbers, 10)
    # print(f"digit_10 = {digit_10}")
    
    first_numbers.append(digit_10)
    # print(f"first_numbers = {first_numbers}")

    digit_11 = calculate_digit(first_numbers, 11)
    # print(f"digit_11 = {digit_11}")

    first_numbers.append(digit_11)
    # print(f"first_numbers = {first_numbers}")

    return cpf == first_numbers


if __name__ == "__main__":
    cpf =  generate_cpf(starts_with="11")

    if is_cpf_valid(cpf):
        print(f"cpf: {cpf}")

    # print([ cpf for _i in range(100) ])
