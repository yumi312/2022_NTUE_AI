
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objs as go

import datetime
#external_stylesheets = ['Dash.css']

colors = {
    'background': '#111111',
    'text':'#35DB00'
}
# Step 1. 啟動應用程序
app = dash.Dash()

# Step 2. 導入資料庫

url='Stock_AAPL/stock_aapl.csv'
st = pd.read_csv(url)

# 下拉式選單的選項設定
features = st.columns[2:11]
opts = [{'label' : i, 'value' : i} for i in features]

# 滑動軸的選項設定
st['Date'] = pd.to_datetime(st.Date)
dates = ['2018-03-17', '2018-04-17', '2018-05-17', '2018-06-17', '2018-07-17', '2018-08-17',
         '2018-09-19', '2018-10-17', '2018-11-17', '2018-12-17', '2019-01-17', '2019-02-17', 
         '2019-03-17', '2019-04-17', '2019-05-17', '2019-06-17', '2019-07-17', '2019-08-17']

# Step 3. 建立儀表板(Dashboard)上的簡單散點圖(scatter)
trace_1 = go.Scatter(x = st.Date, y = st['AAPL.High'],
                    name = 'AAPL HIGH',
                    line = dict(width = 4,
                                color = 'rgb(100, 151, 50)'))
layout = go.Layout(title = '收盤 趨勢圖',
                   hovermode = 'closest')
fig = go.Figure(data = [trace_1], layout = layout)

# Step 4. 建立儀表板(Dashboard)輸出畫面
app.layout = html.Div([
                # 標題及子標題 
                html.Div([
                    html.H1("AAPL 股價 即時看盤"),
                    html.H5('Compute [AI Algorithm] Time: ' + str(datetime.datetime.now())+', Number of Data Updated: '+str(len(st))),
                         ],
                        style = {'padding' : '10px' ,
                              'backgroundColor' : 'black','color':'white','fontSize':'30px'}
                        ),

                # plot
                dcc.Graph(id = 'plot', figure = fig ),

                # dropdown
                html.P([
                    html.Label("選擇股價："),
                    dcc.Dropdown(id = 'opt', options = opts,
                                value = 'AAPL.High')
                        ], style = {'padding' : '30px' ,
                                    'backgroundColor' : '#6aeeb2',
                                    'width': '30%',
                                    'fontSize' : '24px',
                                    'display': 'inline-block'}),
                # 滑動軸 range slider
                html.P([
                    html.Label("選擇時間範圍："),
                    dcc.RangeSlider(id = 'slider',
                                    marks = {i : dates[i] for i in range(1, 18)},
                                    min = 0,
                                    max = 15,
                                    value = [5, 13],
                                    updatemode='drag',
                                    step=None
                                    )
                        ], style = {
                                    'padding' : '30px' , 
                                    'backgroundColor' : '#3aaab2',
                                    'width' : '95%',
                                    'fontSize' : '30px',
                                    'color':'white',
                                    'display': 'inline-block'}
                        ),
                        
                      ])

# Step 5. 互動更新
@app.callback(Output('plot', 'figure'),
             [Input('opt', 'value'),
             Input('slider', 'value')])
             
def update_figure(input1, input2):
    # filtering the data
    st2 = st[(st.Date >= dates[input2[0]]) & (st.Date <= dates[input2[1]])]
    # updating the plot
    trace_1 = go.Scatter(x = st2.Date, y = st2['AAPL.High'],
                        name = 'AAPL HIGH',
                        line = dict(width = 4,
                                    color = 'rgb(229, 151, 50)'))
    trace_2 = go.Scatter(x = st2.Date, y = st2[input1],
                        name = input1,
                        line = dict(width = 4,
                                    color = 'rgb(106, 181, 135)'))
    fig = go.Figure(data = [trace_1, trace_2], layout = {"title": "股價趨勢圖 (Apple Inc.) ",
                                                        'plot_bgcolor': colors['background'],
                                                        'paper_bgcolor': colors['background'],
                                                        'font': {'color': 'pink','size':24},
                                                         'height': 700})
    return fig
  
# Step 6. 完成 Server工作
if __name__ == '__main__':
    app.run_server(debug = False)