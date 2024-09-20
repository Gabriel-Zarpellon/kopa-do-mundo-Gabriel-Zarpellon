from exceptions import NegativeTitleError, InvalidYearCupError, ImpossibleTitlesError
from datetime import datetime


def data_processing(team: dict):
    team_titles = team['titles']

    first_cup_str = team['first_cup']
    first_cup_date = datetime.strptime(first_cup_str, "%Y-%m-%d")
    first_cup_year = first_cup_date.year

    now = datetime.now()
    possible_cups = (int(now.year) - int(first_cup_year)) / 4

    def validate_titles(titles: int):
        if titles < 0:
            raise NegativeTitleError()

    try:
        validate_titles(team_titles)
    except NegativeTitleError as err:
        return err.message

    def validate_cup_year(year: int):
        if (year - 1930) % 4 != 0 or year < 1930:
            raise InvalidYearCupError()

    try:
        validate_cup_year(first_cup_year)
    except InvalidYearCupError as err:
        return err.message

    def validate_titles_number(titles: int):
        if titles > possible_cups:
            raise ImpossibleTitlesError()

    try:
        validate_titles_number(team_titles)
    except ImpossibleTitlesError as err:
        return err.message
