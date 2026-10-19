from flask import Flask, abort, render_template, request

app = Flask(__name__)

# 每部电影使用一个适合放进 URL 的文字标识，叫作 slug。
# 数据放在函数外，让首页和详情页都能读取。
FILMS = [
    {"slug": "nezha", "title": "Ne Zha", "minutes": 110,
     "image": "images/nezha.jpg", "alt": "Ne Zha film poster"},
    {"slug": "hi-mom", "title": "Hi, Mom", "minutes": 128,
     "image": "images/hi-mom.jpg", "alt": "Hi, Mom film poster"},
    {"slug": "earth", "title": "The Wandering Earth", "minutes": 125,
     "image": "images/earth.jpg", "alt": "The Wandering Earth film poster"},
]


@app.route("/")
def index():
    # 1. 浏览器发送 /?movie=Mom；读取名为 movie 的查询参数。
    # query 是我们自己起的 Python 变量名，不需要与参数名 movie 相同。
    query = request.args.get("movie", "").strip() #从请求里找名叫 movie 的参数，把它的值保存到变量 query。如果没有，就用 ""。

    # 2. 用搜索词筛选电影；空字符串会匹配所有电影。
    matches = []
    for film in FILMS:
        if query.casefold() in film["title"].casefold():
            matches.append(film)

    # 3. 左边 query 是模板中的名字；右边 query 是上面的 Python 变量。
    return render_template("movie.html", films=matches, query=query)


# <slug> 捕获 URL 中这一段文字，传给下面函数的 slug 参数。
# 例如 /movies/hi-mom 会调用 movie(slug="hi-mom")。
@app.route("/movies/<slug>")
def movie(slug):
    for film in FILMS:
        if film["slug"] == slug:
            return render_template("movie-detail.html", film=film)
    # 没有对应的电影，返回 404 Not Found。
    abort(404)


# 笔记页路径是 /viewing-notes，模板中直接使用这个地址。
@app.route("/viewing-notes")
def notes():
    return render_template("notes.html")


if __name__ == "__main__":
    app.run(port=5000)
