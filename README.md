# 🍶 Toddy Shop Finder

> Discover authentic Kerala toddy shop experiences — where tradition meets taste.

---

## 🌴 Introduction

Kerala’s toddy shops have evolved into vibrant destinations offering **authentic cuisine, cultural richness, and quality experiences** for locals and tourists alike.

However, there is no centralized platform to discover the best toddy shops based on **hygiene, food quality, and overall experience**.

👉 **Toddy Shop Finder** bridges this gap by providing a modern, community-driven discovery platform.

---

## 🎯 Project Vision

> To become the most trusted platform for discovering authentic toddy shop experiences in Kerala.

---

## 🧭 Project Objectives

* 🔍 Help users find the best toddy shops
* 🧼 Promote hygiene and quality standards
* 📈 Support local businesses
* 🌍 Enhance tourism
* ⭐ Provide user-driven insights

---

## ✨ Key Features

* 🔎 Shop discovery by location
* ⭐ Ratings & reviews
* 🍛 Food highlights
* 🧼 Hygiene indicators
* 📸 Photo sharing
* 🌍 Tourist-friendly info
* ❤️ Favorites & recommendations

---

## 🏗️ Tech Stack

| Layer    | Technology        |
| -------- | ----------------- |
| Backend  | Django + DRF      |
| Frontend | Next.js (Planned) |
| Database | PostgreSQL        |

---

## 📂 Project Structure

```id="proj_struct_updated_001"
toddy_shop_backend/
├── manage.py
├── pyproject.toml
│
├── config/                # Django project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── common/                # Shared infrastructure & utilities
│   ├── exceptions.py      # Custom exception handling
│   ├── middleware.py      # Request/response middleware
│   ├── pagination.py      # Common pagination logic
│   ├── responses.py       # Standard API response format
│   └── utils/             # Helper utilities
│
├── core/                  # Master / reference data (domain layer)
│   ├── models.py          # District, Place, Category, etc.
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
└── shops/                 # Transactional domain (business data)
    ├── models.py          # ToddyShop, License, ShopFoodMapping
    ├── serializers.py
    ├── views.py
    ├── urls.py
    └── migrations/
```

---

## ⚙️ Architecture Decisions


### 🔹 Layered Responsibility

| Layer  | Responsibility            |
| ------ | ------------------------- |
| core   | Master/reference data     |
| shops  | Business/transaction data |
| common | Shared utilities & infra  |
| config | Project configuration     |

---

## 🧩 Core Module Responsibilities

* District
* Place
* Food Category
* Shop Category
* Facility
* Hygiene Tags
* Rating Types
* Media Types
* License Types

---

## 🏪 Shops Module Responsibilities

* Toddy Shop Management
* License Handling
* Shop-Food Mapping
* Shop-related operations

---

## ⚙️ Development Rules

* ✅ Business logic in `views.py`
* ✅ Validation is mandatory
* ✅ Use common response format
* ✅ Use centralized exception handling
* ✅ Logging should be implemented

---

## 🤝 Contributing

We welcome all contributors ❤️

### 🔹 Steps

1. Fork the repository
2. Create a feature branch
3. Pick an issue
4. Submit a Pull Request

---


## 🌟 Future Scope

* 📱 Mobile app integration
* 🗺️ Advanced search & filters
* ⭐ AI-based recommendations
* 🌍 Tourism integration

---

## 💡 Vision Beyond Code

> This project is about **preserving Kerala’s culture**, supporting local businesses, and delivering authentic experiences.

---

## 📄 License

MIT License

---

## 🙌 Acknowledgements

Thanks to all contributors building this platform together 🚀
