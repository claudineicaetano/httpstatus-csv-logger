import csv
import time
import requests
from requests.auth import HTTPProxyAuth

def read_cpfs(csv_file):
    cpfs = []
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cpfs.append(row['cpf'])
    return cpfs

def make_request(cpf, endpoint, proxies, auth):
    payload = {"cpf": cpf}
    response = requests.post(endpoint, json=payload, proxies=proxies, auth=auth)
    return response.status_code

def write_results(csv_file, results):
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['cpf', 'httpstatus'])
        for cpf, status in results:
            writer.writerow([cpf, status])

def append_result(csv_file, cpf, status):
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([cpf, status])

def read_processed_cpfs(csv_file):
    processed_cpfs = set()
    try:
        with open(csv_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                processed_cpfs.add(row['cpf'])
    except FileNotFoundError:
        pass
    return processed_cpfs

def main():
    input_csv = 'input.csv'
    output_csv = 'output.csv'
    endpoint = 'https://your-api-endpoint.com/api'

    proxy_url = 'http://your-proxy-url:port'
    proxy_user = 'your-proxy-username'
    proxy_pass = 'your-proxy-password'
    proxies = {
        'http': proxy_url,
        'https': proxy_url,
    }
    auth = HTTPProxyAuth(proxy_user, proxy_pass)

    cpfs = read_cpfs(input_csv)
    processed_cpfs = read_processed_cpfs(output_csv)

    if not processed_cpfs:
        with open(output_csv, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['cpf', 'httpstatus'])

    for cpf in cpfs:
        if cpf not in processed_cpfs:
            status = make_request(cpf, endpoint, proxies, auth)
            if status in [200, 204]:
                append_result(output_csv, cpf, status)
            time.sleep(15)

if __name__ == "__main__":
    main()
