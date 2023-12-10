import pandas as pd

rzd = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115],
        'rzd_revenue': [1093, 2810, 10283, 5774, 981]
    }
)

auto = pd.DataFrame(
    {
        'client_id': [113, 114, 115, 116, 117],
        'auto_revenue': [57483, 83, 912, 4834, 98]
    }
)

air = pd.DataFrame(
    {
        'client_id': [115, 116, 117, 118],
        'air_revenue': [81, 4, 13, 173]
    }
)

client_base = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115, 116, 117, 118],
        'address': ['Комсомольская 4', 'Энтузиастов 8а', 'Левобережная 1а', 'Мира 14', 'ЗЖБИиДК 1',
                    'Строителей 18', 'Панфиловская 33', 'Мастеркова 4']
    }
).set_index('client_id')

joined_revenue = rzd.set_index('client_id').join(auto.set_index('client_id'), how='outer').join(air.set_index('client_id'), how='outer')

print(
    joined_revenue
)

"""
Output:
           rzd_revenue  auto_revenue  air_revenue
client_id
111             1093.0           NaN          NaN
112             2810.0           NaN          NaN
113            10283.0       57483.0          NaN
114             5774.0          83.0          NaN
115              981.0         912.0         81.0
116                NaN        4834.0          4.0
117                NaN          98.0         13.0
118                NaN           NaN        173.0
"""

print(
    joined_revenue.join(client_base, how='left')
)

"""
Output:
           rzd_revenue  auto_revenue  air_revenue          address
client_id
111             1093.0           NaN          NaN  Комсомольская 4
112             2810.0           NaN          NaN   Энтузиастов 8а
113            10283.0       57483.0          NaN  Левобережная 1а
114             5774.0          83.0          NaN          Мира 14
115              981.0         912.0         81.0        ЗЖБИиДК 1
116                NaN        4834.0          4.0    Строителей 18
117                NaN          98.0         13.0  Панфиловская 33
118                NaN           NaN        173.0     Мастеркова 4
"""
