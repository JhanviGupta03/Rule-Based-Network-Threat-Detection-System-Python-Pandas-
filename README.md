# Rule-Based Network Threat Detection System (Python + Pandas)

## 📌 Overview

This project is a simple rule-based network intrusion detection system built using Python and Pandas. It analyzes simulated network traffic data and determines whether to **ALLOW** or **BLOCK** traffic based on predefined conditions.

---

## 🚀 Features

* Analyzes packet size and failed login attempts
* Uses rule-based logic for threat detection
* Lightweight and beginner-friendly
* Easy to understand and modify

---

## 🧠 Detection Logic

A network request is classified as a threat if:

* Packet size > **1000**
* OR failed login attempts > **2**

### Decision:

* If any condition is met → **BLOCK**
* Otherwise → **ALLOW**

---

## 🛠️ Technologies Used

* Python
* Pandas

---

## 📂 Project Structure

```
.
├── main.py   # Main script containing detection logic
```

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install pandas
```

### 2. Run the script

```bash
python main.py
```

---

## 📊 Sample Output

```
   packet_size  failed_logins Action
0          200              0  ALLOW
1         1500              3  BLOCK
2          300              0  ALLOW
3         2500              4  BLOCK
4          100              1  ALLOW
```

---

## 🎯 Use Case

This project demonstrates:

* Basic cybersecurity threat detection
* Data processing with Pandas
* Rule-based decision systems

---

## ⚠️ Limitations

* Uses static rules (no machine learning)
* Works only on simulated data
* Not suitable for real-world deployment

---

## 📈 Future Improvements

* Add machine learning-based anomaly detection
* Implement real-time monitoring
* Integrate with network security tools

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and enhance the detection logic or add new features.

---

## 📜 License

This project is open-source and available under the MIT License.
