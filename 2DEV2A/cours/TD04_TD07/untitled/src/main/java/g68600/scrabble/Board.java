package g68600.scrabble;

public class Board {
    private Letter[][] squares;
    public Board(){
        this.squares = new Letter[15][15];
    }
// Refactirisation
    private  void assertInside(int row, int col) {
        if (row < 0 || row >= this.squares.length) {
            throw new IllegalArgumentException("Les paramètres doivent se trouver entre 0 et 15.");
        }
        if (col < 0 || col >= this.squares[row].length) {
            throw new IllegalArgumentException("Les paramètres doivent se trouver entre 0 et 15.");
        }
    }

    // Méthode qui retourne une seule lettre à une position row col donnée
    public Letter get(int row, int col){
        assertInside(row,col);
        return this.squares[row][col];
    }
    // Méthode qui va poser des lettres sur le plateau de jeu
    public void setLetters(int row, int col, Direction d, Letter[] letter){
        // vérification que row et col sont dans le tableau avant de les placer
        //assertInside(row,col); Vérification déjà fait dans get
        int dCol = d == Direction.HORIZONTAL ? 1:0;
        int dRow = d == Direction.VERTICAL ? 1:0;
        if (get(row,col) != null)
            throw new IllegalArgumentException("La case n'est pas vide: " + row + " et " + col );
        // Placement de row et col
        for (int i = 0; i < letter.length; i++){
            // A la position row, col on enregistre le i ème élément
            this.squares[row][col] = letter[i];
            col += dCol;
            row += dRow;

        }

    }

}