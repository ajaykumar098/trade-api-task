import httpx
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")


# ✅ FALLBACK REPORT (always works)
def fallback_report(sector: str):
    return f"""
# 📊 Trade Opportunity Report: {sector.title()} Sector (India)

## 🧾 Executive Summary
The {sector} sector in India plays a significant role in economic growth and employment generation.

## 📈 Market Overview
The sector is expanding steadily with increasing domestic demand and export potential.

## 🚀 Key Growth Drivers
- Government initiatives  
- Increasing investments  
- Technological advancements  

## 💰 Trade Opportunities
- Export expansion  
- Supply chain development  
- Infrastructure investments  

## ⚠️ Risks & Challenges
- Market volatility  
- Regulatory changes  

## 🔮 Future Outlook
The sector is expected to grow with strong policy support and innovation.

---
*(Fallback report used due to AI issue)*
"""


async def get_analysis(sector: str):

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

    prompt = f"""
Generate a detailed markdown report for the Indian {sector} sector.

Include:
- Executive Summary
- Market Overview
- Growth Drivers
- Trade Opportunities
- Risks
- Future Outlook

Return ONLY markdown.
"""

    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    try:
        async with httpx.AsyncClient(timeout=30) as client:
            res = await client.post(url, json=payload)

        if res.status_code != 200:
            return fallback_report(sector)

        data = res.json()

        if "candidates" not in data:
            return fallback_report(sector)

        candidate = data["candidates"][0]

        if "content" not in candidate or "parts" not in candidate["content"]:
            return fallback_report(sector)

        return candidate["content"]["parts"][0]["text"]

    except Exception:
        return fallback_report(sector)