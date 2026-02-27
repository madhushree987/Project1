# 🎬 Movie Success Prediction Dashboard

A simple **Flask-based web application** that analyzes IMDb movie data and classifies movies into success categories like **Blockbuster, Hit, Average, and Flop** based on their gross earnings. The app also provides genre-based filtering and a success distribution view.

---

## 📌 Project Overview

This project uses the **IMDb Top 1000 Movies dataset** to:

* Clean and preprocess movie gross revenue data
* Classify movie success based on revenue thresholds
* Display an interactive dashboard using Flask
* Filter movies by genre
* Show success distribution for selected genres

It is ideal for:

* Data Analytics / Data Science mini projects
* Internship or academic submissions
* Learning Flask + Pandas integration

---

## 🛠️ Tech Stack

* **Python 3.x**
* **Flask** – Web framework
* **Pandas** – Data analysis
* **NumPy** – Numerical operations
* **HTML & CSS** – Frontend (embedded template)

---

## 📂 Project Structure

```
Movie-Success-Prediction/
│
├── app.py                         # Flask application
├── imdb_top_1000.csv              # Dataset
├── Movie success prediction.ipynb # Data analysis & exploration notebook
├── README.md                      # Project documentation
```

---

## 📊 Dataset

**Source:** IMDb Top 1000 Movies Dataset

**Key Columns Used:**

* `Series_Title` – Movie name
* `Genre` – Movie genre(s)
* `IMDB_Rating` – IMDb rating
* `Gross` – Total gross revenue

The `Gross` column is cleaned by:

* Removing commas
* Converting to numeric values
* Dropping missing values

---

## 🧠 Success Classification Logic

Movies are classified based on **Gross Revenue**:

| Gross Revenue ($) | Success Category |
| ----------------- | ---------------- |
| > 500,000,000     | Blockbuster      |
| > 100,000,000     | Hit              |
| > 50,000,000      | Average          |
| ≤ 50,000,000      | Flop             |

---

## 🚀 How to Run the Project

### 1️⃣ Install Required Libraries

```bash
pip install flask pandas numpy
```

### 2️⃣ Run the Flask App

```bash
python app.py
```

### 3️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

---

## 🖥️ Application Features

* 🎥 Movie listing with title, genre, rating, gross, and success status
* 🎭 Genre-based filtering (single or multiple genres)
* 📈 Success distribution summary
* 🎨 Clean and responsive UI

---

## 📓 Jupyter Notebook

The file **`Movie success prediction.ipynb`** contains:

* Data exploration
* Data cleaning steps
* Initial analysis and insights

Useful for understanding the logic before deployment.

---

## ✅ Future Enhancements

* Add charts (bar/pie) for success distribution
* Predict success for new movies using ML models
* Improve UI using Bootstrap
* Deploy on Render / Heroku

---

## 👩‍💻 Author

**Madhushree S**
Data Analytics & Python Enthusiast

---

## 📜 License

This project is for **educational purposes only**.

---

✨ *Happy Coding & Data Exploring!* ✨
