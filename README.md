### Subdomain & Path Enumerator

A tool for performing path fuzzing, subdomain enumeration, and subdomain discovery via crt.sh. It is useful for OSINT, penetration testing, and discovering potential vulnerabilities in a network.

### Features
• Path Fuzzing: Performs path fuzzing on a target domain using a wordlist to identify exposed resources.

• Subdomain Enumeration: Uses a wordlist to discover subdomains of a target domain.

• Subdomains from crt.sh: Retrieves subdomains from crt.sh, a service that collects public SSL/TLS certificates.

### Requirements
• Python 3.x

• The required libraries can be installed via pip
 
 ```pip install requests```


### How to Use
1. Path Fuzzing
You can perform path fuzzing on a target domain by specifying a wordlist for the paths:

```python script.py target.com --pathlist path_to_wordlist.txt```

2. Subdomain Enumeration
You can perform subdomain enumeration using a wordlist for subdomains:

```python script.py target.com --subdomainpath subdomain_wordlist.txt```

3. Subdomains from crt.sh
You can retrieve subdomains published via crt.sh:

```python script.py target.com --crtsh```

4. Combining All Operations
You can run multiple operations in a single command:

```python script.py target.com --pathlist path_to_wordlist.txt --subdomainpath subdomain_wordlist.txt --crtsh```

### Arguments
• target: The target domain to scan (e.g., google.com).

• --pathlist: Path to a wordlist for path fuzzing.

• --subdomainpath: Path to a wordlist for subdomain enumeration.

• --crtsh: Enable subdomain enumeration via crt.sh.

### Disclaimer
This tool is intended for educational purposes and legitimate security testing only. It should only be used on systems and networks you have explicit permission to test. Unauthorized use of this tool on networks or systems without consent may be illegal and can lead to severe legal consequences. Always ensure you have proper authorization before conducting any security testing.
By using this tool, you agree that the author is not responsible for any damages, consequences, or legal actions resulting from the misuse of this software.
