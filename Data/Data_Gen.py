from datetime import datetime, time
import json
from typing import List, Dict
import random
from enum import Enum

class LecturerRole(Enum):
    PROFESSOR = "professor"
    ASSISTANT_PROFESSOR = "assistant professor"
    SENIOR_LECTURER = "senior lecturer"
    LECTURER = "lecturer"
    INSTRUCTOR = "instructor"

def generate_faculty_data() -> List[Dict]:
    return [{
        "name": "Computing",
        "code": "FCSC",
        # "departments": [
        #     "Computer Science and Software Engineering",
        #     "Information Technology",
        #     "Cyber Security",
        #     "Interactive Media",
        #     "Information Systems Engineering",
        #     "Data Science"
        # ]
        "departments": "Information Technology"
    }]

def generate_modules() -> List[Dict]:
    return [
        # Year 1 Semester 1 Modules
        {
            "code": "IT1010",  # First 1: Year 1, Second 0: Semester 1
            "name": "Introduction to Computing",
            "long_name": "Introduction to Computing",
            "description": "Basic computing concepts"
        },
        {
            "code": "IT1020",
            "name": "IP",
            "long_name": "Introduction to Programming",
            "description": "Programming fundamentals"
        },
        {
            "code": "IT1030",
            "name": "MC",
            "long_name": "Mathematics for Computing",
            "description": "Mathematical concepts"
        },
        {
            "code": "IT1040",
            "name": "DBMS",
            "long_name": "Database Management Systems",
            "description": "Database fundamentals"
        },

        # Year 1 Semester 2 Modules
        {
            "code": "IT1550",  # First 1: Year 1, Second 5: Semester 2
            "name": "OOP",
            "long_name": "Object Oriented Programming",
            "description": "OOP concepts"
        },
        {
            "code": "IT1560",
            "name": "Web Development",
            "long_name": "Web Development",
            "description": "Web development basics"
        },
        {
            "code": "IT1570",
            "name": "Statistics",
            "long_name": "Statistics for IT",
            "description": "Statistical methods"
        },
        {
            "code": "IT1580",
            "name": "DSA",
            "long_name": "Data Structures and Algorithms",
            "description": "Data structures basics"
        },

        # Year 2 Semester 1 Modules
        {
            "code": "IT2010",  # First 2: Year 2, Second 0: Semester 1
            "name": "Advanced Programming",
            "long_name": "Advanced Programming",
            "description": "Advanced programming concepts"
        },
        {
            "code": "IT2020",
            "name": "DBMS II",
            "long_name": "Advanced Database Systems",
            "description": "Advanced database concepts"
        },
        {
            "code": "IT2030",
            "name": "Software Engineering",
            "long_name": "Software Engineering",
            "description": "Software engineering principles"
        },
        {
            "code": "IT2040",
            "name": "Networking",
            "long_name": "Computer Networks II",
            "description": "Advanced networking concepts"
        },

        # Year 2 Semester 2 Modules
        {
            "code": "IT2550",  # First 2: Year 2, Second 5: Semester 2
            "name": "Mobile Development",
            "long_name": "Mobile Application Development",
            "description": "Mobile app development"
        },
        {
            "code": "IT2560",
            "name": "Web Programming",
            "long_name": "Advanced Web Programming",
            "description": "Advanced web development"
        },
        {
            "code": "IT2570",
            "name": "OS",
            "long_name": "Operating Systems",
            "description": "Operating systems concepts"
        },
        {
            "code": "IT2580",
            "name": "Security",
            "long_name": "Information Security",
            "description": "Information security basics"
        },

        # Year 3 Semester 1 Modules
        {
            "code": "IT3010",  # First 3: Year 3, Second 0: Semester 1
            "name": "Project Management",
            "long_name": "Software Project Management",
            "description": "Project management principles"
        },
        {
            "code": "IT3020",
            "name": "DS",
            "long_name": "Data Science",
            "description": "Introduction to data science"
        },
        {
            "code": "IT3030",
            "name": "AI",
            "long_name": "Artificial Intelligence",
            "description": "AI fundamentals"
        },
        {
            "code": "IT3040",
            "name": "Cloud Computing",
            "long_name": "Cloud Computing",
            "description": "Cloud computing concepts"
        },

        # Year 3 Semester 2 Modules
        {
            "code": "IT3550",  # First 3: Year 3, Second 5: Semester 2
            "name": "ML",
            "long_name": "Machine Learning",
            "description": "Machine learning fundamentals"
        },
        {
            "code": "IT3560",
            "name": "Research Methods",
            "long_name": "Research Methods",
            "description": "Research methodology"
        },
        {
            "code": "IT3570",
            "name": "DevOps",
            "long_name": "DevOps Practices",
            "description": "DevOps principles"
        },
        {
            "code": "IT3580",
            "name": "QA",
            "long_name": "Quality Assurance",
            "description": "Software quality assurance"
        },

        # Year 4 Semester 1 Modules
        {
            "code": "IT4010",  # First 4: Year 4, Second 0: Semester 1
            "name": "Research Project",
            "long_name": "Research Project I",
            "description": "Final year research project"
        },
        {
            "code": "IT4020",
            "name": "Enterprise Architecture",
            "long_name": "Enterprise Architecture",
            "description": "Enterprise systems design"
        },
        {
            "code": "IT4030",
            "name": "Business Analytics",
            "long_name": "Business Analytics",
            "description": "Business analytics and intelligence"
        },

        # Year 4 Semester 2 Modules
        {
            "code": "IT4550",  # First 4: Year 4, Second 5: Semester 2
            "name": "Research Project II",
            "long_name": "Research Project II",
            "description": "Final year research project continuation"
        },
        {
            "code": "IT4560",
            "name": "Emerging Technologies",
            "long_name": "Emerging Technologies",
            "description": "Latest technology trends"
        },
        {
            "code": "IT4570",
            "name": "Professional Practice",
            "long_name": "Professional Practice",
            "description": "Professional development"
        }
    ]

