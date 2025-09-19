import subprocess

result = subprocess.run(["nmap", "-Pn", "-sV", "172.20.55.105/20"],  capture_output=True, text=True)

print(result.stdout)