import pytest
from datetime import timedelta
from src.domain.model import Movie
from src.domain.errors import DuplicateMovieId

def test_must_have_unique_id():
    
    Movie._existing_ids.clear()

    movie1 = Movie("The Matrix", 1, 136)
    assert movie1.movie_id == 1
    
    with pytest.raises(DuplicateMovieId):
        Movie("Avatar", 1, 162)

def test_must_get_formatted_duration():
    
    Movie._existing_ids.clear()

    movie1 = Movie("Movie 1", 1, 120)
    assert movie1.get_formatted_duration() == "2h0min"
    
    movie2 = Movie("Movie 2", 2, 136)
    assert movie2.get_formatted_duration() == "2h16min"
    
    movie3 = Movie("Movie 3", 3, 45)
    assert movie3.get_formatted_duration() == "0h45min"
    
    movie4 = Movie("Movie 4", 4, 60)
    assert movie4.get_formatted_duration() == "1h0min"

def test_must_get_duration_as_timedelta():
    
    Movie._existing_ids.clear()
    
    movie1 = Movie("Movie 1", 1, 120)
    duration = movie1.get_duration_as_timedelta()
    expected = timedelta(minutes=120)
    assert duration == expected
    
    movie2 = Movie("Movie 2", 2, 136)
    duration = movie2.get_duration_as_timedelta()
    expected = timedelta(minutes=136)
    assert duration == expected
    
    movie3 = Movie("Movie 3", 3, 45)
    duration = movie3.get_duration_as_timedelta()
    expected = timedelta(minutes=45)
    assert duration == expected