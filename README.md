* **Author**: Jayesh Sidhwani

99movies is a small project to learn Flask and AngularJS

###Requirements

Requirements are listed in the requirements.txt

###Installation

* Checkout the Github repo
* Install virtualenv
* Install requirements
* Start API server: python api/manage.py
* Start APP server: python app/manage.py
* API runs at localhost:5000 and APP runs at localhost:80


####Usage

##### Movies:
_URL `/`_
```
Lists all the movies. Depending on the authentication; you can edit or delete the movie.
```
---
##### Search API:
_This API is used to do a generic text search._
```python

from lemur.api.search import Search
Search(core).do(**kwargs)

sort_by:        [Default:['sub_category', 'attr_primary_color']] Fields that used for sorting the search results
order:          [Default="asc"] Defines the sorting order. "asc" / "desc"
query:          The search query.
raw:            [Default=False] Pass True if you want the raw search result. If raw is False, all the attributes are
                structures into a Features sub-array
post_process:   [Default=True] Pass False if you don't want to post-process the query results.
                Post process organises the search results into parent and children.
options:        Options query are structured queries that don't pass through NLP processing. It's a dictionary and it's
                required that the values have appropriate keys that are fields in Solr schema. For example,
                {'has_rack': True, 'gender': 'men', 'category': 'Shirts'}. These arguments are passed as-is to Solr
fields:         [Default: settings.PRODUCT_CHILD_FIELD_NAMES] Add more fields if needed. The new fields extend the default
facets:         [Default: settings.FACETS] Add more facets if needed. The new facets extend the default
```
---