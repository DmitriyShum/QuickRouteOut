from flask import Flask, request, jsonify, render_template
import os
import json
import math
import graphlib
import osmnx

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

class Graph:
    def graph():
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(BASE_DIR, "data", "boston_shelters.json")
        with open(path) as file:
            data = json.load(file)

            print(data)

        
    def __init__(self, graph: dict={}):
        self.graph = graph
    def dijkstra(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node] ={}
        return self.graph
if __name__ == "__main__":
    app.run(debug=True)