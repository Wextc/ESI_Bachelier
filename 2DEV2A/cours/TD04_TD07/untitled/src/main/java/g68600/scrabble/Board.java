package g68600.scrabble;

public class Board {
    private Letter[][] squares;
    public Board(){
        this.squares = new Letter[15][15];
    }

    // Méthode qui retourne une seule lettre à une position row col donnée
    public Letter get(int row, int col){
        if(row < 0 || row >= this.squares.length){
            throw new IllegalArgumentException("Les paramètres doivent se trouver entre 0 et 15.");
        }
        if(col < 0 || col >= this.squares[row].length){
            throw new IllegalArgumentException("Les paramètres doivent se trouver entre 0 et 15.");
        }
        return this.squares[row][col];
    }
    // Méthode qui va poser des lettres sur le plateau de jeu
    public void setLetters(int row, int col, Direction d, Letter[] letter){
        // On part de row col
        // On pose la première lettre
        // On avance  en row + 1,col si on va verticalement
        // On avance en row, col + 1 si on va horizontalement
        // On pose la 2 eme lettre
       for (int i = 0; i < letter.length; i++){
           // A la position row, col on enregistre le i ème élément
           this.squares[row][col] = letter[i];
           if (d == Direction.HORIZONTAL){
               col++;
           }else {
                row++;
           }
           

       }


    }
}
