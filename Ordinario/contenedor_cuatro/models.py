from enum import unique
from operator import truediv
from sqlalchemy import  Integer, String, Column
from base_alchemy import *

class AnimeBySearch(Base):
    __tablename__ = 'animebysearch'
    id = Column (Integer, primary_key = True)
    page_id = Column (Integer)
    title = Column (String(150), unique = True)
    episodes = Column (String(20))
    type = Column (String(20))
    rated = Column (String(20))
    image_url = Column (String(200))
    score = Column (String(20))
    synopsis = Column (String(5000))
    airing = Column (String(50))
    members = Column (String(50))

    def __init__(self, page_id, title, episodes, type, rated, image_url, score, synopsis, airing, members) -> None:
        self.page_id = page_id
        self.title = title
        self.episodes = episodes
        self.type = type
        self.rated = rated
        self.image_url = image_url
        self.score = score
        self.synopsis = synopsis
        self.airing = airing
        self.members = members


class AnimeByGenre(Base):
    __tablename__ = 'animebygenre'
    id = Column (Integer, primary_key = True)
    id_genre = Column(Integer)
    page_id = Column (Integer)
    title = Column (String(150), unique = True)
    image_url = Column (String(200))
    episodes = Column (String(20))
    airing = Column (String(50))
    type = Column (String(20))
    start_date = Column (String(50))
    end_date = Column (String(50))
    members = Column (String(50))
    rated = Column (String(20))

    def __init__(self,id_genre, page_id, title, image_url, episodes, airing, type, start_date, end_date, members, rated) -> None:
        self.id_genre = id_genre
        self.page_id = page_id
        self.title = title
        self.image_url = image_url
        self.episodes = episodes
        self.airing = airing
        self.type = type
        self.start_date = start_date
        self.end_date = end_date
        self.members = members
        self.rated = rated


class AnimeById(Base):
    __tablename__ = 'animebyid'
    id = Column(Integer, primary_key = True)
    page_id = Column(Integer)
    image_url = Column(String(200))
    title = Column(String(150), unique = True)
    episodes = Column(String(20))
    status = Column(String(75))
    score = Column(String(20))
    rank = Column(String(20))
    duration = Column(String(50))
    synopsis = Column(String(3000))
    premiered = Column(String(50))
    broadcast = Column(String(80))

    def __init__(self, page_id, image_url ,title, episodes, status, score, rank, duration, synopsis, premiered, broadcast) -> None:
        self.page_id = page_id
        self.image_url = image_url
        self.title = title
        self.episodes = episodes
        self.status = status
        self.score = score
        self.rank = rank
        self.duration = duration
        self.synopsis = synopsis
        self.premiered = premiered
        self.broadcast = broadcast


class MangaSearch(Base):
    __tablename__ = 'mangabysearch'
    id = Column(Integer, primary_key = True)
    page_id = Column(Integer)
    image_url = Column(String(200))
    title = Column(String(150), unique = True)
    publishing = Column(String(50))
    type = Column(String(20))
    chapters = Column(String(20))
    volumes = Column(String(20))
    synopsis = Column(String(3000))
    start_date = Column(String(50))
    end_date = Column(String(50))

    def __init__(self, page_id, image_url ,title, publishing, type, chapters, volumes, synopsis, start_date, end_date) -> None:
        self.page_id = page_id
        self.image_url = image_url
        self.title = title
        self.publishing = publishing
        self.type = type
        self.chapters = chapters
        self.volumes = volumes
        self.synopsis = synopsis
        self.start_date = start_date
        self.end_date = end_date
        
