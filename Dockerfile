# Dockerfile
#שפת התיכנות שממנה דוקר מריץ את האימג'
FROM python:3.9-slim

#הפעלת משתני סביבה כך שתיהיה נראות של משתנים כמו פרינט וכדומה
ENV PYTHONUNBUFFERED 1

#יצירת תיקייה שבה ייכנסו כל הקבצים בשביל ליצור את האימג'
WORKDIR /app

#העתקת התלויות של הפרויקט
COPY requirements.txt /app/

#התקנת התלויות והרצתם ללא השתמשות בזיכרון קאש
RUN pip install --no-cache-dir -r requirements.txt

#העתקת כל הקבצים לתוך תיקיית אפ
COPY . /app/

#הגדרת פורט שעליו ירוץ הדוקר
EXPOSE 5001

#הרצת הפרויקט
CMD ["python", "app.py"]