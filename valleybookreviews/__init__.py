
from valleybookreviews.factory.initialisation import create_app
from valleybookreviews.user.views import user_accounts, login_manager

# Creates App via Flask Application Factory
app = create_app()

# Register the Blueprints to FLask
app.register_blueprint(user_accounts)


# Sets Up the Login Manager
login_manager.init_app(app)
login_manager.login_view = 'login'
