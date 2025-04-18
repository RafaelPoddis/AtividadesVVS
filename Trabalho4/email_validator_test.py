import pytest
from email_validator import validate

def test_should_not_accept_null_strings():
    email = None
    assert not validate(email)

def test_should_not_accept_invalid_input():
    email = 3
    assert not validate(email)

def test_should_not_accept_empty_strings():
    email = ''
    assert not validate(email)

def test_should_accept_valid_email():
    email = 'any@mail.com'
    assert validate(email)

def test_should_not_accept_strings_larger_than_320_chars():
    # email = 'l' * 64 + '@' + 'd' * 128 + '.' + 'd' * 127
    email = 'l' * 64 + '@' + 'd' * 63 + '.' + 'e' * 63 + '.' + 'd' * 63 + '.' + 'e' * 63 + '.com'
    assert not validate(email)

def test_should_accept_strings_equals_to_320_chars():
    email = 'l' * 64 + '@' + 'd' * 63 + '.' + 'e' * 63 + '.' + 'd' * 63 + '.' + 'e' * 63
    print(len(email))
    assert validate(email)

def test_should_not_accept_domain_part_larger_than_255_chars():
    email = 'local@' + 'd' * 128 + '.' + 'd' * 127
    assert not validate(email)

def test_should_not_accept_domain_part_larger_than_255_chars_and_local_part_larger_than_64():
    email = 'l' * 128 + '@' + 'd' * 128 + '.com'
    assert not validate(email)

def test_should_not_accept_local_part_larger_than_64_chars():
    email = 'l' * 65 + '@mail.com'
    assert not validate(email)

def test_should_not_accept_local_part_with_two_dots():
    email = 'any..email@mail.com'
    assert not validate(email)

def test_should_not_accept_local_part_with_ending_dot():
    email = 'any.@mail.com'
    assert not validate(email)

def test_should_not_accept_empty_local_part():
    email = '@mail.com'
    assert not validate(email)

def test_should_not_accept_empty_domain():
    email = 'any@'
    assert not validate(email)

def test_should_not_accept_domain_with_part_larger_than_63_chars():
    email = 'any@' + 'd' * 64 + '.com'
    assert not validate(email)

def test_should_accept_domain_with_part_equals_to_63_chars():
    email = 'any@' + 'd' * 63+ '.com'
    assert validate(email)

def test_should_not_accept_local_part_with_space():
    email = 'any email@mail.com'
    assert not validate(email)


def test_should_not_accept_email_without_an_at_sign():
    email = 'anymail.com'
    assert not validate(email)

def test_should_not_accept_non_strings():
    email = 2
    assert not validate(email)

def test_should_not_accept_local_part_with_invalid_char():
    email = 'anyç@mail.com'
    assert not validate(email)

def test_should_not_accept_domain_part_with_invalid_char():
    email = 'any@mailç.com'
    assert not validate(email)

def test_should_not_accept_multiple_at_sign():
    email = "any@@@mail.com"

    assert not validate(email)
