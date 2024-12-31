# Code Screening: Django REST Framework + Vue.js :🌟

## Overview
This project is part of a code screening assignment that demonstrates building a backend API using Django REST Framework and a responsive frontend using Vue.js. The backend provides an API for posts with comments, while the frontend displays movie details dynamically fetched from an external API.

---

## Features 📝

### Backend (Django REST Framework):
1. **Posts API**:
   - Fetch a list of posts ordered by timestamp (latest first).
   - Display up to 3 comments per post, sorted by timestamp.
   - Includes pagination for efficient data handling.

2. **Random Comments Logic**:
   - Added a commented block of code for fetching 3 random comments instead of the latest.

3. **Custom Pagination**:
   - Configurable page size to manage the number of posts displayed per page.

4. **Testing**:
   - Tested using Postman for endpoints and data handling.

### Frontend (Vue.js):
1. ** Design**:
   - A layout that that is adjusted for desktops (responsiveness - still learning).

2. **Dynamic Data Fetching**:
   - Fetches movie details from the OMDB API.
   - Displays data dynamically on the homepage.

3. **Interactive Elements**:
   - Genre hover effects: Text switches to a genre-specific icon on hover.
   - IMDb ratings displayed as a 5-star scale.
   - Interactive icons for liking and adding to a watchlist with hover animations.

4. **Key Improvement**:
   - Enhanced genre display with hover animations to improve visual appeal.
   - Buffer loading screen that catches attention

---

## Setup and Installation 🛠️

### Prerequisites
- Python 3.10 or above
- Node.js and npm
- Vue CLI

### Backend Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/project-name.git
   cd backend_repo
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run serve
   ```

---

## API Endpoints 🌐

### **Posts Endpoint**
- **GET** `/posts/`
  - Retrieves a paginated list of posts with up to 3 comments per post.

### Follow-Up Question: Random Comments Logic
To fetch 3 random comments instead of sorting by timestamp, uncomment the provided logic in `views.py`:
```python
from random import sample
# Fetch 3 random comments instead of the latest
if comments.count() > 3:
    random_comments = sample(list(comments), 3)
else:
    random_comments = comments
```

---

## File Structure 📂
```
project-name/
|-- backend_repo/
|   |-- apps/
|   |   |-- demo/
|   |       |-- models.py
|   |       |-- serializers.py
|   |       |-- views.py
|-- frontend/
|   |-- src/
|   |   |-- components/
|   |       |-- AppNavbar.vue
|   |       |-- AppHomepage.vue
|   |       |-- MovieDetailsCard.vue
|   |       |-- RatingsDisplay.vue
|-- README.md
```

---

## How to Test 🚀

### Backend:
- Use Postman or cURL to test the `/posts/` endpoint.
- Example cURL command:
  ```bash
  curl -X GET http://127.0.0.1:8000/posts/
  ```

### Frontend:
- Open the application in a browser (`http://localhost:8080/`).
- Test responsiveness by resizing the browser window.

---

## Loom Video 💻
Watch my project walkthrough on Loom: [Loom Video Link](https://www.loom.com/share/d9c64140f2df4f3f9b0e59667b650423)

---

## Acknowledgments
- Django REST Framework
- Vue.js
- OMDB API

---

## Author 🎉
[Shawn Biju Thomas](https://www.linkedin.com/in/shawnthomas02/) 
[GitHub](https://github.com/2347253)
