from test.builder.movie_builder import MovieBuilder
from src.domain.model import Room, Session, RoomStatus
from datetime import datetime, timedelta
from src.domain.errors import RoomOccupied, MovieNotFinished
from unittest.mock import patch
import pytest

def test_calculate_session_end_time():
    room = Room("1")
    movie = MovieBuilder().aMovie().with_duration(90).build()
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    tomorrow_at_seven_pm = tomorrow.replace(hour=19, minute=0, second=0, microsecond=0)
    tomorrow_at_eight_thirty_pm = tomorrow.replace(hour=20, minute=30, second=0, microsecond=0)
    session = Session(room=room, movie=movie, start_time=tomorrow_at_seven_pm)
    assert session.end_time() == tomorrow_at_eight_thirty_pm

def test_seat_available():
    room = Room("1")
    room.reserve_seat(1, 2)

    movie = MovieBuilder().aMovie().with_duration(90).build()

    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    tomorrow_at_seven_pm = tomorrow.replace(hour=19, minute=0, second=0, microsecond=0)
    tomorrow_at_eight_thirty_pm = tomorrow.replace(hour=20, minute=30, second=0, microsecond=0)

    session = Session(room=room, movie=movie, start_time=tomorrow_at_seven_pm)
    assert session.seat_available(1, 1) == True
    assert session.seat_available(2, 1) == False

def test_all_available_seats():
    room = Room("1")
    room.reserve_seat(1, 2)

    movie = MovieBuilder().aMovie().with_duration(90).build()

    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    tomorrow_at_seven_pm = tomorrow.replace(hour=19, minute=0, second=0, microsecond=0)
    tomorrow_at_eight_thirty_pm = tomorrow.replace(hour=20, minute=30, second=0, microsecond=0)

    session = Session(room=room, movie=movie, start_time=tomorrow_at_seven_pm)
    assert session.get_all_available_seats() == 99

    room.reserve_seat(1, 3)
    room.reserve_seat(1, 4)
    room.reserve_seat(1, 5)
    assert session.get_all_available_seats() == 96

def test_session_overlap_same_room():
    room = Room("1")

    movie = MovieBuilder().aMovie().with_duration(90).build()

    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    tomorrow_at_seven_pm = tomorrow.replace(hour=19, minute=0, second=0, microsecond=0)
    tomorrow_at_eight_thirty_pm = tomorrow.replace(hour=20, minute=30, second=0, microsecond=0)

    session1 = Session(room=room, movie=movie, start_time=tomorrow_at_seven_pm)

    with pytest.raises(RoomOccupied):
        Session(room=room, movie=movie, start_time=tomorrow_at_seven_pm)



def test_release_room_when_session_is_finished():

    room = Room("1")

    movie1 = MovieBuilder().aMovie().with_duration(90).build()

    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    tomorrow_at_seven_pm = tomorrow.replace(hour=19, minute=0, second=0, microsecond=0)
    tomorrow_at_eight_forty_pm = tomorrow.replace(hour=20, minute=40, second=0, microsecond=0)
    session1 = Session(room=room, movie=movie1, start_time=tomorrow_at_seven_pm)
    session1.release_room_when_finished(tomorrow_at_eight_forty_pm)

    assert session1.room.status == RoomStatus.AVAILABLE

def test_release_room_with_movie_not_finished():
    room = Room("1")

    movie1 = MovieBuilder().aMovie().with_duration(90).build()

    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    tomorrow_at_seven_pm = tomorrow.replace(hour=19, minute=0, second=0, microsecond=0)
    tomorrow_at_seven_forty_pm = tomorrow.replace(hour=19, minute=30, second=0, microsecond=0)
    session1 = Session(room=room, movie=movie1, start_time=tomorrow_at_seven_pm)

    with pytest.raises(MovieNotFinished):
        session1.release_room_when_finished(tomorrow_at_seven_forty_pm)

