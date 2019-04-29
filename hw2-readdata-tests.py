import numpy as np
import pandas as pd

data = pd.read_csv('https://openei.org/doe-opendata/dataset/5346c5c2-be26-4be7-9663-b5a98cbb7527/resource/096347a1-8be8-4df8-87e3-065531f7215f/download/usretechnicalpotential.csv', index_col = 0)

def test_create_dataframe(df):
    '''
    takes a pandas DataFrame as input and returns True if the following conditions hold:
    - The DataFrame contains only the columns that you specified in #1.
    - The columns contain the correct data type.
    - There are at least 10 rows in the DataFrame.
    '''
    colnames_check = test_colnames(df)
    datatype_check = test_datatypes(df)
    rowcount_check = test_rowcount(df)
    result = colnames_check + datatype_check + rowcount_check
    if result == 3:
        return True
    else:
        return False
    
def test_colnames(df):
    '''
    Check if the dataframe contains only the columns specified in imported dataset.
    Revision: Added .sort() to ensure that the order of columns do not matter.
    '''
    df_isgood = True
    colnames = [
        'urbanUtilityScalePV_GWh',
        'urbanUtilityScalePV_GW',
        'urbanUtilityScalePV_km2',
        'ruralUtilityScalePV_GWh',
        'ruralUtilityScalePV_GW',
        'ruralUtilityScalePV_km2',
        'rooftopPV_GWh',
        'rooftopPV_GW',
        'CSP_GWh',
        'CSP_GW',
        'CSP_km2',
        'onshoreWind_GWh',
        'onshoreWind_GW',
        'onshoreWind_km2',
        'offshoreWind_GWh',
        'offshoreWind_GW',
        'offshoreWind_km2',
        'biopowerSolid_GWh',
        'biopowerSolid_GW',
        'biopowerSolid_BDT',
        'biopowerGaseous_GWh',
        'biopowerGaseous_GW',
        'biopowerGaseous_Tonnes-CH4',
        'geothermalHydrothermal_GWh',
        'geothermalHydrothermal_GW',
        'EGSGeothermal_GWh',
        'EGSGeothermal_GW',
        'hydropower_GWh',
        'hydropower_GW',
        'hydropower_countOfSites'
    ]
    colnames.sort()
    df_colnames = list(df.columns)
    df_colnames.sort()
    if df_colnames == colnames:
        df_isgood = True
        return df_isgood
    else:
        df_isgood = False
        return df_isgood

def test_datatypes(df):
    '''
    Check if the dataframe's columns' datatypes are according to the dataframe specified in imported dataset.
    Revision: Added .sort() and reshuffle the hard-coded column names and types
    to ensure that the order of columns do not matter.
    '''
    df_isgood = True
    dtype_index = np.array([
        'CSP_GW', 'CSP_GWh', 'CSP_km2', 'EGSGeothermal_GW',
        'EGSGeothermal_GWh', 'biopowerGaseous_GW', 'biopowerGaseous_GWh',
        'biopowerGaseous_Tonnes-CH4', 'biopowerSolid_BDT',
        'biopowerSolid_GW', 'biopowerSolid_GWh',
        'geothermalHydrothermal_GW', 'geothermalHydrothermal_GWh',
        'hydropower_GW', 'hydropower_GWh', 'hydropower_countOfSites',
        'offshoreWind_GW', 'offshoreWind_GWh', 'offshoreWind_km2',
        'onshoreWind_GW', 'onshoreWind_GWh', 'onshoreWind_km2',
        'rooftopPV_GW', 'rooftopPV_GWh', 'ruralUtilityScalePV_GW',
        'ruralUtilityScalePV_GWh', 'ruralUtilityScalePV_km2',
        'urbanUtilityScalePV_GW', 'urbanUtilityScalePV_GWh',
        'urbanUtilityScalePV_km2'
    ])
    dtype_columns = np.array([
        'int64', 'int64', 'int64', 'float64', 'float64', 'int64', 'int64',
        'int64', 'int64', 'int64', 'int64', 'int64', 'int64', 'int64',
        'int64', 'int64', 'float64', 'float64', 'float64', 'int64',
        'int64', 'int64', 'int64', 'float64', 'int64', 'int64', 'int64',
        'int64', 'int64', 'int64'
    ])
    datatypes = pd.Series(dtype_columns,index=dtype_index)
    df = df.reindex(sorted(df.columns), axis=1)
    if df.dtypes.equals(datatypes):
        df_isgood = True
        return df_isgood
    else:
        df_isgood = False
        return df_isgood
    
def test_rowcount(df):
    '''
    Check if the number of rows of df is at least 10.
    '''
    if df.shape[0] >= 10:
        df_isgood = True
        return df_isgood
    else:
        df_isgood = False
        return df_isgood
