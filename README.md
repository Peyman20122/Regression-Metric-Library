# Regression-Metric-Library
### **🚀 Evaluating Regression Models with Julia!**  

🔎 **How can we evaluate a regression model with a single score?**  
In this post, we implement a simple yet effective metric in **Julia** that combines **R² Score** and **MAPE** to generate an overall performance score for the model.  

📌 **📜 Julia Code for Model Evaluation Metric:**  
```julia
struct MetricRegLearn
    r2score::Float64
    mape::Float64
end

function metric(m::MetricRegLearn)
    final_score = ((1 - m.mape) + m.r2score) / 2 * 100
    return final_score
end

# Example usage:
model_metrics = MetricRegLearn(0.92, 0.08)
println("Final Score: ", metric(model_metrics))
```

📊 **Why is this metric useful?**  
✅ Combines two widely used evaluation metrics  
✅ Simple and efficient to compute  
✅ Can be extended to include other metrics like **MAE, RMSE, RMSLE**  

💡 **Ideas for improvement:**  
🔹 Incorporating additional metrics such as **SMAPE and Adjusted R²**  
🔹 Using **dynamic weighting** for each metric  

📢 **What metrics do you use for evaluating regression models? 🤔**  
🔗 **#JuliaLang #MachineLearning #Regression #ModelEvaluation**  

[@JuliaLang]([https://github.com/JuliaLang])
[@Juliaorgir]([https://github.com/Juliair-org])

