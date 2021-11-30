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
Housing Finance company deals in all kinds of home loans. They have presence across all urban, semi urban and rural areas. Customer first applies for home loan and after that company validates the customer eligibility for loan. Company wants to automate the loan eligibility process (real-time) based on customer detail provided while filling online application form. These details are:
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
### Inferences Part 1
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
#### 3. Null Values:
|Train Data|Test Data|
|----------|---------|
| 50 - Credit_History | 29 - Credit_History |
| 32 - Self_Employed | 23 - Self_Employed|
| 22 - Loan_Amount | 05 - Loan_Amount |
| 15 - Dependents | 10 - Dependents |
| 14 - Loan_Amount_Terms | 06 - Loan_Amount_Terms |
| 13 - Gender| 11 - Gender |
| 03 - Married||

#### 4. Hypothesis Generation:
* ***Salary:** Applicants with higher income should have higher chances of loan approval*
* ***Credit history:** Applicants who have followed Credit guidelines should have better chances*
* ***Loan Amount:** Lower Loan Amounts should have better chances of approval*
* ***Loan Amount Terms:** Shorter tenures should have better chances of approval*
* ***EMI:** Lower the expected monthly installment for the applicant, compared to income, the better the approval chances*

### *💠 Stage II: Data Visualization*
#### 1. Univariate Analysis on Categorical Data
<img src="https://github.com/amit0902/Loan-Prediction-Deployment/blob/main/IndependentCategory.png" width=90%>

- 80% are Male Applicants, however both Male and Female have got equal proportion of Loan Approval
- 65% are Married and those who are Married have more chances to get Loan Approved
- 85% are Self_Employed, however equal proportion of Loan Approval

#### 2. Univariate Analysis on Ordinal Data
<img src="https://github.com/amit0902/Loan-Prediction-Deployment/blob/main/IndependentOrdinal.jpg" width=90%>

- **57%** are Parents have no Dependents (Newly Married or No Child).
  - However Bank has preferred to give Loan to Couple having **2 Dependents**
- **78%** are Graduate.
  - Those who are **Graduate** have greater chances of Loan Approval
- **37%** are having Property in Semi-Urban area.
  - Those having property in **Semi-Urban area** have greater chances of Loan Approval

#### 3. Univariate Analysis on Numerical Data
<img src="https://github.com/amit0902/Loan-Prediction-Deployment/blob/main/IndependentNumerical.png" width=90%>

- Most of the **data seems to be right skewed** as data congestion towards left side.
- Also from the data we can conclude that if **mean>median (Right Skew)** else vice versa.
- **84%** have Credit History as per guidelines, and mostly those whose Credit History meets guidelines have got Loan Approval
- **85%** have 360 Months (30 Years) of Loan_Amount_Term, however people having Loan_Amount_Term of 1,5, & 10 Year have maximum chances of Loan Approval

#### 4. Inferences Part 2
- Independent Variable [Categorical Type] :
	- Gender & Self_Employed Status doesn't make significant difference in getting Loan.
	- If you are Married then more chances of getting Loan.
- Indpendent Variable [Ordinal Type] :
	- Parents with 2 Dependents have more chances of approval.
	- If you are graduated than more chances of Loan approval.
	- People owning property in Semi-Urban area have greater chances of Loan Approval
- Indpendent Variable [Numerical Type] :
	- Most of data is Right Skewed except Loan_Amount_Term
	- Data also has some outliers present, thereby needs Data Transformation
	- People having Credit History as per guidelines and Loan_Amount_Term of 1,5, & 10 Years have got Loan approval
- Dependent Variable [Target]
	- Almost 70% have Loan Approved
 #### 5. Inferences
 - Observations
	 - Gender and Self_Employed have no significant effect on Loan_Status
	 - If an applicant is Graduated having property in Semi-Urban area and is Married with 2 Dependents and Credit History as per Guidelines with Loan_Amount_Term of 1,5,10 Year then Loan is Approved
- Hypothesis
	- It is not necessary that higher income means higher loan amount for both Applicant Income and Coapplicant Income
	- Gender & Self_Employed is not a criteria for considering Loan Approval
	- Higher Loan Amount Lesser the chance of getting Loan Approved

### *💠 Stage III: Data Processing*

### *💠 Stage IV: Modelling*

### *💠 Stage V: Feature Engineering*

### *💠 Stage VI: Rebuild Model*

### *💠 Stage VII: Predictions*
