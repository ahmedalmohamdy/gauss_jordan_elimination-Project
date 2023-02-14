from os import path


def examples():
    sub = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    eq = int(input("Please enter the number of equation to be solved : "))
    file = open("user_manual.txt", 'w', encoding="utf-8")
    file.write("This file is your catalogue to use this program.\n\n")
    file.write(
        "First, Store your equations in a text file named 'equations.txt'.\n")
    file.write(
        f"If you have {eq} equations, Your text file should be like this:\n")
    file.write(f"Number of equations: {eq}")
    for i in range(1, eq+1):
        file.write("\n")
        file.write(f"eq{i}: ".translate(sub))
        for j in range(1, eq+1):

            file.write(f"a{i}{j}x{j} ".translate(sub))
            if j < eq:
                file.write("+ ")
            else:
                file.write("= ")

        file.write(f"a{i}0".translate(sub))
    file.write(
        "\n\n##########################################################################################")
    file.close()
    print(__file__.replace("getting_info.py", "user_manual.txt"))


def getting_equations():
    equations_file = __file__.replace("getting_info.py", "equations.txt")
    if not path.exists(equations_file):
        print(f"sorry we can't find {equations_file}")
        return None

    # use utf-8 encoding to use subscript numbers
    file = open(equations_file, 'r', encoding="utf-8")
    line1 = file.readline()
    no_eqs = int(line1.split(":")[1].strip())
    lines = file.readlines()
    file.close()

    equations = []
    SUB = str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")
    for line in lines:

        equation = []
        args = {}
        # eq1: 1x₁ 3x₂ -7x₃ 0
        data = line.split(":")[1].replace(" ", "")
        data = data.replace("+", " ")
        data = data.replace("=", " ")
        data = data.replace("-", " -")
        data = data.split()
        # ['1x₁', '3x₂', '-7x₃', '0']

        d = int(data[-1])  # = 0
        for var in data[0:-1]:
            x = var.translate(SUB)
            equation.append(x)
        # ['1x1', '3x2', '-7x3']

        for value in equation:
            args[int(value.split("x")[1])] = int(value.split("x")[0])
        # { 1: 1, 2: 3, 3: -7 }

        # solving problem of removed variables ex: 1x1 + 3x2 = 0
        if len(equation) < no_eqs:
            for i in range(1, no_eqs+1):
                if i not in args:
                    args[i] = 0

        # order keyes in dictionary
        args = {k: args[k] for k in sorted(args)}
        equations.append([*args.values(), d])

    return equations


if __name__ == "__main__":
    examples()
    # print(getting_equation())
