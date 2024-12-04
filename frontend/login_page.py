import reactpy as rp
from reactpy import html

@rp.component
def LoginPage():
    return html.div({"style": {"textAlign": "center", "marginTop": "100px"}}, [
        html.h1("Welcome to Tennis App"),
        html.button({
            "style": {"padding": "10px 20px", "marginRight": "10px"},
            "onclick": lambda: login_with_provider("google")
        }, "Login with Google"),
        html.button({
            "style": {"padding": "10px 20px"},
            "onclick": lambda: login_with_provider("facebook")
        }, "Login with Facebook")
    ])

# Function to initiate SSO login with a provider
def login_with_provider(provider):
    import webbrowser
    webbrowser.open(f"http://localhost:8000/auth/login/{provider}")

# Run the ReactPy login page
rp.run(LoginPage, port=3000)