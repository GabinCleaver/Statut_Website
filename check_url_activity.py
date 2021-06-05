import requests
from colorama import Fore, init

init()

url = input(Fore.YELLOW + "Entrez l'url du site: ")
print(f"Tentative de connexion à {url} pour déterminer l'état de la connexion Internet.")

try:
    requests.get(url, timeout = 10)
    print(Fore.GREEN + f'Connection à {url} avec succès.')
except:
    requests.ConnectionError
    print(Fore.RED + f'Échec de la connexion à {url}.')