def generate_spaces() -> List[Dict]:
    spaces = [
        # PC Labs (LAB prefix)
        {
            "name": "A405",
            "long_name": "PC Lab A405",
            "code": "LAB405",
            "capacity": 60,
            "attributes": {
                "projector": "Yes",
                "computers": "Yes",
                "air_conditioned": "Yes"
            }
        },
        {
            "name": "A412",
            "long_name": "PC Lab A412",
            "code": "LAB412",
            "capacity": 60,
            "attributes": {
                "projector": "Yes",
                "computers": "Yes",
                "air_conditioned": "Yes"
            }
        },
        {
            "name": "B401",
            "long_name": "PC Lab B401",
            "code": "LAB401",
            "capacity": 60,
            "attributes": {
                "projector": "Yes",
                "computers": "Yes",
                "air_conditioned": "Yes"
            }
        },
        {
            "name": "B402",
            "long_name": "PC Lab B402",
            "code": "LAB402",
            "capacity": 60,
            "attributes": {
                "projector": "Yes",
                "computers": "Yes",
                "air_conditioned": "Yes"
            }
        },
        {
            "name": "B403",
            "long_name": "PC Lab B403",
            "code": "LAB403",
            "capacity": 60,
            "attributes": {
                "projector": "Yes",
                "computers": "Yes",
                "air_conditioned": "Yes"
            }
        },
        # Lecture Halls (LH prefix)
        {
            "name": "A410+A411",
            "long_name": "Lecture Hall A410+A411",
            "code": "LH410",
            "capacity": 120,
            "attributes": {
                "projector": "Yes",
                "computers": "No",
                "air_conditioned": "Yes"
            }
        },
        {
            "name": "G1101",
            "long_name": "Lecture Hall G1101",
            "code": "LH1101",
            "capacity": 100,
            "attributes": {
                "projector": "Yes",
                "computers": "No",
                "air_conditioned": "Yes"
            }
        },
        {
            "name": "G1102",
            "long_name": "Lecture Hall G1102",
            "code": "LH1102",
            "capacity": 100,
            "attributes": {
                "projector": "Yes",
                "computers": "No",
                "air_conditioned": "Yes"
            }
        },
        {
            "name": "G1103",
            "long_name": "Lecture Hall G1103",
            "code": "LH1103",
            "capacity": 100,
            "attributes": {
                "projector": "Yes",
                "computers": "No",
                "air_conditioned": "Yes"
            }
        },
        {
            "name": "G1104",
            "long_name": "Lecture Hall G1104",
            "code": "LH1104",
            "capacity": 100,
            "attributes": {
                "projector": "Yes",
                "computers": "No",
                "air_conditioned": "Yes"
            }
        },
        {
            "name": "G1105",
            "long_name": "Lecture Hall G1105",
            "code": "LH1105",
            "capacity": 100,
            "attributes": {
                "projector": "Yes",
                "computers": "No",
                "air_conditioned": "Yes"
            }
        },
        {
            "name": "G1106",
            "long_name": "Lecture Hall G1106",
            "code": "LH1106",
            "capacity": 100,
            "attributes": {
                "projector": "Yes",
                "computers": "No",
                "air_conditioned": "Yes"
            }
        },
        {
            "name": "G1301",
            "long_name": "Lecture Hall G1301",
            "code": "LH1301",
            "capacity": 100,
            "attributes": {
                "projector": "Yes",
                "computers": "No",
                "air_conditioned": "Yes"
            }
        },
        {
            "name": "G1302",
            "long_name": "Lecture Hall G1302",
            "code": "LH1302",
            "capacity": 100,
            "attributes": {
                "projector": "Yes",
                "computers": "No",
                "air_conditioned": "Yes"
            }
        },
        {
            "name": "G1303",
            "long_name": "Lecture Hall G1303",
            "code": "LH1303",
            "capacity": 100,
            "attributes": {
                "projector": "Yes",
                "computers": "No",
                "air_conditioned": "Yes"
            }
        },
        {
            "name": "G1304",
            "long_name": "Lecture Hall G1304",
            "code": "LH1304",
            "capacity": 100,
            "attributes": {
                "projector": "Yes",
                "computers": "No",
                "air_conditioned": "Yes"
            }
        },
        {
            "name": "G1305",
            "long_name": "Lecture Hall G1305",
            "code": "LH1305",
            "capacity": 100,
            "attributes": {
                "projector": "Yes",
                "computers": "No",
                "air_conditioned": "Yes"
            }
        },
        {
            "name": "G604",
            "long_name": "Lecture Hall G604",
            "code": "LH604",
            "capacity": 100,
            "attributes": {
                "projector": "Yes",
                "computers": "No",
                "air_conditioned": "Yes"
            }
        },
        {
            "name": "G605",
            "long_name": "Lecture Hall G605",
            "code": "LH605",
            "capacity": 100,
            "attributes": {
                "projector": "Yes",
                "computers": "No",
                "air_conditioned": "Yes"
            }
        },
        {
            "name": "G606",
            "long_name": "Lecture Hall G606",
            "code": "LH606",
            "capacity": 100,
            "attributes": {
                "projector": "Yes",
                "computers": "No",
                "air_conditioned": "Yes"
            }
        }
    ]
    return spaces

