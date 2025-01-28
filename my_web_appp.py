from flask import Flask, request, redirect, url_for, jsonify, render_template_string
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Enhanced home page with improved styling and animation for shopping theme
    home_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Contact Web Page</title>
        <style>
            body, html {
                height: 100%;
                margin: 0;
                padding: 0;
                font-family: 'Arial', sans-serif;
                background: url('https://krify.co/wp-content/uploads/2021/05/Features-of-online-shopping-website.png') no-repeat center center fixed; 
                background-size: cover;
            }

            .overlay {
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: rgba(0, 0, 0, 0.6); /* slightly less opaque overlay */
                display: flex;
                justify-content: center;
                align-items: center;
            }

            .content {
                text-align: center;
                color: #ffffff;
                animation: slideUpFadeIn 1.2s ease-out forwards;
                opacity: 0; /* Start with content invisible */
            }

            @keyframes slideUpFadeIn {
                0% { transform: translateY(20px); opacity: 0; }
                100% { transform: translateY(0); opacity: 1; } /* End with content fully visible */
            }

            h1 {
    font-size: 2.5rem;
    color: #ff69b4; /* This is a pink color */
    background-color: rgba(255, 255, 255, 0.8); /* Adjusted opacity for a frosted look */
    padding: 20px;
    border: 3px solid #fff;
    display: inline-block;
    margin: 0;
    border-radius: 5px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    animation: scaleIn 0.5s 0.5s ease forwards; /* Animation for the title box */
}


            @keyframes scaleIn {
                from { transform: scale(0.9); }
                to { transform: scale(1); }
            }

            a {
                display: inline-block;
                margin-top: 20px;
                padding: 10px 25px;
                background-color: #ff4500;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                font-weight: bold;
                transition: transform 0.2s ease-out, box-shadow 0.2s ease-out;
            }

            a:hover {
                transform: scale(1.05);
                box-shadow: 0 4px 8px rgba(255, 69, 0, 0.5);
            }
        </style>
    </head>
    <body>
        <div class="overlay">
            <div class="content">
                <h1>Welcome To Our Shopping Contact Page</h1>
                <a href="/contact">Contact Us</a>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(home_html)




@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        response = requests.post('http://localhost:5000/validate', data={'query': message})
        
        if response.status_code == 403:
            error = "Malicious content detected. Your message has not been sent."
            return contact_page(error=error)
        
        return redirect(url_for('thank_you'))

    return contact_page()

def contact_page(error=None):
    contact_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Contact Us</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
        <style>
            body {{
                padding-top: 50px;
                background: linear-gradient(to right, #6dd5ed, #2193b0);
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }}
            .contact-container {{
                background: white;
                padding: 40px;
                border-radius: 8px;
                box-shadow: 0 4px 10px rgba(0,0,0,.1);
                margin-top: 50px;
                transform: scale(0.9);
                animation: scaleIn 0.5s forwards;
            }}
            @keyframes scaleIn {{
                from {{ transform: scale(0.9); opacity: 0; }}
                to {{ transform: scale(1); opacity: 1; }}
            }}
            .form-control, .btn-send {{
                border-radius: 20px;
                transition: all 0.3s ease;
            }}
            .form-control:focus, .btn-send:hover {{
                box-shadow: 0 0 0 2px #2193b0;
                transform: translateY(-2px);
            }}
            .btn-send {{
                background-color: #22a6b3;
                color: white;
                font-size: 16px;
                padding: 10px 20px;
                border: none;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }}
            .btn-send:hover {{
                background-color: #1e90ff;
            }}
            .error-message {{
                color: #ff0000;
                padding: 10px 0;
                margin-top: 20px;
                border: 1px solid #ff0000;
                background-color: #ffe6e6;
                border-radius: 4px;
                text-align: center;
                animation: shake 0.5s ease-in-out;
            }}
            @keyframes shake {{
                0%, 100% {{ transform: translateX(0); }}
                10%, 30%, 50%, 70%, 90% {{ transform: translateX(-10px); }}
                20%, 40%, 60%, 80% {{ transform: translateX(10px); }}
            }}
        </style>
    </head>
    <body>
    <div class="container">
        <div class="row">
            <div class="col-md-8 offset-md-2">
                <div class="contact-container">
                    <h2 class="text-center mb-4">Get in Touch</h2>
                    {'<div class="error-message">' + error + '</div>' if error else ''}
                    <form method="POST" onsubmit="return validateForm()">
                        <div class="form-group">
                            <label for="name">Name</label>
                            <input type="text" class="form-control" name="name" required>
                        </div>
                        <div class="form-group">
                            <label for="email">Email</label>
                            <input type="email" class="form-control" name="email" required>
                        </div>
                        <div class="form-group">
                            <label for="message">Message</label>
                            <textarea class="form-control" name="message" rows="5" required></textarea>
                        </div>
                        <button type="submit" class="btn btn-send">Send Message</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
    <script>
        function validateForm() {{
            // Simple front-end validation can go here
            // Return false to prevent form submission if there is an error
            return true;
        }}
    </script>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
    </body>
    </html>
    """
    return render_template_string(contact_html)


@app.route('/thank_you')
def thank_you():
    thank_you_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Thank You</title>
        <style>
            body, html {
                height: 100%;
                margin: 0;
                font-family: 'Arial', sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                text-align: center;
                background: url('https://source.unsplash.com/featured/?nature') no-repeat center center fixed; 
                background-size: cover;
            }

            .content {
                background: rgba(255, 255, 255, 0.8);
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                transform: scale(0);
                animation: scaleIn 1.0s forwards;
                animation-delay: 0.5s;
            }

            @keyframes scaleIn {
                from {
                    transform: scale(0);
                    opacity: 0;
                }
                to {
                    transform: scale(1);
                    opacity: 1;
                }
            }

            h1 {
                margin: 0;
                color: #333;
                font-size: 3rem;
                line-height: 1.4;
            }

            p {
                font-size: 1.5rem;
                color: #666;
            }

            .button {
                margin-top: 20px;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                background-color: #5cb85c;
                color: white;
                font-size: 1rem;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }

            .button:hover {
                background-color: #4cae4c;
            }
        </style>
    </head>
    <body>
        <div class="content">
            <h1>Thank You For Contacting Us!</h1>
            <p>We have received your message and will get back to you shortly.</p>
            <button class="button" onclick="window.location='/'">Return Home</button>
        </div>
    </body>
    </html>
    """
    return render_template_string(thank_you_html)



if __name__ == "__main__":
    app.run(port=8000)
