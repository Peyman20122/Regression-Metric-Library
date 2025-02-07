# Regression-Metric-Library

### ** What metric does this code calculate?**
This code defines a **Custom Score** for evaluating a regression model, which is a combination of two metrics:

1. **\( R^2 \) (coefficient of determination)**
- Indicates how much of the variance in the actual data the model explains.
- The value is between **0 and 1** (the higher, the better).

2. **\( MAPE \) (Mean Absolute Percentage Error)**
- Indicates the relative error of the model.
- The value is between **0 and 1** (the lower, the better).

### **Formula used in the code:**

![image](https://github.com/user-attachments/assets/3d3297e6-1dce-4252-ae7c-8d4f2f2125e5)

- The value **\( 1 - MAPE \)** is used to reverse the effect of MAPE, so that a lower value gives a better score.
- Finally, the average of the two values ​​is taken and multiplied by 100 to give the output as a percentage.

### **Conclusion**
✅ This class now calculates a metric.
✅ It can be used to analyze various regression models.
✅ The output can be easily prepared as a report.

🚀 **This method is useful for creating a standard library in machine learning!**

## For example

![image](https://github.com/user-attachments/assets/b3e7bc2b-6bb2-4fbb-9f0c-7d773a81e410)

