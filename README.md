# Invoice Extractor 

# Setup Instructions
1. Ensure that you are in `~/.../anchorAlliedDemo/` directory.
2. Install `uv` if not done already
3. Run `uv sync`
4. Activate the virtual environment using `.venv/bin/activate`
5. Duplicate the terminal
6. In one terminal, navigate `cd backend`
7. In the backend directory, create a file named `.env`
8. Add values for `OLLAMA_API_ENDPOINT`, `GROQ_API_KEY` and `GSHEET_WEBHOOK_URL`
9. Next, run `uvicorn app:app --reload`
8. In the other terminal, navigate `cd frontend`
9. There, run `npm i` followed by `npm run dev`