# ------------------------------------------------------------
# SysGuard: Automated System Care Companion (System Maintenance Automation)
# This script is provided for personal convenience and is not
# subject to any specific licensing terms. Feel free to use,
# modify, and distribute this script without formal restrictions.
# Use at your own discretion.
#
# Author: Sedat CALISKAN
# Date: 8/11/2023


import subprocess

def run_command(command):
    subprocess.run(command, shell=True)

# Run chskdsk 

chkdsk_command = 'C:\\Windows\\system32\\cmd.exe /c chkdsk.exe'
run_command(chkdsk_command)

# Prompt the user to continue
input("Press Enter to continue to the next stage (sfc /scannow)...")

# Run sfc /scannow

sfc_command = 'C:\\Windows\\system32\\cmd.exe /c sfc /scannow'
run_command(sfc_command)

# RUn dism /online /cleanup-image /restorehealth
dism_command = 'C:\\Windows\\system32\\cmd.exe /c dism /online /cleanup-image /restorehealth'
run_command(dism_command)


