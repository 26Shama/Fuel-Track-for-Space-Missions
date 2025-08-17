# 🚀 Fuel-Track-for-Space-Missions 
FuelTrack for Space Missions is an AI-powered web application designed to intelligently estimate spacecraft fuel requirements.By leveraging machine learning (Random Forest Regressor) and a user-friendly Flask web interface, it predicts total fuel needed, calculates additional fuel purchases, and estimates overall mission fuel costs.
This project bridges aerospace knowledge and data science to support efficient and cost-conscious mission planning.
## 🎯Objective 
The goal of FuelTrack is to create a reliable, interactive platform where:
-Users can input spacecraft mission parameters (payload, orbit type, thrust, ISP, engine type, launch angle).
-The system predicts fuel required, additional fuel needed, and cost estimates.
-Mission planners receive quick, data-driven insights for fuel budgeting.
-The tool minimizes the risks of over/under-fueling while optimizing costs.
## ✨ Features 
-🔐 User Input Validation for mission parameters
-🛰️ Fuel Requirement Prediction using Random Forest Regressor
-📊 Cost Estimation based on current fuel availability & price per kg
-📉 Fuel Deficit Alerts (Buy More / Sufficient Fuel messages)
-📈 Optional Efficiency Scoring for mission feasibility
-🌐 Interactive Flask Web App with HTML/CSS/Jinja2
-🧹 Preprocessing Pipeline (outlier removal, encoding, transformations)
-📂 Synthetic Dataset Integration (1000+ simulated missions)
