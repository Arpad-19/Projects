import json

def analyse_logs(logs):
    counter = {}

    for line in logs:
        words = line.split()

        if not words:
            continue

        level = words[0]

        if level in counter:
            counter[level] += 1
        else:
            counter[level] = 1

    return counter


def most_common_logs(logs):
    counter = analyse_logs(logs)
    max_count = 0
    most_common = ''

    for level in counter:
        if counter[level] > max_count:
            max_count = counter[level]
            most_common = level

    return most_common


def find_errors(logs):
    errors = []

    for line in logs:
        words = line.split()

        if not words:
            continue

        level = words[0]

        if level == 'ERROR':
            errors.append(line)

    return errors


def find_failed_logins(logs):
    failed_logins = []

    for line in logs:
        words = line.split()

        if 'login' in words and 'failed' in words:
            failed_logins.append(line)

    return failed_logins


def count_failed_logins(logs):
    failed_logins = find_failed_logins(logs)
    counter = {}

    for log in failed_logins:
        words = log.split()
        ip_address = words[1]

        if ip_address in counter:
            counter[ip_address] += 1
        else:
            counter[ip_address] = 1

    return counter


def find_suspicious_ips(logs):
    counter = count_failed_logins(logs)
    suspicious_ips = []

    for ip in counter:
        if counter[ip] >= 3:
            suspicious_ips.append(ip)

    return suspicious_ips


def generate_report(logs):
    log_levels = analyse_logs(logs)
    common_log = most_common_logs(logs)
    errors = find_errors(logs)
    failed_logins = find_failed_logins(logs)
    failed_login_counts = count_failed_logins(logs)
    suspicious_ips = find_suspicious_ips(logs)

    report = {
        "log_levels": log_levels,
        "common_log": common_log,
        "errors": errors,
        "failed_logins": failed_logins,
        "failed_login_counts": failed_login_counts,
        "suspicious_ips": suspicious_ips
    }

    return report

def print_report(report):
    print("========== LOG ANALYSIS REPORT ==========")

    print("\nLog levels:")
    for level in report["log_levels"]:
        print(level, ":", report["log_levels"][level])

    print("\nMost common log level:")
    print(report["common_log"])

    print("\nErrors:")
    for error in report["errors"]:
        print(error.strip())

    print("\nFailed login attempts:")
    for ip in report["failed_login_counts"]:
        print(ip, ":", report["failed_login_counts"][ip])

    print("\nSuspicious IP addresses:")
    for ip in report["suspicious_ips"]:
        print(ip)

def save_report(report, filename):
    with open(filename, 'w', encoding = 'utf-8') as file:
        json.dump(report, file, indent = 4, ensure_ascii = False)

def load_report(filename):
    with open(filename, 'r', encoding = 'utf-8') as file:
        json_report = json.load(file)
    return json_report


with open("server.log", "r") as file:
    logs = file.readlines()

report = generate_report(logs)
save_report(report, 'report.json')
print_report(report)
print(load_report('report.json'))