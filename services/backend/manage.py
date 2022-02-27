import click

from app.config import get_settings
from app.crud import (create_user, get_user_by_username, promote_user,
                      upgrade_user_to_premium)
from app.dependencies import get_db
from app.schemas import UserCreate

settings = get_settings()


@click.group()
def cli():
    pass


@cli.command("create-superuser")
def create_superuser():
    if settings.SUPERUSER == "" or settings.SUPERUSER_PASS == "":
        click.echo(
            click.style(
                "Unable to create superuser. Please make sure SUPERUSER and SUPERUSER_PASS are populated in your environment variables!",
                fg="red",
                bold=True,
            )
        )
        return

    db = next(get_db())
    user_obj = UserCreate(username=settings.SUPERUSER, password=settings.SUPERUSER_PASS)
    user = get_user_by_username(db, user_obj.username)
    if user is None:
        user = create_user(db, user_obj)
        promote_user(db, user.id)
        upgrade_user_to_premium(db, user.id)
        click.echo(click.style("Superuser created!", fg="green", bold=True))
        return
    click.echo(click.style("Superuser already exists!", fg="yellow", bold=True))


@cli.command("seed-db")
def seed_database():
    click.echo(click.style("Adding templates...", fg="yellow", bold=True))
    with open("./templates_seed/sample1.html", "r") as f:
        content = f.readall()
    
    click.echo("Hello")


if __name__ == "__main__":
    cli()
