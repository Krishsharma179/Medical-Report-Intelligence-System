**Medicial-report-Intelligence-system**

A machine learning web application that predicts the likelihood of Diabetes and Coronary Artery Disease (CAD) based on patient health parameters. The app provides predictions along with AI-powered plain-language explanations and actionable health advice.

**Motivation :**
In the real world, doctors are extremely busy and patients often leave a clinic with a report full of numbers BMI, VLDL, HDL, Creatinine  and no idea what any of it means or what they should do about it.
Most people don't know whether their cholesterol is dangerous, whether their urea level is normal, or why their BMI matters. They either forget to ask, don't get the time to ask, or simply can't afford repeated consultations just to understand their own results.
This app bridges that gap.
A patient can enter the values directly from their lab report. The app will:

Predict the likelihood of Diabetes or Heart Disease (CAD)
Explain what each biomedical term actually means in plain, simple language
Tell them whether their specific value is normal or concerning
Give personalised, actionable steps they can take to improve or manage their health

**How it works** 
```
Patient Input Values
        │
        ▼
┌───────────────────┐
│  Query Formation  │  ← Patient values are formatted into a structured query
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│   Retriever       │  ← Searches a medical knowledge base for relevant context
│  (Vector Store)   │    (normal ranges, what each biomarker means, risk factors)
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│   LLM Generator   │  ← Combines retrieved context + patient values to produce
│                   │    a personalised, plain-English explanation + advice
└────────┬──────────┘
         │
         ▼
  Personalised Output
  • What each term means
  • Whether the patient's value is normal / borderline / high
  • Specific steps to improve their health
```

No medical degree required. No waiting room. Just answers. 
** Home screen**

<img width="750" height="500" alt="Screenshot 2026-05-27 165241" src="https://github.com/user-attachments/assets/ed68dc91-106e-4fa5-aaa2-dbfb8bb54651" />

**After clicking Diabetes** _(You can click CAD also)_

<img width="750" height="500" alt="Screenshot 2026-05-27 165257" src="https://github.com/user-attachments/assets/372db403-1c16-45ce-80db-c0ab209251b3" />

**Result**
**Explanations of the biomedical terms**

<img width="501" height="400" alt="Screenshot 2026-05-27 165633" src="https://github.com/user-attachments/assets/870435e3-b6fe-46fe-bcc9-e31f548cbf64" />
<img width="468" height="400" alt="Screenshot 2026-05-27 165509" src="https://github.com/user-attachments/assets/3621e0b4-ef85-478d-8a00-54ce62a25754" />


**suggestions** (To overcome it or control it)

<img width="493" height="884" alt="Screenshot 2026-05-27 165643" src="https://github.com/user-attachments/assets/abd35720-0942-4fff-b8c0-df6b1d8c135d" />


**Project structure**
```
mini_proj_sem5/
├── .venv/                    # Virtual environment
├── artifact/                 # Saved ML model artifacts (.pkl files)
├── datas/                    # Raw datasets
├── ddata/                    # Processed/cleaned data
├── logs/                     # Application logs
├── notebook/                 # Jupyter notebooks (EDA & model training)
├── src/                      # Core source code (pipelines, utils)
├── templates/                # HTML Jinja2 templates
├── app.py                    # Flask application entry point
├── ddata.txt                 # Data reference file
├── rag.ipynb                 # RAG pipeline notebook
├── requirements.txt          # Python dependencies
├── setup.py                  # Package setup
└── README.md
```
**Installation**
```
# 1. Clone the repository
git clone https://github.com/your-username/mini_proj_sem5.git
cd mini_proj_sem5

# 2. Create and activate a virtual environment
python -m venv .venv

# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```
**Run**
```
python app.py
```

