import sys
import pandas as pd


COLUMNS = ['mass', 'fat', 'prot', 'carb', 'energy']


def main(reference_name, values_name):
    for values_name in values_names:
        print_calories(reference_name, values_name)


def print_calories(reference_name, values_name):
    print(reference_name, values_name)
    reference = pd.read_csv(reference_name, index_col='name')
    values = pd.read_csv(values_name, index_col='name')
    values = values.groupby(level=0).sum()

    result = pd.DataFrame()
    for name in values.index:
        row = reference.loc[name] * values.loc[name].mass / 100.0
        row['mass'] = values.loc[name].mass
        result = result.append(row)

    result = result[COLUMNS]
    result = result.append(pd.DataFrame(result.sum(axis=0), columns=['total']).T)
    print(result)


if __name__ == '__main__':
    reference_name = 'reference.csv'
    values_names = ['values.csv']
    if len(sys.argv) > 2:
        reference_name = sys.argv[1]
        values_names = sys.argv[2:]
    main(reference_name, values_names)
