# coding: utf-8
import pandas as pd
df = pd.read_parquet('clean/hh-tus-2024.parquet')
to_remove = ['schedule_id', 'schedule', 'survey_year',
             'nss_region', 'stratum', 'sub_stratum',
             'sub_round', 'fod_sub_region', 'informant_sl_no']
df.drop(to_remove, axis=1, inplace=True)
