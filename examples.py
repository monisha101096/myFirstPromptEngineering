"""
Example Usage and Sample Data
==============================

This file provides examples of how to use the resume generator
with different user profiles.
"""

# Example 1: Software Engineer with Experience
software_engineer_data = {
    "name": "Alex Johnson",
    "mobile": "+1-555-0123",
    "email": "alex.johnson@email.com",
    "location": "Seattle, WA",
    "years_experience": 5,
    "current_role": "Senior Software Engineer",
    "skills": [
        "Problem Solving",
        "System Design",
        "Team Leadership",
        "Agile/Scrum",
        "Code Review"
    ],
    "tech_stack": [
        "Python",
        "Java",
        "JavaScript",
        "React",
        "Node.js",
        "PostgreSQL",
        "MongoDB",
        "Docker",
        "Kubernetes",
        "AWS",
        "Git"
    ],
    "summary": "Experienced software engineer with 5 years of expertise in building scalable web applications and microservices. Proven track record of leading development teams and delivering high-impact projects. Strong focus on code quality, performance optimization, and best practices.",
    "qualifications": [
        {
            "degree": "UG",
            "specialization": "Computer Science",
            "institution": "University of Washington",
            "year": "2018"
        },
        {
            "degree": "12th",
            "specialization": "Science (PCMC)",
            "institution": "Lincoln High School",
            "year": "2014"
        },
        {
            "degree": "10th",
            "specialization": "General",
            "institution": "Lincoln High School",
            "year": "2012"
        }
    ],
    "projects": [
        {
            "name": "Cloud-Native E-Commerce Platform",
            "description": "Architected and developed a microservices-based e-commerce platform handling 50,000+ daily transactions. Implemented real-time inventory management, payment processing, and order fulfillment systems with 99.9% uptime.",
            "technologies": "Python, FastAPI, React, PostgreSQL, Redis, RabbitMQ, Docker, Kubernetes, AWS ECS"
        },
        {
            "name": "Real-Time Analytics Dashboard",
            "description": "Built a comprehensive analytics dashboard for business intelligence, processing 1M+ events daily. Implemented data pipelines, visualizations, and automated reporting features.",
            "technologies": "Python, Apache Kafka, ClickHouse, React, D3.js, AWS Lambda"
        },
        {
            "name": "AI-Powered Recommendation Engine",
            "description": "Developed a machine learning-based recommendation system increasing user engagement by 35%. Implemented collaborative filtering and content-based algorithms with A/B testing framework.",
            "technologies": "Python, TensorFlow, Scikit-learn, Apache Spark, AWS SageMaker"
        }
    ],
    "certifications": [
        {
            "name": "AWS Certified Solutions Architect - Professional",
            "issuer": "Amazon Web Services",
            "year": "2023"
        },
        {
            "name": "Certified Kubernetes Administrator (CKA)",
            "issuer": "Cloud Native Computing Foundation",
            "year": "2022"
        }
    ]
}

# Example 2: Fresh Graduate
fresh_graduate_data = {
    "name": "Sarah Williams",
    "mobile": "+1-555-0456",
    "email": "sarah.williams@email.com",
    "location": "Boston, MA",
    "years_experience": 0,
    "current_role": "Fresher",
    "skills": [
        "Quick Learner",
        "Team Collaboration",
        "Problem Solving",
        "Communication",
        "Time Management"
    ],
    "tech_stack": [
        "Python",
        "Java",
        "HTML/CSS",
        "JavaScript",
        "React",
        "MySQL",
        "Git",
        "Linux"
    ],
    "summary": "Recent computer science graduate with strong academic background and hands-on experience through internships and academic projects. Passionate about software development and eager to contribute to innovative projects. Quick learner with excellent problem-solving abilities.",
    "qualifications": [
        {
            "degree": "UG",
            "specialization": "Computer Science and Engineering",
            "institution": "Massachusetts Institute of Technology",
            "year": "2024"
        },
        {
            "degree": "12th",
            "specialization": "Science",
            "institution": "Boston Latin School",
            "year": "2020"
        },
        {
            "degree": "10th",
            "specialization": "General",
            "institution": "Boston Latin School",
            "year": "2018"
        }
    ],
    "projects": [
        {
            "name": "Campus Event Management System",
            "description": "Developed a full-stack web application for managing campus events with user authentication, event creation, RSVP functionality, and admin dashboard. Used by 500+ students.",
            "technologies": "React, Node.js, Express, MongoDB, JWT"
        },
        {
            "name": "Machine Learning Image Classifier",
            "description": "Built an image classification model using CNN achieving 92% accuracy on test dataset. Implemented data augmentation and transfer learning techniques.",
            "technologies": "Python, TensorFlow, Keras, OpenCV, Jupyter"
        },
        {
            "name": "Personal Finance Tracker",
            "description": "Created a mobile-responsive web app for tracking expenses and income with data visualization and budget alerts. Implemented RESTful API and database design.",
            "technologies": "Python, Flask, SQLite, Chart.js, Bootstrap"
        }
    ],
    "certifications": [
        {
            "name": "Google IT Support Professional Certificate",
            "issuer": "Google (Coursera)",
            "year": "2023"
        },
        {
            "name": "Python for Data Science",
            "issuer": "IBM (Coursera)",
            "year": "2023"
        }
    ]
}

