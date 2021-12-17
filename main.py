from electr import Electr

if __name__ == '__main__':
    e = Electr("electr_in.txt")
    e.form_solutions()
    e.reconstruct_solution()
    print(e.calculate_length_of_lines(e.reconstruct_solution()))
