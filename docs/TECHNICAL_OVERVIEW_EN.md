# TEP Fault Assistant: Technical Overview

The [Chinese implementation and interview guide](TECHNICAL_GUIDE_ZH.md) covers the full code walkthrough, worked examples, 28 interview questions, and hands-on exercises. This English overview is intended for repository visitors.

## What the application does

The interface follows one workflow: **understand the process, check domain facts, then inspect a fault case**.

| Feature | Implementation | Output |
| --- | --- | --- |
| Process overview | Hand-authored SVG, CSS animation, and browser interaction | Five main units, material-flow connections, clickable explanations, and an eight-second teaching animation |
| Domain Q&A | Curated handbook, structural chunks, sparse retrieval with identifier/intent rules, and an online chat model | Answers with references to retrieved passages; clarification or refusal when evidence is insufficient |
| Root-cause exploration | Lagged time-series features, kernel ridge regression, error comparison, statistical filtering, and graph algorithms | Candidate variables, directed Granger-predictive relations, a matrix, and candidate paths |

The process animation and diagnosis calculation do not call the language model. The product uses “Agent” in its UI name, but the current implementation is a fixed workflow; the model does not autonomously call the diagnosis tool.

## Process overview

The page simplifies the Tennessee Eastman Process into a reactor, condenser, vapor–liquid separator, recycle compressor, and stripper. It also shows fresh feeds, recycle streams, purge, and product output. SVG paths and labels live in `process_layout.py`; explanations, animation timing, and interaction live in `process_diagram.py`.

Each highlighted pipe uses an animated SVG stroke. Pipe segments and unit highlights share an eight-second cycle. The playback stops when the graphic is outside the viewport or the page is hidden, and reduced-motion preferences are respected. The animation indicates teaching order and flow direction, not actual residence times or a numerical simulation.

## Knowledge Q&A and retrieval

`TEP_SOURCE_MAP.md` consolidates process structure, equipment, 11 major streams, X1–X52 variables, IDV(1)–IDV(21) fault definitions, dataset scope, and source corrections. `chunk_knowledge.py` splits this version into **110 structured passages**. A variable or fault stays in one passage with its definition, limits, and source metadata.

`retrieve_chunks.py` indexes passage titles, entities, and content with character-level TF-IDF using two- and three-character n-grams. This is a sparse lexical index, not a semantic embedding service or an external vector database. `query_rules.py` identifies entities such as X4 and IDV(7), recognizes common question intents, and prioritizes directly matching knowledge units before considering cosine similarity. The online path sends at most five retrieved passages to the configured chat model.

`followup_query.py` handles limited one-step follow-ups. For example, after “What is IDV(14)?”, “And 15?” can be rewritten as a question about IDV(15). Ambiguous references request clarification. The model sees the resolved question and selected references, not the entire browser conversation.

`qa.py` checks scope and evidence before calling the model, asks it to answer from the supplied passages, and validates that cited reference numbers exist. This numerical citation check does **not** prove that every sentence is supported. Faithfulness still requires review. The browser displays model text with `textContent` and makes the cited passages inspectable.

## Fault analysis

The demonstration loads the public IDV(7) test data and analyzes samples starting at the known fault onset, sample 161. The seven selected variables are X4, X7, X13, X16, X20, X45, and X46. The default window contains 100 samples and uses three historical samples as predictors.

For each target variable, the program trains a full RBF kernel-ridge predictor on all seven variables' histories. It then trains six restricted predictors, each omitting the entire history of one other source variable. A directed relation A → B is considered when including A's history improves held-out prediction of B. Training and testing respect time order; standardization uses training data only. With seven variables, one run fits **49 models** and examines **42 possible directed relations**.

The program compares absolute errors on a chronological test segment, applies a one-sided sign test to the per-sample direction of improvement, and adjusts the 42 p-values using Benjamini–Hochberg. It keeps relations with positive average improvement and adjusted `q < 0.10`. Because nearby time-series test points can be correlated, these significance values are exploratory rather than strict evidence of physical causation.

Candidate roots are selected with a simple graph heuristic: outgoing selected relations minus incoming selected relations. `diagnosis_graph.py` then builds the matrix, SVG graph, feedback groups, and simple candidate paths. Solid edges indicate a pair with only one selected direction; dashed edges indicate that both directions were selected for that pair. Clicking a path highlights the exact directed edges. Path order is an enumeration order, not a probability ranking.

The injected IDV(7) scenario is C-feed pressure loss. X4 measures mixed-feed flow and X45 is a related manipulated variable; neither is a direct pressure-loss measurement. A candidate variable or path is a lead for process interpretation, not a confirmed physical root cause. The prototype has not reproduced every method in the user's thesis or established accuracy across all 21 faults.

## Web application and deployment

The local application uses Python's `ThreadingHTTPServer`, HTML/CSS, and vanilla JavaScript. `POST /api/ask` runs retrieval and model generation; `POST /api/diagnose` computes the selected window and returns rendered results. The API key remains on the Python side, in a private local file or a server environment variable. The repo and the GitHub Pages output contain no model key.

The [GitHub Pages preview](https://corookie.github.io/tep-fault-agent/) serves the interactive process diagram and nine diagnosis parameter combinations precomputed by `export_pages.py`. Pages cannot run the Python backend. Online Q&A on the public domain therefore needs a separate Python host; see the [bilingual deployment guide](../DEPLOYMENT.md). Local mode continues to offer all three features.

As checked on 2026-09-29, the automated suite has **68 passing tests**. Existing retrieval reports are development regression results; they are not an independent answer-accuracy estimate. The project is a local research demonstration with a published static preview, not a validated production diagnosis service.
