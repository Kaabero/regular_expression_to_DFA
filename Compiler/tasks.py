from invoke import task

@task
def start(ctx):
    ctx.run("uvicorn main:app --reload")

@task
def test(ctx):
    ctx.run("pytest src")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")
    ctx.run("coverage report -m")
    ctx.run("coverage html")

@task
def lint(ctx):
    ctx.run("pylint src")