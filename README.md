# About Project

## Understanding the Need

* ❓ Problem: Banks earn profit by providing loan to their authorized customers. Despite intensive screening process, banks are vulnerable to receive the money back in ensured time. Such events lead higher non-performing assets (NPA) thereby impacting the overall robustness of the economy.
* 💡 Solution: This problem can be reolved to a certain limit by automating the vulnerability of borrower based on the provided details. 
**This project was built to help banks predict the impact of incident raised by customers. Morevover, with such online interacting application form, both customers and banks can take decision of their interest seamlessly.*

## Project Flow 
<p align="center">
<img src="https://github.com/amit0902/Loan-Prediction-Deployment/blob/main/Project%20Flow.png" width=800 height=500>
</p>

### *💠 Stage I: Understanding Dataset*
Housing Finance company deals in all kinds of home loans. They have presence across all urban, semi urban and rural areas. Customer first applies for home loan and after that company validates the customer eligibility for loan. Company wants to automate the loan eligibility process (real time) based on customer detail provided while filling online application form. These details are:
* Loan ID
* Gender
* Marital Status
* Education
* Self Employed
* Number of Dependents
* Applicant Income
* Coapplicant Income
* Loan Amount
* Loan Amount Term
* Credit History
* Property Area
* Loan Status (Output Feature)

#### *To automate this process, they have provided a dataset to identify the customers segments that are eligible for loan amount so that they can specifically target these customers.* 
* Train Data: [Train CSV](https://github.com/amit0902/Loan-Prediction-Deployment/blob/main/train.csv)
* Test Data: [Test CSV](https://github.com/amit0902/Loan-Prediction-Deployment/blob/main/test.csv)
### Inferences
<img align="left" src="https://github.com/amit0902/Loan-Prediction-Deployment/blob/main/Slide4.PNG" width=100%> | <img align="left" src="https://github.com/amit0902/Loan-Prediction-Deployment/blob/main/Slide5.PNG" width=100%>
|:---:|:---:|
* There are 614 records in the Train Dataset & 367 records in the Test Dataset.
* There are no duplicated data in Train set.
#### 1. Training Dataset has:
 * Loan_ID | Gender | Married | Dependents | Education | Self_Employed | Property_Area | Loan_status as Object types. 
 * ApplicantIncome field is of Integer type.
 * The other 3 fields namely CoapplicantIncome | Loan_Amount_Term | Credit_History are Floating point type.
#### 2. Testing Dataset has:
 * CoapplicantIncome is of Integer Type not Floating
 * There is no column as Loan_status, that’s what we have to predict by creating a model.

### *💠 Stage II: Data Visualization*

### *💠 Stage III: Data Processing*

### *💠 Stage IV: Modelling*

### *💠 Stage V: Feature Engineering*

### *💠 Stage VI: Rebuild Model*

### *💠 Stage VII: Predictions*
