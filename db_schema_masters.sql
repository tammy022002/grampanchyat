CREATE TABLE Department_Master (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(255)
);

CREATE TABLE Account_Head_Master (
    account_head_id SERIAL PRIMARY KEY,
    account_head_name VARCHAR(255)
);

CREATE TABLE Tax_Type_Master (
    tax_type_id SERIAL PRIMARY KEY,
    tax_type_name VARCHAR(255)
);

CREATE TABLE Contractor_Master (
    contractor_id SERIAL PRIMARY KEY,
    contractor_name VARCHAR(255)
);

CREATE TABLE Status_Master (
    status_id SERIAL PRIMARY KEY,
    status_name VARCHAR(255)
);

CREATE TABLE Designation_Master (
    designation_id SERIAL PRIMARY KEY,
    designation_name VARCHAR(255)
);

CREATE TABLE Payment_Mode_Master (
    payment_mode_id SERIAL PRIMARY KEY,
    payment_mode_name VARCHAR(255)
);

CREATE TABLE Asset_Type_Master (
    asset_type_id SERIAL PRIMARY KEY,
    asset_type_name VARCHAR(255)
);

CREATE TABLE Road_Type_Master (
    road_type_id SERIAL PRIMARY KEY,
    road_type_name VARCHAR(255)
);

CREATE TABLE Loan_Type_Master (
    loan_type_id SERIAL PRIMARY KEY,
    loan_type_name VARCHAR(255)
);

CREATE TABLE Investment_Type_Master (
    investment_type_id SERIAL PRIMARY KEY,
    investment_type_name VARCHAR(255)
);
