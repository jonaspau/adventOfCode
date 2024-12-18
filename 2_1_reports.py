def getreports():
    reports = {}

    with open("2_input.txt", "r") as f:
        for i, line in enumerate(f):
            report_num = len(reports) + 1
            reports[f"r_{report_num}"] = [int(x) for x in line.strip().split()]
    return(reports)


def isMonotonic(values):
    direction = values[1] - values[0]
    for i in range(2, len(values)):
        if direction * (values[i] - values[i-1]) <=0:
            return False
    return True


def noHighIncrease(values):
    for i in range(1, len(values)):
        if abs(values[i] - values[i-1]) >=4:
            return False
    return True


def isSafe(report_values):
    for i in range(len(report_values)):
        modified_report = report_values[:i] + report_values[i+1:]
        if isMonotonic(modified_report) and noHighIncrease(modified_report):
            return True
    return False

def analyzeReports(reports):
    safe_reports = []

    for report_num, report_values in reports.items():
        if isSafe(report_values):
            safe_reports.append(report_num)

    print(f"1: Safe reports: {len(safe_reports)}")


def main():
    reports = getreports()

    analyzeReports(reports)


main()