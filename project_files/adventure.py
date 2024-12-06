import curses

def main(stdscr):
    # Initiera curses
    curses.curs_set(0)  # Dölj markören
    stdscr.nodelay(1)   # Gör getch icke-blockerande
    stdscr.timeout(2000) # Ställ in en timeout för getch (ms)
    
    # Spelvariabler
    rows, cols = 30, 60  # Storlek på spelplanen
    player_pos = [15, 30]  # Startposition för spelaren (centrerad)
    key = None            # Håller koll på vilken knapp som trycks
    
    while True:
        # Ritning av spelplanen
        stdscr.clear()
        for r in range(rows):
            for c in range(cols):
                # Rita väggar på kanterna
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    stdscr.addch(r, c, '#')  # Vägg
                elif [r, c] == player_pos:
                    stdscr.addch(r, c, 'O')  # Placera spelaren
                else:
                    stdscr.addch(r, c, ' ')  # Ritning av spelplanen
        
        stdscr.refresh()

        # Hantera användarinput
        key = stdscr.getch()
        new_pos = player_pos.copy()
        if key == ord('q'):  # Avsluta spelet
            break
        elif key == ord('w'):  # Upp
            new_pos[0] -= 1
        elif key == ord('s'):  # Ner
            new_pos[0] += 1
        elif key == ord('a'):  # Vänster
            new_pos[1] -= 1
        elif key == ord('d'):  # Höger
            new_pos[1] += 1

        # Kontrollera om spelaren försöker gå in i en vägg
        if not (new_pos[0] == 0 or new_pos[0] == rows - 1 or 
                new_pos[1] == 0 or new_pos[1] == cols - 1):
            player_pos = new_pos

if __name__ == "__main__":
    curses.wrapper(main)
