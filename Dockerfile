# 1. Gunakan base image resmi dari Miniconda
# Image ini sudah memiliki Conda terinstal.
FROM continuumio/miniconda3

# Tetapkan direktori kerja di dalam kontainer
WORKDIR /app

# 2. Salin file environment.yml terlebih dahulu
COPY environment.yml .

# 3. Buat environment Conda berdasarkan file .yml
# Perintah ini akan menginstal semua dependensi dari conda dan pip
RUN conda env create -f environment.yml

# Salin sisa kode aplikasi Anda
COPY . .

# Tetapkan environment variable untuk port
ENV PORT=8080

# 4. Perintah untuk menjalankan aplikasi
# Gunakan 'conda run' untuk mengeksekusi perintah dari dalam environment yang baru dibuat
# Ganti 'nama_env_anda' dengan nama environment yang ada di dalam file environment.yml Anda
CMD ["conda", "run", "-n", "batik-api", "gunicorn", "--bind", "0.0.0.0:8080", "--workers", "1", "--threads", "8", "main:app"]