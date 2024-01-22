import dash
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import dcc, html

from profile_pic import *
from projects import *


dash.register_page(__name__, path="/", order=1, name="Portfolio")

layout = html.Div(className="px-0 px-md-3 overview", children=[
    
    html.Div(className="row header", children=[
        html.Div(className="col-lg-8 text-center text-lg-start", children=[
            html.H1("𝐃𝐚𝐭𝐚 𝐏𝐨𝐫𝐭𝐟𝐨𝐥𝐢𝐨", className="display-1 text-warning pt-2 mt-5"),
            html.H2(className="", children=[
                dcc.Markdown(
                    """
                𝐄𝐱𝐩𝐥𝐨𝐫𝐚𝐭𝐨𝐫𝐲 𝐃𝐚𝐭𝐚 𝐀𝐧𝐚𝐥𝐲𝐬𝐢𝐬 •
                𝐀𝐧𝐚𝐥𝐲𝐭𝐢𝐜𝐚𝐥 𝐖𝐞𝐛 𝐀𝐩𝐩𝐥𝐢𝐜𝐚𝐭𝐢𝐨𝐧 •
                𝐃𝐚𝐭𝐚 𝐕𝐢𝐬𝐮𝐚𝐥𝐢𝐳𝐚𝐭𝐢𝐨𝐧 •
                𝐌𝐚𝐜𝐡𝐢𝐧𝐞/𝐃𝐞𝐞𝐩 𝐋𝐞𝐚𝐫𝐧𝐢𝐧𝐠 •
                𝐖𝐞𝐛 𝐒𝐜𝐫𝐚𝐩𝐢𝐧𝐠 •
                𝐏𝐲𝐭𝐡𝐨𝐧 𝐩𝐫𝐨𝐠𝐫𝐚𝐦𝐦𝐢𝐧𝐠
                """
                )
            ])
        ])
    ]),
    
    
    html.Div(className="row mt-5 pt-0 pt-xl-5", children=[
        
        html.Div(className="col-xl-4", children=[
            html.Div(className="px-0 px-lg-5 px-xl-0 div-profile", children=[
                card_profile
            ])
        ]),
        
        html.Div(className="col-xl-8 mt-5", children=[
            
            html.H5("𝐃𝐚𝐬𝐡 𝐏𝐥𝐨𝐭𝐥𝐲 𝐖𝐞𝐛 𝐀𝐩𝐩𝐥𝐢𝐜𝐚𝐭𝐢𝐨𝐧", className="mb-2"),
            html.Hr(className="pt-1 bg-white mb-4"),
            
            html.Div(className="row", children=[
                html.Div(className="col-md-6", children=[
                    card_project(
                        "https://natural-disasters-data-analysis.onrender.com", 
                        "𝐍𝐚𝐭𝐮𝐫𝐚𝐥 𝐃𝐢𝐬𝐚𝐬𝐭𝐞𝐫𝐬 𝐃𝐚𝐭𝐚 𝐀𝐧𝐚𝐥y𝐬𝐢𝐬 𝐀𝐧𝐝 𝐕𝐢𝐬𝐮𝐚𝐥𝐢𝐳𝐚𝐭𝐢𝐨𝐧", 
                        "nd.png",
                        "𝐒𝐭𝐚𝐭𝐢𝐬𝐭𝐢𝐜𝐚𝐥 𝐀𝐧𝐚𝐥𝐲𝐬𝐢𝐬 𝐨𝐟 𝐧𝐚𝐭𝐮𝐫𝐚𝐥 𝐃𝐢𝐬𝐚𝐬𝐭𝐞𝐫𝐬 𝐰𝐨𝐫𝐥𝐝𝐰𝐢𝐝𝐞 𝐚𝐧𝐝 𝐭𝐡𝐞𝐢𝐫 𝐜𝐨𝐫𝐫𝐞𝐥𝐚𝐭𝐢𝐨𝐧 𝐰𝐢𝐭𝐡 𝐂𝐥𝐢𝐦𝐚𝐭𝐞 𝐂𝐡𝐚𝐧𝐠𝐞")
                ]),
                
                html.Div(className="col-md-6", children=[
                    card_project(
                        "https://armed-conflicts-location-and-events-6g5g.onrender.com",
                        "𝐀𝐫𝐦𝐞𝐝 𝐂𝐨𝐧𝐟𝐥𝐢𝐜𝐭𝐬 𝐋𝐨𝐜𝐚𝐭𝐢𝐨𝐧 𝐀𝐧𝐝 𝐄𝐯𝐞𝐧𝐭 𝐃𝐚𝐭𝐚 𝐑𝐞𝐩𝐨𝐫𝐭: 𝐄𝐮𝐫𝐨𝐩𝐞 - 𝟐𝟎𝟐𝟑", 
                        "acled.png",
                        "𝐒𝐭𝐚𝐭𝐢𝐬𝐭𝐢𝐜𝐚𝐥 𝐑𝐞𝐩𝐨𝐫𝐭/𝐀𝐧𝐚𝐥𝐲𝐬𝐢𝐬 𝐨𝐟 𝐚𝐥𝐥 𝐰𝐚𝐫𝐬 𝐩𝐞𝐫𝐩𝐞𝐭𝐫𝐚𝐭𝐞𝐝 𝐢𝐧 𝐄𝐮𝐫𝐨𝐩𝐞 𝐢𝐧 𝐭𝐡𝐞 𝐲𝐞𝐚𝐫 𝟐𝟎𝟐𝟑")
                ]),
                
                html.Div(className="my-3"),
                
                html.Div(className="col-md-6", children=[
                    card_project(
                        "https://sales-dashboard-eda.onrender.com",
                        "𝐃𝐚𝐭𝐚 𝐒𝐜𝐢𝐞𝐧𝐜𝐞 | 𝐃𝐚𝐬𝐡𝐛𝐨𝐚𝐫𝐝 - 𝐒𝐚𝐥e𝐬 𝐃𝐚𝐬𝐡𝐛𝐨𝐚𝐫𝐝 𝐀𝐧𝐚𝐥𝐲𝐬𝐢𝐬", 
                        "sld.png",
                        "𝐒𝐚𝐥𝐞𝐬 𝐃𝐚𝐬𝐡𝐛𝐨𝐚𝐫𝐝 𝐀𝐧𝐚𝐥𝐲𝐬𝐢𝐬 𝐚𝐧𝐝 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐦𝐞𝐧𝐭 𝐨𝐟 𝐀𝐧𝐚𝐥𝐲𝐭𝐢𝐜𝐚𝐥 𝐖𝐞𝐛 𝐀𝐩𝐩𝐥𝐢𝐜𝐚𝐭𝐢𝐨𝐧 𝐰𝐢𝐭𝐡 𝐃𝐚𝐬𝐡/𝐏𝐥𝐨𝐭𝐥𝐲")
                ]),

                html.Div(className="col-md-6", children=[
                    card_project(
                        "https://indicateur-de-performace-vente.onrender.com",
                        "𝐈𝐧𝐝𝐢𝐜𝐚𝐭𝐞𝐮𝐫 𝐝𝐞 𝐏𝐞𝐫𝐟𝐨𝐫𝐦𝐚𝐧𝐜𝐞 - 𝐕𝐞𝐧𝐭𝐞", 
                        "kpi.png",
                        "𝐀𝐧𝐚𝐥𝐲𝐬𝐞 𝐞𝐱𝐩𝐥𝐨𝐫𝐚𝐭𝐨𝐢𝐫𝐞 𝐝𝐞𝐬 𝐝𝐨𝐧𝐧é𝐞𝐬 𝐝𝐞 𝐯𝐞𝐧𝐭𝐞 𝐞𝐭 𝐜𝐨𝐧𝐜𝐞𝐩𝐭𝐢𝐨𝐧 𝐝𝐞 𝐭𝐚𝐛𝐥𝐞𝐚𝐮 𝐝𝐞 𝐛𝐨𝐫𝐝 𝐚𝐯𝐞𝐜 𝐃𝐚𝐬𝐡/𝐏𝐨𝐭𝐥𝐲")
                ]),
                
                html.Div(className="my-3"),
                
                html.Div(className="col-md-6", children=[
                    card_project(
                        "https://indicateur-de-performace-vente.onrender.com",
                        "𝐅𝐢𝐧𝐚𝐧𝐜𝐢𝐚𝐥 𝐀𝐧𝐚𝐥𝐲𝐬𝐢𝐬 𝐀𝐧𝐝 𝐀𝐥𝐠 𝐓𝐫𝐚𝐝𝐢𝐧𝐠 𝐖𝐢𝐭𝐡 𝐏𝐲𝐭𝐡𝐨𝐧", 
                        "Z_FA1.jpg",
                        "𝐀𝐧𝐚𝐥𝐲𝐬𝐞 𝐞𝐱𝐩𝐥𝐨𝐫𝐚𝐭𝐨𝐢𝐫𝐞 𝐝𝐞𝐬 𝐝𝐨𝐧𝐧é𝐞𝐬 𝐝𝐞 𝐯𝐞𝐧𝐭𝐞 𝐞𝐭 𝐜𝐨𝐧𝐜𝐞𝐩𝐭𝐢𝐨𝐧 𝐝𝐞 𝐭𝐚𝐛𝐥𝐞𝐚𝐮 𝐝𝐞 𝐛𝐨𝐫𝐝 𝐚𝐯𝐞𝐜 𝐃𝐚𝐬𝐡/𝐏𝐨𝐭𝐥𝐲")
                ])
            ]),
            
         
        ])
    ]),
    
    
])

   # html.Div(className="row mt-5", children=[

#     html.Div(className="col-lg-4", children=[
#         html.H5("Data Visualization", className=""),
#         html.Div(className="", children=[
#             html.Span("""
#             Data visualization is the process of creating graphical representations of data in order to better understand, analyze, and communicate the insights and patterns that are present in the data. It involves using visual elements, such as charts, graphs, and maps, to represent data in a way that is easy to understand and interpret.

#             Data visualization is an important tool for data analysis, as it allows analysts and decision makers to quickly understand complex data sets and identify patterns, trends, and relationships that might not be immediately apparent in the raw data. It is also a useful tool for communicating the results of data analysis to others, as it can help to make the insights and conclusions more accessible and easier to understand.
#         """)
#         ])
#     ]),

# ]),

  # html.H5("WebScraping", className="mb-3 mt-5"),
# html.Hr(className="py-1 bg-white"),

# html.H5("Machine/Deep Learning", className="mb-3 mt-5"),
# html.Hr(className="py-1 bg-white"),
