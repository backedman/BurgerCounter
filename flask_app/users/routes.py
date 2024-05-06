import base64,io
from io import BytesIO
from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import current_user, login_required, login_user, logout_user
from ..forms import BurgerForm
from ..models import User
from .. import calorie_count_api
from werkzeug.utils import secure_filename



from ..models import User

users = Blueprint("users", __name__)

@users.route("/", methods=["GET", "POST"])
def index():
    if current_user.is_authenticated:
        
        #get burger count
        burger_count = current_user.burger_counter
        calorie_count = current_user.calorie_counter
        
        return render_template('index.html', burger_count=burger_count, calorie_count=calorie_count)
        
    else:
        return redirect(url_for('users.leaderboard'))
    
@users.route("/leaderboard")
def leaderboard():
    top_50 = None
    try:
        top_50 = list(User.objects().aggregate([{'$sort': {'burger_counter' : -1}}, {'$limit': 50}]))
    except Exception as e:
        print("Error occurred:", e)
    
    print(top_50)
    
    return render_template('leaderboard.html', top_50=top_50)


@users.route("/burger", methods=["GET", "POST"])
@login_required
def order_burger():
    
    form = BurgerForm()
    
    if form.validate_on_submit():
        print('here')
        
        buns = form.Buns.data
        patties = form.Buns.data
        lettuce = form.Buns.data
        tomato = form.Buns.data
        
        #NOTE: its definitely better to not be calling the API every time but I wanted to show that ik how to make use of it
        bun_calorie = calorie_count_api('bun') * buns
        patty_calorie = calorie_count_api('hamburger') * patties
        lettuce_calorie = calorie_count_api('lettuce') * lettuce
        tomato_calorie = calorie_count_api('tomato') * tomato
        
        total_calories = bun_calorie + patty_calorie + lettuce_calorie + tomato_calorie
        
        current_calories = current_user.calorie_counter
        current_burgers = current_user.burger_counter
        
        user = User.objects(id=current_user.id).modify(calorie_counter=current_calories+total_calories, burger_counter=current_burgers+1)
        
        user.save()
        
        return redirect(url_for('users.index'))

    return render_template('burger.html', title='Order Burger', form=form)