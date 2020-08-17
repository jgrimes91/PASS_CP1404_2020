FILE = "bloodPressure"

bp_file = open(FILE)
for line in bp_file:
    split_line = line.split(",")
    print("Systolic = {}, diastolic = {}".format(split_line[0], split_line[1]))
bp_file.close()