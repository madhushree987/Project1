from flask import Flask, render_template_string, request
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load Dataset
df = pd.read_csv("imdb_top_1000.csv")

# Clean Gross Column
df['Gross'] = df['Gross'].str.replace(',', '')
df['Gross'] = pd.to_numeric(df['Gross'], errors='coerce')
df = df.dropna(subset=['Gross'])

# Success Classification
def classify_success(gross):
    if gross > 500000000:
        return "Blockbuster"
    elif gross > 100000000:
        return "Hit"
    elif gross > 50000000:
        return "Average"
    else:
        return "Flop"

df['Success'] = df['Gross'].apply(classify_success)

# HTML Template
template = """
<!DOCTYPE html>
<html>
<head>
    <title>Movie Success Dashboard</title>
    <style>
        body { font-family: Arial; background-color: #f4f4f4; padding: 20px; }
        h1 { text-align: center; }
        .card { background: white; padding: 20px; border-radius: 10px; margin-top: 20px; }
        select, button { padding: 8px; margin: 5px; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { padding: 10px; border-bottom: 1px solid #ddd; text-align: left; }
        .success { font-weight: bold; color: green; }
    </style>
</head>
<body>

<h1>🎬 Movie Success Prediction 🎬 </h1>

<form method="POST">
    <label>Select Genre:</label>
    <select name="genre">
        <option value="All">All</option>
        {% for g in genres %}
            <option value="{{g}}" {% if selected_genre == g %}selected{% endif %}>{{g}}</option>
        {% endfor %}
    </select>

    <button type="submit">Update Results</button>
</form>

<div class="card">
<h2>Movies List</h2>
<table>
<tr>
<th>Title</th>
<th>Genre</th>
<th>Rating</th>
<th>Gross ($)</th>
<th>Success</th>
</tr>

{% for row in movies %}
<tr>
<td>{{row['Series_Title']}}</td>
<td>{{row['Genre']}}</td>
<td>{{row['IMDB_Rating']}}</td>
<td>{{"{:,.0f}".format(row['Gross'])}}</td>
<td class="success">{{row['Success']}}</td>
</tr>
{% endfor %}

</table>
</div>

<div class="card">
<h2>Genre Success Distribution</h2>
<ul>
{% for key, value in distribution.items() %}
<li>{{key}} : {{value}}</li>
{% endfor %}
</ul>
</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    selected_genre = "All"
    filtered_df = df.copy()

    if request.method == "POST":
        selected_genre = request.form.get("genre")
        if selected_genre != "All":
            filtered_df = df[df['Genre'].str.contains(selected_genre)]

    genres = sorted(set(g for sub in df['Genre'].str.split(',') for g in sub))

    distribution = filtered_df['Success'].value_counts().to_dict()

    movies = filtered_df.to_dict(orient='records')

    return render_template_string(template,
                                  genres=genres,
                                  movies=movies,
                                  distribution=distribution,
                                  selected_genre=selected_genre)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)