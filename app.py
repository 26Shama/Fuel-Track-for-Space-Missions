from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)   

# Load the trained model
model = joblib.load('spacecraft_fuel_model.pkl')  # Update with actual model file name if different

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    form_data = {
        'payload_kg': request.form.get('payload_kg', ''),
        'thrust_kN': request.form.get('thrust_kN', ''),
        'isp': request.form.get('isp', ''),
        'launch_angle_deg': request.form.get('launch_angle_deg', ''),
        'orbit_type': request.form.get('orbit_type', ''),
        'engine_type': request.form.get('engine_type', ''),
        'current_fuel_kg': request.form.get('current_fuel_kg', ''),
        'fuel_price_per_kg': request.form.get('fuel_price_per_kg', ''),
    }

    error_msg = None
    prediction_text = None

    # Check if any field is missing
    if any(value.strip() == '' for value in form_data.values()):
        error_msg = "⚠ Please fill in all the fields."
        return render_template('index.html', error_msg=error_msg, request=request)

    try:
        # Convert to appropriate types
        payload_kg = float(form_data['payload_kg'])
        thrust_kN = float(form_data['thrust_kN'])
        isp = float(form_data['isp'])
        launch_angle_deg = float(form_data['launch_angle_deg'])
        current_fuel_kg = float(form_data['current_fuel_kg'])
        fuel_price_per_kg = float(form_data['fuel_price_per_kg'])
    except ValueError:
        error_msg = "⚠ Please enter valid numeric values."
        return render_template('index.html', error_msg=error_msg, request=request)

    # Validate categorical choices
    valid_orbits = ['LEO', 'GTO', 'Moon', 'Mars', 'Other']
    valid_engines = ['Liquid', 'Solid', 'Hybrid']

    if form_data['orbit_type'] not in valid_orbits:
        error_msg = "⚠ Invalid orbit type selected."
        return render_template('index.html', error_msg=error_msg, request=request)

    if form_data['engine_type'] not in valid_engines:
        error_msg = "⚠ Invalid engine type selected."
        return render_template('index.html', error_msg=error_msg, request=request)

    # Prepare input for prediction
    input_df = pd.DataFrame([[payload_kg, thrust_kN, isp, launch_angle_deg,
                              form_data['orbit_type'], form_data['engine_type'],
                              current_fuel_kg, fuel_price_per_kg]],
                            columns=['payload_kg', 'thrust_kN', 'isp', 'launch_angle_deg',
                                     'orbit_type', 'engine_type', 'current_fuel_kg', 'fuel_price_per_kg'])

    try:
        # Predict
        fuel_required_kg = model.predict(input_df)[0]
        fuel_to_buy_kg = max(0, fuel_required_kg - current_fuel_kg)
        fuel_cost = fuel_to_buy_kg * fuel_price_per_kg

        prediction_text = (
            f"🚀 Fuel Required: {fuel_required_kg:.2f} kg\n"
            f"🛢 Current Available Fuel: {current_fuel_kg:.2f} kg\n"
            f"⛽ Fuel to Buy: {fuel_to_buy_kg:.2f} kg\n"
            f"💰 Estimated Fuel Cost: ₹{fuel_cost:,.2f}"
        )

    except Exception as e:
        error_msg = f"❌ Prediction error: {str(e)}"

    return render_template('index.html', prediction_text=prediction_text, error_msg=error_msg, request=request)

if __name__ == '__main__':  
    app.run(debug=True)