def generate_years() -> List[Dict]:
    years = []
    for year in range(1, 5):  # 4 years
        for semester in range(1, 3):  # 2 semesters per year
            for group_num in range(1, 6):  # 5 groups per semester
                years.append({
                    "id": f"Y{year}S{semester}.{group_num}",
                    "year": year,
                    "semester": semester,
                    "group_num": group_num,
                    "size": 40
                })
    return years

def generate_users() -> List[Dict]:
    faculty = []
    students = []
    
    # Predefined faculty members
    lecturer_data = [
        ("Nuwan", "Kodagoda", LecturerRole.PROFESSOR.value),
        ("Pradeep", "Abeygunawardhana", LecturerRole.PROFESSOR.value),
        ("Kalpani", "Manathunga", LecturerRole.SENIOR_LECTURER.value),
        ("Samantha", "Rajapaksha", LecturerRole.SENIOR_LECTURER.value),
        ("Anuradha", "Jayakody", LecturerRole.SENIOR_LECTURER.value),
        ("Jeewanee", "Bamunusinghe", LecturerRole.SENIOR_LECTURER.value),
        ("Prasanna", "Haddela", LecturerRole.SENIOR_LECTURER.value),
        ("Dasuni", "Nawinna", LecturerRole.ASSISTANT_PROFESSOR.value),
        ("Anuradha", "Karunasena", LecturerRole.ASSISTANT_PROFESSOR.value),
        ("Koliya", "Pulasinghe", LecturerRole.PROFESSOR.value),
        ("Chandimal", "Jayawardena", LecturerRole.PROFESSOR.value),
        ("Mahesha", "Kapurubandara", LecturerRole.PROFESSOR.value),
        ("Pradeepa", "Samarasinghe", LecturerRole.ASSISTANT_PROFESSOR.value),
        ("Dharshana", "Kasthurirathna", LecturerRole.ASSISTANT_PROFESSOR.value),
        ("Jayantha", "Amararachchi", LecturerRole.ASSISTANT_PROFESSOR.value),
        ("Harinda", "Fernando", LecturerRole.ASSISTANT_PROFESSOR.value),
        ("Dilshan", "De Silva", LecturerRole.ASSISTANT_PROFESSOR.value),
        ("Sanika", "Wijayasekara", LecturerRole.ASSISTANT_PROFESSOR.value),
        ("Nathali", "Silva", LecturerRole.ASSISTANT_PROFESSOR.value),
        ("Sanvitha", "Kasthuriarachchi", LecturerRole.ASSISTANT_PROFESSOR.value),
        ("Janangi", "Senarathna", LecturerRole.INSTRUCTOR.value),
        ("Anjana", "Abeykoon", LecturerRole.INSTRUCTOR.value),
        ("Supipi", "Karunathilaka", LecturerRole.INSTRUCTOR.value),
        ("Rivoni", "De Zoysa", LecturerRole.INSTRUCTOR.value),
        ("Ravindu", "Nethsara", LecturerRole.INSTRUCTOR.value)
    ]
    
    # Add predefined faculty members
    for i, (first, last, role) in enumerate(lecturer_data, 1):
        faculty.append({
            "id": f"FA{i:07d}",
            "first_name": first,
            "last_name": last,
            "username": f"{first.lower()}.{last.lower()}",
            "role": role,
            # "department": random.choice([
            #     "Computer Science and Software Engineering",
            #     "Information Technology",
            #     "Cyber Security",
            #     "Interactive Media",
            #     "Information Systems Engineering",
            #     "Data Science"
            # ])
            "department": "Information Technology"
        })
    
    # Common Sri Lankan names for random generation
    first_names = [
        "Kasun", "Chamara", "Dimuthu", "Sachini", "Malini", "Ishara", 
        "Thilini", "Sanduni", "Hasini", "Kavindi", "Chamika", "Lakshan",
        "Thisara", "Dulani", "Nimali", "Chathura", "Sachitha", "Buddhika",
        "Ishanka", "Thilina", "Dinesh", "Amali", "Nadeeka", "Kumara",
        "Lasith", "Chathurika", "Dilshan", "Madhavi", "Priyanka", "Udaya"
    ]
    
    last_names = [
        "Perera", "Silva", "Fernando", "Dissanayake", "Bandara", "Rajapaksa",
        "Wickramasinghe", "Gunawardena", "Jayasinghe", "Ranasinghe", "Fonseka",
        "Karunaratne", "Mendis", "Weerasinghe", "Amarasinghe", "Nanayakkara",
        "Samarasinghe", "Wijesinghe", "Ratnayake", "Liyanage", "Pathirana",
        "Seneviratne", "Herath", "Alwis", "Gunasekara", "Dharmawardena",
        "Kumarasinghe", "Withana", "Ekanayake", "Jayawardena"
    ]
    
    # Generate additional faculty members to reach 200 total with minimum 20 per role
    current_count = len(faculty)
    role_counts = {role.value: 0 for role in LecturerRole}
    
    # Count existing roles
    for f in faculty:
        role_counts[f["role"]] += 1
    
    # Generate remaining faculty members
    while current_count < 200:
        # Find roles that need more members
        needed_roles = [role.value for role in LecturerRole if role_counts[role.value] < 20]
        
        if not needed_roles:
            # If all roles have minimum 20, randomly choose any role
            role = random.choice([role.value for role in LecturerRole])
        else:
            # Choose from roles that need more members
            role = random.choice(needed_roles)
        
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        
        faculty.append({
            "id": f"FA{current_count + 1:07d}",
            "first_name": first_name,
            "last_name": last_name,
            "username": f"{first_name.lower()}.{last_name.lower()}",
            "role": role,
            "department": "Information Technology"
        })
        
        role_counts[role] += 1
        current_count += 1
    
    # Generate students
    years = generate_years()
    for year in years:
        students.append({
            "id": f"IT{random.randint(100000, 999999)}",
            "first_name": f"Student{random.randint(1, 300)}",
            "last_name": f"Learner{random.randint(1, 300)}",
            "username": f"it{random.randint(100000, 999999)}",
            "role": "student",
            "year_group": year["id"]
        })
    
    return faculty + students

