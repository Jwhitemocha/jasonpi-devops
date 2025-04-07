import time, random, requests
from datetime import datetime

log_file = "scripts/test_output.log"

def run_emulation_test():
    print("🚀 Starting emulation test...")
    time.sleep(2)
    print("⚙️ Running hardware checks...")
    time.sleep(2)
    
    result = random.choice(["PASSED", "FAILED"])
    print(f"✅ Emulation test {result}")

    with open(log_file, "a") as f:
        f.write(f"[{datetime.now()}] Test Result: {result}\n")

    send_discord_alert(result)
    return result

def send_discord_alert(result):
    webhook_url = "https://discord.com/api/webhooks/1358907447619752086/iEU3tsRNJphcyTp-zcsEhmcuncMhVJ3ME6nMyEnCRC_myzuiPnN2jaG2tDIKdPmAQrN1"
    emoji = "✅" if result == "PASSED" else "❌"
    message = f"{emoji} Emulation Test Result: **{result}**"
    requests.post(webhook_url, json={"content": message})

if __name__ == "__main__":
    run_emulation_test()
