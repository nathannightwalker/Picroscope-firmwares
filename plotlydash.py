from dash import Dash, html, Input, Output, callback_context

app = Dash(__name__)

app.layout = html.Div([

    html.Button('UP', id='btn-up', n_clicks=0, style={'width': '5%', 'display': 'inline-block', 'vertical-align': 'middle', 'margin-left': '2.5vw'}),

    html.Div(
        children = [
            html.Button('LEFT', id='btn-left', n_clicks=0, style={'width': '5%', 'display': 'inline-block', 'vertical-align': 'middle', 'margin-left': '0vw'}),
            html.Button('RIGHT', id='btn-right', n_clicks=0, style={'width': '5%', 'display': 'inline-block', 'vertical-align': 'middle', 'margin-left': '0vw'}),
        ]
    ),

    html.Div(
        html.Button('DOWN', id='btn-down', n_clicks=0, style={'width': '5%', 'display': 'inline-block', 'vertical-align': 'top', 'margin-left': '2.5vw'}),
    ),

    html.Div(id='container-button-timestamp')
])

@app.callback(
    Output('container-button-timestamp', 'children'),
    Input('btn-up', 'n_clicks'),
    Input('btn-left', 'n_clicks'),
    Input('btn-right', 'n_clicks'),
    Input('btn-down', 'n_clicks')
)
def displayClick(btn1, btn2, btn3, btn4):
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]
    if 'btn-up' in changed_id:
        msg = 'Button UP was most recently clicked'
    elif 'btn-left' in changed_id:
        msg = 'Button LEFT was most recently clicked'
    elif 'btn-right' in changed_id:
        msg = 'Button RIGHT was most recently clicked'
    elif 'btn-down' in changed_id:
        msg = 'Button DOWN was most recently clicked'
    else:
        msg = 'None of the buttons have been clicked yet'
    return html.Div(msg)

if __name__ == '__main__':
    app.run_server(debug=True)