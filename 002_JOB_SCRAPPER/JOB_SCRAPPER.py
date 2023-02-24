from extractors.wwr import extract_wwr_job
from file import save_to_file

keyword = input("What do you want to search for?")

jobs = extract_wwr_job(keyword)

save_to_file(keyword,jobs)
