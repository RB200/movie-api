from flask import Flask,jsonify,request
import csv

all_movies = []
liked = []
disliked =[]
did_not_watch = []

with open('movies.csv',encoding='utf-8-sig') as f:
    csvReader=csv.reader(f)
    data=list(csvReader)
    all_movies=data[1:]


app = Flask(__name__)

@app.route('/get-movie')

def get_movie():
    return jsonify({
        'data': all_movies[0],
        'status':'Success'
    })

@app.route('/liked-movies',methods=['POST'])

def liked_movies():
    movie = all_movies[0]
    all_movies1 = all_movies[1:]
    liked.append(movie)
    return jsonify({
        'status':'Success'
    }), 201

@app.route('/disliked-movies',methods=['POST'])

def disliked_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    disliked.append(movie)
    return jsonify({
        'status':'Success'
    }),201

@app.route('/unwatched',methods=['POST'])

def unwatched():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    did_not_watch.append(movie)
    return jsonify({
        'status':'Success'
    }),201
if __name__ == '__main__':
    app.run(debug=True,port=8080)

