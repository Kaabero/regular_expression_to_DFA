from invoke import task

@task
def start(ctx):
    ctx.run("uvicorn main:app --reload --host 127.0.0.1 --port 3000")

@task
def test(ctx):
    ctx.run("python -m pytest src")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")
    ctx.run("coverage report -m")
    ctx.run("coverage html")

@task
def lint(ctx):
    ctx.run("pylint src")