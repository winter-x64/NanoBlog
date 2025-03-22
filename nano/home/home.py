from flask import Blueprint, render_template

from nano.database import supabase_client

home_bp = Blueprint(name="home_bp", import_name=__name__, url_prefix="/")


@home_bp.route(rule="/")
def home():
    featured_posts = supabase_client.table("blogs").select("*").execute()
    featured_posts = featured_posts.data
    print(featured_posts)
    return render_template(
        template_name_or_list="landing_page.html", featured_posts=featured_posts
    )
