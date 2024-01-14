import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
   # print("last year:", df.iloc[-1]['Year'])# | == 2013


    # Create scatter plot
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12,6))
    ax.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    # y = mx + c
    # y = dependent variable (sea level) | x = independent variable (years)
    # m = slope                          | c = intercept
    slope, intercept, rvalue, pvalue, stderr = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    #y = slope * df['Year'] + intercept
    future_years = np.arange(df.iloc[-1]['Year']+1, 2051, 1)
    total_years = np.append(df['Year'].values, future_years)
    plt.plot(total_years, slope * total_years + intercept)
  

    # Create second line of best fit
    df2 = df[df['Year']>=2000]
    slope2, intercept2, rvalue2, pvalue2, stderr2 = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
    total_years2 = np.append(df2['Year'].values, future_years)
    plt.plot(total_years2, slope2 * total_years2 + intercept2)


    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_xlabel('Year')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()