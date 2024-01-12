import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean data
df = df[
  ( df['value'] <= df['value'].quantile(0.975) ) &
  ( df['value'] >= df['value'].quantile(0.025) )
]


def draw_line_plot():
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(18,6))
    ax.plot(df.index, df['value'].values, color='red')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_ylabel('Page Views')
    ax.set_xlabel('Date')


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar = df_bar.groupby(pd.Grouper(freq='M')).mean()
    df_bar['year'] = df_bar.index.year
    df_bar['month_name'] = df_bar.index.strftime('%B')
  
    df_bar['month_name'] = pd.Categorical(df_bar['month_name'], categories=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], ordered=True)
  
    df_bar = df_bar.pivot_table(index='year', columns='month_name', values='value')


    fig = df_bar.plot.bar(legend=True, figsize=(7,7), ylabel='Average Page Views', xlabel='Years').figure
    plt.legend(title='Month')

  
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(20,5))
  
    sns.boxplot(df_box, x='year', y='value', hue='year', ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')

    sns.boxplot(df_box, x='month', y='value', hue='month', ax=ax2,
               order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')

  



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
