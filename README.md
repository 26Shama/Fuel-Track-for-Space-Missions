# 🚀 Fuel-Track-for-Space-Missions 
FuelTrack for Space Missions is an AI-powered web app that predicts spacecraft fuel needs using a Random Forest Regressor. Through a simple Flask interface, it estimates total fuel required, additional fuel to purchase, and mission cost, helping planners make efficient and cost-conscious decisions.
<hr style="height:3px; background-color:#bbb; border:none;" />

## 🎯Objective 
The goal of FuelTrack is to create a reliable, interactive platform where:
- Users can input spacecraft mission parameters (payload, orbit type, thrust, ISP, engine type, launch angle).
- The system predicts fuel required, additional fuel needed, and cost estimates.
- Mission planners receive quick, data-driven insights for fuel budgeting.
- The tool minimizes the risks of over/under-fueling while optimizing costs.
  <hr style="height:3px; background-color:#bbb; border:none;" />
  
## ✨ Features 
- 🔐 User Input Validation for mission parameters
- 🛰️ Fuel Requirement Prediction using Random Forest Regressor
- 📊 Cost Estimation based on current fuel availability & price per kg
- 📉 Fuel Deficit Alerts (Buy More / Sufficient Fuel messages)
- 📈 Optional Efficiency Scoring for mission feasibility
- 🌐 Interactive Flask Web App with HTML/CSS/Jinja2
- 🧹 Preprocessing Pipeline (outlier removal, encoding, transformations)
- 📂 Synthetic Dataset Integration (1000+ simulated missions)
  <hr style="height:3px; background-color:#bbb; border:none;" />

  ## 🛠️ Tech Stack

| Layer       | Technology           | Purpose                                   |
|-------------|----------------------|-------------------------------------------|
| Frontend    | HTML, CSS, Jinja2    | User Interface                            |
| Backend     | Python (Flask)       | Server & Prediction API                   |
| ML Model    | Random Forest (Sklearn) | Fuel Requirement Prediction             |
| Libraries   | Pandas, NumPy, Joblib | Data processing & ML pipeline             |
| Dataset     | Synthetic CSV (1000+) | Training & evaluation of predictions      |
<hr style="height:3px; background-color:#bbb; border:none;" />

## 📂 Project Structure  

- backend/ → Flask server & ML model integration  
- templates/ → HTML templates (Jinja2)  
- static/ → CSS, images, and assets  
- dataset/ → Synthetic spacecraft dataset  
- notebooks/ → Jupyter notebooks for model training  
- requirements.txt → Python dependencies  
- README.md → Project documentation  
 <hr style="height:3px; background-color:#bbb; border:none;" />

## 🚀 Installation & Setup  

1. **Clone the Repository**  

```bash
git clone https://github.com/YourUsername/FuelTrack-SpaceMissions.git
cd FuelTrack-SpaceMissions
```

2.**Install Dependencies**
For backend:
```bash
cd backend
pip install -r requirements.txt
```

3.**Run the Application**
Start backend:
```bash
cd backend
python app.py
```
 <hr style="height:3px; background-color:#bbb; border:none;" />
 
## 📸 Screenshots

### 🏠 Home Page 
<img width="1871" height="859" alt="Screenshot 2025-08-17 132350" src="https://github.com/user-attachments/assets/59b61a5f-0f4c-440e-8a72-bd6f83667c43" />


### 📊 Fuel Prediction Result 
<img width="1378" height="164" alt="edited" src="https://github.com/user-attachments/assets/39ed432a-f9c3-473e-a6ce-bf21b66f59df" />

📜 License This project is licensed under the MIT License.
