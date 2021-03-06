from flask import Blueprint
from flask import render_template, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required


from blog.models import Post
main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    # posts = Post.query.paginate(per_page=5)
    #azalan sira ile
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=5)
    return render_template("home.html", posts = posts,current_user=current_user)

@main.route("/about")
def about():
    return render_template("about.html", title="about",current_user=current_user)