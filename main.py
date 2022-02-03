import os

from dotenv import load_dotenv

from headhunter import get_hh_stats as hh
from superjob import get_sj_stats as sj
from utils import languages, get_table


def main():
    load_dotenv()
    superjob_token = os.getenv('SJ_API_KEY')
    hh_table_title = 'HeadHunter Moscow'
    sj_table_title = 'SuperJob Moscow'
    print(get_table(hh(languages), hh_table_title))
    print(get_table(sj(languages, superjob_token), sj_table_title))


if __name__ == '__main__':
    main()
