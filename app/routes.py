def register_routes(api, app, root="api"):

    from app.users import register_routes as attach_users
    attach_users(api, app)
