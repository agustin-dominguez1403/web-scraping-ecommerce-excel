# 📚 Automated E-Commerce Web Scraper & Excel Exporter

A production-ready Python automation tool that scrapes product catalogs across multiple pages, cleans and structures the data, and exports it into a clean, formatted Excel spreadsheet.

---

## 🚀 Key Features

* **Multi-Page Scraping:** Automatically navigates through catalog pagination.
* **Data Cleaning & Parsing:** Cleans currency symbols and converts pricing into numeric `float` types for easy data analysis.
* **Automated Excel Export:** Formats and saves structured data directly to `.xlsx` using Pandas.
* **Polite Scraping:** Includes request delays to ensure respectful server communication.

---

## 🛠️ Built With

* **Python 3**
* **Requests** – HTTP requests handling
* **BeautifulSoup4** – HTML parsing and DOM extraction
* **Pandas & OpenPyXL** – Data manipulation and Excel generation

---

## 📊 Sample Output

The script extracts the following fields for each product:
* **Book Title** (Full string)
* **Clean Price** (Numeric float in GBP)
* **Stock Status** (Availability check)

---

## ⚙️ How to Run
1. Clone or download the repository.
2. Install dependencies:
   ```bash
   pip install requests beautifulsoup4 pandas openpyxl
3. Run the script:
   ```bash
   python proyecto_integrador.py
   ```bash
   git clone [https://github.com/TU_USUARIO/web-scraping-ecommerce-excel.git](https://github.com/TU_USUARIO/web-scraping-ecommerce-excel.git)
