import os
import django
import shutil
import sys

# Setup Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zoco.settings')
django.setup()

from store.models import product, category

# Data from products.js
products_data = [
    { 
        "name": "Emerald Lace Slip", 
        "price": 4499, 
        "img": "zoco-split-1-0.jpg", 
        "category": "Lace Intimates",
        "isNew": True 
    },
    { 
        "name": "Champagne Silk Gown", 
        "price": 8999, 
        "img": "zoco-split-1-1.jpg", 
        "category": "Signature Sets",
        "isNew": False
    },
    { 
        "name": "Midnight Satin Robe", 
        "price": 5999, 
        "img": "zoco-split-2-0.png", 
        "category": "Silk Series",
        "isNew": True 
    },
    { 
        "name": "Rose Petal Chemise", 
        "price": 3499, 
        "img": "zoco-split-2-3.png", 
        "category": "Comfort Specials",
        "isNew": False 
    },
    { 
        "name": "Ivory Garden Dress", 
        "price": 7499, 
        "img": "zoco-product-1.png", 
        "category": "Premium Lace",
        "isNew": True 
    },
    { 
        "name": "Dawn Mist Negligee", 
        "price": 2999, 
        "img": "zoco-split-2-2.png", 
        "category": "Silk Series",
        "isNew": False 
    },
    {
        "name": "Scarlet Velvet Set",
        "price": 6499,
        "img": "zoco-split-2-1.png",
        "category": "Signature Sets",
        "isNew": True
    },
    {
        "name": "Obsidian Silk PJ",
        "price": 5499,
        "img": "zoco-hero.png",
        "category": "Silk Series",
        "isNew": True
    }
]

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ASSETS = os.path.join(BASE_DIR, 'static', 'assets')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
UPLOAD_DIR = os.path.join(MEDIA_ROOT, 'uploads', 'products')

# Create directories
os.makedirs(UPLOAD_DIR, exist_ok=True)

print("Seeding database...")

for item in products_data:
    # 1. Category
    cat_obj, _ = category.objects.get_or_create(name=item["category"])
    
    # 2. Image
    src_path = os.path.join(STATIC_ASSETS, item["img"])
    dst_filename = item["img"]
    dst_path = os.path.join(UPLOAD_DIR, dst_filename)
    
    # Copy file if it exists in source
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path)
        print(f"Copied {item['img']}")
    else:
        print(f"Warning: Source image {src_path} not found.")

    # 3. Product
    # Check if exists by name to avoid duplicates
    prod, created = product.objects.get_or_create(
        name=item["name"],
        defaults={
            "price": item["price"],
            "category": cat_obj,
            "stock_quantity": 50, # Default stock
            "image": f"uploads/products/{dst_filename}",
            "is_new": item["isNew"],
            "is_available": True
        }
    )
    
    if created:
        print(f"Created product: {prod.name}")
    else:
        print(f"Product already exists: {prod.name}")

print("Seeding complete.")
