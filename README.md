# Django REST Framework Transaction

**Transaction APP for Django REST Framework with API Views.**<br>

`DRF Transaction` is a Django App that can for collecting feedback from end user. It's view are based upon
`Django REST Framework's GenericAPIView` and hence it contains a RESTful API views also.


I'll like to mention following names for certain contributions:

- **[Civil Machines Technologies Private Limited](https://github.com/civilmahines)**: For providing me platform and 
funds for research work. This project is hosted currently with `CMT` only. 
- [Himanshu Shankar](https://github.com/iamhssingh): For guiding me and providing me mentorship while doing this
project.
- [Aditya Gupta](https://github.com/ag93999): For updating this repository and projects using this repository as per
the latest standards and making this repository into a library. At the time of this commit, he is an intern with CMT
and is assigned with the task of building this app and making this as a Python Package hosted on PyPi.

#### Installation

- Download and Install via `pip`
```
pip install drf_transaction
```
or<br>
Download and Install via `easy_install`
```
easy_install drf_transaction
```
- Add `drf_transaction` in `INSTALLED_APPS`<br>
```
INSTALLED_APPS = [
    ...
    'drf_transaction',
    ...
]
```
- Include urls of `drf_transaction` in `urls.py`
```
urlpatterns = [
    ...
    path('transaction/', include('drf_transaction.urls')),
    ...
]

# or

urlpatterns = [
    ...
    url(r'transaction/', include('drf_transaction.urls')),
    ...
]
```

- Finally, run `migrate` command
```
python manage.py migrate drf_transaction
```
