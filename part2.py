from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, MetaData
from sqlalchemy import func, asc
from collections import defaultdict

connection_string = 'postgresql://postgres:Nurlybekov123@localhost:5432/postgres'
engine = create_engine(connection_string)

Base = automap_base()
Base.prepare(engine, reflect=True)
User = Base.classes.users  # assuming 'users' is the table name in your database
Caregiver = Base.classes.caregiver
Job = Base.classes.job
Member = Base.classes.member
Address = Base.classes.address
Appointment = Base.classes.appointment
JobApplication = Base.classes.job_application

session = Session(engine)


# 3.1 Update the phone number of Askar Askarov to +77771010001.
askar = session.query(User).filter(User.given_name == 'Askar' and User.surname == 'Askarov').first()

if askar is not None:
    askar.phone_number = '+77771010001'
    session.commit()
else:
    print("User Askar Askarov not found")

# 3.2 Add $0.5 commission fee to the Caregivers’ hourly rate 
# if it's less than $9, or 10% if it's not.

# caregivers = session.query(Caregiver).all()

# for caregiver in caregivers:
#     if float(caregiver.hourly_rate) < 9:
#         caregiver.hourly_rate = float(caregiver.hourly_rate) + 0.5
#     else:
#         caregiver.hourly_rate = float(caregiver.hourly_rate) + float(caregiver.hourly_rate) * 0.1
#     session.commit()

# 4.1 Delete the jobs posted by Bolat Bolatov.

# user = session.query(User).filter(User.given_name == 'Bolat' and User.surname == 'Bolatov').first()

# if user is not None:
#     jobs = session.query(Job).filter(Job.member_user_id == user.user_id).all()
#     for job in jobs:
#         session.delete(job)
#     session.commit()
# else:
#     print("User Bolat Bolatov not found")



# 4.2 Delete all members who live on Turan street. 
# addresses = session.query(Address).filter(Address.street.like('%Turan%')).all()

# for address in addresses:
#     members_to_delete = session.query(Member).filter(Member.member_user_id == address.member_user_id).all()
#     for member in members_to_delete:
#         session.delete(member)

# session.commit()


# 5.1 Select caregiver and member names for the accepted appointments.

appointments = session.query(Appointment).filter(Appointment.status == 'Accepted').all()
for appointment in appointments:
    caregiver = session.query(Caregiver).filter(Caregiver.caregiver_user_id == appointment.caregiver_user_id).first()
    member = session.query(Member).filter(Member.member_user_id == appointment.member_user_id).first()
   
    user1 = session.query(User).filter(User.user_id == caregiver.caregiver_user_id).first()
    if member is not None:
        user2 = session.query(User).filter(User.user_id == member.member_user_id).first()
        print(f"Caregiver {user1.given_name} {user1.surname}")
        print(f"Member {user2.given_name} {user2.surname}")
        print("--------------------")
    else:
        print(f"No member found for appointment {appointment.appointment_id}")
    
# 5.2 List job ids that contain ‘gentle’ in their other requirements.

# jobs = session.query(Job).filter(Job.other_requirements.like('%gentle%')).all()
# for job in jobs:
#     print(job.job_id)

# 5.3 List the work hours of Baby Sitter positions


caregivers = session.query(Caregiver).filter(Caregiver.caregiving_type == 'Baby Sitter').all()
for caregiver in caregivers:
    print(f"{caregiver.caregiver_user_id} {caregiver.hourly_rate}")

# 6.1 Count the number of applicants for each job posted 
# by a member (multiple joins with aggregation)

# Query all jobs
jobs = session.query(Job).all()

for job in jobs:
    # Query all applications for each job
    applications = session.query(JobApplication).filter(JobApplication.job_id == job.job_id).all()
    print(f"Job {job.job_id} has {len(applications)} applicants")

print("--------------------------------------------------")
#6.2 Total hours spent by care givers for all accepted 
# appointments (multiple joins with aggregation)

# Query all appointments
appointments = session.query(Appointment).all()
total_hours = 0
for appointment in appointments:
    if appointment.status == 'Accepted':
        total_hours += appointment.work_hours

print(f"Total hours spent by care givers for all accepted appointments: {total_hours}")

print("--------------------------------------------------")

#6.3 Average pay of caregivers based on accepted appointments (join with aggregation)

avg_pay_query = session.query(
    func.avg(Caregiver.hourly_rate).label('average_pay')
).join(
    Appointment, Caregiver.caregiver_user_id == Appointment.caregiver_user_id
).filter(
    Appointment.status == 'Accepted'
)

# Execute the query
avg_pay = avg_pay_query.one()

# Output the result
print(f"The average pay of caregivers based on accepted appointments is: {avg_pay.average_pay}")

print("--------------------------------------------------")

# 6.4 Caregivers who earn above average based on accepted appointments (multiple join with
# aggregation and nested query)


subq = session.query(
    func.avg(Caregiver.hourly_rate).label('average_hourly_rate')
).join(
    Appointment, Caregiver.caregiver_user_id == Appointment.caregiver_user_id
).filter(
    Appointment.status == 'Accepted'
).subquery()


query = session.query(Caregiver).join(
    Appointment, Caregiver.caregiver_user_id == Appointment.caregiver_user_id
).filter(
    Appointment.status == 'Accepted',
    Caregiver.hourly_rate > subq.c.average_hourly_rate
)

# Execute the query and print results
above_average_caregivers = query.all()
for caregiver in above_average_caregivers:
    print(f"Caregiver ID: {caregiver.caregiver_user_id}, Hourly Rate: {caregiver.hourly_rate}")


print("--------------------------------------------------")


#7 Calculate the total cost to pay for a caregiver for all accepted appointments.
total_cost_query = session.query(
    Caregiver.caregiver_user_id, 
    func.sum(Caregiver.hourly_rate * Appointment.work_hours).label('total_cost')
).join(
    Appointment, Caregiver.caregiver_user_id == Appointment.caregiver_user_id
).filter(
    Appointment.status == 'Accepted'
).group_by(
    Caregiver.caregiver_user_id
)

# Execute the query and print results
total_costs = total_cost_query.all()
for caregiver_id, total_cost in total_costs:
    print(f"Caregiver ID: {caregiver_id}, Total cost: {total_cost}")

print("--------------------------------------------------")

# 8 View all job applications and the applicants
applications = session.query(JobApplication).order_by(asc(JobApplication.job_id)).all()

# Group applications by job_id
grouped_applications = defaultdict(list)
for application in applications:
    grouped_applications[application.job_id].append(application)

# For each job, print the job id and the applicants
for job_id, applications in grouped_applications.items():
    print(f"Job ID: {job_id}")
    for application in applications:
        user = session.query(User).filter(User.user_id == application.caregiver_user_id).first()
        print(f"Applicant: {user.given_name} {user.surname}")
    print("--------------------------------------------------")

