import dash_bootstrap_components as dbc
from dash import html
import dash

card_profile = html.Div(className="div-profile bg-black", children=[
    
    html.Div(className="g-0 d-flex align-items-center div-pic", children=[
        
        html.Div(className="me-2", children=[
            dbc.CardImg(
                src=dash.get_asset_url('cccb-4.png'),
                className="img-fluid rounded-circle image",
            ),
        ]),
        
        html.Div(className="", children=[
            html.H5("Chris Baudelaire .K", className="card-title text-white text-center text-md-start"),
            html.P(
                "This is a wider card with supporting text "
                "below as a natural lead-in to additional "
                "content. This content is a bit longer.",
                className="text-center text-md-start",
            ),
            html.Small(
                "Last updated 3 mins ago",
                className="card-text text-muted",
            ),
        ]),
    ])
])
