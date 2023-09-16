# Lunch Decision Backend

## Setup:
1. Build the Docker image: `docker-compose build`
2. Run the Docker container: `docker-compose up`
3. Access the API at `http://localhost:8000/`
4. You can use `http://localhost:8000/swagger/` to look at the documentation

## API Versioning:
Currently, only version v1 is supported and active. All the endpoints and tests mentioned below are for this version.
But there is everything prepared to add new functionality with v2.

## API Endpoints:

# Authentication:
- `api/v1/auth/register/`: User registration
- `api/v1/auth/login/`: User login
- `api/v1/auth/token-auth/`: Obtain JWT token pair (access and refresh tokens)
- `api/v1/auth/token-refresh/`: Refresh the JWT token
- `api/v1/auth/token-verify/`: Verify the JWT token
# Employees(You need to log in to use it):
- `api/v1/employees/`: List all employees or create a new employee
- `api/v1/employees/`<int:pk>/: Retrieve, update, or delete a specific employee by its primary key (id)
- `api/v1/employees/vote/`: Create a vote
# Restaurants(You need to log in to use it):
- `api/v1/restaurants/`: List all restaurants or create a new restaurant
- `api/v1/restaurants/<int:pk>/`: Retrieve, update, or delete a specific restaurant by its primary key (id)
# Menus(You need to log in to use it):
- `api/v1/restaurants/menus/`: List all menus or create a new menu
- `api/v1/restaurants/menus/<int:pk>/`: Retrieve, update, or delete a specific menu by its primary key (id)
- `api/v1/restaurants/current-day-menu/`: Retrieve the menu for the current day
- `api/v1/restaurants/voting-results/`: Retrieve the voting results


## Testing:
Run tests with: `docker-compose run web pytest`

All tests are currently written for version v1 of the API.
