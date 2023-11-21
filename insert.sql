INSERT INTO USERS (user_id, email, given_name, surname, city, phone_number, profile_description, password) VALUES 
(1, 'joji.pinkguy@nu.edu.kz', 'Joji', 'Pinkguy', 'Astana', '+77027308866', 'Student at Nazarbayev University', 'Hello123'),
(2, 'askar.askarov@gmail.com', 'Askar', 'Askarov', 'Almaty', '+77011377737', 'Software Engineer. Experienced in web development.', 'Pass123!'),
(3, 'alikhan.zhanseitov@yahoo.com', 'Alikhan', 'Zhanseitov', 'Aktau', '+77471234567', 'Business Analyst. Skilled in market research.', 'Secure456'),
(4, 'bakytzhan.tulegenov@hotmail.com', 'Bakytzhan', 'Tulegenov', 'Shymkent', '+77071234567', 'Marketing Specialist. Proficient in SEO and social media marketing.', 'P@ssw0rd'),
(5, 'dana.kazhgaliyeva@gmail.com', 'Dana', 'Kazhgaliyeva', 'Karaganda', '+77771234567', 'Graphic Designer. Expertise in Adobe Creative Suite.', 'DesignPass1'),
(6, 'dauren.zhumagulov@yahoo.com', 'Dauren', 'Zhumagulov', 'Pavlodar', '+77471234567', 'Finance professional. Skilled in financial modeling.', 'MoneyM@tters'),
(7, 'gulzhan.abdullayeva@gmail.com', 'Gulzhan', 'Abdullayeva', 'Taraz', '+77071234567', 'Human Resources Specialist. Experience in talent acquisition.', 'PeopleFirst!'),
(8, 'kuanysh.serikbayev@yahoo.com', 'Kuanysh', 'Serikbayev', 'Semey', '+77771234567', 'Project Manager. Proficient in agile methodologies.', 'ProjectPass123'),
(9, 'nurbolat.zhusupov@hotmail.com', 'Nurbolat', 'Zhusupov', 'Kostanay', '+77471234567', 'Sales Executive. Skilled in negotiation.', 'SalesSuccess1'),
(10, 'yerzhan.temirbekov@gmail.com', 'Yerzhan', 'Temirbekov', 'Uralsk', '+77071234567', 'Data Scientist. Proficient in Python.', 'DataGeek123!');
(11, 'aibek.nurzhanov@mail.com', 'Aibek', 'Nurzhanov', 'Aktau', '+77021234567', 'Entrepreneur in tech industry', 'TechBoss2023'),
(12, 'zhansaya.mukhitdinova@gmail.com', 'Zhansaya', 'Mukhitdinova', 'Kyzylorda', '+77022345678', 'Expert in renewable energy technologies', 'GreenTech2023'),
(13, 'nursultan.zhumagali@yahoo.com', 'Nursultan', 'Zhumagali', 'Taraz', '+77023456789', 'Architect specializing in urban planning', 'UrbanDesign2023'),
(14, 'irina.kairatovna@hotmail.com', 'Irina', 'Kairatovna', 'Pavlodar', '+77024567890', 'Educator and historian', 'HistoryBuff2023'),
(15, 'kanye.west@example.com', 'Kanye', 'West', 'Almaty', '+77025678901', 'Music producer and fashion icon', 'MusicFashion2023'),
(16, 'lionel.messi@football.com', 'Lionel', 'Messi', 'Nur-Sultan', '+77026789012', 'Professional football player', 'FootballStar2023'),
(17, 'bexultan.tokan@business.com', 'Bexultan', 'Tokan', 'Shymkent', '+77027890123', 'Business consultant with focus on startups', 'StartupGuru2023'),
(18, 'dina.satybalova@mail.com', 'Dina', 'Satybalova', 'Aktobe', '+77028901234', 'Civil engineer with a focus on infrastructure', 'BuildFuture2023'),
(19, 'erbolat.dosymbekov@gmail.com', 'Erbolat', 'Dosymbekov', 'Semey', '+77029012345', 'Graphic designer and visual artist', 'DesignArt2023'),
(20, 'gulmira.eskendirova@yahoo.com', 'Gulmira', 'Eskendirova', 'Kokshetau', '+77020123456', 'Molecular biologist researching genetics', 'GeneExplorer2023'),
(21, 'zhanbolat.murzalin@hotmail.com', 'Zhanbolat', 'Murzalin', 'Atyrau', '+77021234567', 'Financial analyst with expertise in market trends', 'MarketAnalyst2023'),
(22, 'bolatov@nu.edu.kz', 'Bolat', 'Bolatov', 'Astana', '+77027308861', 'Student at Nazarbayev University', 'HelloKae');

