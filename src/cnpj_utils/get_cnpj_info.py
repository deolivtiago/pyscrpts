import requests
import time
import urllib3


def get_cnpj_info(cnpj=78242849000169):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    url = f"https://api.opencnpj.org/{cnpj}"
    response = requests.get(url, verify=False)

    if response.status_code == 200:
        data = response.json()
        print(f"{data["cnpj"]}|{data["razao_social"]}|{data["data_inicio_atividade"]}|{data["nome_fantasia"]}")
        time.sleep(5)

        return data
    else:
        print(f"{cnpj}: {response.status_code}")
        return None

if __name__ == "__main__":
    cnpjs = ["78242849000169", "18247063000536", "12345678000190"]
    for cnpj in cnpjs:
        info = get_cnpj_info(cnpj)
        if info:
            with open("output.txt", "a") as f:
                f.write(f"{info}\n")
        else:
            with open("output.txt", "a") as f:
                f.write(f"{cnpj}\n")
