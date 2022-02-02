import requests

from utils import predict_rub_salary


def get_sj_language_stat(language, superjob_token):
    headers = {
        'X-Api-App-Id': superjob_token
    }
    payload = {
        "town": 4,
        "keywords": f"Разработчик {language}",
        "period": 30,
        'count': 100,
        "catalogues": 48,
    }

    vacancies_processed = 0
    salary_total = 0
    average_salary = 0
    more = True
    page = 0
    vacancies = 0

    while more:
        payload['page'] = page
        page += 1
        response = requests.get('https://api.superjob.ru/2.0/vacancies',
                                params=payload, headers=headers)
        response.raise_for_status()
        vacancies = response.json()
        more = vacancies['more']

        for vacancy in vacancies['objects']:
            salary = predict_rub_salary_sj(vacancy)
            if salary:
                salary_total += salary
                vacancies_processed += 1

        page += 1

    if vacancies_processed != 0:
        average_salary = int(salary_total / vacancies_processed)
    vacancies_found = vacancies['total']
    return vacancies_processed, average_salary, vacancies_found


def get_sj_stats(all_languages, superjob_token):
    all_languages_stats = {}
    for language in all_languages:
        vacancies_processed, average_salary, vacancies_found = get_sj_language_stat(language, superjob_token)
        all_languages_stats[language] = {
            'vacancies_found': vacancies_found,
            'vacancies_processed': vacancies_processed,
            'average_salary': average_salary
        }
    return all_languages_stats


def predict_rub_salary_sj(vacancy):
    if vacancy and vacancy['currency'] == 'rub':
        return predict_rub_salary(vacancy['payment_from'], vacancy['payment_to'])
