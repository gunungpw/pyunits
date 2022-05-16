import sys

length = {
    "yottameter": 1e24,
    "zettameter": 1e21,
    "exameter": 1e18,
    "petameter": 1e15,
    "terameter": 1e12,
    "gigameter": 1e9,
    "megameter": 1e6,
    "kilometer": 1e3,
    "hectometer": 1e2,
    "decameter": 1e1,
    "meter": 1e-0,
    "decimeter": 1e-1,
    "centimeter": 1e-2,
    "millimeter": 1e-3,
    "micrometer": 1e-6,
    "nanometer": 1e-9,
    "picometer": 1e-12,
    "femtometer": 1e-15,
    "attometer": 1e-18,
    "zeptometer": 1e-21,
    "yoctometer": 1e-24,
}


def split_args(input_args) -> list:
    list_input = input_args.split(" ", 1)
    return list_input


def check_input(input: str):
    args = split_args(input)
    if args[1] in length.keys():
        pass
    else:
        print("unit not implemented yet!")
        sys.exit()


def check_input_wanted(input: str):
    if input in length.keys():
        pass
    else:
        print("unit not implemented yet!")
        sys.exit()


def convert_to_primitive(unit: list) -> float:
    primitive_value = length.get(unit[1]) * float(unit[0])
    return primitive_value


def convert_to_wanted_value(primitive_value: float, wanted_result: str) -> float:
    result = primitive_value / length.get(wanted_result)
    return result


def main():
    input_questions: str = input("You have = ")
    input_wanted_result: str = input("You want = ")
    check_input(input_questions)
    check_input_wanted(input_wanted_result)
    input_value = split_args(input_questions)
    if input_wanted_result != "meter":
        convert = convert_to_primitive(input_value)
        result = convert_to_wanted_value(convert, input_wanted_result)
        print(result, input_wanted_result)
    elif input_wanted_result == "meter":
        convert = convert_to_primitive(input_value)
        print(convert, input_wanted_result)
    else:
        print("Error")


if __name__ == "__main__":
    main()
