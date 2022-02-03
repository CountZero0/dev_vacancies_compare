from terminaltables import AsciiTable

languages = [
    'JavaScript',
    'Java',
    'Python',
    'Ruby',
    'PHP',
    'C++',
    'C#',
    'C',
    'Go',
    'Objective-C',
    'Scala',
    'Swift',
    'TypeScript',
    'Kotlin'
]


def predict_rub_salary(salary_from, salary_to):
    if salary_from and salary_to:
        return (salary_from + salary_to) / 2
    elif salary_to:
        return salary_to * 0.8
    elif salary_from:
        return salary_from * 1.2


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
