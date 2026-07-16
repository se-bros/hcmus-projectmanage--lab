# Digitization samples

`one-page.png` and `two-page.pdf` are generated assets with original test text, so they can be
used without copyright concerns. Regenerate both files from the repository root with:

```bash
cd src/backend
uv run python ../../samples/generate_samples.py
```

The PDF intentionally contains two pages. It is suitable for checking OCR page numbering, preview
storage, and EPUB content order.
