# Explainer kit

Shared code for the Storylines explainers (`outputs/explainer-*`).

Each explainer folder holds `content.py`, which pairs every piece of on-page text with its source article and the passage that supports it. To rebuild one:

```
python3 outputs/explainer-kit/build.py outputs/explainer-press-ban
```

This writes `index.html` (self-contained, works offline) and `manifest.md` into the folder. The build stops with an error if any quote or figure on the page can't be found in the article it is credited to, or if the page's own text uses an em dash.

- `build.py`: loads the Storyline and fetched sources, runs the checks, renders the page and the manifest.
- `explainer.css`: the shared look. Each explainer sets its own colours in `THEME` and `THEME_DARK`.
- `explainer.js`: shared script (currently empty; page scripts live in each `content.py`).
