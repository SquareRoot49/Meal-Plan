# Meal Planner - Python Flask Application

A modern web application built with Python Flask that helps users design their daily meals based on calorie goals. This application provides personalized meal planning, nutrition tracking, and a comprehensive food database.

## 🍽️ Features

- **Smart Meal Planning**: Generate personalized meal plans based on calorie goals
- **Dietary Preferences**: Support for vegetarian, vegan, gluten-free, and low-carb diets
- **Food Database**: Browse hundreds of healthy foods with detailed nutritional information
- **Nutrition Calculator**: Track calories, protein, carbs, and fats
- **Save & Share**: Save your favorite meal plans for future reference
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Modern UI/UX**: Clean, intuitive interface with smooth animations

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the project files**

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:5000`

## 📁 Project Structure

```
Meal Planner/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/            # HTML templates
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Home page
│   ├── meal_planner.html # Main meal planning interface
│   └── food_database.html # Food browsing interface
├── static/               # Static files
│   ├── css/
│   │   └── styles.css    # Main stylesheet
│   └── js/
│       └── script.js     # JavaScript functionality
└── README_PYTHON.md      # This file
```

## 🎯 How It Works

### 1. Set Your Goals
- Enter your daily calorie target (1200-5000 calories)
- Choose dietary preferences (vegetarian, vegan, etc.)
- Select your activity level

### 2. Generate Meal Plan
- Our algorithm creates a balanced meal plan
- Distributes calories across breakfast, lunch, dinner, and snacks
- Considers your dietary restrictions

### 3. Review & Customize
- View detailed nutritional breakdown
- See protein, carbs, and fat content
- Make adjustments as needed

### 4. Save & Enjoy
- Save your meal plan for later
- Access your saved plans anytime
- Start your healthy eating journey!

## 🍎 Food Database

The application includes a comprehensive database of healthy foods:

- **Breakfast**: Oatmeal, yogurt, eggs, smoothies, etc.
- **Lunch**: Salads, sandwiches, soups, bowls, etc.
- **Dinner**: Lean proteins, vegetables, grains, etc.
- **Snacks**: Fruits, nuts, protein bars, etc.

Each food item includes:
- Calorie content
- Protein, carbohydrate, and fat content
- Category classification

## 🛠️ Technical Details

### Backend (Python Flask)
- **Framework**: Flask 2.3.3
- **Template Engine**: Jinja2
- **Data Storage**: In-memory (can be extended to database)
- **API Endpoints**: RESTful API for meal planning

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with Flexbox and Grid
- **JavaScript**: Interactive features and animations
- **Responsive Design**: Mobile-first approach

### Key Features
- **Algorithm**: Smart calorie distribution across meals
- **Validation**: Form validation and error handling
- **Animations**: Smooth transitions and hover effects
- **Search**: Real-time food search and filtering

## 🔧 Customization

### Adding New Foods
Edit the `FOOD_DATABASE` in `app.py`:

```python
FOOD_DATABASE = {
    'breakfast': [
        {
            'name': 'Your Food Name',
            'calories': 150,
            'protein': 10,
            'carbs': 20,
            'fat': 5,
            'category': 'breakfast'
        }
    ]
}
```

### Modifying Meal Distribution
Update the `calculate_meal_distribution` function in `app.py`:

```python
def calculate_meal_distribution(total_calories):
    # Customize how calories are distributed
    return {
        'breakfast': int(total_calories * 0.25),
        'lunch': int(total_calories * 0.30),
        'dinner': int(total_calories * 0.30),
        'snacks': int(total_calories * 0.15)
    }
```

### Styling Changes
Modify `static/css/styles.css` to customize:
- Colors and themes
- Layout and spacing
- Animations and transitions
- Responsive breakpoints

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production Deployment

1. **Using Gunicorn**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

2. **Using Heroku**
   - Create `Procfile`:
     ```
     web: gunicorn app:app
     ```
   - Deploy to Heroku

3. **Using Docker**
   ```dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   EXPOSE 5000
   CMD ["python", "app.py"]
   ```

## 🔒 Security Considerations

- Update the secret key in `app.py`
- Implement user authentication for production
- Add input validation and sanitization
- Use HTTPS in production
- Consider rate limiting for API endpoints

## 📈 Future Enhancements

- **User Accounts**: Registration and login system
- **Database Integration**: PostgreSQL or MongoDB
- **Recipe Integration**: Add cooking instructions
- **Shopping Lists**: Generate grocery lists from meal plans
- **Progress Tracking**: Track weight and nutrition goals
- **Social Features**: Share meal plans with friends
- **Mobile App**: Native iOS/Android applications
- **AI Integration**: Machine learning for better recommendations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is open source and available under the MIT License.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the documentation
2. Search existing issues
3. Create a new issue with details
4. Contact the development team

## 🎉 Acknowledgments

- Flask community for the excellent framework
- Font Awesome for icons
- Google Fonts for typography
- All contributors and users

---

**Happy meal planning! 🍽️✨** 