from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

# Load the CSV data into a DataFrame
df = pd.read_csv('dump.csv')

@app.route('/')
def index():
    # Extract unique company names (index names) for the list
    companies = df['index_name'].unique()
    return render_template('index.html', companies=companies)

@app.route('/get_chart_data/<company_name>', methods=['GET'])
def get_chart_data(company_name):
    # Filter data for the selected company
    company_data = df[df['index_name'] == company_name]
    
    # Prepare the data for the chart (open, high, low, close values)
    chart_data = {
        "labels": ['Open', 'High', 'Low', 'Close'],
        "values": [
            company_data['open_index_value'].values[0],
            company_data['high_index_value'].values[0],
            company_data['low_index_value'].values[0],
            company_data['closing_index_value'].values[0]
        ]
    }
    return jsonify(chart_data)

if __name__ == '__main__':
    app.run(debug=True)
