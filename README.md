# Meal-Planner

Meal Planner is an application that will create a customized meal plan for you.

## Installation

In your terminal, move to a directory you want the Meal Planner to be installed in. And execute the following commands:
```
git clone https://github.com/Pascal151/Meal-Planner.git && cd meal_planner
```

### Installing the virtual environment
You can install the virtual environment via poetry. If you haven't installed it yet do the following steps in your console:
```
pip install poetry
```
Then execute the following commands:
```
poetry config virtualenvs.in-project true &&
poetry install
```

## Running the Meal Planner App
To run the app simply type
```
poetry run python main.py
```
into your terminal.

### Running the Meal Planner App via Docker
First you need to create a docker image:
```
docker build -t meal_planner_image .
```
When this was sucessful , make sure to run the docker image in interactive mode like this:
```
docker run -it meal_planner_image
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

MIT
