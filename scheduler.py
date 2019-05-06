from multiprocessing import Process

from crawl import crawl_run
from validate import check_run
from flask_api import api_run


if __name__ == '__main__':
    crawler_process = Process(target=crawl_run)
    check_process = Process(target=check_run)
    api_process = Process(target=api_run)

    crawler_process.start()
    check_process.start()
    api_process.start()

    crawler_process.join()
    check_process.join()
    api_process.join()
