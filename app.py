from flask import Flask, render_template, abort

app = Flask(__name__)

CATEGORIES = [
    {
        "slug": "men",
        "name": "Men",
        "description": "Streetwear, jerseys, hoodies, and everyday pieces for men.",
    },
    {
        "slug": "women",
        "name": "Women",
        "description": "Curated women’s pieces with a focus on fit, style, and quality.",
    },
    {
        "slug": "unisex",
        "name": "Unisex",
        "description": "Versatile pieces that work for anyone and make up the core of the store.",
    },
    {
        "slug": "clearance",
        "name": "Clearance",
        "description": "Discounted items and final-price deals from every category.",
    },
]

PRODUCTS = [
    {
        "id": 1,
        "name": "Vintage Track Jacket",
        "category": "men",
        "price": 32,
        "size": "L",
        "condition": "Excellent",
        "image": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?auto=format&fit=crop&w=900&q=80",
        "description": "Clean athletic jacket with lightweight feel and easy everyday styling.",
    },
    {
        "id": 2,
        "name": "Oversized Graphic Tee",
        "category": "unisex",
        "price": 24,
        "size": "XL",
        "condition": "Very Good",
        "image": "https://images.unsplash.com/photo-1523398002811-999ca8dec234?auto=format&fit=crop&w=900&q=80",
        "description": "Relaxed fit tee with bold graphic styling and soft fabric feel.",
    },
    {
        "id": 3,
        "name": "Women’s Cropped Hoodie",
        "category": "women",
        "price": 28,
        "size": "M",
        "condition": "Excellent",
        "image": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?auto=format&fit=crop&w=900&q=80",
        "description": "Comfortable cropped hoodie with clean lines and a modern fit.",
    },
    {
        "id": 4,
        "name": "Clearance Windbreaker",
        "category": "clearance",
        "price": 18,
        "size": "L",
        "condition": "Good",
        "image": "https://images.unsplash.com/photo-1503342217505-b0a15ec3261c?auto=format&fit=crop&w=900&q=80",
        "description": "Lightweight layer at a lower price and good for quick resale movement.",
    },
    {
        "id": 5,
        "name": "Neutral Pullover",
        "category": "unisex",
        "price": 30,
        "size": "M",
        "condition": "Excellent",
        "image": "https://images.unsplash.com/photo-1512436991641-6745cdb1723f?auto=format&fit=crop&w=900&q=80",
        "description": "Minimal pullover that fits the clean unisex look of the shop.",
    },
    {
        "id": 6,
        "name": "Women’s Relaxed Denim",
        "category": "women",
        "price": 35,
        "size": "S",
        "condition": "Very Good",
        "image": "https://images.unsplash.com/photo-1542272604-787c3835535d?auto=format&fit=crop&w=900&q=80",
        "description": "Relaxed denim with a flattering shape and easy styling potential.",
    },
]


def get_category(slug):
    for category in CATEGORIES:
        if category["slug"] == slug:
            return category
    return None


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/shop")
def all_items():
    return render_template("all_items.html", products=PRODUCTS)


@app.route("/category/<slug>")
def category_page(slug):
    category = get_category(slug)

    if category is None:
        abort(404)

    category_products = [product for product in PRODUCTS if product["category"] == slug]

    return render_template(
        "category.html",
        category=category,
        products=category_products,
    )


if __name__ == "__main__":
    app.run(debug=True)