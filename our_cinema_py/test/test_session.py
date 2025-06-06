from test.builder.movie_builder import MovieBuilder
from src.domain.model import Room, Session
from datetime import datetime, timedelta

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

    movie = MovieBuilder().aMovie().with_duration(90).build()

    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    tomorrow_at_seven_pm = tomorrow.replace(hour=19, minute=0, second=0, microsecond=0)
    tomorrow_at_eight_thirty_pm = tomorrow.replace(hour=20, minute=30, second=0, microsecond=0)

    session = Session(room=room, movie=movie, start_time=tomorrow_at_seven_pm)

    
