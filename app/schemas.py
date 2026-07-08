from pydantic import BaseModel, ConfigDict
from datetime import date, datetime
from typing import List, Optional

# Comic
class ComicBase(BaseModel):
    title: str
    link: str
    release_date: Optional[date] = None
    cover_date: Optional[date] = None

class ComicCreate(ComicBase):
    pass

class ComicOut(ComicBase):
    id: int
    volume_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

# Processed Volumes
class ProcessedVolumeBase(BaseModel):
    title: str

class ProcessedVolumeCreate(ProcessedVolumeBase):
    pass

class ProcessedVolumeOut(ProcessedVolumeBase):
    id: int
    processed_at: datetime
    model_config = ConfigDict(from_attributes=True)

# Processed Volume con comics
class ProcessedVolumeDetailOut(ProcessedVolumeOut):
    comics: List[ComicOut] = []
    model_config = ConfigDict(from_attributes=True)