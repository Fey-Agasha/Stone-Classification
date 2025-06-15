import os
from PIL import Image
from tqdm import tqdm

def preprocess_images(src_root, dst_root, target_size=(224, 224)):
    """
    批量预处理图片：Resize后保存到新路径
    Args:
        src_root: 源数据集根目录，例如 './dataset/train_val/train'
        dst_root: 目标数据集根目录，例如 './dataset_processed/train'
        target_size: resize到的大小，默认(224, 224)
    """
    os.makedirs(dst_root, exist_ok=True)

    img_list = os.listdir(src_root)
    print(f"开始处理 {src_root} 中的 {len(img_list)} 张图片...")

    for img_name in tqdm(img_list, desc=f"Processing {os.path.basename(src_root)}"):
        src_path = os.path.join(src_root, img_name)
        dst_path = os.path.join(dst_root, img_name)

        try:
            img = Image.open(src_path).convert('RGB')
            img = img.resize(target_size, Image.BILINEAR)
            img.save(dst_path)
        except Exception as e:
            print(f"❗处理失败: {img_name}, 错误信息: {e}")

    print(f" 完成处理 {src_root} -> {dst_root}")

def main():
    # 配置路径
    original_base = "./dataset/train_val"   # 原始图片总目录
    processed_base = "./dataset_processed"  # 处理后存放目录

    # 分别处理 train, val, test
    splits = ["train", "val"]
    for split in splits:
        src_folder = os.path.join(original_base, split)
        dst_folder = os.path.join(processed_base, split)
        preprocess_images(src_folder, dst_folder, target_size=(224, 224))

    src_test_folder = "./dataset/test/test_images"
    dst_test_folder = "./dataset_processed/test/test_images"
    preprocess_images(src_test_folder, dst_test_folder, target_size=(224, 224))

if __name__ == "__main__":
    main()