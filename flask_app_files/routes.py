from flask_app import app, db
from flask import render_template, request, redirect, url_for
from sqlalchemy import func
from flask_app.models import User, Answers, Questions
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///servey.db'



@app.route('/')
def main():
    return render_template('main.html')


@app.route('/questions')
def question_page():
    questions_list = db.session.query(Questions)
    return render_template(
        'questions.html', questions_list=questions_list
    )


@app.route('/process', methods=['get'])
def answer_process():
    if not request.args:
        return redirect(url_for('question_page'))
    username = request.args.get('username')
    age = request.args.get('age')
    gender = request.args.get('gender')
    education = request.args.get('education')
    linguistics = request.args.get('linguistics')
    user = User(
        username=username,
        age=age,
        gender=gender,
        education=education,
        linguistics=linguistics
    )
    db.session.add(user)
    db.session.commit()
    db.session.refresh(user)
    q1 = request.args.get('q1')
    q2 = request.args.get('q2')
    q3 = request.args.get('q3')
    q4 = request.args.get('q4')
    q5 = request.args.get('q5')
    q6 = request.args.get('q6')
    q7 = request.args.get('q7')
    q8 = request.args.get('q8')
    q9 = request.args.get('q9')
    q10 = request.args.get('q10')
    answer = Answers(id=user.id,
                     q1=q1,
                     q2=q2,
                     q3=q3,
                     q4=q4,
                     q5=q5,
                     q6=q6,
                     q7=q7,
                     q8=q8,
                     q9=q9,
                     q10=q10
                     )
    db.session.add(answer)
    db.session.commit()
    return 'Ok'


@app.route('/stats')
def stats():
    all_info = {}
    age_stats = db.session.query(
        func.avg(User.age),
        func.min(User.age),
        func.max(User.age)
    ).one()
    men_count = 0
    women_count = 0
    ling_count = 0
    not_ling_count = 0
    middle_count = 0
    for el in db.session.query(User):
        if el.gender == "male":
            men_count += 1
        elif el.gender == "female":
            women_count += 1
        if el.linguistics == "yes":
            ling_count += 1
        elif el.linguistics == "no":
            not_ling_count += 1
        else:
            middle_count += 1
    all_info['ling'] = ling_count
    all_info['not_ling'] = not_ling_count
    all_info['middle_count'] = middle_count
    all_info['men'] = men_count
    all_info['women'] = women_count
    all_info['age_mean'] = age_stats[0]
    all_info['age_min'] = age_stats[1]
    all_info['age_max'] = age_stats[2]
    all_info['total_count'] = db.session.query(func.count(User.id))
    all_info['q1_mean'] = db.session.query(func.avg(Answers.q1)).one()[0]
    all_info['q2_mean'] = db.session.query(func.avg(Answers.q2)).one()[0]
    all_info['q3_mean'] = db.session.query(func.avg(Answers.q3)).one()[0]
    all_info['q4_mean'] = db.session.query(func.avg(Answers.q4)).one()[0]
    all_info['q5_mean'] = db.session.query(func.avg(Answers.q5)).one()[0]
    all_info['q6_mean'] = db.session.query(func.avg(Answers.q6)).one()[0]
    all_info['q7_mean'] = db.session.query(func.avg(Answers.q7)).one()[0]
    all_info['q8_mean'] = db.session.query(func.avg(Answers.q8)).one()[0]
    all_info['q9_mean'] = db.session.query(func.avg(Answers.q9)).one()[0]
    all_info['q10_mean'] = db.session.query(func.avg(Answers.q10)).one()[0]
    return render_template('result.html', all_info=all_info)
