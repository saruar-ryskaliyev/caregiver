CREATE TABLE USERS (
    user_id INT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    given_name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20) UNIQUE NOT NULL,
    profile_description TEXT,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE CAREGIVER (
    caregiver_user_id INT PRIMARY KEY,
    photo TEXT,
    gender VARCHAR(10) NOT NULL,
    caregiving_type VARCHAR(50) NOT NULL,
    hourly_rate DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (caregiver_user_id) REFERENCES USERS(user_id)
);

CREATE TABLE MEMBER (
    member_user_id INT PRIMARY KEY,
    house_rules TEXT,
    FOREIGN KEY (member_user_id) REFERENCES USERS(user_id)
);

CREATE TABLE ADDRESS (
    member_user_id INT,
    house_number VARCHAR(10),
    street VARCHAR(255),
    town VARCHAR(255),
    PRIMARY KEY (member_user_id),
    FOREIGN KEY (member_user_id) REFERENCES MEMBER(member_user_id)
);

CREATE TABLE JOB (
    job_id INT PRIMARY KEY,
    member_user_id INT,
    required_caregiving_type VARCHAR(50),
    other_requirements TEXT,
    date_posted DATE,
    FOREIGN KEY (member_user_id) REFERENCES MEMBER(member_user_id)
);

CREATE TABLE JOB_APPLICATION (
    caregiver_user_id INT,
    job_id INT,
    date_applied DATE,
    PRIMARY KEY (caregiver_user_id, job_id),
    FOREIGN KEY (caregiver_user_id) REFERENCES CAREGIVER(caregiver_user_id),
    FOREIGN KEY (job_id) REFERENCES JOB(job_id)
);

CREATE TABLE APPOINTMENT (
    appointment_id INT PRIMARY KEY,
    caregiver_user_id INT,
    member_user_id INT,
    appointment_date DATE,
    appointment_time TIME,
    work_hours INT,
    status VARCHAR(20),
    FOREIGN KEY (caregiver_user_id) REFERENCES CAREGIVER(caregiver_user_id),
    FOREIGN KEY (member_user_id) REFERENCES MEMBER(member_user_id)
);