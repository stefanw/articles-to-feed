from datasette import hookimpl
from datasette.utils.asgi import Response


async def close_window(request):
    return Response.html("""
    <div style="margin: 2rem auto; text-align:center;">
        <h1>Saved!<h1>
        <p>Closing now...</p>
    </div>
    <script>window.setTimeout(()=>{window.close()}, 1000);</script>
    """)


@hookimpl
def register_routes():
    return [
        (r"^/-/close-window$", close_window)
    ]


@hookimpl
def skip_csrf(scope):
    return scope["path"] == "/articles/add_article"
