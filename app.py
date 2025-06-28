from flask import Flask, render_template, request, jsonify, flash, redirect, url_for, session
import os
from datetime import datetime
import json
import random

app = Flask(__name__)
app.secret_key = 'meal-planner-secret-key-2024'

# Sample food database - in a real app, this would come from a database
FOOD_DATABASE = {
    'breakfast': [
        {'name': 'Oatmeal with Berries', 'calories': 150, 'protein': 6, 'carbs': 27, 'fat': 3, 'category': 'breakfast'},
        {'name': 'Greek Yogurt with Honey', 'calories': 120, 'protein': 15, 'carbs': 12, 'fat': 0, 'category': 'breakfast'},
        {'name': 'Scrambled Eggs', 'calories': 140, 'protein': 12, 'carbs': 2, 'fat': 10, 'category': 'breakfast'},
        {'name': 'Whole Grain Toast', 'calories': 80, 'protein': 3, 'carbs': 15, 'fat': 1, 'category': 'breakfast'},
        {'name': 'Smoothie Bowl', 'calories': 200, 'protein': 8, 'carbs': 35, 'fat': 2, 'category': 'breakfast'},
        {'name': 'Avocado Toast', 'calories': 220, 'protein': 8, 'carbs': 20, 'fat': 12, 'category': 'breakfast'},
        {'name': 'Protein Pancakes', 'calories': 180, 'protein': 15, 'carbs': 20, 'fat': 5, 'category': 'breakfast'},
        {'name': 'Cereal with Milk', 'calories': 160, 'protein': 6, 'carbs': 28, 'fat': 3, 'category': 'breakfast'}
    ],
    'lunch': [
        {'name': 'Grilled Chicken Salad', 'calories': 250, 'protein': 30, 'carbs': 8, 'fat': 12, 'category': 'lunch'},
        {'name': 'Quinoa Bowl', 'calories': 320, 'protein': 12, 'carbs': 45, 'fat': 8, 'category': 'lunch'},
        {'name': 'Turkey Sandwich', 'calories': 280, 'protein': 18, 'carbs': 35, 'fat': 10, 'category': 'lunch'},
        {'name': 'Vegetable Soup', 'calories': 120, 'protein': 6, 'carbs': 20, 'fat': 2, 'category': 'lunch'},
        {'name': 'Salmon with Rice', 'calories': 380, 'protein': 25, 'carbs': 35, 'fat': 15, 'category': 'lunch'},
        {'name': 'Pasta Primavera', 'calories': 300, 'protein': 10, 'carbs': 45, 'fat': 8, 'category': 'lunch'},
        {'name': 'Bean Burrito', 'calories': 320, 'protein': 12, 'carbs': 50, 'fat': 6, 'category': 'lunch'},
        {'name': 'Caesar Salad', 'calories': 200, 'protein': 8, 'carbs': 10, 'fat': 15, 'category': 'lunch'}
    ],
    'dinner': [
        {'name': 'Grilled Salmon', 'calories': 280, 'protein': 34, 'carbs': 0, 'fat': 15, 'category': 'dinner'},
        {'name': 'Lean Beef Steak', 'calories': 320, 'protein': 35, 'carbs': 0, 'fat': 18, 'category': 'dinner'},
        {'name': 'Vegetarian Stir Fry', 'calories': 220, 'protein': 8, 'carbs': 35, 'fat': 6, 'category': 'dinner'},
        {'name': 'Chicken Breast', 'calories': 165, 'protein': 31, 'carbs': 0, 'fat': 3.6, 'category': 'dinner'},
        {'name': 'Shrimp Pasta', 'calories': 380, 'protein': 25, 'carbs': 45, 'fat': 12, 'category': 'dinner'},
        {'name': 'Lentil Curry', 'calories': 280, 'protein': 15, 'carbs': 45, 'fat': 4, 'category': 'dinner'},
        {'name': 'Baked Cod', 'calories': 200, 'protein': 25, 'carbs': 0, 'fat': 10, 'category': 'dinner'},
        {'name': 'Tofu Stir Fry', 'calories': 240, 'protein': 12, 'carbs': 25, 'fat': 10, 'category': 'dinner'}
    ],
    'snacks': [
        {'name': 'Apple', 'calories': 95, 'protein': 0.5, 'carbs': 25, 'fat': 0.3, 'category': 'snacks'},
        {'name': 'Almonds', 'calories': 160, 'protein': 6, 'carbs': 6, 'fat': 14, 'category': 'snacks'},
        {'name': 'Banana', 'calories': 105, 'protein': 1.3, 'carbs': 27, 'fat': 0.4, 'category': 'snacks'},
        {'name': 'Greek Yogurt', 'calories': 100, 'protein': 17, 'carbs': 6, 'fat': 0.5, 'category': 'snacks'},
        {'name': 'Carrot Sticks', 'calories': 160, 'protein': 1, 'carbs': 12, 'fat': 0.3, 'category': 'snacks'},
        {'name': 'Hummus with Pita', 'calories': 180, 'protein': 6, 'carbs': 25, 'fat': 6, 'category': 'snacks'},
        {'name': 'Protein Bar', 'calories': 200, 'protein': 20, 'carbs': 15, 'fat': 8, 'category': 'snacks'},
        {'name': 'Mixed Berries', 'calories': 60, 'protein': 1, 'carbs': 15, 'fat': 0.5, 'category': 'snacks'}
    ]
}

