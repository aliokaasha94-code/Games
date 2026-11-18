import requests
import json

base_url = "https://emad-afandi-games-hub.pages.dev"

# 1. Test /api/games (Queries D1 live)
print("Testing /api/games...")
try:
    r = requests.get(f"{base_url}/api/games", timeout=10)
    print(f"Status: {r.status_code}")
    data = r.json()
    games = data.get('games', [])
    print(f"Games returned from D1: {len(games)}")
    if games:
        print(f"First game from D1: {games[0].get('name')} ({games[0].get('id')})")
except Exception as e:
    print("Error /api/games:", e)

# 2. Test /api/chat with Gemini AI
print("\nTesting /api/chat...")
try:
    payload = {
        "messages": [
            {"role": "user", "content": "رشحلي لعبة خفيفة لشخصين في الكافيه"}
        ]
    }
    r = requests.post(f"{base_url}/api/chat", json=payload, timeout=15)
    print(f"Status: {r.status_code}")
    print("Response preview:", r.text[:200])
except Exception as e:
    print("Error /api/chat:", e)
