from channels.routing import route


channel_routing = [
    route("http.request", "app.consumers.http_consumer"),
]
