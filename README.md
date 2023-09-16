# Lunch Decision Backend

## Setup:
1. Build the Docker image: `docker-compose build`
2. Run the Docker container: `docker-compose up`
3. Access the API at `http://localhost:8000/`
4. You can use `http://localhost:8000/swagger/` to look at the documentation

## API Endpoints:

# Authentication:
- `auth/register/`: User registration
- `auth/login/`: User login
- `auth/token-auth/`: Obtain JWT token pair (access and refresh tokens)
- `auth/token-refresh/`: Refresh the JWT token
- `auth/token-verify/`: Verify the JWT token
# Employees(You need to log in to use it):
- `employees/`: List all employees or create a new employee
- `employees/`<int:pk>/: Retrieve, update, or delete a specific employee by its primary key (id)
- `employees/vote/`: Create a vote
# Restaurants(You need to log in to use it):
- `restaurants/`: List all restaurants or create a new restaurant
- `restaurants/<int:pk>/`: Retrieve, update, or delete a specific restaurant by its primary key (id)
# Menus(You need to log in to use it):
- `restaurants/menus/`: List all menus or create a new menu
- `restaurants/menus/<int:pk>/`: Retrieve, update, or delete a specific menu by its primary key (id)
- `restaurants/current-day-menu/`: Retrieve the menu for the current day
- `restaurants/voting-results/`: Retrieve the voting results


## Testing:
Run tests with: `docker-compose run web pytest`

