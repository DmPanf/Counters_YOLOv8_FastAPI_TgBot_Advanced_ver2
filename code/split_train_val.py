import os
import random
import shutil

def split_dataset(images_dir='./images', labels_dir='./labels', val_percent=0.1):
    # Получаем список всех изображений и меток
    image_files = [f for f in os.listdir(images_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
    label_files = [f.replace('.jpg', '.txt').replace('.jpeg', '.txt').replace('.png', '.txt') for f in image_files]
    
    # Перемешиваем список
    random.shuffle(image_files)
    
    # Вычисляем количество изображений для валидации
    val_count = int(len(image_files) * val_percent)
    
    # Делим на обучающий и валидационный наборы
    val_images = image_files[:val_count]
    train_images = image_files[val_count:]
    
    val_labels = label_files[:val_count]
    train_labels = label_files[val_count:]
    
    # Создаем директории для train и val, если они еще не существуют
    os.makedirs('./train/images', exist_ok=True)
    os.makedirs('./train/labels', exist_ok=True)
    os.makedirs('./val/images', exist_ok=True)
    os.makedirs('./val/labels', exist_ok=True)
    
    # Копируем файлы в соответствующие директории
    for img in train_images:
        shutil.copy(os.path.join(images_dir, img), './train/images/')
    for lbl in train_labels:
        shutil.copy(os.path.join(labels_dir, lbl), './train/labels/')
        
    for img in val_images:
        shutil.copy(os.path.join(images_dir, img), './val/images/')
    for lbl in val_labels:
        shutil.copy(os.path.join(labels_dir, lbl), './val/labels/')

# Вызов функции для разделения датасета
split_dataset()
