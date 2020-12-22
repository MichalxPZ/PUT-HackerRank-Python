def convert(n):
    for i in range(n):
        line = input()
        line = line.split()
        if line[1] == 'Kelvin' and line[2] == 'Celsius':
            KtC(int(line[0]))
        if line[1] == 'Kelvin' and line[2] == 'Fahrenheit':
            KtF(int(line[0]))
        if line[1] == 'Celsius' and line[2] == 'Kelvin':
            CtK(int(line[0]))
        if line[1] == 'Celsius' and line[2] == 'Fahrenheit':
            CtF(int(line[0]))
        if line[1] == 'Fahrenheit' and line[2] == 'Kelvin':
            FtK(int(line[0]))
        if line[1] == 'Fahrenheit' and line[2] == 'Celsius':
            FtC(int(line[0]))


def KtC(temperature):
    if temperature < 0:
        print("NO")
    else:
        temperature = temperature - 273.15
        temperature = round(temperature, 2)
        temperature = "{:.2f}".format(temperature)
        print(temperature)


def KtF(temperature):
    if temperature < 0:
        print("NO")
    else:
        temperature = temperature * 9 / 5 - 459.67
        temperature = round(temperature, 2)
        temperature = "{:.2f}".format(temperature)
        print(temperature)


def CtK(temperature):
    if temperature < -273.15:
        print("NO")
    else:
        temperature = temperature + 273.15
        temperature = round(temperature, 2)
        temperature = "{:.2f}".format(temperature)
        print(temperature)


def CtF(temperature):
    if temperature < -273.15:
        print("NO")
    else:
        temperature = temperature * 9 / 5 + 32
        temperature = round(temperature, 2)
        temperature = "{:.2f}".format(temperature)
        print(temperature)


def FtC(temperature):
    if temperature < -459.67:
        print("NO")
    else:
        temperature = (temperature - 32) * 5 / 9
        temperature = round(temperature, 2)
        temperature = "{:.2f}".format(temperature)
        print(temperature)


def FtK(temperature):
    if temperature < -459.67:
        print("NO")
    else:
        temperature = (temperature + 459.67) * 5 / 9
        temperature = round(temperature, 2)
        temperature = "{:.2f}".format(temperature)
        print(temperature)


def main():
    convert(int(input()))


if __name__ == '__main__':
    main()
