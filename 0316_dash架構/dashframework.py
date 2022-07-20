
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objs as go

import datetime
# external_stylesheets = ['Dash.css']

# Step 1. 啟動應用程序
app = dash.Dash()

# Step 2. 導入資料庫
st = pd.read_csv("WBdataEN-5y.csv")

# Step 3. 建立儀表板(Dashboard)上的簡單散點圖(scatter)


# Step 4. 建立儀表板(Dashboard)輸出畫面
app.layout = html.Div([
    # 標題及子標題
    html.Div(["test"]),

    # plot
    dcc.Graph(id='plot', figure=fig),

])

# Step 5. 互動更新
# callback function

# Step 6. 完成 Server工作
if __name__ == '__main__':
    app.run_server(debug=False)
