from flask import Flask, render_template, request
from typing import Dict

from similars_model.inference import SimilarBooks
from similars_model.metadata import BookData

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    user_input_text: str = request.form['text_synopsis']
    #user_input_text = request.form['text_synopsis']
    title = SimilarBooks(input_synopsis=user_input_text)
    data: Dict = {
        title_id: BookData(book_id=title_id)
        for title_id in title.sim_title_ids
    }
    ids = title.sim_title_ids
    sim_score = title.sim_strengths

    return render_template("result.html",
                           input_synopsis=user_input_text,
                           t0_book_url=data[ids[0]].book_url,
                           t0_image_url=data[ids[0]].image_url,
                           t0_title=data[ids[0]].title,
                           t0_author=data[ids[0]].author,
                           t0_year=data[ids[0]].year,
                           t0_publisher=data[ids[0]].publisher,
                           t0_rating=data[ids[0]].rating,
                           t0_rating_count=data[ids[0]].rating_count,
                           t0_record_rating=data[ids[0]].record_rating,
                           t0_synopsis=data[ids[0]].synopsis,
                           t0_sim_score=sim_score[ids[0]],
                           t1_book_url=data[ids[1]].book_url,
                           t1_image_url=data[ids[1]].image_url,
                           t1_title=data[ids[1]].title,
                           t1_author=data[ids[1]].author,
                           t1_year=data[ids[1]].year,
                           t1_publisher=data[ids[1]].publisher,
                           t1_rating=data[ids[1]].rating,
                           t1_rating_count=data[ids[1]].rating_count,
                           t1_record_rating=data[ids[1]].record_rating,
                           t1_synopsis=data[ids[1]].synopsis,
                           t1_sim_score=sim_score[ids[1]],
                           t2_book_url=data[ids[2]].book_url,
                           t2_image_url=data[ids[2]].image_url,
                           t2_title=data[ids[2]].title,
                           t2_author=data[ids[2]].author,
                           t2_year=data[ids[2]].year,
                           t2_publisher=data[ids[2]].publisher,
                           t2_rating=data[ids[2]].rating,
                           t2_rating_count=data[ids[2]].rating_count,
                           t2_record_rating=data[ids[2]].record_rating,
                           t2_synopsis=data[ids[2]].synopsis,
                           t2_sim_score=sim_score[ids[2]],
                           t3_book_url=data[ids[3]].book_url,
                           t3_image_url=data[ids[3]].image_url,
                           t3_title=data[ids[3]].title,
                           t3_author=data[ids[3]].author,
                           t3_year=data[ids[3]].year,
                           t3_publisher=data[ids[3]].publisher,
                           t3_rating=data[ids[3]].rating,
                           t3_rating_count=data[ids[3]].rating_count,
                           t3_record_rating=data[ids[3]].record_rating,
                           t3_synopsis=data[ids[3]].synopsis,
                           t3_sim_score=sim_score[ids[3]],
                           t4_book_url=data[ids[4]].book_url,
                           t4_image_url=data[ids[4]].image_url,
                           t4_title=data[ids[4]].title,
                           t4_author=data[ids[4]].author,
                           t4_year=data[ids[4]].year,
                           t4_publisher=data[ids[4]].publisher,
                           t4_rating=data[ids[4]].rating,
                           t4_rating_count=data[ids[4]].rating_count,
                           t4_record_rating=data[ids[4]].record_rating,
                           t4_synopsis=data[ids[4]].synopsis,
                           t4_sim_score=sim_score[ids[4]],
                           sim_score=title.sim_strengths,
                           tags=title.top_tags)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)
