# 🚀 AI-Powered Professional Resume Generator

A comprehensive resume generation system powered by **Llama AI** from Hugging Face. This application features an interactive web interface, AI-enhanced content generation, professional PDF creation, and AWS S3 cloud storage integration.

## ✨ Features

- **Interactive Web Form**: Beautiful, responsive interface for data collection
- **AI Enhancement**: Llama model integration for professional content improvement
- **Multiple Qualifications**: Support for 10th, 12th, UG, PG, PhD with specializations
- **Dynamic Projects**: Add multiple projects with descriptions and technologies
- **Optional Certifications**: Include professional certifications
- **Professional PDF**: High-quality resume generation with proper formatting
- **AWS S3 Upload**: Automatic cloud storage with shareable links
- **Google Colab Ready**: Optimized for running in Colab notebooks

## 📋 Prerequisites

### For Google Colab (Recommended)
- Google account
- No local setup required!

### For Local Execution
- Python 3.8 or higher
- pip package manager
- (Optional) AWS account for S3 uploads
- (Optional) Hugging Face account for certain models

## 🚀 Quick Start - Google Colab

1. **Upload the Notebook**
   - Go to [Google Colab](https://colab.research.google.com/)
   - Upload `resume_generator_colab.ipynb`

2. **Run the Notebook**
   ```
   Runtime → Run all
   ```

3. **Access the Application**
   - Wait for the ngrok URL to appear
   - Click the public URL link
   - Fill in your details and generate your resume!

## 💻 Local Installation

### Step 1: Clone or Extract the Project

```bash
# If you have the ZIP file
unzip resume_generator_project.zip
cd resume_generator_project
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: (Optional) Configure Hugging Face Token

For certain Llama models, you need to:
1. Visit [Hugging Face](https://huggingface.co/)
2. Create an account and get your access token
3. Accept the model license (e.g., for Llama models)

```bash
# Set your token
export HUGGING_FACE_TOKEN="your_token_here"
```

### Step 5: (Optional) Configure AWS S3

If you want to upload resumes to S3:

```bash
export AWS_ACCESS_KEY_ID="your_access_key"
export AWS_SECRET_ACCESS_KEY="your_secret_key"
export AWS_BUCKET_NAME="your_bucket_name"
export AWS_REGION="us-east-1"
```

## 📖 Usage Guide

### Using the Web Interface

1. **Personal Information**
   - Enter your full name, mobile, email, and location

2. **Education Section**
   - Select degree level (10th, 12th, UG, PG, PhD)
   - Add specialization (e.g., "Computer Science")
   - Provide institution name and year
   - Click "+ Add More Education" for additional qualifications

3. **Professional Experience**
   - Enter years of experience
   - Specify current role or "Fresher"

4. **Skills & Technologies**
   - List core skills (comma-separated)
   - List tech stack (comma-separated)

5. **Professional Summary**
   - Write a brief summary about yourself
   - AI will enhance this for a professional tone

6. **Projects**
   - Add project name, description, and technologies
   - Click "+ Add More Projects" for additional entries

7. **Certifications (Optional)**
   - Add certification name, issuer, and year
   - Click "+ Add More Certifications" as needed

8. **Generate**
   - Click "Generate Professional Resume"
   - Wait for AI processing
   - Download your PDF!

## 🏗️ Project Structure

```
resume_generator_project/
├── resume_generator_colab.ipynb  # Main Colab notebook
├── requirements.txt               # Python dependencies
├── README.md                      # This file
├── .gitignore                    # Git ignore patterns
└── output/                       # Generated resumes (created automatically)
```

## 🔧 Configuration

### Model Selection

In the notebook, you can change the Llama model:

```python
# Default: Llama-3.2-1B (fast, good for Colab)
llama_enhancer = LlamaResumeEnhancer("meta-llama/Llama-3.2-1B")

# Better quality (requires more RAM):
# llama_enhancer = LlamaResumeEnhancer("meta-llama/Llama-3.2-3B")
# llama_enhancer = LlamaResumeEnhancer("meta-llama/Llama-2-7b-chat-hf")
```

### PDF Customization

Modify the `ProfessionalResumeGenerator` class to customize:
- Colors and styling
- Font sizes
- Section ordering
- Layout preferences

### AWS S3 Configuration

You can configure S3 credentials in three ways:

1. **Environment Variables** (Recommended)
   ```bash
   export AWS_ACCESS_KEY_ID="..."
   export AWS_SECRET_ACCESS_KEY="..."
   export AWS_BUCKET_NAME="..."
   ```

2. **In the Notebook**
   ```python
   s3_uploader.configure_credentials(
       aws_access_key="...",
       aws_secret_key="...",
       bucket_name="...",
       region="us-east-1"
   )
   ```

3. **Via API Endpoint**
   ```bash
   curl -X POST http://localhost:5000/configure-s3 \
     -H "Content-Type: application/json" \
     -d '{"aws_access_key":"...","aws_secret_key":"...","bucket_name":"..."}'
   ```

## 🎯 API Endpoints

If you want to integrate with other applications:

### Generate Resume
```bash
POST /generate-resume
Content-Type: application/json

{
  "name": "John Doe",
  "mobile": "+1234567890",
  "email": "john@example.com",
  "location": "New York, NY",
  "years_experience": 3,
  "current_role": "Software Engineer",
  "skills": ["Python", "React"],
  "tech_stack": ["AWS", "Docker"],
  "summary": "Experienced developer...",
  "qualifications": [...],
  "projects": [...],
  "certifications": [...]
}
```

### Download Resume
```bash
GET /download/<filename>
```

### Configure S3
```bash
POST /configure-s3
Content-Type: application/json

{
  "aws_access_key": "...",
  "aws_secret_key": "...",
  "bucket_name": "...",
  "region": "us-east-1"
}
```

## 🐛 Troubleshooting

### Model Loading Issues

**Problem**: "You need to accept the model license"

**Solution**:
1. Visit the model page on Hugging Face
2. Log in and accept the license agreement
3. Use your HF token in the notebook

### Memory Issues

**Problem**: "CUDA out of memory" or "Killed"

**Solution**:
- Use a smaller model (Llama-3.2-1B)
- In Colab: Runtime → Change runtime type → GPU
- Reduce `max_new_tokens` in generation

### AWS S3 Upload Fails

**Problem**: S3 upload returns error

**Solution**:
- Verify AWS credentials are correct
- Check bucket permissions
- Ensure bucket exists and is in the correct region
- Verify IAM user has `s3:PutObject` permission

### ngrok Connection Issues

**Problem**: ngrok URL doesn't load

**Solution**:
- Restart the server cell
- Check if Flask is running (look for error messages)
- Try accessing the local URL first: `http://localhost:5000`

## 📊 Technical Details

### AI Model
- **Default**: Llama-3.2-1B (1 billion parameters)
- **Purpose**: Enhance professional summaries and project descriptions
- **Processing**: On-device inference (no external API calls)

### PDF Generation
- **Library**: ReportLab
- **Format**: A4 size, professional styling
- **Features**: Custom fonts, colors, sections, bullet points

### Frontend
- **Technology**: Pure HTML/CSS/JavaScript
- **Design**: Modern, gradient-based UI
- **Responsive**: Works on mobile and desktop

### Backend
- **Framework**: Flask (Python)
- **Deployment**: ngrok tunnel (for Colab)
- **Storage**: Local filesystem + optional S3

## 🔐 Security Notes

- Never commit AWS credentials to version control
- Use environment variables for sensitive data
- The `.gitignore` file is configured to exclude credentials
- S3 buckets should have proper access policies
- Consider using IAM roles instead of access keys

## 🤝 Contributing

This is a standalone project, but you can extend it:

1. Add more AI models (GPT, Claude, etc.)
2. Support more resume templates
3. Add email delivery functionality
4. Create a database for resume storage
5. Add user authentication
6. Support multiple languages

## 📝 License

MIT License - Feel free to use and modify!

## 🆘 Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the code comments in the notebook
3. Ensure all dependencies are installed correctly

## 🎓 Example Resume Data

Here's a sample data structure for testing:

```json
{
  "name": "Jane Smith",
  "mobile": "+1-555-0100",
  "email": "jane.smith@email.com",
  "location": "Austin, TX",
  "years_experience": 2,
  "current_role": "Data Scientist",
  "skills": ["Machine Learning", "Data Analysis", "Statistics"],
  "tech_stack": ["Python", "TensorFlow", "SQL", "Pandas"],
  "summary": "Data scientist with expertise in machine learning...",
  "qualifications": [
    {
      "degree": "PG",
      "specialization": "Data Science",
      "institution": "MIT",
      "year": "2022"
    }
  ],
  "projects": [
    {
      "name": "Predictive Analytics Platform",
      "description": "Built ML models for sales forecasting",
      "technologies": "Python, Scikit-learn, AWS"
    }
  ],
  "certifications": [
    {
      "name": "TensorFlow Developer Certificate",
      "issuer": "Google",
      "year": "2023"
    }
  ]
}
```

## 🚀 Advanced Usage

### Custom PDF Styling

Modify the `_create_custom_styles()` method in `ProfessionalResumeGenerator`:

```python
self.styles.add(ParagraphStyle(
    name='CustomTitle',
    fontSize=28,  # Larger title
    textColor=colors.HexColor('#FF6B6B'),  # Red accent
    # ... more customization
))
```

### Using Different AI Models

```python
# Use a different model
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "mistralai/Mistral-7B-v0.1"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
```

### Batch Processing

```python
# Generate multiple resumes
resumes_data = [data1, data2, data3]  # List of resume data

for data in resumes_data:
    filename = f"{data['name']}_{timestamp}.pdf"
    resume_generator.generate_resume(data, filename)
```

## 📚 Dependencies

Main libraries used:
- `transformers`: Hugging Face transformers for AI models
- `torch`: PyTorch for model inference
- `reportlab`: PDF generation
- `flask`: Web server
- `boto3`: AWS SDK for S3 uploads
- `pyngrok`: Public URL tunneling

---

**Happy Resume Building! 🎉**

For the best experience, use Google Colab with GPU runtime enabled.
