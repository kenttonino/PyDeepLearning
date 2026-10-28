.PHONY: dep run

dep:
	pip install -r requirements.txt

run:
	# make run dataset=redwine
	clear
	python3 ./src/main.py --dataset $(dataset)
