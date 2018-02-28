import csv

with open('names.csv', 'r') as cf:
    cf_read = csv.DictReader(cf)

    with open('name.csv', 'w') as cw:
        field_names = ['first_name', 'last_name', 'email']
        cf_writer = csv.DictWriter(cw, fieldnames=field_names, delimiter='\t')
        cf_writer.writeheader()
        for l in cf_read:
            del l['email']
            cf_writer.writerow(l)


