def save_to_file(file_name, jobs):
    
    file = open(f"{file_name}.csv", "w",encoding='utf-8' )
    
    file.write("Position,Company,Location,URL\n")

    for job in jobs:
        print(f"{job['position']},{job['company']},{job['region']},{job['link']}")
        file.write(f"{job['position']},{job['company']},{job['region']},{job['link']}\n")

    file.close()