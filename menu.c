#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void startScreen() { printf("=== START SCREEN ===\n"); }
void cli_menu_one_line() {
  printf("Running CLI One-Line...\n");
  sleep(3);
  system("./run-cli-oneline.sh");
}
void cli_menu_muilti_line() { printf("Running CLI Multi-Line...\n"); }
void gui_menu_one_line() { printf("Opening GUI One-Line...\n"); }
void gui_menu_multi_line() { printf("Opening GUI Multi-Line...\n"); }

void main_menu()
{
    char char_choice[3];
    int int_choice = 0;

    do
    {
        system("clear"); 
        
        startScreen();
        printf("\n");
        printf("Welcome -- Converter Menu: \n\n");
        printf("1 --- CLI-Menu One-Line\n");
        printf("2 --- CLI-Menu Multi-Line\n");
        printf("\n");
        printf("3 --- GUI-Menu One-Line\n");
        printf("4 --- GUI-Menu Multi-Line\n");
        printf("q --- Exit\n\n");
        printf("Your choice: ");

        scanf("%2s", char_choice);

        
        if (char_choice[0] == 'q') {
            printf("\nExiting program...\n");
            break; 
        }

        int_choice = atoi(char_choice);

        switch (int_choice) 
        {
            case 1:
                cli_menu_one_line();
                break;
            case 2:
                cli_menu_muilti_line();
                break;
            case 3:
                gui_menu_one_line();
                break;
            case 4:
                gui_menu_multi_line();
                break;
            default:
                printf("\nInvalid option! Try again.\n");
                break;
        }

        
        if (int_choice != 0) {
            printf("\nPress Enter to return to menu...");
            getchar(); getchar(); 
        }

    } while (char_choice[0] != 'q');
}

int main() {
    main_menu();
    return 0;
}
