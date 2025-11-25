
---

# **mytestproject**

Bu proje, üzerinde çalıştığım konuları test etmek ve ana projeme entegre edilmeden önce doğrulamak için oluşturulmuş bir deneme ortamıdır. Burada başarılı şekilde çalıştırdığım yapı ve fonksiyonları daha sonra ana projeye aktarırım.

---

## **📥 Projeyi İndirme**

Proje dosyalarını Git komutlarıyla klonladıktan sonra aşağıdaki adımları izleyebilirsiniz:

---

## **🧱 Sanal Ortam (Virtual Environment) Oluşturma**

```bash
python3 -m venv venv   # kendi sanal ortam adınızı verebilirsiniz
```

### **Linux / macOS için aktifleştirme**

```bash
source venv/bin/activate
```

### **Windows için aktifleştirme**

```bash
source venv/Scripts/activate
```

---

## **📦 Gerekli Paketleri Yükleme**

```bash
pip install -r requirements.txt
```

---

## **🚀 Projeyi Çalıştırma**

### **Linux**

Aşağıdaki komutla çalıştırabilirsiniz:

```bash
./server-com
```

Bu komutu kullanmak istemezseniz:

```bash
python3 manage.py runserver
```

### **Windows**

```bash
python manage.py runserver
```

---

