from requests import get, Timeout, Response
from ssl import SSLError
from time import sleep
from typing import Any
from argparse import ArgumentParser


def path_reaper(target: str, pathlist: str) -> list[str]:
    true_words: list[str] = []
    with open(pathlist, 'r') as wordlist:
        lenght_wordlist = len(wordlist.readlines())
        print(f"Scanning {lenght_wordlist} paths...")
    with open(pathlist, 'r') as wordlist:
        for word in wordlist:
            word = word.strip()
            url = f'http://{target}/{word}'
            try:
                response = get(url, timeout=5)
                if response.status_code == 200:
                    print(f"Found: {url}")
                    true_words.append(word)
                elif response.status_code == 404:
                    continue
                elif response.status_code == 403:
                    print(f"Forbidden: {url}")
                    true_words.append(word)
                else:
                    print(f"Unexpected Status Code: {url} - {response.status_code}")
                    true_words.append(word)
            except Timeout as e:
                print(f"Timeout Error: {url} - {str(e)}")
            except Exception as e:
                continue
            sleep(1)
    return true_words


def subdomains_reaper(target: str, subdomainpath: str) -> list[str]:
    true_subdomains: list[str] = []
    with open(subdomainpath, 'r') as subdomainlist:
        lenght_subdomainlist = len(subdomainlist.readlines())
        print(f"Scanning {lenght_subdomainlist} subdomains...")
    with open(subdomainpath, 'r') as subdomainlist:
        for subdomain in subdomainlist:
            subdomain = subdomain.strip()
            url = f"http://{subdomain}.{target}"
            try:
                response = get(url, timeout=5)
                if response.status_code == 200:
                    print(f"Found: {url}")
                    true_subdomains.append(subdomain)
                elif response.status_code == 404:
                    continue
                elif response.status_code == 403:
                    print(f"Forbidden: {url}")
                    true_subdomains.append(subdomain)
                else:
                    print(f"Unexpected Status Code: {url} - {response.status_code}")
                    true_subdomains.append(subdomain)
            except SSLError:
                response = get(f"http://{subdomain}.{target}", timeout=5)
            except Timeout as e:
                print(f"Timeout Error: {url} - {str(e)}")
            except Exception as e:
                continue
            sleep(1)


import requests


def crtsh_reaper(domain: str) -> list[str]:
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        res: Response = get(url, timeout=10)
        res.raise_for_status()
        data: Any = res.json()
        subdomains: set[str] = set()
        for entry in data:
            name_value = entry.get("name_value")
            if name_value:
                for sub in name_value.split('\n'):
                    if sub.endswith(domain):
                        subdomains.add(sub.strip())
        return sorted(subdomains)
    except Exception as e:
        print(f"Errore con crt.sh: {e}")
        return []


def main():
    parser = ArgumentParser(description='Path fuzzing, enumeration of subdomains and crt.sh')
    parser.add_argument('target', help='Domain to scan (es: google.com)')
    parser.add_argument('--pathlist', help='Wordlist per i path')
    parser.add_argument('--subdomainpath', help='Wordlist per i subdomain')
    parser.add_argument('--crtsh', action='store_true', help='Enumera subdomain da crt.sh')
    args = parser.parse_args()

    if args.pathlist:
        found_paths = path_reaper(args.target, args.pathlist)
        print(f"\n[+] Path trovati:\n{found_paths}")

    if args.subdomainpath:
        found_subs = subdomains_reaper(args.target, args.subdomainpath)
        print(f"\n[+] Subdomain trovati:\n{found_subs}")

    if args.crtsh:
        found_subs = crtsh_reaper(args.target)
        print(f"\n[+] Subdomain trovati da crt.sh:\n{found_subs}")


if __name__ == "__main__":
    main()
