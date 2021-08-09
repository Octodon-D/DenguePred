import numpy as np
from sklearn.metrics import mean_squared_error, explained_variance_score, mean_absolute_error
import pandas as pd
import matplotlib.pyplot as plt


def plotting_time_feat(df, features, start, stop, scaler=False):
    """
    Function subsets input dataframe to features and further to a certain time period and plots selected features.
    Features can be scaled by the StandardScaler of sklearn. 
    If observation period should be one year set start and stop to the same year
    ----------
    Parameters
    
    df: dataframe with time as index
    features: list of feature names (column names) which should be plotted
    start: str of start point of the plot. Either year (e.g. '2001') or year month combination (e.g. '2001-01')
    stop: str of end point of the plot. Formated like start. 
    scaler: bool, (default False) if True StandardScaler of sklearn will be applied to features.
    
    """
    
    df1 = df[features]
    df2 = df1[start:stop]
    
    if scaler:
        from sklearn.preprocessing import StandardScaler
        scaler = StandardScaler()
        df_plot = scaler.fit_transform(df2)
        df_plot = pd.DataFrame(df_plot, columns=df2.columns, index=df2.index)
    else:
        df_plot = df2
    
    fig, ax = plt.subplots(figsize=(10,5))
    df_plot.plot(ax=ax);
    ax.set_title(f'From {start} to {stop}', fontsize=16)
    ax.set_xlabel('Time', fontsize=14)
    ax.tick_params(axis='x', labelrotation=30)
    if scaler:
        ax.set_title(f'From {start} to {stop} (Scaled)', fontsize=16)
    else:
        ax.set_title(f'From {start} to {stop}', fontsize=16)

        
def rem_col(df, col):
    '''
    Removes columns from a dataframe that contain a string.
    '''
    return df.loc[:,~df.columns.str.contains(col)]


def rem_cols(df, cols):
    '''
    Removes multiple columns from a dataframe that contain a string in a given list.
    '''
    for colname in cols:
        df = df.loc[:,~df.columns.str.contains(colname)]
    return df

  
def std_scaler(df):
    '''
    Sklearn StandardScaler applied to a pandas dataframe for the use with method chaining.
    '''
    colnames = df.columns.to_list()
    scaler = StandardScaler()
    df = scaler.fit_transform(df)
    df = pd.DataFrame(df)
    df.columns = colnames
    return df

    
def train_test_timesplit(df, ratio=0.75):
    '''
    Performs a train test split for time series on a dataframe with a datetime index.

    Parameter:
    ratio determines the fraction of the training part relative to the original dataframe.
    Output:
    Two dataframes, the first being the training one.
    '''
    time_index = list(df.index)
    df = df.reset_index()
    df_train = df.loc[:int(len(time_index)*ratio),:]
    df_train.index = time_index[:int(len(time_index)*ratio)+1]
    df_test = df.loc[int(len(time_index)*ratio)+1:,:]
    df_test.index = time_index[int(len(time_index)*ratio)+1:]
    return df_train, df_test


def custom_dropper(df, cols):
    '''
    Drops rows of a data frame that have missing values in some of the columns.
    ------------------
    In: 
    df: a data frame
    cols: columns in which to look for missing values
    ------------------
    Out: a data frame
    '''
    return df[df.index.isin(df[cols].dropna().index)]

def model_classification(actual, predicted): 

    """
    Prints out RSME, MAE and explained variance score
    """
    print('-'*20)
    print(f'RMSE: {round(np.sqrt(mean_squared_error(actual, predicted)),2)}')
    print('-'*20)
    print(f'MAE: {round(mean_absolute_error(actual, predicted),2)}')
    print(f'Explained variance: {round(explained_variance_score(actual, predicted),3)}')
    print('-'*20)

    
def log_cases(df):
    df = df.assign(logged_cases = lambda df: np.log(df['total_cases']+1))
    return df