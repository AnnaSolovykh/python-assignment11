import plotly.express as px
import plotly.data as pldata

# TASK 3
df = pldata.wind(return_type='pandas')

print("First 10 rows:")
print(df.head(10))
print("Last 10 rows:")
print(df.tail(10))

# Clean data: convert strength column to numeric
def convert_strength_to_numeric(strength_str):
    if '-' in strength_str:
        start, end = strength_str.split('-')
        return (float(start) + float(end)) / 2
    elif '+' in strength_str:
        base_value = float(strength_str.replace('+', ''))
        return base_value + 0.5
    else:
        return float(strength_str)

df['strength_numeric'] = df['strength'].apply(convert_strength_to_numeric)

fig = px.scatter(
    df, 
    x='strength_numeric', 
    y='frequency', 
    color='direction',
    title='Wind Strength vs Frequency by Direction',
    labels={
        'strength_numeric': 'Wind Strength',
        'frequency': 'Frequency',
        'direction': 'Direction'
    },
    hover_data={
        'direction': True,
        'strength': True,  
        'strength_numeric': ':.1f',
        'frequency': ':.2f'
    }
)

fig.write_html("wind.html", auto_open=True)
print("Plot saved as wind.html")