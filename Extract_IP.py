import requests
from bs4 import BeautifulSoup

def extract_ips(url):        
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text,'html.parser')
        ip_text = soup.get_text()
        ips = ip_text.split('\n')
        ips.sort()
        return ips
    else:
        print(f"Error al obtener la página. Código de estado: {response.status_code}")

def export_results(list):  
  with open('ipList.txt', 'w') as archivo:
    for elemento in list:
      archivo.write(str(elemento) + '\n')
        
if __name__ == '__main__': 
    url = 'https://www.dan.me.uk/torlist/'
    ips = extract_ips(url)  
    export_results(ips)   
    