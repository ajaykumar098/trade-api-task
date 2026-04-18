from fastapi import APIRouter, Request, Depends
from app.gemini import get_analysis
from app.utils import verify_key, track, validate_sector

router = APIRouter()


@router.get("/analyze/{sector}")
async def analyze(request: Request, sector: str, api_key: str = Depends(verify_key)):

    # Validate input
    validate_sector(sector)

    # Track session
    ip = request.client.host
    track(ip)

    # Get AI-generated markdown report
    report = await get_analysis(sector)

    return {
        "sector": sector,
        "report": report
    }
