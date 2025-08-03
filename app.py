from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    try:
        data = pd.read_csv('clustered_customers.csv')
        preview = data.head(10).to_html(classes='table table-striped', index=False)
    except Exception as e:
        preview = f"<p>Error loading clustered data: {e}</p>"

    return render_template('index.html', table=preview)

if __name__ == '__main__':
    app.run(debug=True, port=10000)
