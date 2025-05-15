# 🔖 Developed by ryo_sukuna_2004 | All rights reserved 🔒

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.table import Table
import os
import subprocess
import time

console = Console()
DOWNLOAD_HISTORY = []

DEVELOPER_SIGNATURE = "ryo_sukuna_2004"

def check_signature():
    if DEVELOPER_SIGNATURE != "ryo_sukuna_2004":
        console.print("[bold red]❌ Unauthorized modification detected![/bold red]")
        console.print("[yellow]Please credit the original developer: ryo_sukuna_2004[/yellow]")
        exit()

def show_instagram_support():
    console.print(Panel.fit(
        "[bold green]💖 Support the developer by following on Instagram![/bold green]\n"
        "📸 [cyan]@ryo_sukuna_2004[/cyan] — your support means a lot 🙏",
        title="📢 Spread the Love", subtitle="Follow & Share"))

def banner():
    console.clear()
    console.print(Panel.fit(
        "[bold cyan]🎵 Termux Media Downloader 🎥[/bold cyan]\n"
        "[green]By: [bold]ryo_sukuna_2004[/bold][/green]",
        title="🚀 Welcome", subtitle="Your all-in-one downloader"))
    show_instagram_support()

def choose_platform():
    console.print("\n[bold magenta]Choose a platform to download from:[/bold magenta]")
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("Option", justify="center")
    table.add_column("Platform", justify="left")
    table.add_row("1", "YouTube")
    table.add_row("2", "Facebook")
    table.add_row("3", "Instagram")
    table.add_row("4", "Spotify")
    table.add_row("5", "Change Download Folder")
    table.add_row("6", "Show Download History")
    table.add_row("7", "Clear Temporary Files")
    table.add_row("0", "Exit")
    console.print(table)

def get_output_folder():
    default_path = "/sdcard/Download/"
    folder = Prompt.ask("[yellow]Enter download path[/yellow]", default=default_path)
    if not os.path.exists(folder):
        os.makedirs(folder)
    return folder

def run_yt_dlp(url, output_path):
    console.print(f"[green]Downloading from:[/green] {url}")
    command = [
        "yt-dlp", "--extract-audio", "--audio-format", "mp3",
        "--embed-thumbnail", "--add-metadata",
        "-o", f"{output_path}/%(title)s.%(ext)s", url
    ]
    subprocess.run(command)

def run_spotdl(url, output_path):
    os.chdir(output_path)
    subprocess.run(["spotdl", url])

def clear_cache():
    console.print("[yellow]Cleaning up temporary files...[/yellow]")
    os.system("rm -rf ~/.cache/yt-dlp ~/.spotdl")
    console.print("[green]✔ Cache cleared successfully![/green]")

def download_history():
    console.print("[bold blue]📜 Download History:[/bold blue]")
    if not DOWNLOAD_HISTORY:
        console.print("[italic]No downloads yet.[/italic]")
    else:
        for entry in DOWNLOAD_HISTORY:
            console.print(f"• {entry}")

def main():
    check_signature()
    output_path = "/sdcard/Download/"
    while True:
        banner()
        choose_platform()
        choice = Prompt.ask("[bold cyan]Enter your choice[/bold cyan]")

        if choice == "1":
            url = Prompt.ask("Paste the YouTube link")
            run_yt_dlp(url, output_path)
            DOWNLOAD_HISTORY.append(f"YouTube: {url}")
        elif choice == "2":
            url = Prompt.ask("Paste the Facebook video link")
            run_yt_dlp(url, output_path)
            DOWNLOAD_HISTORY.append(f"Facebook: {url}")
        elif choice == "3":
            url = Prompt.ask("Paste the Instagram video/reel link")
            run_yt_dlp(url, output_path)
            DOWNLOAD_HISTORY.append(f"Instagram: {url}")
        elif choice == "4":
            url = Prompt.ask("Paste the Spotify song/playlist link")
            run_spotdl(url, output_path)
            DOWNLOAD_HISTORY.append(f"Spotify: {url}")
        elif choice == "5":
            output_path = get_output_folder()
        elif choice == "6":
            download_history()
            Prompt.ask("\nPress enter to return to the menu")
        elif choice == "7":
            clear_cache()
            time.sleep(1)
        elif choice == "0":
            console.print("[bold red]Exiting... Bye![/bold red]")
            break
        else:
            console.print("[red]Invalid option![/red]")
        again = Confirm.ask("\n[bold magenta]Do you want to download another file?[/bold magenta]")
        if not again:
            console.print("[bold green]Thanks for using the downloader![/bold green]")
            break

if __name__ == "__main__":
    main()