INSERT INTO CAREGIVER (caregiver_user_id, photo, gender, caregiving_type, hourly_rate) VALUES
(2, 'photo_url_2', 'Male', 'Elderly Care', 8.50),
(3, 'photo_url_3', 'Male', 'Baby Sitter', 9.75),
(6, 'photo_url_6', 'Male', 'Special Needs Care', 12.25),
(9, 'photo_url_9', 'Female', 'Senior Care', 10.50),
(11, 'photo_url_11', 'Female', 'Senior Care', 12.75),
(12, 'photo_url_12', 'Male', 'Senior Care', 12.75),
(13, 'photo_url_13', 'Female', 'Baby Sitter', 4.15),
(14, 'photo_url_14', 'Male', 'Special Needs Care', 15.0),
(15, 'photo_url_15', 'Female', 'Elderly Care', 20.75);


INSERT INTO MEMBER (member_user_id, house_rules) VALUES
(1, 'No smoking'),
(4, 'No pets'),
(5, 'Have a car'),
(10, 'Cooking'),
(16, 'Cleaning'),
(17, 'No smoking'),
(18, 'Pets allowed'),
(19, 'Have a car'),
(20, 'Cooking'),
(21, 'Cleaning');

INSERT INTO ADDRESS (member_user_id, house_number, street, town) VALUES
(1, '55', 'Turan', 'Astana'),
(4, '12', 'Tole Bi', 'Shymkent'),
(5, '24', 'Kabanbay', 'Astana'),
(10, '1', 'Satpayev', 'Atyrau'),
(16, '101', 'Abay Avenue', 'Almaty'),
(17, '202', 'Saryarka', 'Nur-Sultan'),
(18, '303', 'Baytursynov Street', 'Kostanay'),
(19, '404', 'Dostyk', 'Pavlodar'),
(20, '505', 'Gogol Street', 'Karaganda'),
(21, '606', 'Zhibek Zholy', 'Taraz');

INSERT INTO JOB (job_id, member_user_id, required_caregiving_type, other_requirements, date_posted) VALUES
(1, 1, 'Baby Sitter', 'I need gentle care of my dog', '2023-01-01'),
(2, 4, 'Elderly Care', 'Required gentle care', '2023-02-15'),
(3, 5, 'Pet Care', 'Experienced with dogs', '2023-03-20'),
(4, 10, 'Cooking', 'Professional chef preferred', '2023-04-01'),
(5, 16, 'House Cleaning', 'Experienced and reliable', '2023-04-15'),
(6, 17, 'Personal Assistant', 'Non-smoker essential', '2023-05-01'),
(7, 18, 'Pet Care', 'Comfortable with multiple pets', '2023-05-15'),
(8, 19, 'Driver', 'Valid driver’s license and own car required', '2023-06-01'),
(9, 20, 'Cooking', 'Specializes in local cuisine', '2023-06-15'),
(10, 21, 'House Cleaning', 'Attention to detail and efficiency required', '2023-07-01');


INSERT INTO JOB_APPLICATION (caregiver_user_id, job_id, date_applied) VALUES
(2, 4, '2023-04-02'),
(3, 5, '2023-04-16'),
(6, 6, '2023-05-02'),
(9, 7, '2023-05-16'),
(11, 8, '2023-06-02'),
(12, 9, '2023-06-16'),
(13, 10, '2023-07-02'),
(14, 4, '2023-04-03'),
(15, 5, '2023-04-17');

INSERT INTO APPOINTMENT (appointment_id, caregiver_user_id, member_user_id, appointment_date, appointment_time, work_hours, status) VALUES
(1, 2, 1, '2023-08-01', '09:00', 4, 'Accepted'),
(2, 3, 5, '2023-08-02', '10:00', 3, 'Accepted'),
(3, 6, 10, '2023-08-03', '11:00', 5, 'Accepted');
