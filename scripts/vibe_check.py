import os
import requests
import re
from pathlib import Path

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1358907447619752086/iEU3tsRNJphcyTp-zcsEhmcuncMhVJ3ME6nMyEnCRC_myzuiPnN2jaG2tDIKdPmAQrN1" 
def check_vibes():
    vibe_score = 100
    notes = []

    for py_file in Path(".").rglob("*.py"):
        if "venv" in str(py_file):
            continue

        with open(py_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Check for TODOs or FIXMEs
        for i, line in enumerate(lines):
            if "TODO" in line or "FIXME" in line:
                notes.append(f"🔧 Found TODO/FIXME in {py_file} (line {i+1})")
                vibe_score -= 10

        # Check for long functions
        func_matches = re.findall(r'def .+\):\n((?:\s{4}.+\n)+)', "".join(lines), re.MULTILINE)
        for block in func_matches:
            if block.count("\n") > 25:
                notes.append(f"📏 Long function in {py_file} — consider refactoring")
                vibe_score -= 15

        # Check for debug prints
        for line in lines:
            if "print(" in line and "test" in line:
                notes.append(f"🐞 Debug print found in {py_file}")
                vibe_score -= 5

    emoji = "☕️" if vibe_score >= 80 else "😬" if vibe_score >= 50 else "🔥"
    result = f"{emoji} Cappucino says: Vibe Score: **{vibe_score}/100**"

    payload = {
        "content": result + "\n" + "\n".join(notes[:5] or ["✅ Code vibes are clean. Keep sipping!"])
    }

    requests.post(DISCORD_WEBHOOK_URL, json=payload)

if __name__ == "__main__":
    check_vibes()
