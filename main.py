import pandas as pd
import numpy as np
import csv

from tools import file_io as fio
from tools import time_io as tio


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parent_dir = "/Users/siyanhu/Documents/IETI_ACM_SAMPLE/"
    sample_csv_path = parent_dir + "sample.csv"
    test_csv_path = parent_dir + "ICIIPcsv.csv"

    titles = ['_id', 'conf', 'full_paper', 'type',
              'title_1st', 'first_name_1st', 'mid_name_1st', 'surname_1st', 'suffix_1st',
              'order_1st', 'bool_1st',
              'blank_1', 'blank_2', 'blank_3',
              'email_1st',
              'department_1st', 'univ_1st', 'city_1st', 'state_1st', 'nation_1st',
              'department_2st', 'univ_2st', 'city_2st', 'state_2st', 'nation_2st',
              'catalogue', 'num_1', 'num_2', 'num_3', 'num_4', 'num_5']

    sample_dp = pd.read_csv(sample_csv_path, header=None, names=titles)
    test_dp = pd.read_csv(test_csv_path, header=None, names=titles)

    sample_df = pd.DataFrame(sample_dp)
    test_df = pd.DataFrame(test_dp)

    txt_sample_path = parent_dir + 'txtsample.txt'
    txt_sample_list = list()
    with open(txt_sample_path, 'r') as f:
        content = f.readlines()
        for line in content:
            print(line)
            components = line.split(',')
            print(len(components))
            print(components)
            txt_sample_list.append(components)

    txt_sample_df = pd.DataFrame(txt_sample_list, columns=titles)

    ts = str(tio.current_timestamp(milli_second=False))
    # sample_df.to_csv(parent_dir+'sample_' + ts + '.csv', na_rep=' ', header=False, index=False)
    test_df.to_csv(parent_dir+'test_' + ts + '.csv', na_rep=' ', header=txt_sample_list[0], index=False)
    txt_sample_df.to_csv(parent_dir + 'txt_sample_' + ts + '.csv', na_rep=' ', header=txt_sample_list[0], index=False)


