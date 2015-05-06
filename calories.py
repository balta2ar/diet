import sys
import pandas as pd


#: All known columns
COLUMNS = ['mass', 'fat', 'prot', 'carb', 'cal', 'cost']

#: Columns that are used to calculate total_% column
TOTAL = ['fat', 'prot', 'carb']


def main(reference_name, values_name):
    pd.set_option('precision', 2)
    for values_name in values_names:
        print_calories(reference_name, values_name)


def print_calories(reference_name, values_name):
    print(reference_name, values_name)
    reference = pd.read_csv(reference_name, index_col='name', comment='#')
    values = pd.read_csv(values_name, index_col='name', comment='#')
    values = values.groupby(level=0).sum()

    result = pd.DataFrame()
    for name in values.index:
        if name in reference.index:
            row = reference.loc[name] * values.loc[name].mass / 100.0
        else:
            row = pd.DataFrame([[0.0] * len(COLUMNS)],
                               [name], COLUMNS)
        row['mass'] = values.loc[name].mass
        result = result.append(row)

    # Reorder columns
    result = result[COLUMNS]

    # Produce total
    total = pd.DataFrame(result.sum(axis=0), columns=['total']).T
    result = result.append(total)

    # Produce % of fat, prot, carb
    total_sum = total[TOTAL].values.sum()
    total_percent = total * 0
    total_percent.update(100 * total[TOTAL] / total_sum)
    total_percent.rename(index={'total': 'total_%'}, inplace=True)
    result = result.append(total_percent)

    # TODO: add cost/price

    print(result)


if __name__ == '__main__':
    reference_name = 'reference.csv'
    values_names = ['values.csv']
    if len(sys.argv) > 2:
        reference_name = sys.argv[1]
        values_names = sys.argv[2:]
    main(reference_name, values_names)
