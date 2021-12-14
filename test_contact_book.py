from hamcrest import *
import pytest

from contact_book import Book


def test_read_file():
    b = Book('new_file_1')
    name = 'a'
    surname = 'b'
    mail = 'c'
    phone = 'e'
    work = 'd'
    b.add(name, surname, mail, phone, work)
    b.write_file()
    c = Book('new_file_1')
    p = c.persons[0]
    assert_that(p.name, equal_to(name))
    assert_that(p.surname, equal_to(surname))
    assert_that(p.mail, equal_to(mail))
    assert_that(p.phone, equal_to(phone))
    assert_that(p.work, equal_to(work))