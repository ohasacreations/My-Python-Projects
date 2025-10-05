import os
import time
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

# Initialize Rich Console for beautiful output
console = Console()

# --- Global State ---
balance = 1000.0

# --- Helper Functions ---
def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_goodbye():
    """Displays a stylized goodbye message."""
    clear_screen()
    console.print(Panel(
        Text("Thank you for using our ATM!\nHave a great day.", justify="center", style="bold magenta"),
        title="[bold green]Goodbye![/bold green]",
        border_style="green"
    ))
    time.sleep(2)
    clear_screen()

# --- Core ATM Functions ---
def display_menu():
    """Displays the main ATM menu in a formatted panel."""
    menu_text = Text(justify="left")
    menu_text.append("1. Check Balance\n", style="bold cyan")
    menu_text.append("2. Deposit Money\n", style="bold green")
    menu_text.append("3. Withdraw Money\n", style="bold yellow")
    menu_text.append("4. Exit\n", style="bold red")

    console.print(Panel(
        menu_text,
        title="[bold blue]ATM MENU[/bold blue]",
        subtitle="[default]Select an option[/default]",
        border_style="blue",
        padding=(1, 2)
    ))

def check_balance():
    """Displays the current account balance."""
    clear_screen()
    balance_text = Text(f"Your current balance is: ", style="white")
    balance_text.append(f"₹{balance:,.2f}", style="bold green")
    
    console.print(Panel(
        balance_text,
        title="[bold cyan]Balance Inquiry[/bold cyan]",
        border_style="cyan",
        padding=1
    ))
    input("\nPress Enter to continue...")

def deposit_money():
    """Handles the deposit logic."""
    clear_screen()
    console.print(Panel("[bold yellow]Enter amount to deposit:[/bold yellow]", border_style="yellow"))
    try:
        amount_str = console.input("[bold green]>[/bold green] ")
        d_amount = float(amount_str)

        if d_amount <= 0:
            console.print(Panel("❌ [bold red]Deposit amount must be positive.[/bold red]"))
        else:
            global balance
            balance += d_amount
            success_text = Text("✅ Deposit Successful!\n", style="white")
            success_text.append("New Balance: ", style="white")
            success_text.append(f"₹{balance:,.2f}", style="bold green")
            console.print(Panel(success_text, title="[bold green]Success[/bold green]", border_style="green"))
            
    except ValueError:
        console.print(Panel("❌ [bold red]Invalid input. Please enter a numeric value.[/bold red]"))
    
    input("\nPress Enter to continue...")

def withdraw_money():
    """Handles the withdrawal logic."""
    clear_screen()
    console.print(Panel("[bold yellow]Enter amount to withdraw:[/bold yellow]", border_style="yellow"))
    try:
        amount_str = console.input("[bold red]>[/bold red] ")
        w_amount = float(amount_str)

        if w_amount <= 0:
            console.print(Panel("❌ [bold red]Withdrawal amount must be positive.[/bold red]"))
        elif w_amount > balance:
            console.print(Panel("❌ [bold red]Insufficient funds! Cannot complete withdrawal.[/bold red]"))
        else:
            global balance
            balance -= w_amount
            success_text = Text("✅ Withdrawal Successful!\n", style="white")
            success_text.append("New Balance: ", style="white")
            success_text.append(f"₹{balance:,.2f}", style="bold green")
            console.print(Panel(success_text, title="[bold green]Success[/bold green]", border_style="green"))

    except ValueError:
        console.print(Panel("❌ [bold red]Invalid input. Please enter a numeric value.[/bold red]"))
    
    input("\nPress Enter to continue...")


# --- Main Application Loop ---
def main():
    """The main function to run the ATM application."""
    while True:
        clear_screen()
        display_menu()
        
        try:
            choice_str = console.input("[bold cyan]Enter your choice (1-4): [/bold cyan]")
            user_input = int(choice_str)

            if user_input == 1:
                check_balance()
            elif user_input == 2:
                deposit_money()
            elif user_input == 3:
                withdraw_money()
            elif user_input == 4:
                show_goodbye()
                break
            else:
                console.print("\n[bold red]❌ Invalid choice. Please enter a number between 1 and 4.[/bold red]")
                time.sleep(2) # Pause to let user read the message
        
        except ValueError:
            console.print("\n[bold red]❌ Invalid input. Please enter a number.[/bold red]")
            time.sleep(2) # Pause to let user read the message

if __name__ == "__main__":
    main()