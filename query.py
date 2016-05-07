"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.

# print Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

# print Model.query.filter_by(name='Corvette', brand_name='Chevrolet').all()

# Get all models that are older than 1960.

# print Model.query.filter(Model.year > 1960).all()

# Get all brands that were founded after 1920.

# print Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".

# print Model.query.filter(Model.name.like("Cor%")).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.

# print Brand.query.filter(Brand.founded == 1903, Brand.discontinued.is_(None)).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded 
# before 1950.

# print Brand.query.filter((Brand.founded < 1950) | (Brand.discontinued.isnot(None))).all()

# Get any model whose brand_name is not Chevrolet.

# print Model.query.filter(Model.brand_name != "Chevrolet").all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    # Bind the variable cars to a list of Model objects
    cars = Model.query.filter(Model.year == year).all()

    for car in cars:

        print "Model: {}, Brand: {}, Headquarters: {}".format(car.name,
                                                              car.brand_name,
                                                              car.brand.headquarters)
        print "\n"


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brands = db.session.query(Brand).group_by(Brand.name, Brand.id).all()

    for brand in brands:

        models = brand.models
        print "Brand: {}".format(brand.name)
        print "-------------------"

        for model in models:
            print "Model: {}".format(model.name)


# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
     
    # The returned value of this query is: <Brand brand_id=1 name=Ford founded=1903 headquarters=Dearborn, MI discontinued=None>.
    # The datatype is an object of the Brand class. 
    
# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

    # An association table is an intermediary table that manages the relationship between two tables.
    # It only stores the primary keys of these two tables as foreign keys.

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    """Return a list of Brand objects that contain or equal string input."""

    return Brand.query.filter(Brand.name.like('%{}%'.format(mystr))).all()


def get_models_between(start_year, end_year):
    """Return a list of Model objects between and including the start year but excluding the end year."""

    return Model.query.filter((start_year <= Model.year), (end_year > Model.year)).all()


