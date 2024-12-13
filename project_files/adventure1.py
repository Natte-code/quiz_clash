import curses


def main(stdscr):
     # Initiera curses
    curses.curs_set(0)  # Dölj markören
    stdscr.nodelay(1)   # Gör getch icke-blockerande
    stdscr.timeout(2000) # Ställ in en timeout för getch (ms)
    
     # Spelvariabler
    rows, cols = 40, 40  # Storlek på spelplanen
    player_pos = [38, 19]  # Startposition för spelaren (centrerad)
    block_pos = []  # Position för objekt
    goal_pos = [20, 20]  # Positionen för rörbart objekt#
    door_pos = [[13, 1], [12, 2], [11, 3], [33, 1], [32, 2], [31, 3]]
    wall_hole = [30, 0]
    key = None            # Håller koll på vilken knapp som trycks
    message = ""
    while True:
        # Ritning av spelplanen
         stdscr.clear()
         for r in range(rows):
             for c in range(cols):
                 # Rita väggar på kanterna
                 if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and (r, c) != wall_hole:
                     stdscr.addch(r, c, '#')  # Vägg
                 elif [r, c] in door_pos:
                     stdscr.addch(r, c, '/')
                 elif [r, c] in block_pos:
                     stdscr.addch(r, c, 'B') # Placerar object
                 elif [r, c] == goal_pos:
                     stdscr.addch(r, c, 'X')  # Placerar rörbart objekt
                 elif [r, c] == player_pos:
                     stdscr.addch(r, c, 'O')  # Placera spelaren
                 else:
                     stdscr.addch(r, c, ' ')  # Ritning av spelplanen
                     
         stdscr.addstr(rows, 0, f"Message: {message}")
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
         # Kontrollera om spelaren försöker gå in i en vägg eller ett objekt
         if not ((new_pos[0] == 0 or new_pos[0] == rows - 1 or 
                 new_pos[1] == 0 or new_pos[1] == cols - 1) and tuple(new_pos) != wall_hole) and \
                new_pos not in block_pos:
            
             player_pos = new_pos
            
         if player_pos == goal_pos:
            message = "you win" #Ändra denna till vad man vill ska hända
            

if __name__ == "__main__": 
	curses.wrapper(main)
