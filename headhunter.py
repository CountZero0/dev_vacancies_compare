import requests

from utils import predict_rub_salary


def get_hh_language_stat(language):
    payload = {
        "text": f"name:Программист {language}",
        "area": 1,
        "period": 30,
        'per_page': 100,
    }

    vacancies_processed = 0
    salary_total = 0
    page = 0
    vacancies = 0
    pages_number = 1

    while page < pages_number:
        response = requests.get('https://api.hh.ru/vacancies', params=payload)
        response.raise_for_status()
        vacancies = response.json()
        pages_number = vacancies['pages']

        for vacancy in vacancies['items']:
            salary = predict_rub_salary_hh(vacancy)
            if salary:
                salary_total += salary
                vacancies_processed += 1

        page += 1

    average_salary = int(salary_total / vacancies_processed)
    vacancies_found = vacancies['found']
    return vacancies_processed, average_salary, vacancies_found


def predict_rub_salary_hh(vacancy):
    salary_data = vacancy['salary']
    if salary_data and salary_data['currency'] == 'RUR':
        salary_from = salary_data['from']
        salary_to = salary_data['to']
        return predict_rub_salary(salary_from, salary_to)


def get_hh_stats(all_languages):
    all_languages_stats = {}
    for language in all_languages:
        vacancies_processed, average_salary, vacancies_found = get_hh_language_stat(language)
        all_languages_stats[language] = {
            'vacancies_found': vacancies_found,
            'vacancies_processed': vacancies_processed,
            'average_salary': average_salary
        }
    return all_languages_stats
