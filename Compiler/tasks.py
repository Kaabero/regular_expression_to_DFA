from invoke import task

@task
def start(c):
    c.run("uvicorn main:app --reload")