from flask import render_template, request, redirect, Blueprint
from companyblog.models import BlogPost,User
from sqlalchemy import or_


core = Blueprint('core', __name__)

@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    search_query = request.args.get('search', '')

    if search_query:
        blog_posts = BlogPost.query.filter(
            or_(
                BlogPost.title.ilike(f'%{search_query}%'),
                BlogPost.text.ilike(f'%{search_query}%')
            )
        ).order_by(BlogPost.date.desc()).paginate(page=page, per_page=5)
    else:
        blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=5)

    return render_template('index.html', blog_posts=blog_posts)

@core.route('/info')
def info():
    return render_template('info.html')

@core.route('/find-people', methods=['GET', 'POST'])
def find_people():
    search_query = request.args.get('search', '')

    # For demo: query users by username containing search_query (case-insensitive)
    if search_query:
        users = User.query.filter(User.username.ilike(f'%{search_query}%')).all()
    else:
        users = []

    return render_template('findpeople.html', users=users, search_query=search_query)

