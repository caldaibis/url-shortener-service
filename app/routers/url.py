from fastapi.responses import Response, RedirectResponse
from app.database.session import SessionLocal, get_db
from fastapi import APIRouter, Request, Depends, HTTPException, status
from app.database.models import Url
from app.database.schemas import UrlRequest, UrlResponse
from app.util.helpers import hashcode, shortlink

router = APIRouter()

@router.post("/shorten", response_model=UrlResponse, status_code=status.HTTP_201_CREATED)
async def create_shortlink(url: UrlRequest, request: Request, db: SessionLocal = Depends(get_db)) -> Response:
    url_object: Url = db.query(Url).filter(Url.original == url.url).first()
    
    if not url_object:
        url_object = Url(url.url, hashcode(url.url))
        db.add(url_object)
        db.commit()
        db.refresh(url_object)
        
        return UrlResponse(
            original=url_object.original,
            shortlink=shortlink(request, url_object.hashcode),
            hits=url_object.hits,
            created_on=url_object.created_on
        )
    
    return RedirectResponse(url=shortlink(request, url_object.hashcode), status_code=303)

@router.get("/urls/{input_hashcode}")
async def redirect_to_url(input_hashcode: str, db: SessionLocal = Depends(get_db)) -> RedirectResponse:
    url_object: Url = db.query(Url).filter(Url.hashcode == input_hashcode).first()
    
    if not url_object:
        raise HTTPException(status_code=404, detail="Url not found!")
    
    # Increment 'hits' column
    url_object.hits += 1
    db.commit()
    db.refresh(url_object)
    
    return RedirectResponse(url=url_object.original, status_code=307)

@router.get("/urls/{input_hashcode}/stats", response_model=UrlResponse)
async def shortlink_stats(input_hashcode: str, request: Request, db: SessionLocal = Depends(get_db)) -> UrlResponse:
    url: Url = db.query(Url).filter(Url.hashcode == input_hashcode).first()
    
    if not url:
        raise HTTPException(status_code=404, detail="Url not found!")
    
    return UrlResponse(
        original=url.original,
        shortlink=shortlink(request, url.hashcode),
        hits=url.hits,
        created_on=url.created_on
    )
