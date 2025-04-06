# playwright_core_e2e_visual_test_automation

End to end and visual test automation suite for Coupang core pc_web and mobile_web by using Python, Pytest and Playwright


## Getting Sgtarted

### Requirements

* python
* pytest
* pytest-playwright
* pytest-playwright-visual
* pytest-xdist
* playwright
* dotenv
* python-dotenv


### Installtion

1. Install Python
2. Clone/download this repositiry to your local machine
3. Create a python virtual environment in the copied folder and activate it.
4. Install required librarys
5. Create .env file under the root folder with a set of coupang accounts and password that will be used in the scripts
```
CORE_REAL_USER_PASSWORD = 'xxxxxxx'
CORE_REAL_USEr_EMAIL = 'xxxxxx@xxxxxx.xxx'

CORE_TEST_USER_PASSWORD = "xxxxxxx"
CORE_TEST_USER_PAID = "xxxxxxx@cp.com"
CORE_TEST_USER_PAID_2 = "xxxxxxxx@cp.com"
CORE_TEST_USER_NOT_MEMBER = "xxxxxxxx@cp.com"
CORE_TEST_USER_WITHDRAWN = "xxxxxxxx@cp.com"
CORE_TEST_USER_ON_HOLD = "xxxxxxxx@cp.com"
```


### Test Execution
Execute test script(s) to make a base of visual test (i.e, create/update screenshots for visual test)
```
>>pytest {folder_path} --update-sanpshots
>>pytest tests/TEST_VISUAL --update-snapshots
>>pytest tests/TEST_E2E/web/{file_name}.py --update-snapshots
>>pytest tests/TEST_E2E/web/{file_name}.py::{function_name} --update-snapshots
```


Execute test scrip(s) in a certain folder
```
>>pytest {folder_path}
>>pytest tests/TEST_VISUAL
>>pytest tests/TEST_E2E/web
```


Execute test script(s) by marker(s)
```
# single marker
>>pytest {folder_path} -m {marker}
>>pytest -m loyalty
>>pytest -m functional_test
>>pytest tests/TEST_VISUAL -m loyalty

# multiple markers
>>pytest {folder_path} -m "{marker #1} and {marker #2} and ..."
>>pytest tests/TEST_VISUAL -m "loyalty and regression test"
>>pytest -m "loyalty and regression_test and visual_test"
```

## Help