def generate_activities() -> List[Dict]:
    activities = []
    activity_counter = 1
    
    print("\nGenerating activities:")
    # Generate activities for each module
    modules = generate_modules()
    for module in modules:
        year = int(module['code'][2])  # Extract year from module code (IT1xxx -> year 1)
        semester = 2 if int(module['code'][3]) >= 5 else 1  # Semester 1: 0-4, Semester 2: 5-9
        print(f"\nProcessing module: {module['code']} ({module['name']})")
        print(f"Year: {year}, Semester: {semester}")
        
        # Generate subgroup IDs for this year and semester
        subgroup_ids = [f"Y{year}S{semester}.{i}" for i in range(1, 6)]
        print(f"Groups: {', '.join(subgroup_ids)}")
        
        # Lecture (2 hours)
        activities.append({
            "code": f"AC-{activity_counter:03d}",
            "name": f"{module['name']} Lecture",
            "subject": module['code'],
            "teacher_ids": [f"FA{random.randint(1, 10):07d}"],
            "subgroup_ids": subgroup_ids,  # All groups for this year/semester
            "duration": 2,
            "type": "Lecture",
            "space_requirements": ["Lecture Hall"]
        })
        print(f"Created lecture activity for groups: {', '.join(subgroup_ids)}")
        activity_counter += 1
        
        # Tutorial groups (1 hour each)
        for group_num in range(1, 6):
            subgroup_id = f"Y{year}S{semester}.{group_num}"
            activities.append({
                "code": f"AC-{activity_counter:03d}",
                "name": f"{module['name']} Tutorial - Group {group_num}",
                "subject": module['code'],
                "teacher_ids": [f"FA{random.randint(1, 10):07d}"],
                "subgroup_ids": [subgroup_id],
                "duration": 1,
                "type": "Tutorial",
                "space_requirements": ["Tutorial Room", "Lecture Hall"]
            })
            print(f"Created tutorial activity for group: {subgroup_id}")
            activity_counter += 1
        
        # Practical sessions (2 hours each) for programming/technical modules
        if any(keyword in module['name'].lower() for keyword in ['programming', 'database', 'networks', 'web']):
            for group_num in range(1, 6):
                subgroup_id = f"Y{year}S{semester}.{group_num}"
                activities.append({
                    "code": f"AC-{activity_counter:03d}",
                    "name": f"{module['name']} Practical - Group {group_num}",
                    "subject": module['code'],
                    "teacher_ids": [f"FA{random.randint(1, 10):07d}"],
                    "subgroup_ids": [subgroup_id],
                    "duration": 2,
                    "type": "Practical",
                    "space_requirements": ["Computer Lab"]
                })
                print(f"Created practical activity for group: {subgroup_id}")
                activity_counter += 1
    
    print(f"\nTotal activities generated: {activity_counter - 1}")
    return activities

