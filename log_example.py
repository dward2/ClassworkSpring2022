import logging


def analyze_data_file(filename):
    in_file = open(filename, 'r')
    line_number = 0
    keep_reading = True
    while keep_reading:
        data_line = in_file.readline()
        if not data_line:
            logging.info("Reached end of file")
            keep_reading = False
        else:
            line_number += 1
            process_line(data_line, line_number)
    in_file.close()


def process_line(data_line, line_number):
    data_points = data_line.strip('\n').split(',')
    if len(data_points) != 5:
        logging.warning("Not 5 data points in line {}".format(line_number))
    data = [float(i) for i in data_points]
    if any(i < 0 for i in data):
        logging.error("Negative value present in line {}".format(line_number))
        return False
    if all(1.0 <= i <= 4.0 for i in data):
        return True
    else:
        logging.debug("Out of range in line {}".format(line_number))
        return True


if __name__ == "__main__":
    logging.basicConfig(filename="example.log", level=logging.INFO)
    analyze_data_file("tsh_class_data.txt")
