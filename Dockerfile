FROM python:3.10-slim-bookworm AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends build-essential

# إنتاج بيئة وهمية لتثبيت الحزم فيها بعيداً عن مجلد الجذر
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.10-slim-bookworm

WORKDIR /app

# نقل البيئة الوهمية الجاهزة للصورة النهائية
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY . .

# إنشاء مستخدم غير روت ومنحه الصلاحيات الكاملة على مجلد العمل والبيئة
RUN useradd -m appuser && chown -R appuser:appuser /app /opt/venv
USER appuser

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"

EXPOSE 8000

CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]