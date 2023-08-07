from flask import Flask,render_template,request
#from elasticsearch import Elasticsearch
import json
#from bert import *

#old url for less data
#es_url = 'https://1pdwgdsjzl:mu42svkygj@student-search-6649495957.us-east-1.bonsaisearch.net:443'

#new url for large data
#es_url = 'https://9yn9ttqsvv:83o1rv776k@student-search-3456745800.us-west-2.bonsaisearch.net:443'
#es = Elasticsearch(es_url)
#es.ping()

app = Flask(__name__)

@app.route('/')
def msg():
    return render_template('index.html')

# @app.route("/search", methods=['POST','GET'])
# def search():
#     search_term = request.form["input"]
#     res= es.search(index='patents', body={"query": {"match": 
#                                                   {"title": search_term}
#                                                   }})
#     return render_template('search.html',res=res)
                           
# @app.route("/bert", methods=['POST','GET'])
# def bert():
#     search_term = request.form["input"]
#     D, I = vector_search([search_term], model, index, num_results=10)
#     #print(f'distance: {D.flatten().tolist()}\n\n paper IDs: {I.flatten().tolist()}')
#     res= id2details(df, I)
#     #print(res)
#     return render_template('bert.html',res=res)


# main driver function
if __name__ == '__main__':
	app.run(port=8080)