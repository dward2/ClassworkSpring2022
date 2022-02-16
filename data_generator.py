import random


def generate_data():
    NO_DATA = 1000
    with open("tsh_class_data.txt", 'w') as out_file:
        for i in range(NO_DATA):
            out_string = ""
            for j in range(5):
                data = generate_data_point()
                out_string += "{},".format(data)
            out_string = out_string.rstrip(',')
            out_file.write("{}\n".format(out_string))


def d6():
    return random.randint(1, 6)


def generate_data_point():
    roll = d6() + d6() + d6()
    if roll <= 4:
        data = random.random() * 1.0
    elif roll >= 17:
        data = random.random() * 5 + 5.0
    else:
        data = random.random() * 3 + 1.0
    data = round(data, 1)
    return data


if __name__ == '__main__':
    generate_data()
