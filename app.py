from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
import os
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a secure secret key

# Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'  # Update with your email
app.config['MAIL_PASSWORD'] = 'your-app-password'     # Update with your app password

# Sample data - you can replace this with a database
services = [
    {
        'id': 1,
        'title': 'Web Development',
        'description': 'Custom websites and web applications built with modern technologies and best practices.',
        'icon': 'fas fa-code',
        'price': '$500 - $5000'
    },
    {
        'id': 2,
        'title': 'Mobile Apps',
        'description': 'Native and cross-platform mobile applications for iOS and Android devices.',
        'icon': 'fas fa-mobile-alt',
        'price': '$1000 - $10000'
    },
    {
        'id': 3,
        'title': 'UI/UX Design',
        'description': 'Beautiful and intuitive user interfaces designed with user experience in mind.',
        'icon': 'fas fa-paint-brush',
        'price': '$300 - $3000'
    },
    {
        'id': 4,
        'title': 'Digital Marketing',
        'description': 'Strategic marketing solutions to grow your online presence and reach your audience.',
        'icon': 'fas fa-chart-line',
        'price': '$200 - $2000'
    }
]

projects = [
    {
        'id': 1,
        'title': 'E-commerce Platform',
        'description': 'A modern e-commerce website with payment integration',
        'image': 'project1.jpg',
        'category': 'Web Development',
        'client': 'TechCorp Inc.'
    },
    {
        'id': 2,
        'title': 'Fitness App',
        'description': 'Mobile app for tracking workouts and nutrition',
        'image': 'project2.jpg',
        'category': 'Mobile Development',
        'client': 'FitLife'
    },
    {
        'id': 3,
        'title': 'Restaurant Website',
        'description': 'Responsive website with online ordering system',
        'image': 'project3.jpg',
        'category': 'Web Development',
        'client': 'TasteBuds Restaurant'
    }
]

@app.route('/')
def home():
    return render_template('index.html', services=services, projects=projects)

@app.route('/about')
def about():
    stats = {
        'projects': 500,
        'clients': 50,
        'experience': 5,
        'team_members': 12
    }
    return render_template('about.html', stats=stats)

@app.route('/services')
def services_page():
    return render_template('services.html', services=services)

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', projects=projects)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # Basic validation
        if not all([name, email, subject, message]):
            flash('Please fill in all fields.', 'error')
            return redirect(url_for('contact'))
        
        # Here you would typically save to database and send email
        # For now, we'll just flash a success message
        flash('Thank you for your message! We\'ll get back to you soon.', 'success')
        
        # Log the contact form submission
        print(f"New contact form submission from {name} ({email}): {subject}")
        
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.route('/api/services')
def api_services():
    return jsonify(services)

@app.route('/api/projects')
def api_projects():
    return jsonify(projects)

@app.route('/service/<int:service_id>')
def service_detail(service_id):
    service = next((s for s in services if s['id'] == service_id), None)
    if service is None:
        flash('Service not found.', 'error')
        return redirect(url_for('services_page'))
    return render_template('service_detail.html', service=service)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = next((p for p in projects if p['id'] == project_id), None)
    if project is None:
        flash('Project not found.', 'error')
        return redirect(url_for('portfolio'))
    return render_template('project_detail.html', project=project)

@app.route('/blog')
def blog():
    # Sample blog posts - you can replace with database
    posts = [
        {
            'id': 1,
            'title': 'The Future of Web Development',
            'excerpt': 'Exploring the latest trends and technologies in web development...',
            'author': 'John Doe',
            'date': '2024-01-15',
            'category': 'Technology'
        },
        {
            'id': 2,
            'title': 'Designing for Mobile First',
            'excerpt': 'Why mobile-first design is crucial for modern websites...',
            'author': 'Jane Smith',
            'date': '2024-01-10',
            'category': 'Design'
        }
    ]
    return render_template('blog.html', posts=posts)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 