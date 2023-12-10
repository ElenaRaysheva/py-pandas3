import pandas as pd

def source_type(param):
    traffic_source = param.traffic_source.lower()
    region = param.region.lower()

    if traffic_source in ['yandex', 'google']:
        return 'organic'

    if traffic_source in ['paid', 'email'] and region == 'russia':
        return 'ad'
    elif region != 'russia':
        return 'other'

    return param.traffic_source


logs = pd.read_csv('./visit_log.csv', sep=';')
logs['source_type'] = logs.apply(source_type, 1)

print(logs)

"""
Output:
        timestamp    visit_id                                 url   region     user_id traffic_source source_type
0      1549980692  e3b0c44298  https://host.ru/3c19b4ef7371864fa3   Russia  b1613cc09f         yandex     organic
1      1549980704  6e340b9cff  https://host.ru/c8d9213a31839f9a3a   Russia  4c3ec14bee         direct      direct
2      1549980715  96a296d224  https://host.ru/b8b58337d272ee7b15   Russia  a8c40697fb         yandex     organic
3      1549980725  709e80c884  https://host.ru/b8b58337d272ee7b15   Russia  521ac1d6a0         yandex     organic
4      1549980736  df3f619804  https://host.ru/b8b58337d272ee7b15   Russia  d7323c571c         yandex     organic
...           ...         ...                                 ...      ...         ...            ...         ...
18933  1550094288  57e5ba8560  https://host.ru/c2382eb3d6afc8d0f3  Belarus  98b19810d0           paid       other
18934  1550094296  6f9389ec1b  https://host.ru/f1eb4601740d627ab0   Russia  32ebb20c13           paid          ad
18935  1550094308  e8cf2eb8e6  https://host.ru/a5dda93e70318570c0  Belarus  b85baa8c73         yandex     organic
18936  1550094314  79530b9a67  https://host.ru/6fda01ec57f23abc9e   Russia  e154b06121           paid          ad
18937  1550094323  b3b634f824  https://host.ru/39fa884393666d45fc   Russia  7d27a58fb8          email          ad
"""
