from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from workcontacts import manager
from workcontacts.manager import ContactManager
from workcontacts.models.contact import Contact
from rich.table import Table
from workcontacts.storage import save_contacts, load_contacts, backup_contacts, restore_backup
from workcontacts.export import (
    export_contacts_to_csv,
    import_contacts_from_csv
)

console = Console()


def start():
    welcome_panel = Panel(
        "[bold green]Welcome to WorkContacts![/bold green]\n"
        "Your personal contact management system",
        title="WorkContacts",
        border_style="blue"
    )

    console.print(welcome_panel)
def show_menu():
    console.print("\n[bold cyan]Main Menu[/bold cyan]")
    console.print("1. Add contact")
    console.print("2. List contacts")
    console.print("3. Search contact")
    console.print("4. Update contact")
    console.print("5. Delete contact")
    console.print("6. Exit")
    console.print("7. Create backup")
    console.print("8. Restore backup")
    console.print("9. Filter contacts by category")
    console.print("10. Contact statistics")
    console.print("11. Export contacts to CSV")
    console.print("12. Import contacts from CSV")
    choice = Prompt.ask(
        "\n[bold yellow]Select an option[/bold yellow]",
        choices=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    )

    return choice
def handle_choice(choice, manager):
    if choice == "1":
        first_name = Prompt.ask("First name")
        last_name = Prompt.ask("Last name")
        email = Prompt.ask("Email")
        phone = Prompt.ask("Phone (optional)")
        contact = Contact(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone or None
        )

        try:
            manager.add_contact(contact)
            save_contacts(manager.contacts, "contacts.json")
            
            console.print(f"DEBUG: Total contacts: {len(manager.contacts)}")
            console.print("[bold green]Contact added successfully![/bold green]")
        except ValueError as error:
            console.print(f"[bold red]Error: {error}[/bold red]")
            

   
    elif choice == "2":
        if not manager.contacts:
            console.print("[yellow]No contacts found.[/yellow]")
        else:
            table = Table(title="Contact List")

            table.add_column("First Name", style="cyan")
            table.add_column("Last Name", style="green")
            table.add_column("Email", style="yellow")
            table.add_column("Phone", style="magenta")
            table.add_column("Category", style="blue")
            table.add_column("Notes", style="white")

            for contact in sorted(manager.contacts, key=lambda contact: contact.last_name.lower()):
                table.add_row(
                    contact.first_name,
                    contact.last_name,
                    contact.email,
                    contact.phone or "-",
                    contact.category,
                    contact.notes or "-"
                )

            console.print(table)


    elif choice == "3":
        email = Prompt.ask("Enter the email to search")

        contact = manager.find_by_email(email)

        if contact is None:
            console.print("[yellow]Contact not found.[/yellow]")
        else:
            console.print("[bold green]Contact found![/bold green]")
            console.print(f"Name: {contact.first_name} {contact.last_name}")
            console.print(f"Email: {contact.email}")
            console.print(f"Phone: {contact.phone or 'Not provided'}")

    
    elif choice == "4":
        email = Prompt.ask("Enter the email of the contact to update")

        contact = manager.find_by_email(email)

        if contact is None:
            console.print("[yellow]Contact not found.[/yellow]")
        else:
            console.print("[green]Contact found. Enter new details.[/green]")

            first_name = Prompt.ask("New first name", default=contact.first_name)
            last_name = Prompt.ask("New last name", default=contact.last_name)
            new_email = Prompt.ask("New email", default=contact.email)
            phone = Prompt.ask("New phone", default=contact.phone or "")

            try:
                manager.update_contact(
                    email,
                    first_name=first_name,
                    last_name=last_name,
                    email=new_email,
                    phone=phone or None
                )

                save_contacts(manager.contacts, "contacts.json")

                console.print("[bold green]Contact updated successfully![/bold green]")

            except ValueError as error:
                console.print(f"[bold red]Error: {error}[/bold red]")

    elif choice == "5":
        email = Prompt.ask("Enter the email of the contact to delete")

        contact = manager.find_by_email(email)

        if contact is None:
            console.print("[yellow]Contact not found.[/yellow]")
        else:
            confirm = Prompt.ask(
                f"Delete {contact.first_name} {contact.last_name}?",
                choices=["y", "n"],
                default="n"
            )

            if confirm == "y":
                manager.delete_by_email(email)
                save_contacts(manager.contacts, "contacts.json")
                console.print("[bold green]Contact deleted successfully![/bold green]")
            else:
                console.print("[yellow]Deletion cancelled.[/yellow]")

    elif choice == "6":
        console.print("[yellow]Goodbye![/yellow]")

    elif choice == "7":
        backup_contacts(manager.contacts)
        console.print(
            "[bold green]Backup created successfully![/bold green]"
        )

    elif choice == "8":
        confirm = Prompt.ask(
            "This will replace your current contacts. Continue?",
            choices=["y", "n"],
            default="n"
        )

        if confirm == "y":
            restored_contacts = restore_backup()

            if not restored_contacts:
                console.print(
                    "[bold red]Backup is empty or does not exist. "
                    "Restoration cancelled.[/bold red]"
                )
            else:
                manager.contacts = restored_contacts
                save_contacts(manager.contacts, "contacts.json")

                console.print(
                    "[bold green]Backup restored successfully![/bold green]"
                )
        else:
            console.print("[yellow]Restoration cancelled.[/yellow]")

    elif choice == "9":
        category = Prompt.ask(
            "Enter category to filter (personal/work)"
        ).lower()

        filtered_contacts = manager.filter_by_category(category)
        if not filtered_contacts:
            console.print("[yellow]No contacts found in this category.[/yellow]")
        else:
            table = Table(title=f"Contacts - {category}")

            table.add_column("First Name", style="cyan")
            table.add_column("Last Name", style="green")
            table.add_column("Email", style="yellow")
            table.add_column("Phone", style="magenta")
            table.add_column("Category", style="blue")
            table.add_column("Notes", style="white")

            for contact in sorted(filtered_contacts, key=lambda contact: contact.last_name.lower()):
                table.add_row(
                    contact.first_name,
                    contact.last_name,
                    contact.email,
                    contact.phone or "-",
                    contact.category,
                    contact.notes or "-"
                )

            console.print(table)

    elif choice == "10":
        stats = manager.get_statistics()

        table = Table(title="Contact Statistics")

        table.add_column("Statistic", style="cyan")
        table.add_column("Count", style="green")

        table.add_row("Total contacts", str(stats["total"]))
        table.add_row("Personal contacts", str(stats["personal"]))
        table.add_row("Work contacts", str(stats["work"]))
        table.add_row("Contacts without phone", str(stats["without_phone"]))

        console.print(table)

    elif choice == "11":
        if not manager.contacts:
            console.print("[yellow]No contacts to export.[/yellow]")
        else:
            export_contacts_to_csv(manager.contacts)
            console.print(
                "[bold green]Contacts exported successfully to contacts.csv![/bold green]"
            )

    elif choice == "12":
        try:
            imported_contacts, invalid_count = import_contacts_from_csv()
            added = 0
            skipped = 0

            for contact in imported_contacts:
                try:
                    manager.add_contact(contact)
                    added += 1
                except ValueError:
                    skipped += 1

            save_contacts(manager.contacts, "contacts.json")

            console.print(
                f"[bold green]Imported {added} contacts successfully![/bold green]"
            )

            if skipped:
                console.print(
                    f"[yellow]Skipped {skipped} duplicate contacts.[/yellow]"
                )
                if invalid_count:
                    console.print(
                        f"[red]Skipped {invalid_count} invalid contacts.[/red]"
                    )

        except FileNotFoundError:
            console.print("[bold red]CSV file not found.[/bold red]")




def run():
    manager = ContactManager()
    manager.contacts = load_contacts("contacts.json")

    start()

    while True:
        choice = show_menu()
        handle_choice(choice, manager)

        if choice == "6":
            break


def main():
    run()
