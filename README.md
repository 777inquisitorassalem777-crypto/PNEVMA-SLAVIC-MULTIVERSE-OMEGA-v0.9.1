# PNEVMA–SLAVIC MULTIVERSE Ω v0.9.1

Research platform integrating:

- **Slavic Semantic Core** — dual-level analysis of sacred lexicon (волхв, ведун, …)
- **Many-Worlds Engine** — hypothesis branching, superposition, collapse (Everett-inspired model)
- **Synchronicity Detector** — meaningful resonance & archetypes (Jung/Pauli-inspired model)
- **PNEVMA Core** — multi-agent reasoning, reflective continuity, safety, provenance ledger

```
ВЕДУН → ВОЛХВ → ВЕЩУН → ХАРАКТЕРНИК
         ↕
   Many-Worlds + Synchronicity
         ↕
 Reflective Continuity · Safety · Ledger
```

## Research framing

This project studies reflective continuity of lexical knowledge, multi-perspective
semantic reasoning, and provenance-tracked hypotheses under uncertainty.

**It does not claim:**
- physical parallel universes
- consciousness or spiritual animation of the software
- operational ability to locate or return the soul of a deceased person

Terms such as “soul”, “spirit”, “archetype”, “numinous” are research metaphors
or historical-linguistic objects only.

## Quick start

```bash
# Full demo (Many-Worlds + Synchronicity + Slavic analysis)
python pnevma_multiverse.py

# Analyze a lexeme
python pnevma_multiverse.py "волхв"
python pnevma_multiverse.py "ведун"
python pnevma_multiverse.py "характерник"

# List lexemes
python pnevma_multiverse.py --lexemes

# Legacy CLI (agents only)
python slavic_cognitive_agent.py --demo

# API
make api          # http://localhost:8000/docs
```

No external dependencies beyond the Python standard library for `pnevma_multiverse.py`.

For the modular stack (FastAPI, NetworkX):

```bash
pip install -r requirements.txt
```

## Structure

```
pnevma_slavic_core/
├── pnevma_multiverse.py       # ★ Single-script full integration (v0.9.1)
├── slavic_cognitive_agent.py  # CLI orchestrator (v0.2)
├── app/
│   ├── agents/                # Vedun, Volkhv, Veshchun, Kharakternik
│   ├── graph/                 # NetworkX Knowledge Graph
│   └── api/                   # FastAPI
├── data/lexemes.json
├── docs/
│   └── SYMBIOSIS.md           # Boundaries & roadmap
├── tests/
├── docker-compose.yml
├── Dockerfile
├── Makefile
└── requirements.txt
```

## Seed lexemes

| Lexeme       | Period            | Principle                         |
|--------------|-------------------|-----------------------------------|
| волхв        | early             | special word + ritual             |
| ведун        | early             | SEE → KNOW                        |
| вещун        | early–middle      | knowledge → proclamation          |
| знахарь      | middle            | practical knowledge               |
| бая          | archaic           | word as action                    |
| характерник  | late (15–16th c.) | character → will → action         |

## Safety invariants

1. Safety before autonomy  
2. Provenance before optimisation  
3. Reflection before self-modification  
4. Bounded experimentation  
5. Human oversight remains final authority  
6. Spiritual terminology = metaphor or historical data only  

## License

MIT (see project history). Research use.
