import json
import tabulate

if __name__ == "__main__":
    o = {}
    with open('./simple-data.json') as file:
        o = json.load(file)

    for record in o['imdata']:
        for subject in record:
            values = []
            l = []
            for k in record[subject]['attributes']:
                l.append(record[subject]['attributes'][k])
            values.append(l)
            print(subject)
            print(tabulate.tabulate(values, headers=record[subject]['attributes']))
            print('\n')