# Example 3: Data Scientist
data_scientist_data = {
    "name": "Michael Chen",
    "mobile": "+1-555-0789",
    "email": "michael.chen@email.com",
    "location": "San Francisco, CA",
    "years_experience": 4,
    "current_role": "Senior Data Scientist",
    "skills": [
        "Machine Learning",
        "Statistical Analysis",
        "Data Visualization",
        "A/B Testing",
        "Research & Development"
    ],
    "tech_stack": [
        "Python",
        "R",
        "SQL",
        "TensorFlow",
        "PyTorch",
        "Scikit-learn",
        "Pandas",
        "NumPy",
        "Tableau",
        "Apache Spark",
        "AWS",
        "Docker"
    ],
    "summary": "Data scientist with 4 years of experience developing machine learning models and deriving actionable insights from complex datasets. Expertise in statistical analysis, predictive modeling, and data-driven decision making. Proven track record of delivering business value through data science solutions.",
    "qualifications": [
        {
            "degree": "PG",
            "specialization": "Data Science and Analytics",
            "institution": "Stanford University",
            "year": "2020"
        },
        {
            "degree": "UG",
            "specialization": "Mathematics and Statistics",
            "institution": "UC Berkeley",
            "year": "2018"
        }
    ],
    "projects": [
        {
            "name": "Customer Churn Prediction Model",
            "description": "Developed a machine learning model to predict customer churn with 87% accuracy, enabling proactive retention strategies that reduced churn by 23%.",
            "technologies": "Python, XGBoost, Scikit-learn, Pandas, Matplotlib, AWS SageMaker"
        },
        {
            "name": "NLP-Based Sentiment Analysis System",
            "description": "Built an NLP pipeline for analyzing customer feedback across multiple channels, processing 100K+ reviews monthly. Implemented BERT-based classification with 91% accuracy.",
            "technologies": "Python, TensorFlow, BERT, spaCy, Flask, Elasticsearch"
        },
        {
            "name": "Real-Time Fraud Detection",
            "description": "Designed and deployed a real-time fraud detection system using ensemble methods, reducing fraudulent transactions by 65% while maintaining low false positive rates.",
            "technologies": "Python, Apache Kafka, Random Forest, LightGBM, Redis, Docker"
        }
    ],
    "certifications": [
        {
            "name": "TensorFlow Developer Certificate",
            "issuer": "Google",
            "year": "2022"
        },
        {
            "name": "AWS Certified Machine Learning - Specialty",
            "issuer": "Amazon Web Services",
            "year": "2023"
        }
    ]
}

