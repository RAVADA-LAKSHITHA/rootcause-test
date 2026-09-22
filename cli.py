import typer
import requests

app = typer.Typer(no_args_is_help=True)

@app.command()
def deploy(repo: str = typer.Option(..., help="GitHub repo, e.g. RAVADA-LAKSHITHA/rootcause-test")):
    """Trigger a deploy for the given repo."""
    typer.echo(f"Triggering deploy for {repo}...")
    # For now this just pings your own local server as a placeholder.
    # Later this will call Founder 1's real deploy endpoint.
    try:
        resp = requests.get("http://localhost:8000/health")
        typer.echo(f"Backend status: {resp.json()}")
    except Exception as e:
        typer.echo(f"Could not reach backend: {e}")

@app.command()
def status():
    """Check backend status."""
    typer.echo("Status check not implemented yet.")

if __name__ == "__main__":
    app()