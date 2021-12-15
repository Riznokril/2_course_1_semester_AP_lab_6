from electr import Electr

if __name__ == '__main__':
    e = Electr()
    e.read_data("electr_in.txt")
    print(e.counting_length_of_lines())