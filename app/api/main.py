"""FastAPI слой для PNEVMA–SLAVIC SEMANTIC CORE Ω"""

from __future__ import annotations
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from app.agents.orchestrator import SlavicCognitiveAgent

app = FastAPI(
    title="PNEVMA–SLAVIC SEMANTIC CORE Ω",
    description="Когнитивный API: Vedun → Volkhv → Veshchun → Kharakternik",
    version="0.2.0",
)

agent = SlavicCognitiveAgent()


class QueryRequest(BaseModel):
    query: str


@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <html>
    <head><title>PNEVMA–SLAVIC SEMANTIC CORE Ω</title>
    <style>
      body { font-family: system-ui; max-width: 800px; margin: 2rem auto; padding: 0 1rem; }
      h1 { color: #1a1a2e; }
      code { background: #f0f0f0; padding: 2px 6px; border-radius: 4px; }
      a { color: #16213e; }
    </style>
    </head>
    <body>
      <h1>PNEVMA–SLAVIC SEMANTIC CORE Ω</h1>
      <p>Когнитивная архитектура на основе праславянской семантики.</p>
      <ul>
        <li><a href="/docs">Swagger UI</a></li>
        <li><code>GET /lexemes</code> — список лексем</li>
        <li><code>GET /analyze/{word}</code> — разбор слова</li>
        <li><code>GET /graph</code> — семантический граф</li>
      </ul>
      <p>CLI: <code>python slavic_cognitive_agent.py "волхв"</code></p>
    </body>
    </html>
    """


@app.get("/lexemes")
def list_lexemes():
    return {"lexemes": agent.vedun.list_lexemes()}


@app.get("/analyze/{word}")
def analyze_word(word: str):
    result = agent.analyze(word)
    if not result["found"]:
        raise HTTPException(status_code=404, detail=result.get("message"))
    return result


@app.post("/analyze")
def analyze_post(req: QueryRequest):
    return agent.analyze(req.query)


@app.get("/graph")
def get_graph():
    return agent.graph.to_dict()
