def process_text(filename):

    file = open(filename,'r')

    data = []

    for line in file.readlines():
        data += line.replace("\n"," ").split(" ")

    return data


