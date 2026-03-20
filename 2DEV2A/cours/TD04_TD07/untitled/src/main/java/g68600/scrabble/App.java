package g68600.scrabble;
import java.util.Scanner;   // ✅ OBLIGATOIRE
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
public class App {
    public static void main(String[] args) {
        Board b = new Board();
        // b[0][0] cela ne marche pas. Il faut utiliser get. Il faut créer un nouveau array
        Letter[] letters = new Letter[]{
                new Letter('A'),
                new Letter('B')
        };
        b.setLetters(0,0, Direction.HORIZONTAL, letters);
        System.out.println(b.get(0,1).getLetter());

    }
}