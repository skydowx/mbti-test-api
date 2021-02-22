# MBTI test API

## TODO
- configure following dockerized services:
    - postgres
    - mongodb
- Also setup the following for the project:
    - pylint
    - pydantic
    - pytest

## Steps to run

1. Download [BERT base model](https://drive.google.com/file/d/1RZfRdgFt2llPRWqXHwNiYej8BgZJHInf/view?usp=sharing) and move it in `mbti-test-api/backend/personality_analysis/app/utils/model_weights`

2. Run the following commands:
```
# Navigate in the project directory
cd mbti-test-api

# Create a virtualenv
python -m virtualenv mbti-api-env

# Activate
source mbti-api-env/bin/activate

# Install dependencies
pip install -r backend/personality_analysis/requirements.txt

# Navigate into the relevant directory
cd backend/personality_analysis/app

# Run the uvicorn server
uvicorn routes:app

```
## Model Credits
- [Social BERTerfly](https://github.com/MLH-Fellowship/Social-BERTerfly)
