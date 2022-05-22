# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
from dash.dependencies import Input, Output, State
from dash import dcc
from dash import html

app = dash.Dash()
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

app.layout = html.Div(

	children = [ 
        dcc.Checklist(
            id='biglist1',  
            options=['1,1', '1,2', '1,3', '1,4', '1,5', '1,6'],
            value=[],
            inline=True
        ),

        dcc.Checklist(
            id='biglist2',  
            options=['2,1', '2,2', '2,3', '2,4', '2,5', '2,6'],
            value=[],
            inline=True
        ),

        dcc.Checklist(
            id='biglist3',  
            options=['3,1', '3,2', '3,3', '3,4', '3,5', '3,6'],
            value=[],
            inline=True
        ),

        dcc.Checklist(
            id='biglist4',  
            options=['4,1', '4,2', '4,3', '4,4', '4,5', '4,6'],
            value=[],
            inline=True
        ),
        
        html.Div(id='on')
	]
    
)

@app.callback(
	Output('on', 'children'),
	[Input('biglist1', 'value'),
     Input('biglist2', 'value'),
     Input('biglist3', 'value'),
     Input('biglist4', 'value'),]
)
def update_on(value1, value2, value3, value4):

    a = value1
    b = value2
    c = value3
    d = value4

    x = a + b + c + d

    print (x)
    
    return "boxes on are {}".format(x)

if __name__ == '__main__':
    app.run_server(debug=True)

