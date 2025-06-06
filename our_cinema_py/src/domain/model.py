from dataclasses import dataclass, field
from enum import Enum
from src.domain.errors import DuplicateRoomName, RoomOccupied
from datetime import datetime, timedelta

class SeatStatus(Enum):
    AVAILABLE = "available"
    RESERVED = "reserved"
    OCCUPIED = "occupied"

class RoomStatus(Enum):
    AVAILABLE = "available"
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

    
ASCII_CODE_FOR_A = 65

@dataclass
class Room:
    name: str
    rows: list[list[Seat]]
    status: RoomStatus = RoomStatus.AVAILABLE

    def __init__(self, name, seats=None):
        self.name = name
        self.rows = []
        if seats is None:
            self.create_list_of_seats()
            return
        row_code = ASCII_CODE_FOR_A
        for row in seats:
            row_seats = []
            row_name = chr(row_code)
            for j in range(row):
                seat = Seat(row=row_name, number=j+1)
                row_seats.append(seat)
            self.rows.append(row_seats)
            row_code += 1

    @property
    def is_available(self):
        return self.status == RoomStatus.AVAILABLE
    
    def reserve(self):
        if self.status == RoomStatus.AVAILABLE:
            self.status = RoomStatus.OCCUPIED
            return True
        return False
    
    def release(self):
        self.status = RoomStatus.AVAILABLE

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

    def reserve_seat(self, row_index: int, seat_index: int) -> bool:
        self.rows[row_index][seat_index].reserve()

        return self.rows[row_index][seat_index].confirm()
            
    def check_if_seat_is_available(self, seat_index: int, row_index: int) -> bool:

        return self.rows[row_index][seat_index].is_available
        
    
@dataclass
class Theater:
    rooms: list[Room] = field(default_factory=list)

    def add(self, room):
        if self.duplicate_room_name(room):
            raise DuplicateRoomName
        self.rooms.append(room)

    def remove(self, room):
        self.rooms.remove(room)

    def duplicate_room_name(self, room):
        return [theater_room for theater_room in self.rooms if theater_room.name == room.name]
    
@dataclass
class Movie:
    title: str
    genre: str
    duration: int

    def formatted_duration(self):
        hours = self.duration // 60
        minutes = self.duration % 60
        if minutes > 0 and hours > 0:
            return f"{hours}h{minutes}min"
        elif hours > 0:
            return f"{hours}h"
        else:
            return f"{minutes}min"
        
    def get_duration_as_timedelta(self):
        return timedelta(minutes=self.duration)
        
@dataclass
class Session:
    room: Room
    movie: Movie
    start_time: datetime

    def __init__(self, room, movie, start_time):
        self.room = room
        self.movie = movie
        self.start_time = start_time

        if self.room.reserve() == False:
            raise RoomOccupied

    def end_time(self):
        return self.start_time + self.movie.get_duration_as_timedelta()

    def seat_available(self, seat_index: int, row_index: int) -> bool:
        return self.room.check_if_seat_is_available(seat_index, row_index)

    def get_all_available_seats(self):
        return self.room.available_seats()
    
    
    #mock nao funcionou
    def release_room_when_finished(self, current_time: datetime):


        if self.end_time() <= current_time:
            self.room.release()
        
        return
    
# 6. Detect session overlap same room
