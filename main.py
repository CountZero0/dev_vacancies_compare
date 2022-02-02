import os

from dotenv import load_dotenv
from terminaltables import AsciiTable

from headhunter import get_hh_stats as hh
from superjob import get_sj_stats as sj
from utils import languages


def get_table(all_languages_stats, table_title=''):
    table_data = [
        [
            'Язык программирования',
            'Вакансий найдено',
            'Вакансий обработано',
            'Средняя зарплата'
        ]
    ]

    for language, stats in all_languages_stats.items():
        table_data.append(
            [
                language,
                stats['vacancies_found'],
                stats['vacancies_processed'],
                stats['average_salary']
            ]
        )
    table = AsciiTable(table_data, table_title)
    return table.table


def main():
    load_dotenv()
    superjob_token = os.getenv('SJ_API_KEY')
    hh_table_title = 'HeadHunter Moscow'
    sj_table_title = 'SuperJob Moscow'
    print(get_table(hh(languages), hh_table_title))
    print(get_table(sj(languages, superjob_token), sj_table_title))


if __name__ == '__main__':
    main()
