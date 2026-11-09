# ResearchPilot AI — CSV Data Analysis Dashboard

ResearchPilot is a Streamlit application for exploring tabular datasets. Upload a CSV file to inspect its structure, review data quality, explore descriptive statistics, and generate visual summaries.

## Features

- Upload and inspect CSV datasets.
- View dataset dimensions, column data types, and numerical and categorical features.
- Identify missing values and duplicate rows.
- Generate descriptive statistical summaries.
- Explore numerical distributions with histograms and box plots.
- Visualize categorical counts and numerical relationships with charts, including a correlation heatmap.

## Tech Stack

- Python
- Streamlit
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn (listed in the project dependencies)

## Project Structure

```text
research_agent/
├── app.py
├── src/
│   ├── analyzer.py
│   └── visualizer.py
├── requirements.txt
└── readme.md
```

The Streamlit interface is defined in `app.py`; dataset analysis and chart generation are organized in the `src` package.

## Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/shaik-zabi-321/research_agent.git
   cd research_agent
   ```

2. Create and activate a virtual environment (recommended).

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the application:

   ```bash
   streamlit run app.py
   ```

5. Open the local URL printed by Streamlit and upload a CSV file.

## Live Demo

https://researchagent-v1.streamlit.app/

## Scope

This project focuses on exploratory data analysis and dataset inspection. Its visualizations and summaries support analysis; they do not by themselves establish statistical significance or predictive performance.
