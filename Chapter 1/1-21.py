import re

if __name__ == '__main__':
    with open('redata.txt', 'r') as file:
        for line in file.readlines():
            m = re.match('\w+ (\w+) .+', line)
            print(m.group(1))