def generate_constraints() -> List[Dict]:
    return [
        {
            "name": "No Teacher Overlap",
            "description": "A teacher cannot be scheduled for multiple activities at the same time",
            "type": "hard",
            "weight": 10
        },
        {
            "name": "No Student Group Overlap",
            "description": "A student group cannot be scheduled for multiple activities at the same time",
            "type": "hard",
            "weight": 10
        },
        {
            "name": "No Room Overlap",
            "description": "A room cannot be scheduled for multiple activities at the same time",
            "type": "hard",
            "weight": 10
        },
        {
            "name": "Room Type Match",
            "description": "Activities must be scheduled in rooms that match their requirements",
            "type": "hard",
            "weight": 10
        },
        {
            "name": "Room Capacity",
            "description": "Room capacity must be sufficient for the student group size",
            "type": "hard",
            "weight": 10
        }
    ]

def generate_complete_dataset():
    dataset = {
        "faculties": generate_faculty_data(),
        "modules": generate_modules(),
        "spaces": generate_spaces(),
        "years": generate_years(),
        "users": generate_users(),
        "activities": generate_activities(),
        "constraints": generate_constraints()
    }
    return dataset

def save_dataset(dataset, filename="sliit_computing_dataset.json"):
    with open(filename, 'w') as f:
        json.dump(dataset, f, indent=2)

if __name__ == "__main__":
    dataset = generate_complete_dataset()
    save_dataset(dataset)
    print("SLIIT Computing dataset generated successfully!")