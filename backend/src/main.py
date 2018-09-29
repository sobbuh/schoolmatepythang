# coding=utf-8

from .entities.entity import Session, engine, Base
from .entities.survey import Survey

# generate database schema
Base.metadata.create_all(engine)

# start session
session = Session()

# check for existing data
surveys = session.query(Survey).all()

if len(surveys) == 0:
    # create and persist dummy exam
    python_survey = Survey("Communication", "Review Your Communication This Sprint", "script")
    session.add(python_survey)
    session.commit()
    session.close()

    # reload surveys
    surveys = session.query(Survey).all()

# show existing surveys
print('### Surveys:')
for survey in surveys:
    print(f'({survey.id}) {survey.title} - {survey.description}')
