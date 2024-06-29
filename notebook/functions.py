import pandas as pd


def lowercase_columns(df: pd.DataFrame) -> pd.DataFrame:
    '''
    This function does...

    Inputs:
    ... type

    Outputs:
    ... type
    '''


    df.columns = df.columns.str.lower().str.replace(' ', '_')
    for col in df.columns:
        if df[col].dtype == 'object':  # Check if the column contains strings/object type
            df[col] = df[col].str.lower().str.replace(' ', '_')
    
    return df


