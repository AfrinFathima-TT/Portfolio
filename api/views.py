from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse


# Create your views here.
class About_View(View):
    def get(self,request):
        data = {
            "ID"                 : 201,
            "Name"               : "Zaya",
            "Professional Title" : "Python Developer",
            "Bio"                : "I am paasionate about backend developing ",
            "Email"              : "Zaya@gmail.com",
            "Contact Number"     : 7043567432,
            "Dob"                : "22/08/2004",
            "GitHub Link"        : "https://github.com/zaya",
            "LinkedIn Link"      : "https://linkedin.com/in/zaya"

        }
        return JsonResponse(data)
class Education_View(View):
    def get(self,request):
        data = {
            "ID"                 : 201,
            "Institution"        : "GEC Kannur",
            "Degree"             : "B.Tech",
            "University"         : "KTU University",
            "Location"           :"Kannur",
            "Start Year"         :2022,
            "End Year"           :2026,
            "CGPA"               :9.6,
            "Description"        :"Iam completed my b.tech in CSE in the year 2026"
        }
        return JsonResponse(data)
class Project_view(View):
    def get(self,request):
        data = [
            {
                "ID"       :1,
                "Title"    :" Personal Expense Tracker",
                "Short Description" : "A simple application for tracking and managing daily expenses.",
                "Long Description"  : " A personal finance application that allows users to record income and expenses, categorize transactions, and monitor their spending. It provides a clear overview of financial activities and helps users manage their monthly budget.",
                "Technologies Used" : ["Python", "Django", "MySQL", "HTML", "CSS", "JavaScript"],
                "Live_url"     :"https://personal-expense-tracker.example.com",
                "Github_url"    :"https://github.com/zaya/personal-expense-tracker",
                "image_url"   :"https://api.yourdomain.com/media/projects/personal_expense_tracker.png",
                "Featured"  :"True"

            },
            {
                "ID"     :2,
                "Title"    :" Fake & Real Image Detection",
                "Short Description" : "An AI-based system that detects whether an image is real or AI-generated.",
                "Long Description"  : " A deep learning project that analyzes images and classifies them as real or fake.",
                "Technologies Used" : ["Python", "PyTorch", "EfficientNet", "OpenCV", "NumPy"],
                "Live_url"     :"https://Fake-Real-Image-Detection.example.com",
                "Github_url"    :"https://github.com/zaya/Fake-real-image-detection",
                "image_url"   :"https://api.yourdomain.com/media/projects/fake_real_image_detection.png",
                "Featured"  :"True"
            },
            {
                "ID"     :3,
                "Title"    :"Weather Application",
                "Short Description" : " A web application that displays current weather information for different locations.",
                "Long Description"  : " A responsive weather application that allows users to search for a city and view information such as temperature, humidity, wind speed, and weather conditions.",
                "Technologies Used" : ["HTML", "CSS", "JavaScript", "REST API"],
                "Live_url"     :"https://weather-application.example.com",
                "Github_url"    :"https://github.com/zaya/weather-application",
                "image_url"   :"https://api.yourdomain.com/media/projects/weather_application.png",
                "Featured"  :"True"
            }

        ]
        return JsonResponse(data,safe=False)
class Skills_View(View):
    def get(self,request):
        data = [
            {
                "ID" : 1,
                "Skill_Name" :"Python",
                "Category"  :"Programming Language",
                "Proficency_Lavel" : "Advanced",
                "Years_of_experience" : 4
            },
            {
                "ID" : 2,
                "Skill_Name" :"Django",
                "Category"  :"Backend",
                "Proficency_Lavel" : "Intermediate",
                "Years_of_experience" : 3
            },
            {
                "ID" : 3,
                "Skill_Name" :"React",
                "Category"  :"Frontend",
                "Proficency_Lavel" : "Advanced",
                "Years_of_experience" : 4
            }
        ]
        return JsonResponse(data,safe=False)

class Experience_View(View):
    def get(self,request):
        data =[
            {
                "ID" : 1,
                "Job_title" : "Software Engineer",
                "Company" :"ABC Tech solutions",
                "Loction" : "Cochin,Kerala",
                "Start_Date" : "2020/06/22",
                "End_Date" : "2022/02/18",
                "Currently_Working" :"False",
                "Description" :"Worked on developing and maintaining web applications."
            },
            {
                "ID" : 2,
                "Job_title" : "Backend Developer",
                "Company" :"Infosys",
                "Loction" : "Calicut,Kerala",
                "Start_Date" : "2022/02/28",
                "End_Date" : "2024/10/02",
                "Currently_Working" :"False",
                "Description" :"Worked on developing and maintaining backend of applications."
            },
            {
                "ID" : 3,
                "Job_title" : "Frontend Developer",
                "Company" :"TCS",
                "Loction" : "Trivandrum,Kerala",
                "Start_Date" : "2024/10/16",
                "End_Date" : "null",
                "Currently_Working" :"True",
                "Description" :"Worked on developing and maintaining frontend of applications."
            }
        ]
        return JsonResponse(data,safe=False)
class Certification_view(View):
    def get(self,request):
        data = [
            {
                "ID" : 1,
                "Certification_Name"  : "Python Programming",
                "Organization_Name" : "Coursera",
                "Issued_year":2024
            },
            {
                "ID" : 2,
                "Certification_Name"  : "Introduction to Artificial Intelligence",
                "Organization_Name" : "Abc Technologies",
                "Issued_year":2023
            },
            {
                "ID" : 3,
                "Certification_Name"  : "Full Stack Web Development",
                "Organization_Name" : "NPTEL",
                "Issued_year":2025
            }
        ]
        return JsonResponse(data,safe=False)
class Service_View(View):
    def get(self,request):
        data = [
            {
                "ID" : 1,
                "Service_Name" : "Web Development",
                "Description" : " Building responsive and user-friendly websites and web applications based on client requirements.",
                "Technologies_Used" : ["HTML", "CSS", "JavaScript", "Django", "React"]
            },
            {
                "ID" : 2,
                "Service_Name" : "Backend Development",
                "Description" : " Designing and implementing server-side logic, APIs, and database management for web applications.",
                "Technologies_Used" : ["Python", "Django", "Flask", "Node.js", "MySQL", "PostgreSQL"]
            },
            {
                "ID" : 3,
                "Service_Name" : "Data Analysis",
                "Description" : " Analyzing and interpreting complex data sets to provide actionable insights and support decision-making.",
                "Technologies_Used" : ["Python", "Pandas", "NumPy", "Matplotlib", "Seaborn"]
            }
        ]
        return JsonResponse(data,safe=False)