# Gunakan base image Python resmi
FROM python:3.11-slim

# Tetapkan direktori kerja di dalam kontainer
WORKDIR /app

# Salin berkas dependensi dan install
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Salin semua kode aplikasi ke dalam direktori kerja
COPY . .

# Tetapkan environment variable PORT yang akan digunakan oleh Cloud Run
ENV PORT 8080

# Perintah untuk menjalankan aplikasi menggunakan Gunicorn (server WSGI production)
# Gunicorn lebih direkomendasikan untuk production daripada server bawaan Flask
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "1", "--threads", "8", "main:app"]