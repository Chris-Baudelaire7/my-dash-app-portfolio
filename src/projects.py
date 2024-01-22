import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify
import dash
from dash import html, dcc

# 'filled', 'outline', 'light', 'gradient', 'dot'

def hashtag(tag, color):
    return dmc.Badge([tag], color=color, size="xs", variant="gradient", className="me-1")



def card_project(source, title, image, description):
    return dmc.Card(
        children=[
            dmc.CardSection(
                html.Div(className="container", children=[
                    dmc.Image(
                        src=dash.get_asset_url(image),
                        height=220,
                        className="card_img"
                    ),
                    
                    html.Div(className="middle", children=[
                        html.A(href=source, className="text", target="_blank", children=[
                            "VIEW APP ", DashIconify(icon="bytesize:external", width=20, color="white", inline=True)
                        ])
                    ])
                ])
            ),
            html.Div(className="d-flex justify-content-between align-items-center mt-2", children=[
                html.H6(title),
                html.Div(className="d-inline ap px-", children=[
                    html.Small("Analytics", className="text-white"),
                    html.Small("Paper", className="text-danger"),
                ])
            ]),
            dcc.Markdown(
                description,
                className="text-muted"
            ),

            html.Div(className="d-flex justify-content-between", children=[

                html.Div(className="", children=[
                    hashtag("Python", "yellow"),
                    hashtag("Pandas", "yellow"),
                    hashtag("Numpy", "yellow")
                ]),

                html.A(href="https://natural-disasters-data-analysis.onrender.com", children=[
                    DashIconify(icon="logos:github-octocat",
                                width=25, color="white")
                ]),

            ])
        ],
        withBorder=False,
        shadow="xl",
        radius="md",
    )
