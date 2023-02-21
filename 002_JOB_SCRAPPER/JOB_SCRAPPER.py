from extractors.wwr import extract_wwr_job

keyword = input("What do you want to search for?")

file = open(f"{keyword}.csv", "w",encoding='utf-8' )

file.write("Position,Company,Location,URL\n")

jobs = extract_wwr_job("python")

for job in jobs:
    print(f"{job['position']},{job['company']},{job['region']},{job['link']}")
    file.write(f"{job['position']},{job['company']},{job['region']},{job['link']}\n")

file.close()
