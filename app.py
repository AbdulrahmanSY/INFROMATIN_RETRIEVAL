import pickle
from flask import Flask, render_template, request, jsonify
from crawling.urls import urls
from search_and_rank import search
from suggestion import suggestion as su
import path as p 
from matching import matching as m
app = Flask(__name__)


@app.route('/')
def search_engine():
    return render_template("searchengine.html", pagetitle='Search Engine')


@app.route('/search', methods=['GET', 'POST'])
def search_route():
    global top_result
    if request.method == 'POST':
        top_result =[]
        query = request.form['query']
        category = request.form['category']
        if not category:
            category = 'crawling'
        if category == 'clinic' or category == 'lotte' :
            top_result = m.Search_of_query(query,category)
        if query == "":
            return render_template("searchengine.html", pagetitle='Search Engine')
        if category == 'crawling' :
            top_result = search(query, urls)

        if top_result is None:
            return render_template('notfound.html', pagetitle='Not Found')
        return render_template('results.html', data=top_result, pagetitle='search results')
    return render_template('searchengine.html', pagetitle='Search Engine')


# Assuming you have a list of suggestions available
# SUGGESTIONS = ['apple', 'banana', 'cherry', 'date', 'elderberry']

@app.route('/suggestions')
def get_suggestions():
    query = request.args.get('query')
    if query:
        try:
            suggestions = su.fetch_suggestion(query, p.ds_f_queries_path)
            return jsonify(suggestions)
        except Exception as e:
            # Log the error or provide a more detailed error message
            print(f"Error fetching suggestions: {e}")
            return jsonify([]), 500
    else:
        return jsonify([])
@app.route('/a')
def a():
    return render_template("graph/a.html", pagetitle='a', image='images/a.jpg')


@app.route('/b')
def b():
    return render_template("graph/b.html", pagetitle='b', image='images/b.jpg')


@app.route('/c')
def c():
    return render_template("graph/c.html", pagetitle='c', image='images/c.jpg')


@app.route('/d')
def d():
    return render_template("graph/d.html", pagetitle='d', image='images/d.jpg')


@app.route('/e')
def e():
    return render_template("graph/e.html", pagetitle='e', image='images/e.jpg')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
