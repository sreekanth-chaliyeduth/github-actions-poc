install:
	pip install -r requirements.txt
	playwright install

test:
	pytest --alluredir=reports/allure-results

report:
	allure serve reports/allure-results

clean:
	rm -rf reports .pytest_cache
