import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go

pol = pd.read_csv("datasets/pollution_with_coordinates.csv")
pol_clean = pol.dropna(subset=["lat", "lng", "aqi_value"]).copy()


scaler = StandardScaler().fit(pol_clean[["lat", "lng"]])

X_all = scaler.transform(pol_clean[["lat", "lng"]])
y_all = pol_clean["aqi_value"].clip(upper=250)
best_k_mae = 21
model = KNeighborsRegressor(n_neighbors=best_k_mae, weights="distance")
model.fit(X_all, y_all)


step = 0.5
lats = np.arange(-90,  90 + step, step)
lons = np.arange(-180, 180 + step, step)
grid = pd.DataFrame([(lat, lon) for lat in lats for lon in lons], columns=["lat", "lng"])


app = dash.Dash(__name__)
app.layout = html.Div([
    html.H2("Click anywhere on the map to predict AQI"),
    dcc.Graph(id='map', config={'scrollZoom': True}, style={'height': '80vh'}),
    html.Div(id='prediction-output', style={'fontSize': 24, 'marginTop': 20})
])


@app.callback(
    Output('map', 'figure'),
    Input('map', 'clickData')
)
def update_map(clickData):
    marker_lat, marker_lon = 20, 0
    if clickData:
        marker_lat = clickData['points'][0]['lat']
        marker_lon = clickData['points'][0]['lon']

    fig = go.Figure()
    fig.add_trace(go.Scattermapbox(
        lat=grid["lat"], lon=grid["lng"],
        mode='markers',
        marker=dict(size=2, opacity=0),
        hoverinfo='none'
    ))

    fig.add_trace(go.Scattermapbox(
        lat=[marker_lat], lon=[marker_lon],
        mode='markers',
        marker=dict(size=12, color='orange'),
        hoverinfo='none'
    ))
    fig.update_layout(
        mapbox_style="open-street-map",
        mapbox=dict(center=dict(lat=20, lon=0), zoom=2),  
        margin=dict(l=0, r=0, t=0, b=0)
    )
    return fig


@app.callback(
    Output('prediction-output', 'children'),
    Input('map', 'clickData')
)
def predict_aqi(clickData):
    if not clickData:
        return "Click on the map to predict AQI."
    lat = clickData['points'][0]['lat']
    lon = clickData['points'][0]['lon']
    X_new = scaler.transform([[lat, lon]])
    pred = model.predict(X_new)[0]
    return f"Predicted AQI at ({lat:.4f}, {lon:.4f}) is {pred:.1f}"


if __name__ == '__main__':
    app.run(debug=True)
