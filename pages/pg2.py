import dash
from dash import dcc, html

dash.register_page(__name__, name='Comeming soon')
#dash.register_page(__name__, path='/', name='Homememe')

layout = html.Div(
    [
        dcc.Markdown('# Liên hệ user 201353 để oder chức năng - 500k/Task!')
    ]
)