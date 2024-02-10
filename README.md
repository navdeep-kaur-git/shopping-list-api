# Shopping list API
A Shopping List API: using FASTApi framework

## How to run this API?
```
python3 ./src/main.py
```

## How to use this API?

| API                 | Method | Request Body                                                              | Description                            |
|---------------------|--------|---------------------------------------------------------------------------|----------------------------------------|
| /shopping-list      | GET    |                                                                           | Get all shopping items                 |
| /shopping-list/`{id}` | GET    |                                                                           | Get an item using id                   |
| /shopping-list      | POST   | `{"name": "Bread", "quantity": 2}`                         | Create a new item in the shopping list |
| /shopping-list/`{id}` | PUT    | `{"name": "Milk", "quantity": 3, "is_done": true}` | Update an item                         |
| /shopping-list/`{id}` | DELETE |                                                                           | Remove an item from the list           |