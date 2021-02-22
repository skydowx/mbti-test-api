# MBTI test API

## TODO
- configure following dockerized services:
    - postgres
    - mongodb
- Also setup the following for the project:
    - pylint
    - pydantic
    - pytest

## Dependencies
- docker
- docker-compose

## Steps to run

1. Download [BERT base model](https://drive.google.com/file/d/1RZfRdgFt2llPRWqXHwNiYej8BgZJHInf/view?usp=sharing) and move it in `mbti-test-api/backend/personality_analysis/app/utils/model_weights`

2. Run the following commands:
```
cd mbti-test-api
docker-compose up
```
## Model Credits
- [Social BERTerfly](https://github.com/MLH-Fellowship/Social-BERTerfly)
