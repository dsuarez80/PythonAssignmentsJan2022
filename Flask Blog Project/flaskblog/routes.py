from flask import render_template, url_for, flash, redirect, request, abort
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
import secrets
import os
from PIL import Image

@app.route("/")
@app.route("/home")
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title = "About")

@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.username.data}", "success")
        return redirect(url_for('login'))

    return render_template("register.html", title = "Register", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(email = form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember= form.remember.data)
            next_page = request.args.get('next')
            flash("Login Successful!", "success")
            return redirect(next_page) if next_page else redirect(url_for('home'))

        flash("Login Unsuccessful. Please check email and password", "danger")
    return render_template("login.html", title = "Login", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_pfp(form_pfp):
    random_hex = secrets.token_hex(8)
    x, f_ext = os.path.split(form_pfp.filename)
    pfp_fn = random_hex + f_ext

    pfp_path = os.path.join(app.root_path, "static/profile_pics", pfp_fn)

    output_size = (125, 125)
    i = Image.open(form_pfp)
    i.thumbnail(output_size)

    i.save(pfp_path)

    return pfp_fn

@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    form = UpdateAccountForm()

    if form.validate_on_submit():
        if form.pfp.data:
            pfp = save_pfp(form.pfp.data)
            current_user.image_file = pfp

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Account updated.", "success")
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        
    image_file = url_for("static", filename = "profile_pics/" + current_user.image_file)
    return render_template("account.html", title = "Account", image_file = image_file, form = form)

def save_content_image(form_ci):
    random_hex = secrets.token_hex(8)
    x, f_ext = os.path.split(form_ci.filename)
    ci_fn = random_hex + f_ext
    ci_path = os.path.join(app.root_path, "static/post_images", ci_fn)
    
    i = Image.open(form_ci)

    i.save(ci_path)

    return ci_fn

@app.route("/post/new", methods=["GET", "POST"])
@login_required
def new_post():
    form = PostForm()

    if form.validate_on_submit():
        post = Post(title = form.title.data, content = form.content.data, author = current_user)

        if form.content_image.data:
            content_image = save_content_image(form.content_image.data)
            post.content_image = content_image

        db.session.add(post)
        db.session.commit()
        flash("Post successfully created", "success")
        return redirect(url_for('home'))

    return render_template("create_post.html", title = "New Post", legend = "New Post", form=form)

@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.content_image:
        content_image = url_for("static", filename = "post_images/" + post.content_image)
        return render_template("post.html", title = post.title, post = post, content_image = content_image)
    return render_template("post.html", title = post.title, post = post)

@app.route("/post/<int:post_id>/update", methods=["GET", "POST"])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)

    if post.author != current_user:
        abort(403)

    form = PostForm()

    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data

        if form.content_image.data:
            content_image = save_content_image(form.content_image.data)
            post.content_image = content_image
        
        db.session.commit()
        flash("Post updated.", "success")
        return redirect(url_for('post', post_id = post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content

    return render_template("create_post.html", title = "Update Post", legend = "Update Post", form=form)

@app.route("/post/<int:post_id>/delete", methods=["POST"])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)

    if post.author != current_user:
        abort(403)
    
    db.session.delete(post)
    db.session.commit()
    flash("Post deleted.", "success")
    return redirect(url_for("home"))

@app.route("/users_list")
@login_required
def users_list():
    if current_user.username != "admin":
        abort(403)

    users = User.query.all()
    return render_template("users_list.html", title = "Users List", users = users)

@app.route("/announcements")
def announcements():
    return render_template('announcements.html', title = "Announcements")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500