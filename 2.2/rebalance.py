import pandas as pd
import numpy as np

# Function to rebalance the portfolio according to the asset cap
def rebalance_portfolio(df, asset_cap, total_capital):
    # Calculate initial percentages
    df['Cap'] = df['MCAP'] / df['MCAP'].sum()
    df['Capped %'] = np.minimum(df['Cap'], asset_cap)
    df['Excess'] = df['Cap'] - df['Capped %']
    
    # Calculate the total excess percentage that needs to be redistributed
    total_excess = df['Excess'].sum()
    
    # Redistribute the excess to the coins under the cap proportionally
    df['Redistribution'] = df.apply(
        lambda x: (x['Excess'] / total_excess) * df['Capped %'].sum() if x['Cap'] < asset_cap else 0,
        axis=1
    )
    df['Final %'] = df['Capped %'] + df['Redistribution']
    
    # Calculate the final amount and USD value for each asset based on the final percentages
    df['Final Amount'] = (df['Final %'] * total_capital) / df['Price']
    df['Final USD Value'] = df['Final Amount'] * df['Price']
    
    # Drop the intermediate columns to clean up the DataFrame
    df = df.drop(columns=['Cap', 'Capped %', 'Excess', 'Redistribution'])
    
    return df

# Example data
data = {
    'Ticker': ['BTC', 'ETH', 'LTC'],
    'Amount': [10, 13.333333, 16.666667],
    'USD Value': [500, 333.33, 166.67],
    'MCAP': [20000, 10000, 5000],
    'Price': [50, 25, 10]
}
df = pd.DataFrame(data)

# Set asset cap and total capital
asset_cap = 0.5
total_capital = 10000

# Run the rebalance function
rebalanced_df = rebalance_portfolio(df, asset_cap, total_capital)
print(rebalanced_df)
