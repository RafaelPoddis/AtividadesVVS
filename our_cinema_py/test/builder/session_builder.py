from test.builder.movie_builder import MovieBuilder
from src.domain.model import Session, Room
from datetime import datetime, timedelta

class SessionBuilder:
    session: Session

    def __init__(self):
        pass

    def aSession(self):
        self.session = Session(room=Room("1"), movie=MovieBuilder().aMovie().with_duration(90).build(), start_time=tomorrow_at_seven_pm)
        return self

    def build(self):
        return self.movie
    
    def with_start_time(self, start_time):
        self.movie.duration = duration
        return self


# room = Room("1")
# room.reserve_seat(1, 2)

# movie = MovieBuilder().aMovie().with_duration(90).build()

# today = datetime.now()
# tomorrow = today + timedelta(days=1)
# tomorrow_at_seven_pm = tomorrow.replace(hour=19, minute=0, second=0, microsecond=0)
# tomorrow_at_eight_thirty_pm = tomorrow.replace(hour=20, minute=30, second=0, microsecond=0)

# session = Session(room=room, movie=movie, start_time=tomorrow_at_seven_pm)