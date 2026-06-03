import json
import os
from flask import current_app, request


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as raw_data:
        return json.load(raw_data)


def save_file(filename, file_data):
    with open(filename, 'w', encoding='utf-8') as raw_data:
        json.dump(file_data, raw_data, ensure_ascii=False, indent=4)


def save_poster(file_storage):
    if not file_storage:
        return None
    filename = file_storage.filename
    save_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    file_storage.save(save_path)
    return filename


def make_dict():
    film_name = request.form['film_name']
    director_name = request.form['director_name']
    cast_text = request.form['cast_text']
    discrp_text = request.form['discrp_text']
    whatch_date = request.form['whatch_date']
    poster_file = request.files['poster']
    rating = request.form['rating']

    if poster_file:
        filename = poster_file.filename
        save_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        poster_file.save(save_path)

    film_dict = {'film': film_name,
                 'director': director_name,
                 'cast': cast_text,
                 'description': discrp_text,
                 'whatch_date': whatch_date,
                 'poster': filename,
                 'rating': rating}
    return film_dict
