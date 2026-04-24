# Invoice Extractor 

# Setup Instructions
1. Ensure that you are in `~/.../anchorAlliedDemo/backend` directory.
2. Install `uv` if not done already
3. Run `uv sync`
4. Activate the virtual environment using `.venv/bin/activate`
5. Duplicate the terminal
6. In the backend directory, create a file named `.env`
7. Add values for `OLLAMA_API_ENDPOINT`, `GROQ_API_KEY`, `GSHEET_WEBHOOK_URL` and `FIREWORKS_AI_API_KEY`
8. Note: To get the GSHEET WEBHOOK URL, go to the excel sheet > Extensions > App Script > Deploy > Manage Deployments > Web app URL. In case this URL does not work, create a new deployment and use that url.
9. Next, run `uvicorn app:app --reload`
10. In the other terminal, navigate `cd frontend`
11. Create a new file in frontend `.env.development` and `.env.production`, and put the respective server URLs.
12. There, run `npm i` followed by `npm run dev`