def calculate_meal_distribution(total_calories):
    """Calculate how many calories to allocate to each meal"""
    if total_calories <= 1200:
        return {
            'breakfast': int(total_calories * 0.25),
            'lunch': int(total_calories * 0.35),
            'dinner': int(total_calories * 0.30),
            'snacks': int(total_calories * 0.10)
        }
    elif total_calories <= 1800:
        return {
            'breakfast': int(total_calories * 0.25),
            'lunch': int(total_calories * 0.30),
            'dinner': int(total_calories * 0.30),
            'snacks': int(total_calories * 0.15)
        }
    else:
        return {
            'breakfast': int(total_calories * 0.25),
            'lunch': int(total_calories * 0.30),
            'dinner': int(total_calories * 0.25),
            'snacks': int(total_calories * 0.20)
        }

def generate_meal_plan(target_calories, preferences=None):
    """Generate a meal plan based on target calories and preferences"""
    meal_distribution = calculate_meal_distribution(target_calories)
    meal_plan = {}
    total_calories = 0
    
    for meal_type, target_meal_calories in meal_distribution.items():
        available_foods = FOOD_DATABASE[meal_type]
        
        # Filter by preferences if provided
        if preferences and 'dietary_restrictions' in preferences:
            restrictions = preferences['dietary_restrictions']
            if 'vegetarian' in restrictions:
                available_foods = [f for f in available_foods if 'chicken' not in f['name'].lower() and 'beef' not in f['name'].lower() and 'salmon' not in f['name'].lower() and 'cod' not in f['name'].lower()]
            if 'vegan' in restrictions:
                available_foods = [f for f in available_foods if 'yogurt' not in f['name'].lower() and 'eggs' not in f['name'].lower()]
        
        # Select foods that fit within calorie target
        selected_foods = []
        current_calories = 0
        
        # Try to find a combination that fits the target
        attempts = 0
        while current_calories < target_meal_calories and attempts < 50:
            food = random.choice(available_foods)
            if current_calories + food['calories'] <= target_meal_calories * 1.2:  # Allow 20% overage
                selected_foods.append(food)
                current_calories += food['calories']
            attempts += 1
        
        meal_plan[meal_type] = {
            'foods': selected_foods,
            'total_calories': current_calories,
            'target_calories': target_meal_calories
        }
        total_calories += current_calories
    
    meal_plan['total_calories'] = total_calories
    meal_plan['target_calories'] = target_calories
    
    return meal_plan

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/meal-planner')
def meal_planner():
    return render_template('meal_planner.html')

@app.route('/generate-meal-plan', methods=['POST'])
def generate_meal_plan_route():
    data = request.get_json()
    target_calories = int(data.get('target_calories', 2000))
    preferences = data.get('preferences', {})
    
    meal_plan = generate_meal_plan(target_calories, preferences)
    
    return jsonify({
        'success': True,
        'meal_plan': meal_plan
    })

@app.route('/food-database')
def food_database():
    return render_template('food_database.html', food_database=FOOD_DATABASE)

@app.route('/nutrition-calculator')
def nutrition_calculator():
    return render_template('nutrition_calculator.html')

@app.route('/calculate-nutrition', methods=['POST'])
def calculate_nutrition():
    data = request.get_json()
    foods = data.get('foods', [])
    
    total_calories = 0
    total_protein = 0
    total_carbs = 0
    total_fat = 0
    
    for food in foods:
        total_calories += food.get('calories', 0)
        total_protein += food.get('protein', 0)
        total_carbs += food.get('carbs', 0)
        total_fat += food.get('fat', 0)
    
    return jsonify({
        'total_calories': total_calories,
        'total_protein': round(total_protein, 1),
        'total_carbs': round(total_carbs, 1),
        'total_fat': round(total_fat, 1)
    })

@app.route('/save-meal-plan', methods=['POST'])
def save_meal_plan():
    data = request.get_json()
    meal_plan = data.get('meal_plan')
    
    # In a real app, you would save this to a database
    # For now, we'll just store it in the session
    session['saved_meal_plan'] = meal_plan
    
    return jsonify({
        'success': True,
        'message': 'Meal plan saved successfully!'
    })

@app.route('/saved-plans')
def saved_plans():
    saved_plan = session.get('saved_meal_plan')
    return render_template('saved_plans.html', saved_plan=saved_plan)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        if not all([name, email, message]):
            flash('Please fill in all fields.', 'error')
        else:
            flash('Thank you for your message! We\'ll get back to you soon.', 'success')
        
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.route('/api/foods')
def api_foods():
    """API endpoint to get all foods"""
    all_foods = []
    for category, foods in FOOD_DATABASE.items():
        for food in foods:
            food_copy = food.copy()
            food_copy['category'] = category
            all_foods.append(food_copy)
    
    return jsonify(all_foods)

@app.route('/api/foods/<category>')
def api_foods_by_category(category):
    """API endpoint to get foods by category"""
    if category in FOOD_DATABASE:
        return jsonify(FOOD_DATABASE[category])
    else:
        return jsonify({'error': 'Category not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 