import streamlit as st
import pandas as pd 
from crud import * 
import datetime
import streamlit.components.v1 as stc


def main():
    st.title("Caregiver Database Assignment Saruar Ryskaliyev")
    menu = ["Create", "Read", "Update", "Delete"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Create":
        table_name = "USERS"
        st.subheader("Add Item")
        table_name = st.selectbox("Table Name",["USERS","CAREGIVER","member",
                                                "address","job","job_application","appointment"])
        if table_name == "USERS":
            user_id = st.text_input("ID")
            email = st.text_input("Email")
            given_name = st.text_input("Given Name")
            surname = st.text_input("Surname")
            city = st.text_input("City")
            phone_number = st.text_input("Phone Number")
            profile_description = st.text_input("Profile Description")
            password = st.text_input("Password")
            if st.button("Add User"):
                if user_id == " " or email == " " or given_name == " " or surname == " " or city == " " or phone_number == " " or profile_description == " " or password == " ":
                    st.warning("Please Fill All The Fields")
                elif user_id.isdigit() == False:
                    st.warning("ID must be a number")
                elif not read_data(table_name).empty and str(user_id) in str(read_data(table_name)['user_id'].values):
                    st.warning("ID already exists")
                else:
                    add_data(table_name,[user_id, email, given_name, surname, city, phone_number, profile_description, password])
                    st.success("Added ::{} ::To Users".format(profile_description))
        elif table_name == "CAREGIVER":
            caregiver_user_id = st.text_input("User ID")
            photo = st.text_input("Photo URL")
            gender = st.selectbox("Gender", ["Male", "Female"])
            caregiving_type = st.selectbox("Caregiving Type", ["Elderly Care", "Baby Sitter", "Special Needs Care", "Senior Care"])
            hourly_rate = st.text_input("Hourly Rate")

            if st.button("Add Caregiver"):
                if caregiver_user_id == " " or photo == " " or gender == " " or caregiving_type == " " or hourly_rate == " ":
                    st.warning("Please Fill All The Fields")
                elif caregiver_user_id.isdigit() == False:
                    st.warning("User ID must be a number")
                elif not read_data(table_name).empty and str(caregiver_user_id) in str(read_data(table_name)['caregiver_user_id'].values):
                    st.warning("User ID already exists")
                elif not hourly_rate.replace('.', '', 1).isdigit():
                        st.warning("Hourly Rate must be a number")
                elif check_user_id_exists(caregiver_user_id) == False:
                    st.warning("User ID does not exist")
                else:
                    add_data(table_name, [caregiver_user_id, photo, gender, caregiving_type, hourly_rate])
                    st.success("Added ::{} ::To Caregiver".format(caregiver_user_id))
        
        elif table_name == "member":
            member_user_id = st.text_input("User ID")
            house_rules = st.text_input("House Rules")

            if st.button("Add Member"):
                if member_user_id == " " or house_rules == " ":
                    st.warning("Please Fill All The Fields")
                elif member_user_id.isdigit() == False:
                    st.warning("User ID must be a number")
                elif not read_data(table_name).empty and str(member_user_id) in str(read_data(table_name)['member_user_id'].values):
                    st.warning("User ID already exists")
                elif check_user_id_exists(member_user_id) == False:
                    st.warning("User ID does not exist")
                else:
                    add_data(table_name, [member_user_id, house_rules])
                    st.success("Added ::{} ::To Member".format(member_user_id))
        elif table_name == "address":
            member_user_id = st.text_input("User ID")
            house_number = st.text_input("House Number")
            street = st.text_input("Street")
            town = st.text_input("Town")

            if st.button("Add Address"):
                if member_user_id == " " or street == " " or town == " " or house_number == " ":
                    st.warning("Please Fill All The Fields")
                elif member_user_id.isdigit() == False:
                    st.warning("User ID must be a number")
                elif not read_data(table_name).empty and str(member_user_id) in str(read_data(table_name)['member_user_id'].values):
                    st.warning("User ID already exists")
                elif check_user_id_exists(member_user_id) == False:
                    st.warning("User ID does not exist")
                else:
                    add_data(table_name, [member_user_id, house_number, street, town])
                    st.success("Added ::{} ::To Address".format(member_user_id))
        elif table_name == "job":
            job_id = st.text_input("Job ID")
            member_user_id = st.text_input("Member User ID")
            required_caregiving_type = st.selectbox("Caregiving Type", ["Elderly Care", "Baby Sitter", "Special Needs Care", "Senior Care"])
            other_requirements = st.text_input("Other Requirements")
            date_posted = st.date_input("Date Posted")
            date_posted = date_posted.strftime("%Y-%m-%d")

            if st.button("Add Job"):
                if job_id == " " or member_user_id == " " or required_caregiving_type == " " or other_requirements == " " or date_posted == " ":
                    st.warning("Please Fill All The Fields")
                elif job_id.isdigit() == False:
                    st.warning("Job ID must be a number")
                elif member_user_id.isdigit() == False:
                    st.warning("Member User ID must be a number")
                elif not read_data(table_name).empty and str(job_id) in str(read_data(table_name)['job_id'].values):
                    st.warning("Job ID already exists")
                elif check_member_id_exist(member_user_id) == False:
                    st.warning("Member User ID does not exist")
                else:
                    add_data(table_name, [job_id, member_user_id, required_caregiving_type, other_requirements, date_posted])
                    st.success("Added ::{} ::To Job".format(job_id))
        
        elif table_name == "job_application":
            caregiver_user_id = st.text_input("Caregiver User ID")
            job_id = st.text_input("Job ID")
            date_applied = st.date_input("Date Applied")
            date_applied = date_applied.strftime("%Y-%m-%d")

            if st.button("Add Job Application"):
                if caregiver_user_id == " " or job_id == " " or date_applied == " ":
                    st.warning("Please Fill All The Fields")
                elif caregiver_user_id.isdigit() == False:
                    st.warning("Caregiver User ID must be a number")
                elif job_id.isdigit() == False:
                    st.warning("Job ID must be a number")
                elif read_data(table_name).empty and str(caregiver_user_id) in str(read_data(table_name)['caregiver_user_id'].values):
                    st.warning("Caregiver User ID does not exist")
                elif check_user_id_exists(caregiver_user_id) == False:
                    st.warning("Caregiver User ID does not exist")
                elif check_job_id_exist(job_id) == False:
                    st.warning("Job ID does not exist")
                else:
                    add_data(table_name, [caregiver_user_id, job_id, date_applied])
                    st.success("Added ::{} ::To Job Application".format(caregiver_user_id))
                
        elif table_name == "appointment":
            appointment_id = st.text_input("Appointment ID")
            caregiver_user_id = st.text_input("Caregiver User ID")
            member_user_id = st.text_input("Member User ID")
            appointment_date = st.date_input("Appointment Date")
            appointment_time = st.time_input("Appointment Time")
            work_hours = st.text_input("Work Hours")
            status = st.selectbox("Status", ["Accepted", "Rejected", "Pending"])

            appointment_date = appointment_date.strftime("%Y-%m-%d")
            appointment_time = appointment_time.strftime("%H:%M")

            if st.button("Add Appointment"):
                if appointment_id == " " or caregiver_user_id == " " or member_user_id == " " or appointment_date == " " or appointment_time == " " or status == " ":
                    st.warning("Please Fill All The Fields")
                elif appointment_id.isdigit() == False:
                    st.warning("Appointment ID must be a number")
                elif caregiver_user_id.isdigit() == False:
                    st.warning("Caregiver User ID must be a number")
                elif member_user_id.isdigit() == False:
                    st.warning("Member User ID must be a number")
                elif read_data(table_name).empty and str(caregiver_user_id) in str(read_data(table_name)['caregiver_user_id'].values):
                    st.warning("Caregiver User ID does not exist")
                elif read_data(table_name).empty and str(appointment_id) in str(read_data(table_name)['appointment_id'].values):
                    st.warning("Appointment ID already exists")
                elif check_user_id_exists(caregiver_user_id) == False:
                    st.warning("Caregiver User ID does not exist")
                elif check_user_id_exists(member_user_id) == False:
                    st.warning("Member User ID does not exist")
                elif work_hours.isdigit() == False:
                    st.warning("Work Hours must be a number")
                else:
                    add_data(table_name, [appointment_id, caregiver_user_id, member_user_id, appointment_date, appointment_time, work_hours, status])
                    st.success("Added ::{} ::To Appointment".format(appointment_id))



    elif choice == "Read":
        st.subheader("View Table")
        table_name = st.selectbox("Table Name",["users","caregiver","member",
                                                "address","job","job_application","appointment"])
        result = read_data(table_name)
        if result.empty:
            st.warning("No data available")
        else:
            st.write(result)

    elif choice == "Update":
        st.subheader("Update Table")
        table_name = st.selectbox("Table Name",["users","caregiver","member",
                                                "address","job","job_application","appointment"])
        data = read_data(table_name)
        if len(data) == 0:
            st.warning("No data to update")
        else:
            st.write(data)
            row = st.text_input("Enter which row to update")
            if row == '':
                st.warning("Please input a row number")
            elif not row.isnumeric() or int(row) > len(data) or int(row) < 0:
                st.warning("Please input a valid row number")
            else:
                row = int(row)
                st.write('Unchangeable key ' + data.columns[0] + ': ', data.iloc[row,0])
                for i in range(1, len(data.columns)):
                    data.iloc[row,i] = st.text_input(data.columns[i],data.iloc[row,i])
                if st.button("Update"):
                    if len(data) == 0:
                        st.warning("Table is empty")
                    else:
                        update_data(table_name, row, data)
                        st.success("Updated Row {}".format(row))   
                        data = read_data(table_name)
                        st.header("Changed Table")
                        if len(data) == 0:
                            st.warning("Table is empty")
                        else:
                            st.write(data) 


    elif choice == "Delete":
        st.subheader("Delete Row")
        table_name = st.selectbox("Table Name",["users","caregiver","member",
                                                "address","job","job_application","appointment"])
        st.header("Initial Table")
        data = read_data(table_name)
        if data.empty:
            print("Table is empty")
            st.warning("Table is empty")
        else:
            st.write(data)
            row = st.text_input("Enter which row to delete")
            if row == '':
                st.warning("Please input a row number")
            elif not row.isnumeric() or int(row) > len(data) or int(row) < 0:
                st.warning("Please input a valid row number")
            else:
                row = int(row)
                if st.button("Delete"):
                    delete_data(table_name, row, data)
                    st.success("Deleted Row {}".format(row))    
                    data = read_data(table_name)
                    st.header("Changed Table")
                    if data.empty:
                        st.warning("Table is empty")
                    else:
                        st.write(data)

if __name__ == '__main__':
    main()