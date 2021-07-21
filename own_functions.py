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
    import pandas as pd
    import matplotlib.pyplot as plt
    
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