# Example 4: DevOps Engineer
devops_engineer_data = {
    "name": "Emily Rodriguez",
    "mobile": "+1-555-0321",
    "email": "emily.rodriguez@email.com",
    "location": "Austin, TX",
    "years_experience": 3,
    "current_role": "DevOps Engineer",
    "skills": [
        "CI/CD Pipeline Design",
        "Infrastructure as Code",
        "Cloud Architecture",
        "Automation",
        "Monitoring & Logging"
    ],
    "tech_stack": [
        "Kubernetes",
        "Docker",
        "Terraform",
        "Ansible",
        "Jenkins",
        "GitLab CI",
        "AWS",
        "Azure",
        "Prometheus",
        "Grafana",
        "ELK Stack",
        "Python",
        "Bash"
    ],
    "summary": "DevOps engineer with 3 years of experience designing and implementing scalable infrastructure and CI/CD pipelines. Expert in containerization, orchestration, and cloud technologies. Passionate about automation, reliability, and enabling development teams to ship faster.",
    "qualifications": [
        {
            "degree": "UG",
            "specialization": "Information Technology",
            "institution": "University of Texas at Austin",
            "year": "2021"
        },
        {
            "degree": "12th",
            "specialization": "Science",
            "institution": "Austin High School",
            "year": "2017"
        }
    ],
    "projects": [
        {
            "name": "Multi-Cloud Infrastructure Automation",
            "description": "Designed and implemented Infrastructure as Code using Terraform to manage resources across AWS and Azure. Reduced infrastructure provisioning time by 70% and improved consistency.",
            "technologies": "Terraform, AWS, Azure, Python, GitLab CI"
        },
        {
            "name": "Kubernetes Migration & Optimization",
            "description": "Led the migration of 50+ microservices to Kubernetes, implementing auto-scaling, service mesh, and monitoring. Improved application availability to 99.95% and reduced infrastructure costs by 40%.",
            "technologies": "Kubernetes, Docker, Istio, Prometheus, Grafana, Helm"
        },
        {
            "name": "CI/CD Pipeline Enhancement",
            "description": "Revamped CI/CD pipelines using GitLab CI and Jenkins, implementing automated testing, security scanning, and blue-green deployments. Reduced deployment time from 2 hours to 15 minutes.",
            "technologies": "GitLab CI, Jenkins, Docker, SonarQube, Trivy, ArgoCD"
        }
    ],
    "certifications": [
        {
            "name": "Certified Kubernetes Administrator (CKA)",
            "issuer": "Cloud Native Computing Foundation",
            "year": "2023"
        },
        {
            "name": "AWS Certified DevOps Engineer - Professional",
            "issuer": "Amazon Web Services",
            "year": "2024"
        },
        {
            "name": "HashiCorp Certified: Terraform Associate",
            "issuer": "HashiCorp",
            "year": "2022"
        }
    ]
}

# Example 5: Business Analyst
business_analyst_data = {
    "name": "David Kim",
    "mobile": "+1-555-0654",
    "email": "david.kim@email.com",
    "location": "Chicago, IL",
    "years_experience": 2,
    "current_role": "Business Analyst",
    "skills": [
        "Requirements Analysis",
        "Data Analysis",
        "Stakeholder Management",
        "Process Improvement",
        "Documentation"
    ],
    "tech_stack": [
        "SQL",
        "Excel",
        "Power BI",
        "Tableau",
        "JIRA",
        "Confluence",
        "Python",
        "R"
    ],
    "summary": "Business analyst with 2 years of experience bridging the gap between business needs and technical solutions. Skilled in requirements gathering, data analysis, and process optimization. Strong communicator with ability to translate complex technical concepts for stakeholders.",
    "qualifications": [
        {
            "degree": "PG",
            "specialization": "Business Analytics",
            "institution": "Northwestern University",
            "year": "2022"
        },
        {
            "degree": "UG",
            "specialization": "Business Administration",
            "institution": "University of Illinois",
            "year": "2020"
        }
    ],
    "projects": [
        {
            "name": "Sales Performance Dashboard",
            "description": "Created interactive dashboards for tracking sales metrics across regions, enabling data-driven decision making. Identified key trends leading to 15% increase in quarterly revenue.",
            "technologies": "Power BI, SQL Server, DAX, Excel"
        },
        {
            "name": "Process Automation Initiative",
            "description": "Analyzed and documented business processes, identifying automation opportunities. Worked with development team to implement solutions that saved 200+ hours monthly.",
            "technologies": "JIRA, Confluence, Python, UiPath"
        }
    ],
    "certifications": [
        {
            "name": "Certified Business Analysis Professional (CBAP)",
            "issuer": "IIBA",
            "year": "2023"
        },
        {
            "name": "Microsoft Certified: Power BI Data Analyst",
            "issuer": "Microsoft",
            "year": "2023"
        }
    ]
}

# Dictionary of all examples for easy access
EXAMPLE_RESUMES = {
    "software_engineer": software_engineer_data,
    "fresh_graduate": fresh_graduate_data,
    "data_scientist": data_scientist_data,
    "devops_engineer": devops_engineer_data,
    "business_analyst": business_analyst_data
}

# Usage example
if __name__ == "__main__":
    print("Available example resumes:")
    for key in EXAMPLE_RESUMES.keys():
        print(f"  - {key}")
    
    print("\nTo use an example:")
    print("  from examples import EXAMPLE_RESUMES")
    print("  data = EXAMPLE_RESUMES['software_engineer']")
    print("  resume_generator.generate_resume(data, 'output.pdf')")
