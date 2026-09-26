.PHONY: demo interactive lexemes graph api test docker-up docker-down install

install:
	pip install -r requirements.txt

demo:
	python slavic_cognitive_agent.py --demo

interactive:
	python slavic_cognitive_agent.py --interactive

lexemes:
	python slavic_cognitive_agent.py --lexemes

graph:
	python slavic_cognitive_agent.py --graph

api:
	uvicorn app.api.main:app --reload --host 0.0.0.0 --port 8000

test:
	python -m pytest tests/ -v

docker-up:
	docker compose up --build -d

docker-down:
	docker compose down
