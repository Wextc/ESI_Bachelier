package g68600.scrabble;
public class Letter {

    private char letter;

    public Letter(char letter) {
        this.letter = Character.toUpperCase(letter);
    }

    public char getLetter() {
        return letter;
    }

    @Override
    public String toString() {
        return String.valueOf(letter);
    }
}