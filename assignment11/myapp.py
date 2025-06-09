from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata

# TASK 4
df = pldata.gapminder()

countries = df['country'].unique()

app = Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id="country-dropdown",
        options=[{"label": country, "value": country} for country in countries],
        value="Canada"
    ),
    dcc.Graph(id="gdp-growth")
])

@app.callback(
    Output("gdp-growth", "figure"),
    [Input("country-dropdown", "value")]
)
def update_graph(country):
    filtered_df = df[df['country'] == country]
    
    fig = px.line(
        filtered_df, 
        x="year", 
        y="gdpPercap", 
        title=f"GDP per Capita Growth - {country}"
    )
    
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="GDP per Capita (USD)",
        yaxis_tickformat="$,.0f"
    )
    
    return fig

if __name__ == "__main__":
    app.run(debug=True)