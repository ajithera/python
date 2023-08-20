def import_csv(csvfilename):
    data = []
    with open(csvfilename, "r", encoding="utf-8", errors="ignore") as scraped:
        reader = csv.reader(scraped, delimiter=',')
        row_index = 0
        for row in reader:
            if row:  # avoid blank lines
                row_index += 1
                columns = [str(row_index), row.index('EMPLOYEE_ID'), row.index('FIRST_NAME')]
                data.append(columns)
    return data

dat = import_csv(file_path)
last_rw = dat[-1]
last_rw
