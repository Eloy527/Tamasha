from . import main
from flask_login import login_required, current_user
from .api import get_upcoming,get_popular,get_movies_detalies,get_simmilar_detalies,movie_trailer
from flask import render_template,request, redirect, session
from .forms import CommentForm
from data_base import db,Liked,Comment,User


@main.route('/')
@main.route('/HOME')
def index():
    upcoming_movies = get_upcoming()
    popular_movies = get_popular()

    return render_template('index.html', upcoming_movies=upcoming_movies[0:5],
    popular_movies=popular_movies[0:12],main_movie=popular_movies[0])
@main.route('/popular')
def show_populars ():
    page = request.args.get('page', 1) 
    movies = get_popular(page)
    return render_template('movie_list.html',movies=movies)
@main.route('/upcoming')
def show_upcomings ():
    page = request.args.get('page', 1) 
    movies = get_upcoming(page)
    return render_template('movie_list.html',movies=movies)
@main.route('/movie/<int:id>',methods=['GET', 'POST'])
@login_required
def show_mivie_detalis(id):
    form = CommentForm()
    if form.validate_on_submit():
        content=form.content.data
        comment = Comment(content=content,user_id=current_user.id,movie_id=id)
        db.session.add(comment)
        db.session.commit()
        print('Comment: ',comment)
    print("id:",id)

    comment=Comment.query.filter_by(movie_id=id).all()
    print('Comments: ',comment)

    movie = get_movies_detalies(id)

    simmilar = get_simmilar_detalies(id)

    video_key = movie_trailer(id)

    return render_template('details.html',movie=movie,simmilar_movies=simmilar[0:1],form=form,comments=comment,video_key=video_key)
@main.route('/like_movie/<int:id>')
@login_required  
def liked_movies(id) :
    movie = get_movies_detalies(id)
    liked_movie = Liked(
        id = id,
        title = movie.get('title'),
        date = movie.get('release_date'),
        rate = movie.get('vote_average'),
        poster_path = movie.get('poster_path'),
        user_id = current_user.id

    )
    db.session.add(liked_movie)
    db.session.commit()
    return redirect('/')

@main.route('/profile')
@login_required  
def profil() :
    movies = current_user.liked_movies

    return render_template('profile.html',movies=movies)
@main.route('/movie/<int:id>/like')
def like(id):
    movie = get_movie_details(id)
    sent_movie = Liked.query.filter_by(title=movie.get('title'), user_id = current_user.id).first()
    if sent_movie:
        db.session.delete(sent_movie)
        db.session.commit()
    if not sent_movie:
        liked_movie = Liked(
            id = id,
            title = movie.get('title'),
            date = movie.get('release_date'),
            rate = movie.get('vote_average'),
            poster_path = f"https://image.tmdb.org/t/p/w200{ movie.get('poster_path') }",
            user_id = current_user.id
        )
        db.session.add(liked_movie)
        db.session.commit()
        print('liked movie id: ', id, "user liked:", current_user)
    return redirect(request.referrer)

