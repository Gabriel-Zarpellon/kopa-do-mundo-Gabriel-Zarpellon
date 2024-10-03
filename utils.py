from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError
from datetime import datetime


def data_processing(team: dict):
    team_titles = team["titles"]

    first_cup_str = team["first_cup"]
    first_cup_date = datetime.strptime(first_cup_str, "%Y-%m-%d")
    first_cup_year = first_cup_date.year
    last_cup_year = 2022

    now = datetime.now()
    possible_cups = (int(now.year) - int(first_cup_year)) / 4

    validate_titles(team_titles)
    validate_cup_year(first_cup_year)
    validate_titles_number(team_titles, possible_cups, first_cup_year, last_cup_year)


def validate_titles(titles: int):
    if titles < 0:
        raise NegativeTitlesError("titles cannot be negative")


def validate_cup_year(year: int):
    if (year - 1930) % 4 != 0 or year < 1930:
        raise InvalidYearCupError("there was no world cup this year")


def validate_titles_number(
    titles: int, possible_cups: int, first_cup_year: int, last_cup_year: int
):
    if titles > possible_cups:
        if first_cup_year == last_cup_year and titles == 1:
            pass
        else:
            raise ImpossibleTitlesError(
                "impossible to have more titles than disputed cups"
            )
