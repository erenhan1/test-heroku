from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

# Load the dataset
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

# Initialize the Dash app
app = Dash(__name__)

# Expose the Flask server to be used by Heroku
server = app.server

# Define the layout with a single dropdown and three side-by-side graphs
app.layout = html.Div([
    html.H2(children='Country Data Dashboard', style={'textAlign': 'center', 'color': '#FFFFFF'}),

    # Dropdown for selecting a country
    dcc.Dropdown(df.country.unique(), 'Bulgaria', id='dropdown-selection',
                 style={'width': '50%', 'margin': '0 auto', 'background-color': '#2C3E50', 'color': 'black'}),

    # Div to hold the graphs side by side
    html.Div([
        dcc.Graph(id='graph-content-1', style={'display': 'inline-block', 'width': '32%'}),
        dcc.Graph(id='graph-content-2', style={'display': 'inline-block', 'width': '32%'}),
        dcc.Graph(id='graph-content-3', style={'display': 'inline-block', 'width': '32%'})
    ], style={'display': 'flex', 'justify-content': 'space-between', 'background-color': '#2C3E50', 'padding': '10px'})
])

# Callback to update all three graphs based on the selected country
@callback(
    [Output('graph-content-1', 'figure'),
     Output('graph-content-2', 'figure'),
     Output('graph-content-3', 'figure')],
    [Input('dropdown-selection', 'value')]
)
def update_graphs(value):
    dff = df[df.country == value]

    # First graph: Population over time with enhanced styling
    fig1 = px.line(
        dff, x='year', y='pop', title='Population Over Time',
        color_discrete_sequence=['#FF5733'],  # Flashy orange color
        line_shape='spline',  # Smooth curves
        render_mode='svg'  # Higher quality rendering
    )
    fig1.update_layout(
        title_font=dict(size=20, color='#FFFFFF', family="Arial"),
        plot_bgcolor='#1C1C1C',
        paper_bgcolor='#1C1C1C',
        font=dict(color='#FFFFFF', size=12),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False)
    )

    # Second graph: GDP per capita over time with enhanced styling
    fig2 = px.line(
        dff, x='year', y='gdpPercap', title='GDP Per Capita Over Time',
        color_discrete_sequence=['#33FF57'],  # Flashy green color
        line_shape='spline'
    )
    fig2.update_layout(
        title_font=dict(size=20, color='#FFFFFF', family="Arial"),
        plot_bgcolor='#1C1C1C',
        paper_bgcolor='#1C1C1C',
        font=dict(color='#FFFFFF', size=12),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False)
    )

    # Third graph: Life expectancy over time with enhanced styling
    fig3 = px.line(
        dff, x='year', y='lifeExp', title='Life Expectancy Over Time',
        color_discrete_sequence=['#5733FF'],  # Flashy purple color
        line_shape='spline'
    )
    fig3.update_layout(
        title_font=dict(size=20, color='#FFFFFF', family="Arial"),
        plot_bgcolor='#1C1C1C',
        paper_bgcolor='#1C1C1C',
        font=dict(color='#FFFFFF', size=12),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False)
    )

    return fig1, fig2, fig3

# Run the app locally
if __name__ == '__main__':
    app.run_server(debug=True)
