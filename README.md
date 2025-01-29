# Novel Hunter API

**Novel Hunter** is a Flask-based web application designed to provide novel rankings, chapter lists, and detailed novel information. It allows users to fetch top-ranked novels, retrieve chapter listings, and explore specific novel details via simple API endpoints.

This project is designed to make it easier for users to discover and read their favorite novels, with features like fetching top novels by category, viewing detailed novel information, and navigating through chapters.

---

## Features

- **Top Novel List**: Retrieves a list of top-ranked novels based on time frame and genre.
- **Novel Information**: Fetches detailed information about a specific novel.
- **Chapter List**: Displays a list of chapters for a specific novel.
- **Chapter Information**: Shows detailed information for a specific chapter.
- **API Documentation**: Full documentation of the API endpoints is available via `/docs` route.

---

## API Endpoints

### 1. Home Route
- **URL**: `/`
- **Method**: `GET`
- **Description**: Returns the home content of the application.

### 2. Top Novel List
- **URL**: `/novel`
- **Method**: `GET`
- **Query Parameters**:
  - `time`: Time frame for the ranking (e.g., "Monthly")
  - `type`: Type of novel (e.g., "Fantasy", "Action")
- **Description**: Retrieves a list of top-ranked novels based on the specified time and type.

#### Example Request:
```
GET /novel?time=Monthly&type=Fantasy
```

#### Example Response:
```json
{
  "status": "success",
  "novel_list": [
    {"title": "Novel 1", "rank": 1},
    {"title": "Novel 2", "rank": 2}
  ]
}
```

### 3. Novel Information
- **URL**: `/novels/<url>`
- **Method**: `GET`
- **Description**: Retrieves detailed information about a specific novel using its URL.

#### Example Request:
```
GET /novels/novel-123
```

#### Example Response:
```json
{
  "status": "success",
  "novel_info": {
    "title": "Novel 1",
    "author": "Author Name",
    "genre": "Fantasy"
  }
}
```

### 4. Chapters List
- **URL**: `/chapters/<url>/<number>`
- **Method**: `GET`
- **Description**: Retrieves a list of chapters for a specific novel and chapter number.

#### Example Request:
```
GET /chapters/novel-123/1
```

#### Example Response:
```json
{
  "status": "success",
  "chapters": [
    {"chapter_title": "Chapter 1", "chapter_link": "link_to_chapter_1"},
    {"chapter_title": "Chapter 2", "chapter_link": "link_to_chapter_2"}
  ]
}
```

### 5. Chapter Information
- **URL**: `/info/<url>/<id>`
- **Method**: `GET`
- **Description**: Retrieves detailed information about a specific chapter of a novel.

#### Example Request:
```
GET /info/novel-123/1
```

#### Example Response:
```json
{
  "status": "success",
  "chapter_info": {
    "title": "Chapter 1",
    "content": "This is the content of chapter 1..."
  }
}
```

---

## Running the Application Locally

### Prerequisites

- Python 3.x
- Flask

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/novel-hunter.git
   cd novel-hunter
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app:
   ```bash
   python app.py
   ```

4. Visit `http://127.0.0.1:5000` in your browser to view the application.

---

### `requirements.txt` Example

```txt
Flask==2.0.2
```

---

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Open a pull request to the main repository.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Author

**Novel Hunter** is maintained by [Your Name](https://github.com/yourusername). Feel free to open an issue or contribute to the project!
