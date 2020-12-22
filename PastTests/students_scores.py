def calculate_avg(grades):
    student_avg = []
    test_avg = {}
    test_avg_list = []
    for i in grades.keys():
        summ = 0
        for j in grades[i]:
            summ += float(j[1])
            if j[0] in test_avg.keys():
                test_avg[j[0]].append(j[1])
            else:
                test_avg[j[0]] = [j[1]]
        summ = summ / len(grades[i])
        student_avg.append((i, summ))

    for i in test_avg.keys():
        avg = 0
        for j in test_avg[i]:
            avg += float(j)
        avg = avg / len(test_avg[i])
        test_avg_list.append((i, avg))
    student_avg.sort()
    test_avg_list.sort()
    for i in student_avg:
        print(i[0], i[1])
    for i in test_avg_list:
        print(i[0], i[1])


def main():
    N = int(input())
    grades = {}
    for i in range(N):
        line = input().split()
        student_grades = []
        for e in range(1, len(line)):
            student_grades.append((line[e].split(":")[0], line[e].split(":")[1]))

        grades[line[0]] = student_grades
    calculate_avg(grades)


if __name__ == '__main__':
    main()
