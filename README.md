## ⚖️ Utility Meter Reading Recognition Project

### Overview
This project aims to automate the process of utility meter (water, gas, electricity) reading using advanced computer vision and machine learning techniques. The core technologies include FastAPI, YOLOv8, and a Telegram Bot (AIOGram) running in a Docker container on Linux Manjaro with an NVidia RTX 3090 Ti GPU.

### System Architecture
```mermaid
graph LR
    A[Telegram User] -->|Send Image| B(Telegram Bot)
    B --> C{FastAPI Server}
    C -->|Image Processing| D[YOLOv8 Model]
    D -->|Extracted Readings| C
    C -->|Response| B
    B -->|Reading Results| A
```

### Features
- Image submission via Telegram Bot.
- Real-time processing with YOLOv8 for accurate meter reading.
- Fast and scalable backend with FastAPI.
- High-performance computing with NVidia RTX 3090 Ti.

### Prerequisites
- Docker
- Linux Manjaro
- NVidia GPU support

### Installation
1. Clone the repository:
   ```
   git clone [repository-url]
   ```
2. Navigate to the project directory:
   ```
   cd utility-meter-reading-recognition
   ```
3. Build the Docker container:
   ```
   docker build -t utility-meter-reading .
   ```

### Usage
1. Start the Docker container:
   ```
   docker run --gpus all -p 80:80 utility-meter-reading
   ```
2. Interact with the Telegram Bot by sending images of utility meters.

---

![image](https://github.com/DmPanf/Counters_YOLOv8_FastAPI_TgBot_Advanced_ver2/assets/99917230/5bd0eb08-3d61-4ec1-88e3-d6e7347e65e8)
![image](https://github.com/DmPanf/Counters_YOLOv8_FastAPI_TgBot_Advanced_ver2/assets/99917230/a76d8321-b870-4544-bc6b-b7fbf5bc022e)

---

### Contributing
Contributions to this project are welcome! Please fork the repository and submit pull requests with your enhancements.

### License
This project is licensed under the [MIT License](LICENSE).

### Contact
For any inquiries, please contact [project-email].

---

