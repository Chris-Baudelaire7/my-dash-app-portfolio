import dash
from flask import Flask
from dash import html, Dash, dcc
import dash_bootstrap_components as dbc


app_params = {
    "server": Flask(__name__),
    "title": "Chris Baudelaire - Data - Portfolio",
    "use_pages": True,
    "update_title": "Wait a moment...",
    "url_base_pathname": "/",
    "external_stylesheets": [dbc.themes.CYBORG, dbc.icons.BOOTSTRAP],
    "suppress_callback_exceptions": True,
    "meta_tags": [{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}]
}

server_params = {"debug": True, "port": 2147}


app = Dash(__name__, **app_params)

server = app.server

app.layout = html.Div(id="app-root", className="app-root", children=[

    dcc.Loading(
        html.Div(id="pages", className="pages", children=[
            dash.page_container
        ]),
        fullscreen=True, type="graph", style={"background": "black"}
    )

])


if __name__ == '__main__':
    app.run_server(**server_params)
