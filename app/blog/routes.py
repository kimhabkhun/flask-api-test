from . import blog
# from flask import render_template

@blog.route("")
def get_blog():
    return "this is blog page"