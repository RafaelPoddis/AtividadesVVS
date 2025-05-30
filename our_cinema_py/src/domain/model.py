from src.domain.errors import DuplicateRoomName, DuplicateMovieId
from dataclasses import dataclass, field
from datetime import timedelta
from enum import Enum

class SeatStatus(Enum):
    AVAILABLE = "available"
    RESERVED = "reserved"
    OCCUPIED = "occupied"

@dataclass
class Seat:
    row: str
    number: int
    status: SeatStatus = SeatStatus.AVAILABLE

    @property
    def is_available(self):
        return self.status == SeatStatus.AVAILABLE
    
    def reserve(self):
        if self.status == SeatStatus.AVAILABLE:
            self.status = SeatStatus.RESERVED
            return True
        return False
    
    def confirm(self):
        if self.status == SeatStatus.RESERVED:
            self.status = SeatStatus.OCCUPIED
            return True
        return False
    
    def release(self):
        self.status = SeatStatus.AVAILABLE

    
@dataclass
class Room:
    name: str
    rows: list[list[Seat]]

    def __init__(self, name, seats=None):
        self.name = name
        self.rows = []
        if seats is None:
            self.create_list_of_seats()
            return
        i = 65
        for row in seats:
            row_seats = []
            row_name = chr(i)
            for j in range(row):
                seat = Seat(row=row_name, number=j+1)
                row_seats.append(seat)
            self.rows.append(row_seats)
            i += 1

    def create_list_of_seats(self):
        for i in range(10):
            row = chr(i + 65)
            row_seats = []
            for j in range(10):
                seat = Seat(row=row, number=j+1)
                row_seats.append(seat)
            self.rows.append(row_seats)

    def capacity(self):
        seats = 0
        for row in self.rows:
            seats += len(row)
        return seats
    
    def available_seats(self):
        available_seats = 0
        for row in self.rows:
            for seat in row:
                if seat.is_available:
                    available_seats += 1
        return available_seats
    
@dataclass
class Theater:
    rooms: list[Room] = field(default_factory=list)

    def add(self, room):
        if self.duplicate_room_name(room):
            raise DuplicateRoomName()
        self.rooms.append(room)

    def remove(self, room):
        self.rooms.remove(room)

    def duplicate_room_name(self, room):
        return [theater_room for theater_room in self.rooms if theater_room.name == room.name]

@dataclass
class Movie:
    name: str
    duration: int
    movie_id: int

    _existing_ids = set()

    def __init__(self, name, movie_id, duration):
        if movie_id in Movie._existing_ids:
            raise DuplicateMovieId
        
        self.name = name
        self.movie_id = movie_id
        self.duration = duration
        Movie._existing_ids.add(movie_id)

    def get_formatted_duration(self) -> str:
        horas: int = self.duration // 60
        minutes: int = self.duration % 60
        return f"{horas}h{minutes}min"
    
    def get_duration_as_timedelta(self) -> timedelta:
        horas: int = self.duration // 60
        minutes: int = self.duration % 60
        return timedelta(minutes=self.duration)

    def duplicate_movie_id(self, movie_id):
        return [theater_room for theater_room in self.movie_id if theater_room == movie_id]